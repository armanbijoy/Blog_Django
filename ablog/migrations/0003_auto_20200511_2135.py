# Generated by Django 3.0.5 on 2020-05-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0002_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='Coding', max_length=255),
        ),
    ]
