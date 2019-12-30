from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<str:pk>/', views.gamepage, name='gamepage'),
    path('category/<str:pk>', views.categorypage, name='categorypage'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('becomepremium/<str:pk>', views.becomepremium, name='becomepremium'),
    path('leaderboards', views.leaderboards, name='leaderboards'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('forgotPassword2/<str:pk>/', views.forgotPassword2, name='forgotPassword2'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('addFavorite/<str:pk>/', views.addfavorite, name="addFavorite"),
    path('removeFavorite/<str:pk>/', views.removefavorite, name="removeFavorite"),
    path('suggestGame', views.suggestGame, name="suggestGame"),
    path('viewSuggestions', views.viewSuggestions, name="viewSuggestions"),
    path('suggestion/<int:pk>', views.suggestion, name="suggestion"),
    path('addFavoriteCategory/<str:pk>/', views.addfavoritecategory, name="addfavoritecategory"),
    path('removeFavoriteCategory/<str:pk>/', views.removefavoritecategory, name="removefavoritecategory"),
    path('searchpage', views.searchpage, name="searchpage")

]
