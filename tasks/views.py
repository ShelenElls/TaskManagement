from django.shortcuts import render
from django.views.generic.edit import CreateView
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.id])
