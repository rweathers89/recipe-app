# Generated by Django 4.2.14 on 2024-08-05 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_difficulty_alter_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('intermediate', 'Intermediate'), ('hard', 'Hard')], default='Easy', max_length=20),
        ),
    ]
