from django.urls import path
from jobs.views import IndexJobDetailView, IndexJobsListView


urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", IndexJobDetailView.as_view(), name="job"),
]
