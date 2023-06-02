# Generated by Django 4.1.3 on 2023-06-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="content",
            new_name="description",
        ),
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, upload_to="book_covers"),
        ),
    ]