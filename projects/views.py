# from django.shortcuts import redirect
from django.views.generic.list import ListView
from projects.models import Project

# Create your views here
# 1st- list view
# class ModelNameListView(ListView):
#     model = ModelName
#     template_name = "model_names/list.html"


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"

    # def get_queryset(self):
    #     return Project.objects.filter(members=self.request.user)
