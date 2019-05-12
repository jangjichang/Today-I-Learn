from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404

from mysite.views import LoginRequiredMixin
from .models import Work, Card, Activity
from .forms import CardForm, CardInlineFormSet

# Create your views here.


class WorkCardLV(LoginRequiredMixin, ListView):
    model = Work

    def get_queryset(self):
        return Work.objects.filter(owner=self.request.user)


class WorkCreateView(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['name',]
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        context = super(WorkCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CardInlineFormSet(self.request.POST)
        else:
            context['formset'] = CardInlineFormSet()
        return context

    # form은 work, formset은 card
    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for cardform in formset:
            cardform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('todolist:index')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = Work
    fields = ['name', ]
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        if self.request.user != Work.objects.get(id=self.kwargs['pk']).owner:
            raise Http404
        else:
            context = super(WorkUpdateView, self).get_context_data(**kwargs)
            if self.request.POST:
                context['formset'] = CardInlineFormSet(self.request.POST, instance=self.object)
            else:
                context['formset'] = CardInlineFormSet(instance=self.object)
            return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        for cardform in formset:
            cardform.instance.owner = self.request.user
            cardform.instance.work = Work.objects.get(id=self.kwargs['pk'])
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('todolist:index')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = Work
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        if self.request.user != Work.objects.get(id=self.kwargs['pk']).owner:
            raise Http404
        else:
            context = super(WorkDeleteView, self).get_context_data(**kwargs)
            return context


class WorkCompleteView(LoginRequiredMixin, DeleteView):
    model = Work

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        object.owner.score += 1
        success_url = reverse_lazy('todolist:index')
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        if self.request.user != Work.objects.get(id=self.kwargs['pk']).owner:
            raise Http404
        else:
            context = super(WorkCompleteView, self).get_context_data(**kwargs)
            return context


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        if self.request.user != Work.objects.get(id=self.kwargs['fk']).owner:
            raise Http404
        else:
            context = super(CardCreateView, self).get_context_data(**kwargs)
            return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.work = Work.objects.get(id=self.kwargs['fk'])
        return super(CardCreateView, self).form_valid(form)


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        if self.request.user != Card.objects.get(id=self.kwargs['pk']).owner:
            raise Http404
        else:
            context = super(CardUpdateView, self).get_context_data(**kwargs)
            return context


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = reverse_lazy('todolist:index')

    def get_context_data(self, **kwargs):
        if self.request.user != Card.objects.get(id=self.kwargs['pk']).owner:
            raise Http404
        else:
            context = super(CardDeleteView, self).get_context_data(**kwargs)
            return context


class CardCompleteView(LoginRequiredMixin, DeleteView):
    pass

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
