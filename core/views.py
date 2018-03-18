from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from painting.models import Painting


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'

    template_name = 'core/home.html'


class SearchView(View):
    template_name = 'core/search.html'

    def get(self, request):
        qs = Painting.objects.all()
        context = {
            'profile': request.user.profile if request.user.is_authenticated else None,
            'painting_count': Painting.objects.count(),
            'paintings': qs,
            'genres': ['жанр1', 'жанр2'],
            'techniques': ['техника1', 'техника2'],
        }
        return render(request, self.template_name, context)
