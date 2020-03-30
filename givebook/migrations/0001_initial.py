# Generated by Django 2.2 on 2020-03-30 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookadd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('Bookadd_img', models.ImageField(upload_to='images/')),
                ('isbno', models.IntegerField(unique=True)),
                ('availability', models.IntegerField(default=1)),
                ('pageno', models.IntegerField(null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]