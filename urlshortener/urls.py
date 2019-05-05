from django.conf.urls import url
from django.urls import path, include
from .api.routers import router
from . import views


urlpatterns = [
	url(r'^api/', include(router.urls)),
	path('', views.ShortlinkView.as_view()),
	path('links/', views.ShortLinkListView.as_view()),
	path('l/<slug:shortcode>/', views.ShortLinkRedirect.as_view())
	]








