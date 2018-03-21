from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import DetailView

from painting.forms import PaintingForm
from painting.models import Painting


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
