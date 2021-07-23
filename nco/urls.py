from django.urls import path
from django.conf import settings
from nco import views
from django.conf.urls.static import static


urlpatterns = [
    path("news/", views.NewsView.as_view()),
    path("news/<int:id>/", views.NewsViewItem.as_view()),
    path("laws/", views.LawsView.as_view()),
    path("laws/<int:id>/", views.LawsViewItem.as_view()),
    path("posts/<str:category>/", views.PostsViewItem.as_view()),
    path("favourites/", views.FavouritesItem.as_view()),
    path('register/', views.RegisterView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
