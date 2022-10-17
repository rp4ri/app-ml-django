#from django.conf.urls import url, include
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView # import PredictView
from apps.endpoints.views import ABTestViewSet
from apps.endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    #url(r"^", include(router.urls)),
    #path("", include(router.urls)),
    #re_path(r"^", include(router.urls)),
    #url(r"^api/v1/", include(router.urls)),
    path("api/v1/", include(router.urls)),
    
    # add predicted url
    #url(r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
    path("api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict"),
    #url(r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab")
    path("api/v1/stop_ab_test/<str:ab_test_id>", StopABTestView.as_view(), name="stop_ab"),
    #url(r"^api/v1/(?P<endpoint_name>.+)/abtest/(?P<abtest_id>.+)/stop$", StopABTestView.as_view(), name="stopabtest"),
    #path("api/v1/<str:endpoint_name>/abtest/<str:abtest_id>/stop", StopABTestView.as_view(), name="stopabtest"),
]