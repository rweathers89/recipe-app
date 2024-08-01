from django.db import models
from django.shortcuts import reverse

# Create your models here.
#difficulty_choices= (('easy', 'Easy'), ('medium', 'Medium'), ('intermediate', 'Intermediate'), ('hard', 'Hard'))

class Recipe(models.Model):
    #recipe_id = models.Count(auto_now_add=True)
    name = models.CharField(max_length=120)
    ingredients = models.TextField(help_text="Separate ingredients by a comma")
    cooking_time = models.FloatField(help_text="minutes")
    pic = models.ImageField(upload_to="recipes", default="no_picture.jpg")
    difficulty = models.CharField(max_length=20, blank=True, null=True)

    # calculate difficulty of recipe using cooking time and number of ingredients
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty

    # Override the save method to calculate difficulty before saving a new recipe via the form
    def save(self, *args, **kwargs):
        self.calculate_difficulty()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Name: {self.name}"
        # return f"id: {self.id} Name: {self.name}"
    
    def get_absolute_url(self):
        return reverse ("recipes:recipes_detail", kwargs={"pk": self.pk})