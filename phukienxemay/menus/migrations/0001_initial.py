# Generated by Django 2.1.1 on 2018-09-26 09:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sub_menu_name', models.CharField(max_length=100)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='menus.Menu')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]