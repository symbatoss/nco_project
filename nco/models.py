from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Photos(models.Model):

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
    photo = models.ImageField(upload_to='photo')
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Category(models.Model):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    name = models.CharField(max_length=255)


class Laws(models.Model):

    class Meta:
        verbose_name = "Закон"
        verbose_name_plural = "Законы"
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Posts(models.Model):

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


class Favourites(models.Model):
    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
    bools = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news")


