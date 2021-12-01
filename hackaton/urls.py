
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from hackaton import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('category/', include('applications.category.urls')),
    path('order/', include('applications.order.urls')),
    path('product/', include('applications.product.urls')),
    path('review/', include('applications.review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
