# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include(todo.urls)),
# ]
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns =[
    path('', views.indexpage, name='indexpage')
]