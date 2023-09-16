from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.user_profile, name='user_profile'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('account/', views.account_user, name='account'),
    path('edit_account/', views.edit_account_user, name='edit_account'),

    path('create_skill/', views.create_skill, name='create_skill'),
    path('update_skill/<str:pk>/', views.update_skill, name='update_skill'),
    path('delete_skill/<str:pk>/', views.delete_skill, name='delete_skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<pk>', views.view_message, name='message'),
    path('create-message/<profile_pk>', views.create_message, name='create-message'),

]
