# Generated by Django 2.1.7 on 2019-04-10 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_evenement_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.EvenementCategory'),
        ),
    ]