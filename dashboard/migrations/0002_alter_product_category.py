# Generated by Django 4.2.11 on 2024-06-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Drinks', 'Drinks'), ('Cooking Utensil', 'Cooking Utensil'), ('Personal Hygiene', 'Personal Hygiene')], max_length=20, null=True),
        ),
    ]