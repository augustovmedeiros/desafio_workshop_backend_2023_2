from rest_framework import routers
from django.urls import include, path
from apps.shows.api.viewsets import CategoriaViewSet, ArtistaViewSet, ShowViewSet

router = routers.DefaultRouter()
router.register("categorias", CategoriaViewSet)
router.register("artistas", ArtistaViewSet)
router.register("shows", ShowViewSet)

urlpatterns = [
    path("", include(router.urls))
]
