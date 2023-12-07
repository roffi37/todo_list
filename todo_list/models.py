from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(null=False, default=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_at")
