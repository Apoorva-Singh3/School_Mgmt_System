from django.db import models

# Models created here

# School model
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# Student model
class Student(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    enrollment = models.Field(unique=True)
    school_id = models.ForeignKey(School, on_delete=models.DO_NOTHING, default=1) 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
