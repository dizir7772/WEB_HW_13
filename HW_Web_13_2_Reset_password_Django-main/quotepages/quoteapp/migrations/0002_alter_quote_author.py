# Generated by Django 4.1.7 on 2023-12-20 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quoteapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quoteapp.author"
            ),
        ),
    ]
