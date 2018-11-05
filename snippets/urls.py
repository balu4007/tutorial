from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import snippet_details, snippet_list

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>', snippet_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
