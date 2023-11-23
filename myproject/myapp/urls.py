# myapp/urls.py
from django.urls import path
from .views import index
from .views import GameDetailView, TagView, TagDetailView, SearchView, AllGamesView, IndexView, play_html_view, aboutus_view, GameSearchView, RegisterView, MyProjLoginView, MyProjLogout
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register_page/', RegisterView.as_view(), name='register_page'),
    path('logout_page/', MyProjLogout.as_view(), name='logout_page'),
    path('login_page/', MyProjLoginView.as_view(), name='login_page'),
    path('aboutus/', aboutus_view.as_view(), name='aboutUs'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('play/<str:filename>.html/', play_html_view, name='play-html'),
    path('t/tag_list/', TagView.as_view(), name='tag'),
    path('t/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('games/search/', SearchView.as_view(), name='rule'),
    path('allgames/', AllGamesView.as_view(), name='allgames'),
    path('allgames/<str:filename>.html/', play_html_view, name='play-html'),
    path('t/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('t/', TagView.as_view(), name='tag'),
    path('search/', GameSearchView.as_view(), name='game_search'),
]