from django.urls import path
from app2.views import *

app_name='nothing'
urlpatterns=[
    path('CEO/',CEO,name='CEO'),
    path('AA/',AA,name='AA')
]