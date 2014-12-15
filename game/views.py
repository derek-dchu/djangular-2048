from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'

    login_url = reverse_lazy('account:account_login')