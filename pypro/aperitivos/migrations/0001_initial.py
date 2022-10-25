# Generated by Django 4.1.2 on 2022-10-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('vimeo_id', models.CharField(max_length=50)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
