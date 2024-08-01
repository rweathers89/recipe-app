# Generated by Django 4.2.14 on 2024-08-01 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_pic_alter_recipe_cooking_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
    ]
