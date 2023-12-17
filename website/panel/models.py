from django.db import models
from accounts.models import User
#------------------------------------
class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User,null=True,blank=True,related_name="projects",on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name="member_of_project")

    def __str__(self):
        return self.name
#------------------------------------
class Section(models.Model):
    project = models.ForeignKey(Project, related_name="sections",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#------------------------------------
class Task(models.Model):
    creator = models.ForeignKey(User,related_name="craeted_tasks",on_delete=models.CASCADE)
    under_taker = models.ForeignKey(User,null=True,blank=True,related_name="tasks",on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    check_box = models.BooleanField(default=False)
    priority = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    secion = models.ForeignKey(Section, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.label
#------------------------------------
class Label(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name="labels", on_delete=models.CASCADE)
#------------------------------------