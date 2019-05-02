from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from mysite.views import LoginRequiredMixin
from .models import Work, Card, Activity
from .forms import CardForm

# Create your views here.


class WorkCardLV(LoginRequiredMixin, ListView):
    model = Work

    def get_queryset(self):
        return Work.objects.filter(owner=self.request.user)


class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['name']
    success_url = reverse_lazy('todolist:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(WorkCreateView, self).form_valid(form)


class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = Work
    fields = ['name']
    success_url = reverse_lazy('todolist:index')


class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = Work
    success_url = reverse_lazy('todolist:index')


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('todolist:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.work = Work.objects.get(id=self.kwargs['fk'])
        return super(CardCreateView, self).form_valid(form)


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('todolist:index')


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('todolist:index')

# ToDo: Activity 기능 추가하기
# class ActivityCreateView(LoginRequiredMixin, CreateView):
#     model = Activity
# 
# 
# class ActivityUpdateView(LoginRequiredMixin, UpdateView):
#     model = Activity
# 
# 
# class ActivityDeleteView(LoginRequiredMixin, DeleteView):
#     model = Activity