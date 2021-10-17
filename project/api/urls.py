from django.urls import path
from api.views.verify_otp_views import VerifyOTPView
from api.views.register_view import RegisterView
from api.views.login import LoginAPIView
from api.views.logout_view import LogoutAPIView
from api.views.forgot_password_view import ForgotPasswordView
from api.views.password_reset import SetNewPasswordAPIView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('logout/',LogoutAPIView.as_view(), name = 'logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', SetNewPasswordAPIView.as_view(), name='reset-password'),
]
