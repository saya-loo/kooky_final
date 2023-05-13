from django.db import models
from django.contrib import auth


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    name = models.CharField(max_length=50)
    cooking = models.IntegerField()
    crop = models.IntegerField()
    instruction = models.TextField(max_length=500)
    rating = models.IntegerField(default=1)
    calories = models.IntegerField()
    total = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='photo/')

    class difficulty(models.TextChoices):
        EASY = "EASY", "Easy"
        MEDIUM = "MEDIUM", "Medium"
        HARD = "HARD", "Hard"
    level = models.CharField(choices=difficulty.choices, max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField(max_length=150)
    rating = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    image = models.ImageField(blank=False)


