from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from profile.forms import SignUpForm


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def post(self, request):
        form = SignUpForm(request.POST)
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
