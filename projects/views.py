from django.shortcuts import redirect
from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
# 1st- list view
# class ModelNameListView(ListView):
#     model = ModelName
#     template_name = "model_names/list.html"


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("home")

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
