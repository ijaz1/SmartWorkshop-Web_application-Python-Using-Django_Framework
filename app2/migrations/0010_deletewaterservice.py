# Generated by Django 3.2.7 on 2022-01-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0009_addwaterservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletewaterservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]