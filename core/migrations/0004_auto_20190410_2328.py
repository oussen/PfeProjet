# Generated by Django 2.1.7 on 2019-04-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evenement_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postule',
            name='upload_cv',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]