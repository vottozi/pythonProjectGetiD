from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name = 'hello'),
    path('tvshow/', views.TvShowView.as_view(), name='tvshow'),
    path('tvshow_detail/<int:id>/', views.TvShowDetailView.as_view(), name='show_detail'),
]