# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-13 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', pyuploadcare.dj.models.ImageField(blank=True)),
                ('name', models.CharField(blank=True, max_length=31)),
                ('caption', models.CharField(blank=True, max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.CharField(default='Hi!', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='insta.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
