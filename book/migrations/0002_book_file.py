# Generated by Django 5.1.2 on 2024-10-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, upload_to='book_file/'),
        ),
    ]
