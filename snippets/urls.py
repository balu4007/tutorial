from django.urls import path,include
from .views import snippet_details,snippet_list


urlpatterns=[
    path('snippets/', snippet_list),
    path('snippets/<int:pk>', snippet_details),
]