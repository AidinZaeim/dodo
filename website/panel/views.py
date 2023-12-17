from django.shortcuts import render
from django.views import View
from .models import Project
# Create your views here.


# class Management(View):

#     def get(self,request):
#         return render(request,"panel/management.html")
#------------------------------------
class ProjectDetail(View):

    def get(self,request,id):
        projects_obj = Project.objects.get(id=id)
        sections = projects_obj.sections.all()
        


        Info = {
            'project' : projects_obj,
            'sections' : sections,
        }


        return render(request,"panel/projectDetail.html",Info) 
#------------------------------------    
