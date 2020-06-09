from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    # path('change-password/', ChangePassword.as_view(), name='change-password-API')
]