# Generated by Django 3.0.3 on 2020-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200220_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
