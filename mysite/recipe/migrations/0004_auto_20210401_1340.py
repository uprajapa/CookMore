# Generated by Django 3.1.6 on 2021-04-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20210328_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.FileField(upload_to='recipe/static/assets/images/'),
        ),
    ]
