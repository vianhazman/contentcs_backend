# Generated by Django 2.2.5 on 2019-11-11 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0007_auto_20191103_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='course_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='objects.Course'),
        ),
        migrations.AlterField(
            model_name='video',
            name='section_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='objects.Section'),
        ),
    ]
