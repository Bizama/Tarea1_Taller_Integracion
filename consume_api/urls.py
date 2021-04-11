from django.urls import path
from . import views

app_name = 'consume_api'

urlpatterns = [
    path('', views.main_page, name='home'),
    path('breaking_bad', views.breakin_seasons, name='breaking bad episodes'),
    path('better_call', views.seul_seasons, name='better call saul episodes'),
    path('breaking_episodes/<str:season>/', views.breaking_episodes, name='breakingseason'),
    path('better_call_saul_episodes/<str:season>/', views.seul_episodes, name='saulseason'),
    path('character/<int:id>/', views.get_character, name='Personaje'),
    path('episode/<int:id>/', views.get_episode, name='episode'),
    path('search/', views.search_character, name='search_result')
]
