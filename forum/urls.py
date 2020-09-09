from django.urls import path
from . import views

urlpatterns = [
    path('', views.showposts),
    path('publishpost/', views.publishpost),
    path('unpublishpost/', views.unpublishpost)
]