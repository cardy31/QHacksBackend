from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scheduler import views

urlpatterns = [
    path('scheduler/', views.SchedulerList.as_view()),
    path('scheduler/<int:pk>', views.SchedulerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)