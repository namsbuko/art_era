from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from profile.forms import SignUpForm, ProfileEditForm


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
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})


class EditProfileView(LoginRequiredMixin, View):
    form_class = ProfileEditForm
    template_name = 'profile/edit.html'

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            profile = form.save()
            print(request.FILES)
            print(form.cleaned_data)
            profile.user.email = form.cleaned_data['email']
            profile.user.save(update_fields=['email'])
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        user = request.user
        form = self.form_class(initial={'email': user.email}, instance=user.profile)
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile/info.html'

    def get(self, request):
        profile = request.user.profile

        return render(request, self.template_name, {'profile': profile})



