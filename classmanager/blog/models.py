from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
# from django.contrib.auth.models import AbstractUser
from classroom.models import Teacher

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


#
# class User(AbstractUser):
#     pass

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='blog_1images/', blank=True, default='blog_1images/defaultblog.jpg')
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Post')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
