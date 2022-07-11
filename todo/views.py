from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task



class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    queryset = Tag.objects.all()
    context_object_name = "tags"
    success_url = reverse_lazy("todo:tag_list")


class TagDetailView(generic.DetailView):
    model = Tag
    success_url = reverse_lazy("todo:tag_detail")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag_list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("todo:task_list")


class TaskDetailView(generic.DetailView):
    model = Task
    success_url = reverse_lazy("todo:task_detail")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
