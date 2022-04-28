# Generated by Django 4.1.dev20220328112539 on 2022-04-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=0, max_length=20)),
                ('username', models.CharField(default=0, max_length=20)),
                ('email', models.CharField(default=0, max_length=30)),
                ('password', models.CharField(default=0, max_length=20)),
                ('level', models.IntegerField(default=1)),
                ('country', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Global',
        ),
    ]
