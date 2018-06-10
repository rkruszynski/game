from django.urls import path

from legendary import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('hero/delete/<int:hero_id>/', views.hero_delete, name='hero_delete'),
    path('thanks/', views.thanks, name='thanks'),
    path('add_team/', views.add_team, name='add_team'),
    path('teams/', views.teams_page, name='teams_page'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('', views.index, name='index'),
    path('add_mastermind', views.add_mastermind, name='add_mastermind'),
    path('masterminds', views.masterminds_page, name='mastermind_page'),
    path('add_scheme', views.add_scheme, name='add_scheme'),
    path('schemes', views.schemes_page, name='schemes_page'),
]
