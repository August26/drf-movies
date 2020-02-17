import requests
from bs4 import BeautifulSoup
import json
import asyncio


class MovieData:

    @staticmethod
    def generator_movie_link(cookies: str):
        """
        Генератор ссылок фильмов с названием фильмов
        :param cookies: Куки определенного города
        :return: Ссылка и название фильма
        """
        cnt = 0
        cookie = {'cookie': cookies}
        while True:
            try:
                content_page = requests.get(f'https://kassa.rambler.ru/creationsblock/17?currenttab=Cinemas&skip={cnt}',
                                            cookies=cookie).content
                dict_content = json.loads(content_page)
                if dict_content['list'] == '\n':
                    break
                soup = BeautifulSoup(dict_content['list'], 'html')
                drop_slider = soup.findAll('span', class_='mb_item')
                for element in drop_slider:
                    link = str(element.find('a').get('href')).split('/')
                    title = element.find('h3', class_='mb_item__title').text
                    yield title, link[-1]
                cnt += 24
            except Exception as e0:
                print(e0)

    @staticmethod
    def get_dates_movie(city: str, movie_code: str):
        """
        Получение дат примьер по нужному фильму
        :param city: Город, по к-му будет поиск
        :param movie_code: Код фильма
        :return: Список дат примьер фильма и фото фильма
        """
        try:
            content_movie = requests.get(f'https://kassa.rambler.ru/{city}/movie/{movie_code}').content
            soup = BeautifulSoup(content_movie, 'html')
            date_link = soup.findAll('span', class_='date_link')
            result = [item.get('data-url')[-10:].replace(".", "-") for item in date_link]
            try:
                image = soup.find('img').get("src")
            except:
                image = 'https://rest-info.com/design/default_3/images/none.png'
            return result, image
        except Exception as e0:
            print(e0)

    @staticmethod
    def get_list_element(html, attr: str, tag='span', method='class'):
        """
        Свитч кейс для получения запрашиваемых данных с html страницы
        :param html: Страница, к-рую парсим
        :param attr: Атрибут элемента
        :param tag: Элемент
        :param method: Метод, к к-му относится элемент
        :return: Список с данными по запросу, в случае если метод не найдет вернет None
        """
        tag_attr = {
            'class': [item.text for item in html.findAll(tag, class_=attr)],
            'itemprop': [item.text for item in html.findAll(tag, itemprop=attr)],
        }
        return tag_attr.get(method, "None")

    @staticmethod
    def price_type_time_handler(priceType: list, times: list):
        """
        Метод для обработки цены, типа сеанса и времени сеанса
        :param priceType: список типов сеансов с ценой
        :param times: список времени сеансов
        :return: список таплов из типа сеанса, времени его проведения, цена (дефолтное значение - 0)
        """
        sessions = []
        for index, case in enumerate(priceType):
            switch = {
                True: None,
                "2D" in case: "2D",
                "3D" in case: "3D",
                "4DX" in case: "4DX",
                "IMAX" in case: "IMAX"
            }[True]
            if switch != None:
                price = [item for item in case.split() if item.isdigit()]
                sessions.append((switch, times[index], int(*price) + 0))
        return sessions

    @staticmethod
    def get_info(city: str, movie_code: str, date: str):
        """
        Генератор для получения всех необходимых данных для нашего сервиса
        :param city: Город, по к-му будет поиск
        :param movie_code: Код фильма
        :param date: Дата примьеры
        :return: Все запрашиваемые данные из цикла
        """
        try:
            day_content = requests.get(f'https://kassa.rambler.ru/{city}/movie/{movie_code}?date={date}').content
            soup = BeautifulSoup(day_content, 'html')
            list_items = soup.find_all('div', class_='rasp_item')
            for item in list_items:
                cinema = MovieData.get_list_element(html=item, attr='s-name')
                address = MovieData.get_list_element(html=item, attr='streetAddress', method='itemprop')
                price_and_type = MovieData.get_list_element(html=item, attr='rasp_type', tag='div')
                time_seanse = [MovieData.get_list_element(html=active_time, attr='btn_rasp', tag='li') for active_time in
                               item.findAll('ul', class_='rasp_time')]
                data_sessions = MovieData.price_type_time_handler(price_and_type, time_seanse)
                yield ''.join(cinema), ''.join(address), data_sessions
        except Exception as e0:
            print(e0)


async def main_movies_and_dates(city, city_id, cook):
    for movie, movie_code in MovieData.generator_movie_link(cook):
        content_movie, image = MovieData.get_dates_movie(city, movie_code)
        await asyncio.sleep(1)
        response = requests.post(f"http://127.0.0.1:8000/film/", data={"title": movie, "photo": image,
                                                                       "id_film": movie_code, "city_film": city_id},
                                 headers=TOKEN).json()
        id_film = response['id']
        for date in content_movie:
            requests.post(f"http://127.0.0.1:8000/presentation/", data={"data_session": date,
                                                                        "film_presentations": id_film}, headers=TOKEN)
    print(f"movie done {city} - {city_id}")


async def main_post_info(city, movie_code, dates):
    for presen in dates:
        presen_json = requests.get(f'http://127.0.0.1:8000/presentation/{presen}/').json()
        await asyncio.sleep(1)
        date = presen_json['data_session']
        presen_id = presen_json['id']
        for cinema, address, data_sessions in MovieData.get_info(city, movie_code, date):
            for ds in data_sessions:
                type_ds, time_ds, price_ds = ds
                requests.post(f"http://127.0.0.1:8000/info/", data={"place": cinema, "address": address,
                                                                    "session": type_ds,
                                                                    "time_session": ','.join(time_ds).replace(' ', '').replace("\n", ""),
                                                                    "price": price_ds, "info_presen": presen_id},
                              headers=TOKEN)
    print(city)


async def start1():
    tasks = []

    for city in CITIES:
        town = city['city']
        town_id = city['id']
        town_cookie = city['cookie']
        task = asyncio.create_task(main_movies_and_dates(town, town_id, town_cookie))
        tasks.append(task)
    await asyncio.gather(*tasks)


async def start2():
    tasks = []

    for city in CITIES:
        town = city['city']
        towm_film = city['films']
        for item in towm_film:
            movie_json = requests.get(f'http://127.0.0.1:8000/film/{item}/').json()
            code = movie_json['id_film']
            film_presen = movie_json['presentations']
            task = asyncio.create_task(main_post_info(town, code, film_presen))
            tasks.append(task)
    print(len(tasks))
    await asyncio.gather(*tasks)


if __name__ == '__main__':

    TOKEN = {'Authorization': 'Token 698bde37501ec71ddb0157a0951d5943ca57ecf8'}
    CITIES = requests.get("http://127.0.0.1:8000/city/").json()
    asyncio.run(start1())
    # asyncio.run(start2())
