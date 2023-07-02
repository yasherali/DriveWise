from django.contrib import admin
from django.urls import path
from apis.views import Signup, CustomUserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Signup.as_view()),
    path('login/', CustomUserLoginView.as_view()),
]
