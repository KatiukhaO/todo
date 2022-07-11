from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "create_task", "deadline", "done")
    search_fields = ("tags", "content")
    list_filter = ("tags",)
