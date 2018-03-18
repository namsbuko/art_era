from django.conf.urls import url

from core.views import HomeView, SearchView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search/*$', SearchView.as_view(), name='search'),
]
