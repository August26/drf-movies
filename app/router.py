from movieapi.views import MovieView, CitiesView, FilmsView, PresentationView, InfoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Movie', MovieView)
router.register('city', CitiesView)
router.register('film', FilmsView)
router.register('presentation', PresentationView)
router.register('info', InfoView)
