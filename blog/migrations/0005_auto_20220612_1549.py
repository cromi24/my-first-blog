# Generated by Django 3.2.13 on 2022-06-12 12:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_total_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='total_views',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.DeleteModel(
            name='Ip',
        ),
        migrations.AddField(
            model_name='postviews',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
