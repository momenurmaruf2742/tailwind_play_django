# Generated by Django 4.2.16 on 2024-09-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_section', '0006_alter_herocontant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologysvg',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
