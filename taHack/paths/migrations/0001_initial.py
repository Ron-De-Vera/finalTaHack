# Generated by Django 4.2.7 on 2023-11-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.AutoField(primary_key=True, serialize=False)),
                ('CourseTitle', models.CharField(max_length=255)),
                ('CourseDescription', models.TextField()),
                ('Author', models.CharField(max_length=100)),
                ('Duration', models.DurationField()),
                ('Rating', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]