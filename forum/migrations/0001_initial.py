# Generated by Django 3.1.1 on 2020-09-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='From administration', max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True)),
            ],
        ),
    ]