# Generated by Django 4.1.7 on 2023-03-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CZ', 'Cheese'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CR', 'Curd'), ('IC', 'Ice-Creams'), ('ML', 'Milk')], max_length=2)),
                ('Product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
