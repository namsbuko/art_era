from django.conf.urls import url

from painting.views import PaintingAddView, PaintingEditView, PaintingInfoView

urlpatterns = [
    url(r'^add/$', PaintingAddView.as_view(), name='painting_add'),
    url(r'^(?P<painting_id>[0-9]+)/edit/$', PaintingEditView.as_view(), name='painting_edit'),
    url(r'^(?P<painting_id>[0-9]+)/$', PaintingInfoView.as_view(), name='painting_info'),
]
