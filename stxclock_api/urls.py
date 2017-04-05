from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'exchanges', views.ExchangeViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'weekends', views.WeekendViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
        # url(r'^$', views.index, name='stxclock'),
        url(r'^api/', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        ]
