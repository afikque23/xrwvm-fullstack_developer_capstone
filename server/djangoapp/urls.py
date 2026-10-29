from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Static pages
    path('about/', TemplateView.as_view(template_name='djangoapp/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='djangoapp/contact.html'), name='contact'),

    # HTML Views
    path('', views.home_html_view, name='home_html'),
    path('home/', views.home_html_view, name='home_html_alt'),
    path('dealer_view/<int:dealer_id>/', views.dealer_detail_html_view, name='dealer_detail_html'),
    path('post_review_view/<int:dealer_id>/', views.post_review_html_view, name='post_review_html'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration, name='register'),

    # Dealers API
    path('dealerships/', views.get_dealerships, name='dealerships'),
    path('dealerships/<str:state>/', views.get_dealerships, name='dealerships_by_state'),

    # Dealer details API
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # Cars
    path('get_cars/', views.get_cars, name='get_cars'),

    # Add review
    path('add_review/', views.add_review, name='add_review'),

    # Sentiment analysis (direct Django endpoint)
    path('analyze_review/<path:text>/', views.analyze_review, name='analyze_review'),

    # Microservice direct endpoints matching rubric
    path('fetchDealers', views.fetch_dealers_api, name='fetch_dealers'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state_api, name='fetch_dealers_by_state'),
    path('fetchDealer/<int:dealer_id>', views.fetch_dealer_by_id_api, name='fetch_dealer_by_id'),
    path('fetchReviews/dealer/<int:dealer_id>', views.fetch_reviews_by_dealer_api, name='fetch_reviews_by_dealer'),
    path('analyze/<path:text>', views.analyze_review_api, name='analyze_review_direct'),
]
