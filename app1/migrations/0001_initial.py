# Generated by Django 3.2.7 on 2021-12-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signuptb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('phonenumber', models.BigIntegerField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
