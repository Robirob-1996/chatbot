from django.urls import include, path
from . import views

urlpatterns = [
    path('some-url/', views.some_view, name='some_view_name'),
    path('', include ('chatbot.urls')),
]
