# Generated by Django 2.2.6 on 2020-04-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talpynroot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Name of article')),
                ('article_text', models.TextField(verbose_name='Text of Article')),
                ('pub_date', models.DateTimeField(verbose_name='Date of publication')),
            ],
        ),
    ]