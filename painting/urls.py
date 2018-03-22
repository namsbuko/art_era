from django.conf.urls import url

from painting.views import PaintingAddView, PaintingEditView, PaintingInfoView, PaintingListView

min_cost = '(min_cost=(?P<min_cost>[0-9]+))?'
max_cost = '(&max_cost=(?P<max_cost>[0-9]+))?'

min_year = '(&min_year=(?P<min_year>[0-9]+))?'
max_year = '(&max_year=(?P<max_year>[0-9]+))?'

techniques = '(&techniques=(?P<techniques>[a-zа-яA-ZА-Я,]+))?'

genres = '(&genres=(?P<genres>[a-zа-яA-ZА-Я,]+))?'

search_url = r'^' + ''.join((min_cost, max_cost, min_year,
                             max_year, techniques, genres)) + '$'

urlpatterns = [
    url(r'^add/$', PaintingAddView.as_view(), name='painting_add'),
    url(r'^(?P<painting_id>[0-9]+)/edit/$', PaintingEditView.as_view(), name='painting_edit'),
    url(r'^(?P<painting_id>[0-9]+)/$', PaintingInfoView.as_view(), name='painting_info'),
    url(search_url, PaintingListView.as_view(), name='painting_list')
]
