# Generated by Django 3.2 on 2021-07-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_posts_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]