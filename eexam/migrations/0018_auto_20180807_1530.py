# Generated by Django 2.0.7 on 2018-08-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eexam', '0017_blog_useremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
