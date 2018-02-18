from django.conf.urls import url

from profile.views import SignUpView, EditProfileView, ProfileView

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^profile/edit$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^profile/$', ProfileView.as_view(), name='profile_info')
]
