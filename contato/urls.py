
from django.urls import path
from contato import views
from django.conf.urls import include
app_name = 'contato'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # CRUD
    path('contato/<int:contato_id>/detail/', views.contato, name='contato'),
    path('contato/create/', views.create, name='create'),
    path('contato/<int:contato_id>/update/', views.update, name='update'),
    path('contato/<int:contato_id>/delete/', views.delete, name='delete'),

    # user c
    path('user/create', views.register, name='register'),
]


