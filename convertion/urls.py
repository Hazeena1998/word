from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.myview,name="home"),
    path('datas',v.datas,name="datas")
]