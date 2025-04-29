from django.urls import path
from .views import index, UserProfileView
from . import views

app_name = 'manga'

urlpatterns = [
    path('', index, name='index'),
    path('<int:book_id>/', views.show, name='show'),
    # path('<int:id_compte>/', views.compte, name='compte'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('api/user-profile/', UserProfileView.as_view(), name='user_profile'),
]