from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from todoapp.views import LoginRequiredMixin
from .models import WorkList, Card, Activity

# Create your views here.


class ListCardLV(LoginRequiredMixin, ListView):
    model = WorkList


class ListCreateView(LoginRequiredMixin, CreateView):
    model = WorkList


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkList


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkList


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card