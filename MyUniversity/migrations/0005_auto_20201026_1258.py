# Generated by Django 3.1.2 on 2020-10-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUniversity', '0004_auto_20201026_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
