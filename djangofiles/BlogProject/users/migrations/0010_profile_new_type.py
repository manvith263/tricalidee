# Generated by Django 2.2 on 2019-06-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_change_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='new_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Author', 'Author'), ('Reader', 'Reader')], default=None, max_length=20, null=True),
        ),
    ]
