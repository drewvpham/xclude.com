from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from users import views as user_views
from memberships.views import Index
from django.contrib.auth import views as auth_views
from chat.views import index

urlpatterns = [

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('memberships/', include('memberships.urls', namespace='memberships')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('accounts/', include('allauth.urls')),
    path('videos/', include('videos.urls', namespace='videos')),
    path('store/', include('store.urls', namespace='store-home')),
    path('chat/', include('chat.urls', namespace='chat')),
    url(r'^', include('videos.urls', namespace='videos')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
