from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from todoapp.views import LoginRequiredMixin
from .models import WorkList, Card, Activity

# Create your views here.

# To Do: 로그인한 사용자가 소유한 레코드만 넘기도록 추가하기


class ListCardLV(LoginRequiredMixin, ListView):
    model = WorkList

    def get_queryset(self):
        return WorkList.objects.filter(owner=self.request.user)


class ListCreateView(LoginRequiredMixin, CreateView):
    model = WorkList
    fields = ['name']
    success_url = reverse_lazy('workmanagement:worklist_show')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ListCreateView, self).form_valid(form)


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkList
    fields = ['name']
    success_url = reverse_lazy('workmanagement:worklist_show')


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkList
    success_url = reverse_lazy('workmanagement:worklist_show')


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['name', 'description', 'deadline_date']
    success_url = reverse_lazy('workmanagement:worklist_show')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.worklist = WorkList.objects.get(id=self.kwargs['fk'])
        return super(CardCreateView, self).form_valid(form)


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['name', 'description', 'deadline_date']
    success_url = reverse_lazy('workmanagement:worklist_show')


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('workmanagement:worklist_show')
