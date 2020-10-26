from django.urls import path, include
from users import views as user_views
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path ('register/',user_views.register,name='register'), 	
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', auth_views.LoginView.as_view(template_name='users/profile.html'), name='profile'),
    path ('change_password/',user_views.change_password,name='change_password'),
	path ('contact/',views.contact,name='contact'),
	path ('about/',views.about,name='about'),

	]