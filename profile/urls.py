from django.conf.urls import url

from profile.views import SignUpView, EditProfileView, ProfileView, ProfileMessageView

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^profile/edit$', EditProfileView.as_view(), name='profile_edit'),
    url(r'^profile/$', ProfileView.as_view(), name='profile_info'),
    url(r'^profile/messages$', ProfileMessageView.as_view(), name='profile_messages'),
]
