# Generated by Django 2.1.1 on 2018-09-27 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='sub_menu_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='menus.SubMenu'),
        ),
    ]