from django.db import models


# Create your models here.Models are basically the tables, each model represents a table in the database.




class Article(models.Model):  # This is basically deciding the schema of the table
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    # add thumbnail later
    # add in author later






# Migrations python manage.py migrate
# these 2 are the steps to do each time there is a change in the models
# python manage.py makemigrations
# python manage.py migrate
# open the interactive shell python manage.py shell  https://www.youtube.com/watch?v=eio1wDUHFJE&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=8
