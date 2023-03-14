# Generated by Django 4.1.6 on 2023-03-10 09:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_todolist_date_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projectlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание проекта')),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания проекта')),
                ('date_completed', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата выполнения')),
            ],
        ),
        migrations.AddField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.projectlist', verbose_name='Проект'),
        ),
    ]