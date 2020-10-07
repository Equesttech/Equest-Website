from django.db import models
from django.contrib.auth.models import AbstractUser
from classroom.models import User


# Create your models here.
# class User(AbstractUser):
#     pass


# Alternative is to use choices if data is static, but this looks cleaner
# https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
class Course(models.Model):
    COURSE_CHOICES = (
        ('Data Science', 'Data Science'),
        ('Python', 'Python'),
        ('ArchiCAD', 'ArchiCAD'),
        ('AutoCAD', 'AutoCAD'),
        ('Web Development', 'Web Development')

    )
    course = models.CharField(choices=COURSE_CHOICES, max_length=100, default="")

    def __str__(self):
        return f"{self.course}"

class Topic(models.Model):
    group = models.CharField(max_length=16)
    topic = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.group} {self.topic}"

class Question(models.Model):
    title = models.CharField(max_length=128, null=True)
    content = models.CharField(max_length=2000) # ~350-400 words
    image = models.ImageField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userqns")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjectqns")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="lvlqns")
    datetime_created = models.DateTimeField(auto_now_add=True)
    saved_by = models.ManyToManyField(User, blank=True, related_name="savedqns")

    def __str__(self):
        return f"{self.user}: {self.content}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="qnans")
    content = models.TextField()    # Trying out TextField instead of CharField
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userans")
    datetime_created = models.DateTimeField(auto_now_add=True)
    upvoted_by = models.ManyToManyField(User, blank=True, related_name="upvotedans")
    downvoted_by = models.ManyToManyField(User, blank=True, related_name="downvotedans")

    def __str__(self):
        return f"{self.user} answered: {self.content}"