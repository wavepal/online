# myapp/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render
from .models import Game
from .models import Tag
from django.db.models import Q
from .models import Liked
from .forms import AuthUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.conf import settings
from .forms import SearchForm
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import AuthUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm  # Замените путь на вашу форму
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Game
from django.shortcuts import render
import logging
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.conf import settings
import os

def index(request):
    return render(request, 'index.html')

class GameSearchView(ListView):
    model = Game
    template_name = 'game_search.html'
    context_object_name = 'games'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Game.objects.filter(game_name__icontains=query)
        return Game.objects.all()

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        context['games'] = Game.objects.filter(tags=tag)
        return context

class TagView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

class TagView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        context['games'] = Game.objects.filter(tags=tag)
        return context

class SearchView(ListView):
    model = Game
    template_name = 'search_results.html'
    context_object_name = 'games'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(Q(game_name__icontains=query))

class IndexView(ListView):
    model = Game
    template_name = 'index.html'
    context_object_name = 'games'

class AllGamesView(ListView):
    model = Game
    template_name = 'allgames.html'
    context_object_name = 'games'

class aboutus_view(ListView):
    model = Game
    template_name = 'aboutUs.html'
    context_object_name = 'games'

def play_html_view(request, filename):
    # Получите путь к HTML-файлу на основе параметра file_id
    html_file_path = os.path.join(settings.BASE_DIR, 'myapp', 'static', 'myapp', 'games', f'{filename}.html')

    try:
        # Откройте и прочитайте HTML-файл
        with open(html_file_path, 'r') as html_file:
            html_content = html_file.read()

        # Отправьте содержимое HTML-файла на клиент
        return HttpResponse(html_content)
    except FileNotFoundError:
        # Если файл не найден, верните 404 ошибку
        return HttpResponseNotFound("HTML file not found.")

class MyProjLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_msg = 'User successfully created'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Дополнительный код после успешного создания пользователя
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]  # Используйте 'password1', так как это поле пароля
        aut_user = authenticate(username=username, password=password)

        if aut_user is not None:
            login(self.request, aut_user)

        return response

class MyProjLogout(LogoutView):
    next_page = reverse_lazy('index')
