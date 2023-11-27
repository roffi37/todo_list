from django.urls import path, include

from todo_list.views import index

urlpatterns = [
    path("", index),
]
