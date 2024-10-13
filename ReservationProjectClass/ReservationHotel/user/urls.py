# we set api in this part

from django.urls import path
from user.views import *

app_name ="user"
urlpatterns = [
    path("create/" ,CreateUserView.as_view() , name= "create")
]

# now we must register url pattern in url.py in root app (reservation)
