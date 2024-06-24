# Generated by Django 4.2.11 on 2024-06-23 17:12

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
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Rice', 'Rice'), ('Banana', 'Banana'), ('Milk', 'Milk'), ('Sugar', 'Sugar'), ('Coffee', 'Coffee'), ('Noodle', 'Noodle'), ('Bread', 'Bread')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]