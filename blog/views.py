from typing import List
from django.db.models import deletion
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class AListView(ListView):
    model = Article
    template_name = 'home.html'

class ADetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class AUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields=('title', 'image', 'body', 'summary')
    template_name = 'article_edit.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ADeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ACreatView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields=('title', 'image', 'body', 'summary', 'author')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

