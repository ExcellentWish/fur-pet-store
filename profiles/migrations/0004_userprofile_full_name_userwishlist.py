# Generated by Django 4.1.3 on 2023-02-15 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_color'),
        ('profiles', '0003_userprofile_default_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
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