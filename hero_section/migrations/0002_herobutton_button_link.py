# Generated by Django 4.2.16 on 2024-09-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herobutton',
            name='button_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
