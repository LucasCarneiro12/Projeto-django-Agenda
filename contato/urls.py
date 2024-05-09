
from django.urls import path
from contato import views
from django.conf.urls import include
app_name = 'contato'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # contato CRUD
    path('contato/<int:contato_id>/detail/', views.contato, name='contato'),
    path('contato/create/', views.create, name='create'),
    path('contato/<int:contato_id>/update/', views.update, name='update'),
    path('contato/<int:contato_id>/delete/', views.delete, name='delete'),

    # user c
    path('user/create', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]


