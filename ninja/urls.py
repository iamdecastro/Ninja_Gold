from django.urls import path
from . import views


urlpatterns = [
    
    
    path('process_money/<place>',views.updateGold),
    path("",views.index)
    # path("users",views.create_user)  

]


