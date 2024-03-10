from rest_framework.routers import DefaultRouter

from .views import AuthorViewset, MovieViewset

router = DefaultRouter()
router.register(r"movies", MovieViewset, basename="movie")
router.register(r"authors", AuthorViewset, basename="author")
urlpatterns = router.urls
