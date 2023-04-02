from rest_framework import routers
from api.views import FilmeViewSet

router = routers.DefaultRouter()
router.register(r'', FilmeViewSet)

urlpatterns = router.urls