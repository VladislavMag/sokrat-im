from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
from django.contrib.auth import views as authViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('reg', userViews.register, name='reg'),

    path('profile', userViews.profile, name='profile'),

    path('user', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),

    path('exit', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
