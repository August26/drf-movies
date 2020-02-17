import sqlite3 as lite

con = lite.connect('db.sqlite3')

with con:
    cur = con.cursor()
    # cur.execute("DROP table new__movieapi_films;")
    cur.execute("DELETE FROM movieapi_info;")
    cur.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='movieapi_info';")
    # cur.execute("SELECT * FROM auth_user")
    # cur.execute("pragma table_info(account_emailaddress);")
    # cur.execute("DELETE FROM account_emailaddress where user_id='2'")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()

    for row in rows:
        print(row)

# movieapi_film movieapi_presentation