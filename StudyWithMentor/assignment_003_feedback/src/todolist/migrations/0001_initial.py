# Generated by Django 2.1 on 2019-05-01 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-modify_date'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('deadline', models.DateField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modify_date'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modify_date'],
            },
        ),
        migrations.AddField(
            model_name='card',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.Work'),
        ),
        migrations.AddField(
            model_name='activity',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.Card'),
        ),
        migrations.AddField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
