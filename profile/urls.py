from django.conf.urls import url

from profile.views import SignUpView, EditProfileView, \
    ProfileView, ProfileMessageView, ProfileDetailView, \
    ProfileCabinetView, ProfileNotificationView

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^profile/edit$', EditProfileView.as_view(), name='profile_edit'),
    url(r'^profile/$', ProfileView.as_view(), name='profile_info'),
    url(r'^profile/messages$', ProfileMessageView.as_view(), name='profile_messages'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', ProfileDetailView.as_view(), name='profile_detail_info'),
    url(r'^profile/notification/$', ProfileNotificationView.as_view(), name='profile_notifications'),
    url(r'^profile/cabinet/$', ProfileCabinetView.as_view(), name='profile_cabinet'),
]
