from django.db import models


# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title must be longer than 2 characters buddy"

        if len(post_data['network']) < 2:
            errors['network'] = "Network must be longer than 2 characters buddy"

        if (post_data['release_date']) == "":
            errors['release_date'] = "Enter a proper date buddy"
        
        if len(post_data['desc']) < 10:
            errors['desc'] = "Description must be longer than 10 characters buddy"
        return errors
    def edit_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title must be longer than 2 characters buddy"

        if len(post_data['network']) < 2:
            errors['network'] = "Network must be longer than 2 characters buddy"

        if (post_data['release_date']) == "":
            errors['release_date'] = "Enter a proper date buddy"
        
        if len(post_data['desc']) < 10:
            errors['desc'] = "Description must be longer than 10 characters buddy"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()