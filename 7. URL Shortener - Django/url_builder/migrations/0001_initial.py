# Generated by Django 4.0.3 on 2022-03-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initUrl', models.URLField(unique=True)),
                ('shortcutCode', models.CharField(max_length=6, unique=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date of creation of the shorcut')),
                ('username', models.CharField(max_length=20)),
                ('numberAccess', models.IntegerField(default=0)),
            ],
        ),
    ]
