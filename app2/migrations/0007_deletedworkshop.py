# Generated by Django 3.2.7 on 2021-12-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_alter_addemployees_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletedworkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshopname', models.CharField(max_length=20)),
                ('workshopplace', models.CharField(max_length=20)),
                ('phonenumber', models.BigIntegerField()),
                ('workshopemail', models.CharField(max_length=20)),
                ('workshoppassword', models.CharField(max_length=10)),
            ],
        ),
    ]
