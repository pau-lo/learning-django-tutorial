# Generated by Django 3.0 on 2020-04-06 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_auto_20200406_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(default='eagle1.jpg', upload_to='gallery'),
        ),
    ]
