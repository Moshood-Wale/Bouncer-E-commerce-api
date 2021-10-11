from django.urls import path
from api.views.verify_otp_views import VerifyOTPView
from api.views.register_view import RegisterView
from api.views.login import LoginAPIView
from api.views.logout_view import LogoutAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('logout/',LogoutAPIView.as_view(), name = 'logout'),
]
