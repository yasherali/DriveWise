# Generated by Django 4.2.2 on 2023-07-02 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_customuser_is_staff_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]