# Generated by Django 4.1.13 on 2024-09-24 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hero_section', '0007_technologysvg_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cta',
            fields=[
                ('autocreateupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hero_section.autocreateupdate')),
                ('cta_title', models.CharField(blank=True, max_length=250, null=True)),
                ('cta_subtitle', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'CTA',
                'verbose_name_plural': 'CTAs',
            },
            bases=('hero_section.autocreateupdate', models.Model),
        ),
        migrations.CreateModel(
            name='CtaButton',
            fields=[
                ('autocreateupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hero_section.autocreateupdate')),
                ('button_name', models.CharField(blank=True, max_length=255, null=True)),
                ('button_link', models.TextField(blank=True, null=True)),
                ('ctas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cta.cta')),
            ],
            options={
                'verbose_name': 'CTA Button',
                'verbose_name_plural': 'CTA Buttons',
            },
            bases=('hero_section.autocreateupdate', models.Model),
        ),
    ]
