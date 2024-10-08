# Generated by Django 4.1.13 on 2024-09-25 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hero_section', '0007_technologysvg_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('autocreateupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hero_section.autocreateupdate')),
                ('client_name', models.CharField(max_length=255)),
                ('client_position', models.CharField(help_text='e.g., Founder @ Rolex', max_length=255)),
                ('feedback', models.TextField()),
                ('star_rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('author_image', models.ImageField(upload_to='testimonials/')),
                ('company_name', models.CharField(max_length=255)),
            ],
            bases=('hero_section.autocreateupdate', models.Model),
        ),
        migrations.CreateModel(
            name='TestimonialSection',
            fields=[
                ('autocreateupdate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hero_section.autocreateupdate')),
                ('title', models.CharField(default='What our Clients Say', max_length=255)),
                ('subtitle', models.CharField(default='Testimonials', max_length=255)),
                ('description', models.TextField(default='There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration in some form.')),
            ],
            options={
                'verbose_name': 'Testimonial Section',
                'verbose_name_plural': 'Testimonial Sections',
            },
            bases=('hero_section.autocreateupdate', models.Model),
        ),
    ]
