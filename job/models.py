from django.db import models

# Create your models here.

Job_TYPE = {
    'Full Time':'Full_Time',
    'Part TIme':'Part_TIme',
}



class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=Job_TYPE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(default=0)
    vacancy = models.IntegerField(default=1) 
    experience = models.IntegerField(default=1)

    def __str__ (self):
       return self.title

