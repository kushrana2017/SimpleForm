# Generated by Django 2.2.13 on 2020-06-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('number', models.CharField(default='', max_length=13)),
                ('paddress', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LogInInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
