from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='pokemons_index'),
    # localhost:8000
    path('pokemons/<int:pokemon_id>/', views. pokemons_detail, name='pokemons_detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name= 'pokemons_create'),
    path('pokemons/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemons_delete'),
    path('pokemons/<int:pokemon_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('pokemons/<int:pokemon_id>/assoc_toy/<int:toy_id>/',views.assoc_toy, name='assoc_toy'),
    path('accounts/signup/', views.signup, name='signup'),
]
