from django.urls import path
from .views import *


app_name = "home"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home,name="home"),

]
