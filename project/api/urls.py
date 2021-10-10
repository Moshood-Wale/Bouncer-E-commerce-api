from django.urls import path
from api.views.verify_otp_views import VerifyOTPView
from api.views.register_view import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify'),

]
