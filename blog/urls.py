from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000/blog/
    path('about/', views.about, name='about'), # http://127.0.0.1:8000/about/
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]

