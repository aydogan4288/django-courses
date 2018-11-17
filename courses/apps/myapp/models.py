from __future__ import unicode_literals
from django.db import models
import re
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name must contain at least 5 characters!"
        if not NAME_REGEX.match(postData['name']):
            errors['name'] = 'Name cannot contain special characters!'

        if len(postData['description']) < 15:
            errors['description'] = "Description must contain at least 15 characters!"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __str__(self):
        return self.name
