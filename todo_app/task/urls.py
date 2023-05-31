from rest_framework.routers import SimpleRouter

from .views.task import TaskViewSet

router = SimpleRouter(trailing_slash=False)
router.register('task', TaskViewSet)

urlpatterns = router.urls
