from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=300)
    release_date = models.DateField()
    main_actors = models.CharField(max_length=300)
    genre = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000)
    poster = models.ImageField(upload_to="movie_posters/",null=True)
    trailer = models.CharField(max_length=300)
    created_by = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default="cinemana")
    password = models.CharField(max_length=200,default="@123#")
    gender = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(upload_to="user_images/")
    created_at = models.DateField(auto_now_add=True)