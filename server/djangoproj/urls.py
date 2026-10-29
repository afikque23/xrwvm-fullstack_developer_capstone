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
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'frontend/static')
