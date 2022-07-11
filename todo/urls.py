from django.urls import path

from todo.views import TagListView, TagDetailView, TaskListView, \
    TaskDetailView, TagCreateView, TagUpdateView, TagDeleteView, \
    TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("tags/", TagListView.as_view(),
         name="tag_list"),
    path("tags/create/", TagCreateView.as_view(),
         name="tag_create"),
    path("tags/<slug:slug>/update/", TagUpdateView.as_view(),
         name="tag_update"),
    path("tags/<slug:slug>/delete/", TagDeleteView.as_view(),
         name="tag_delete"),
    path("tags/<slug:slug>/", TagDetailView.as_view()
         , name="tag_detail"),

    path("", TaskListView.as_view(),
         name="task_list"),
    path("<int:pk>/", TaskDetailView.as_view(),
         name="task_detail"),
    path("create/", TaskCreateView.as_view(),
         name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(),
             name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(),
             name="task_delete"),


]

app_name = "todo"
