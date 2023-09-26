# Generated by Django 4.2.5 on 2023-09-26 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название урока')),
                ('url_link', models.URLField(blank=True, null=True, verbose_name='URL на урок')),
                ('video_duration', models.PositiveIntegerField(default=0, verbose_name='Продолжительность')),
                ('products', models.ManyToManyField(to='application.product')),
            ],
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Просмотрено', 'Viewed'), ('Не просмотрено', 'Not Viewed')], default='Не просмотрено', max_length=30)),
                ('video_view', models.PositiveIntegerField(default=0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='lesson.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
