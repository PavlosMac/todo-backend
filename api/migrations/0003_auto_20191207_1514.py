# Generated by Django 3.0 on 2019-12-07 15:14

from django.db import migrations
from datetime import datetime

def update_date_created(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Todo = apps.get_model("api", "Todo")
    for todo in Todo.objects.all():
        todo.date_created = datetime.now()
        todo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191207_1504'),
    ]

    operations = [
        migrations.RunPython(update_date_created)
    ]
