# Generated by Django 2.2.6 on 2020-05-01 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200501_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='take_friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Friend'),
        ),
    ]
