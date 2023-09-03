from django.urls import path
from .views import UserRegister

app_name="accounts"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register', UserRegister.as_view(), name='register')
]
