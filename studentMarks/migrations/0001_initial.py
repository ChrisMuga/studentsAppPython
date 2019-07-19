# Generated by Django 2.2.3 on 2019-07-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('currentClass', models.CharField(max_length=2)),
                ('emailAddress', models.CharField(max_length=200, unique=True)),
                ('dateOfBirth', models.CharField(max_length=200)),
                ('currentStream', models.CharField(max_length=1)),
            ],
        ),
    ]
