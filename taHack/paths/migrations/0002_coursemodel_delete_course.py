# Generated by Django 4.2.7 on 2023-11-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseTitle', models.CharField(max_length=255)),
                ('CourseDescription', models.TextField()),
                ('Author', models.CharField(max_length=100)),
                ('Duration', models.DurationField()),
                ('Rating', models.IntegerField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]