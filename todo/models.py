from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=False)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("todo:tag_detail", kwargs={"slug": self.slug})


class Task(models.Model):
    content = models.TextField()
    create_task = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("todo:task_detail", kwargs={"pk": self.pk})
