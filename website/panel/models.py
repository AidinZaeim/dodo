from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser,null=True,blank=True,related_name="projects",on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser,related_name="member_of_project")

    def __str__(self):
        return self.name


class Section(models.Model):
    project = models.ForeignKey(Project, related_name="sections",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    priority_choices = (
        ('a' , 'مهم و فوری'),
        ('b' ,'مهم و غیر فوری'),
        ('c' ,'غیر مهم و فوری'),
        ('d' ,'غیر مهم و غیر فوری'),
    )
    creator = models.ForeignKey(CustomUser,null=True,blank=True,related_name="craeted_tasks",on_delete=models.CASCADE)
    under_taker = models.ForeignKey(CustomUser,null=True,blank=True,related_name="tasks",on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    check_box = models.BooleanField(default=False)
    priority = models.CharField(max_length=1,choices=priority_choices)
    description = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    secion = models.ForeignKey(Section, related_name="tasks", on_delete=models.CASCADE)



    def __str__(self):
        return self.label
