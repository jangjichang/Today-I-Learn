# Generated by Django 2.1 on 2019-04-24 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workmanagement', '0003_auto_20190424_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workmanagement.Card'),
            preserve_default=False,
        ),
    ]