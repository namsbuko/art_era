from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from profile.forms import SignUpForm, ProfileEditForm
from profile.models import Profile


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('email')
            user.save()
            user.refresh_from_db()
            user.profile.fio = form.cleaned_data.get('fio')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.user = user
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return redirect('home') \
            if request.user.is_authenticated \
            else render(request, self.template_name, {'form': self.form_class()})


class EditProfileView(LoginRequiredMixin, View):
    form_class = ProfileEditForm
    template_name = 'profile/edit.html'

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            profile = form.save()
            profile.user.email = form.cleaned_data['email']
            profile.user.save(update_fields=['email'])
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        user = request.user
        form = self.form_class(initial={'email': user.email}, instance=user.profile)
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile/info.html'
    login_url = 'login'

    def get(self, request):
        profile = request.user.profile
        profile.avatar_url = profile.avatar.url if profile.avatar else ''
        profile_url = request.user.profile.avatar.url \
            if request.user.profile.avatar else ''
        return render(request, self.template_name, {'profile': profile,
                                                    'profile_url': profile_url})


class ProfileMessageView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/messages.html'


class ProfileNotificationView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/notification.html'


class ProfileCabinetView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/cabinet.html'


class ProfileDetailView(LoginRequiredMixin, View):
    template_name = 'profile/info.html'
    login_url = 'login'

    def get(self, request, profile_id):
        profile = get_object_or_404(Profile, pk=profile_id)
        context = {
            'profile': profile,
            'no_edit': True,
            'profile_url': request.user.profile.avatar.url if
            request.user.profile.avatar else ''
        }
        return render(request, self.template_name, context)
