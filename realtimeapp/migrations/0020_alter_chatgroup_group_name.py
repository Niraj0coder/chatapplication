# Generated by Django 5.0.6 on 2024-06-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtimeapp', '0019_groupmessage_is_read_alter_chatgroup_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]