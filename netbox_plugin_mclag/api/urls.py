from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_plugin_mclag'

router = NetBoxRouter()
router.register('domains', views.McDomainViewSet)
router.register('mclags', views.McLagViewSet)
router.register('interfaces', views.McInterfaceViewSet)

urlpatterns = router.urls
