# Generated by Django 4.1.3 on 2022-11-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=9, null=True)),
                ('timeslot', models.CharField(choices=[('7-9 am', '7-9 am '), ('9-11 am', '9-11 am '), ('11-1 pm', '11-1 pm '), ('2-4 pm', '2-4 pm '), ('4-6 pm', '4-6 pm ')], max_length=9, null=True)),
                ('unitName', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('lecturer', models.CharField(max_length=100)),
            ],
        ),
    ]