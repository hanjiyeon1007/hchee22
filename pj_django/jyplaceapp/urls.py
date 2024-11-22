from django.urls import path
from jyplaceapp import views 
urlpatterns = [
    path('',views.mainpg, name ='mainpg'),
]