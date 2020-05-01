# Generated by Django 2.2.6 on 2020-05-01 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200424_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FriendName', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='take_friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.Friend'),
        ),
    ]
