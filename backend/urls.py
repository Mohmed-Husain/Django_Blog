from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-test-email/', user_views.send_test_email, name='send_test_email'), #temporary
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
          auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
            ), name='password_reset'),
    path('password-reset/done/',
          auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
            ), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #       auth_views.PasswordResetConfirmView.as_view(
    #           template_name='users/password_reset_confirm.html'
    #           ), name='password_reset_confirm'),

    path('', include('blog.urls') ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
