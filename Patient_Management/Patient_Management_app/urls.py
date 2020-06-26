from django.conf.urls import url
from django.urls import path
from Patient_Management_app import views

app_name = 'patient_management_app'

urlpatterns = [
	path('register/',views.register,name='register'),
	path('user_login/',views.user_login,name='user_login')
]