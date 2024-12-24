from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField # type: ignore

def get_category_id():
    # Replace with the logic to get the default category ID
    return 1

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField
    location = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True)
    description = models.TextField(blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True)

# blog/models.py

class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    body = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
    category = models.ForeignKey(
        to=Category,
        related_name="posts",
        default=get_category_id,
        on_delete=models.SET_DEFAULT,
        blank=False,
        null=False,
    )

    feature_image = models.ImageField(upload_to="uploads/", null=True, blank=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)