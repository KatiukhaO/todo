from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TagForm, TaskForm, SearchForm
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
    queryset = Task.objects.all().prefetch_related(
        "tags").order_by("done", "-create_task")
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("todo:task_list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.request.GET.get("tags", "")
        context["search_form"] = SearchForm(initial={"tags": tags})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(tags__name__icontains=form.cleaned_data["tags"])
        return self.queryset


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


def change_status_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse("todo:task_list"))
