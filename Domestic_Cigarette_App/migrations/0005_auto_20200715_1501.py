# Generated by Django 3.0.8 on 2020-07-15 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Domestic_Cigarette_App', '0004_domestic_cigarette_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domestic_cigarette_comment',
            name='Object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Domestic_Cigarette_App.Domestic_Cigarette'),
        ),
    ]