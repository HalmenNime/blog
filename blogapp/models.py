from django.db import models
from django.urls import reverse
# Створення модель і класс
class Category(models.Model):
    category_name = models.CharField(max_length=25)
# Створенная класса поста
class Post(models.Model):
    post_header = models.CharField(max_length=100)
    post_text = models.TextField()
    author = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default = "no category")
    image = models.ImageField(upload_to="images/", default=None, null=True)
    # Функция для получення пост і його потрібним айді
    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)])
