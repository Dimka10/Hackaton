from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)