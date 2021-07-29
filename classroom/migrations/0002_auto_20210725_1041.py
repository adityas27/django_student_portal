# Generated by Django 3.2.5 on 2021-07-25 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module', '0001_initial'),
        ('assignment', '0001_initial'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(to='module.Module'),
        ),
        migrations.AddField(
            model_name='course',
            name='questions',
            field=models.ManyToManyField(to='question.Question'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('graded', 'Graded')], default='pending', max_length=10, verbose_name='Status')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('graded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.submission')),
            ],
        ),
    ]
