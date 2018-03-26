from datetime import datetime

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q, Min, Max
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from rest_framework import generics, status
from rest_framework.response import Response

from painting.forms import PaintingForm
from painting.models import Painting
from painting.serializers import PaintingSerializer


class PaintingAddView(LoginRequiredMixin, View):
    template_name = 'painting/add.html'
    login_url = 'login'
    form_class = PaintingForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save(commit=False)
            painting.owner = request.user.profile
            painting.save()
            return redirect('profile_info')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class()})


class PaintingEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'painting/edit.html'
    login_url = 'login'
    form_class = PaintingForm

    raise_exception = True

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=self.painting)
        if form.is_valid():
            form.save()
            return redirect('profile_info')
        return render(request, self.template_name, {'form': form})

    def get(self, request, **kwargs):
        form = self.form_class(instance=self.painting)
        return render(request, self.template_name, context={'form': form})

    def test_func(self):
        self.painting = get_object_or_404(Painting, id=self.kwargs['painting_id'])
        return self.request.user.profile == self.painting.owner


class PaintingInfoView(LoginRequiredMixin, View):
    template_name = 'painting/info.html'
    login_url = 'login'

    def get(self, request, painting_id):
        profile = request.user.profile
        painting = get_object_or_404(Painting, pk=painting_id)
        context = {
            'profile': profile,
            'painting': painting
        }
        return render(request, self.template_name, context)


class PaintingListView(generics.ListAPIView):
    serializer_class = PaintingSerializer

    def get_params(self):
        params = Painting.objects\
            .aggregate(min_cost=Min('cost'), max_cost=Max('cost'),
                       min_year=Min('creation_year'), max_year=Max('creation_year'))
        return {
            'genres': Painting.GENRES,
            'techniques': Painting.TECHNIQUES,
            'cost': {'min': params['min_cost'], 'max': params['max_cost']},
            'year': {'min': params['min_year'], 'max': params['max_year']},
        }

    def get_queryset(self):
        genres = self.kwargs.get('genres')
        techniques = self.kwargs.get('techniques')
        min_cost = self.kwargs.get('min_cost') or 0
        max_cost = self.kwargs.get('max_cost') or 10000000
        min_year = self.kwargs.get('min_year') or 0
        max_year = self.kwargs.get('max_year') or datetime.now().year

        f = Q(cost__gte=min_cost, cost__lte=max_cost)
        f &= Q(creation_year__gte=min_year, creation_year__lte=max_year)
        if genres:
            f &= Q(genre__in=filter(None, genres.split(',')))
        if techniques:
            f &= Q(technique__in=filter(None, techniques.split(',')))

        return Painting.objects.filter(f)[:12]

    def get(self, request, *args, **kwargs):
        painting = self.get_queryset()
        serializer = self.serializer_class(painting, many=True)

        response = {
            'params': self.get_params(),
            'paintings': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
