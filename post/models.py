from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=150)
    little_title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos')
    big_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=150)
    little_content = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MakepostCat(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name
