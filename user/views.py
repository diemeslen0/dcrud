from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader

from user.models import User
from user.forms import UserAdminCreationForm


class IndexView(LoginRequiredMixin, TemplateView):
    '''
    Selecting all users that are not superuser to
    show on index page.
    '''
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class CreateUserView(LoginRequiredMixin, CreateView):
    '''
    Used to create the users using the custom model created
    '''
    model = User
    template_name = 'user/create.html'
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CreateUserView, self).form_valid(form)


class UpdateUserView(LoginRequiredMixin, UpdateView):
    '''
    Used to update one user. I check if the user is creation from the logged user.
    '''
    model = User
    template_name = 'user/update.html'
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('index')

    def get_queryset(self, *args, **kwargs):
        qs =  super(UpdateUserView, self).get_queryset(*args, **kwargs).filter(creator=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['owner'] = User.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)
        return context


class DeleteUserView(LoginRequiredMixin, DeleteView):
    '''
    Used to delete a user. I check if the logged user is the creator
    of the user in danger.
    '''
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('index')
    
    def get_queryset(self, *args, **kwargs):
        return super(DeleteUserView, self).get_queryset(*args, **kwargs).filter(creator=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['owner'] = User.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)
        return context




class Template404View(TemplateView):
    '''
    Used to handle Page not Found error
    '''
    template_name = '404.html'


class Template500View(TemplateView):
    '''
    Used to handle Server Error Page
    '''
    template_name = '500.html'
