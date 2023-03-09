from django.urls import path
from app1.views import *

app_name='something'
urlpatterns=[
    path('RRR/',RRR,name='RRR'),
    path('warrior/',warrior,name='warrior'),
]