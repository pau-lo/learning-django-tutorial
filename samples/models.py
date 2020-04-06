from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, default=1,)
    photo = models.ImageField(upload_to="gallery", default='eagle1.jpg')

    def __str__(self):
        return self.title
