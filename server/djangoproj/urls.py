"""URL configuration for djangoproj project."""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', views.home_html_view, name='home'),
    path('dealerships/', views.home_html_view, name='dealerships_html'),
    path('dealer/<int:dealer_id>/', views.dealer_detail_html_view, name='dealer_html'),
    path('post_review/<int:dealer_id>/', views.post_review_html_view, name='post_review_html'),

    # Direct microservice endpoints required by rubric
    path('fetchDealers', views.fetch_dealers_api, name='fetch_dealers_root'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state_api, name='fetch_dealers_by_state_root'),
    path('fetchDealer/<int:dealer_id>', views.fetch_dealer_by_id_api, name='fetch_dealer_by_id_root'),
    path('fetchReviews/dealer/<int:dealer_id>', views.fetch_reviews_by_dealer_api, name='fetch_reviews_by_dealer_root'),
    path('analyze/<path:text>', views.analyze_review_api, name='analyze_review_root'),
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'frontend/static')
