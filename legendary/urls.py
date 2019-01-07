from django.urls import path

from legendary import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('hero/best/<int:hero_id>/', views.hero_best_team, name='hero_best_beam'),
    path('hero/delete/<int:hero_id>/', views.hero_delete, name='hero_delete'),
    path('villains/delete/<int:villain_id>/', views.delete_villain, name='delete_villain'),
    path('thanks/', views.thanks, name='thanks'),
    path('add_team/', views.add_team, name='add_team'),
    path('teams/', views.teams_page, name='teams_page'),
    path('games', views.games_page, name='games_page'),
    path('games/add_game', views.add_game, name='add_game'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('', views.index, name='index'),
    path('add_mastermind', views.add_mastermind, name='add_mastermind'),
    path('villains/', views.villains, name='villains'),
    path('henchmen/', views.henchman, name='henchmen'),
    path('add_villain/', views.add_villain, name='add_villain'),
    path('add_henchman/', views.add_henchman, name='add_henchman'),
    path('masterminds', views.masterminds_page, name='mastermind_page'),
    path('add_scheme', views.add_scheme, name='add_scheme'),
    path('schemes', views.schemes_page, name='schemes_page'),
    path('statistics', views.statistics, name='statistics'),
]
