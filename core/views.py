from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from painting.models import Painting
from profile.models import Profile


class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return redirect('profile_info')


class SearchView(View):
    template_name = 'core/search.html'

    def get(self, request):
        context = {
            'profile': request.user.profile if request.user.is_authenticated else None,
            'painting_count': Painting.objects.count(),
            'paintings': Painting.objects.all(),
            'profiles': Profile.objects.annotate(paintings_count=Count('paintings'))
        }
        return render(request, self.template_name, context)
