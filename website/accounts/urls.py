from django.urls import path
from .views import CustomUserRegister, CustomLoginView

app_name="accounts"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register', CustomUserRegister.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login')
]
