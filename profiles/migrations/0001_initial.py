# Generated by Django 4.1.3 on 2023-02-24 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_email', models.EmailField(default='', max_length=254)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_wishlist', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wishlist', to='profiles.userprofile')),
            ],
        ),
    ]
