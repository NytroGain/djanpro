# Generated by Django 2.0.7 on 2018-07-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eexam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
            ],
        ),
    ]
