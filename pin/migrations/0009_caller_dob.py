# Generated by Django 4.1.1 on 2023-01-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0008_caller_education_caller_gender_caller_management_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caller',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]