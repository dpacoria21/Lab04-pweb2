# Generated by Django 4.0.5 on 2022-06-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_alter_persona_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
