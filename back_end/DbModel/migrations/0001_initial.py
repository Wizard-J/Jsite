# Generated by Django 2.2.2 on 2019-09-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='其它', max_length=20)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('createdBy', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='未命名', max_length=50)),
                ('author', models.CharField(default='未署名', max_length=50)),
                ('content', models.TextField(default='')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('createdBy', models.CharField(max_length=50)),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbModel.Tag')),
            ],
        ),
    ]
