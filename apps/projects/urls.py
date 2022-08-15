from django.urls import path

from apps.projects.views import ProjectAssigmentsView, ProjectDetailsView, ProjectsView


urlpatterns = [
    path("", ProjectsView.as_view(), name="projects"),
    path("<int:project_id>/", ProjectDetailsView.as_view(), name="project-details"),
    path("<int:project_id>/users/", ProjectAssigmentsView.as_view(), name="project-assigments"),
]
