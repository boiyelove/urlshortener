from django.urls import path
from . import views



urlpatterns = [
	path('', views.ShortlinkView.as_view()),
	path('links/', views.ShortLinkListView.as_view()),
	path('l/<slug:shortcode>/', views.ShortLinkRedirect.as_view())
	]