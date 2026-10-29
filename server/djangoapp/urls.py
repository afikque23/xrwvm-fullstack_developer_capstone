from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Static pages
    path('about/', TemplateView.as_view(template_name='djangoapp/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='djangoapp/contact.html'), name='contact'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration, name='register'),

    # Dealers
    path('dealerships/', views.get_dealerships, name='dealerships'),
    path('dealerships/<str:state>/', views.get_dealerships, name='dealerships_by_state'),

    # Dealer details
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # Cars
    path('get_cars/', views.get_cars, name='get_cars'),

    # Add review
    path('add_review/', views.add_review, name='add_review'),

    # Sentiment analysis (direct Django endpoint)
    path('analyze_review/<path:text>/', views.analyze_review, name='analyze_review'),
]
