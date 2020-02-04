from movieapi.views import MovieView, CitiesView, FilmsView, PresentationView, InfoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Movie', MovieView)
router.register('cities', CitiesView)
router.register('films', FilmsView)
router.register('presentation', PresentationView)
router.register('info', InfoView)
