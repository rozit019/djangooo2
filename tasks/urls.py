from django .urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/posts/', views.get_posts,name='get_posts'),
        #   views.index indx chai functioj name
]