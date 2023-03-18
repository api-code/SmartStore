# Generated by Django 4.1.7 on 2023-03-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminHome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Role', models.CharField(max_length=150)),
                ('salary', models.FloatField(max_length=150)),
            ],
        ),
    ]