# Generated by Django 3.0.5 on 2020-05-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0003_auto_20200511_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]