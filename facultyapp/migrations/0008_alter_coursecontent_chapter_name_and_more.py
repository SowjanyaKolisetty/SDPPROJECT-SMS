# Generated by Django 5.0 on 2024-02-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0007_rename_contentimage_coursecontent_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='chapter_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='chapter_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='topic',
            field=models.CharField(max_length=100),
        ),
    ]
