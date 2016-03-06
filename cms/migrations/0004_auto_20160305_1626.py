# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20160305_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '\u6210\u5458', 'verbose_name_plural': '\u6210\u5458'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '\u7814\u7a76\u9879\u76ee', 'verbose_name_plural': '\u7814\u7a76\u9879\u76ee'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Member', verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category', verbose_name='\u6587\u7ae0\u5206\u7c7b'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='\u6b63\u6587'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_url',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='\u5c01\u9762\u56fe\u94fe\u63a5'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='member',
            name='intro',
            field=models.TextField(blank=True, null=True, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u6307\u5bfc\u8001\u5e08'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='intro',
            field=models.TextField(blank=True, null=True, verbose_name='\u9879\u76ee\u4ecb\u7ecd'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(through='cms.Membership', to='cms.Member', verbose_name='\u6240\u6709\u6210\u5458'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
    ]