from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # routes for Simple JWT’s views
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # DRF's default login and logout views for use with the browsable API
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
]

urlpatterns += [
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')) # This path is for 404
]