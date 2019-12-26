from django.urls import path

from .views import *

app_name = 'videos'


urlpatterns = [
    path('', VideoListView.as_view(), name='videos-home'),
    path('upload/', VideoCreateView.as_view(), name='upload'),
    path('<slug>/', VideoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', VideoUpdateView.as_view(), name='video-update'),
    path('<int:pk>/delete/', VideoDeleteView.as_view(), name='video-delete'),
    # path('<video_slug>/<lesson_slug>',
    #      LessonDetailView.as_view(), name='lesson-detail')
]
