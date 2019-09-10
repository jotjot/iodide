# Generated by Django 2.2.5 on 2019-09-05 15:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notebooks', '0003_notebook_revisions_most_recent_first'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', help_text='The status of the remote operation, string-based for easier inspection', max_length=10)),
                ('backend', models.CharField(help_text="The slug of the remote kernel backend, e.g. 'query'", max_length=24)),
                ('parameters', django.contrib.postgres.fields.jsonb.JSONField(help_text='The parameters as provided as part of the remote chunk content')),
                ('filename', models.CharField(blank=True, help_text='The filename as provided as part of the remote chunk content', max_length=120, null=True)),
                ('snippet', models.TextField(help_text='The actual snippet to be sent to the remote kernel for processing, e.g a SQL query')),
                ('scheduled_at', models.DateTimeField(auto_now_add=True, help_text='The datetime when the remote operation was first created')),
                ('started_at', models.DateTimeField(blank=True, help_text='The datetime when the remote operation started running', null=True)),
                ('ended_at', models.DateTimeField(blank=True, help_text='The datetime when the remote operation was completed successfully', null=True)),
                ('failed_at', models.DateTimeField(blank=True, help_text='The datetime when the remote operation failed at', null=True)),
                ('notebook', models.ForeignKey(help_text='A back-reference for use in the file modal', on_delete=django.db.models.deletion.CASCADE, related_name='remote_operations', to='notebooks.Notebook')),
            ],
            options={
                'verbose_name': 'Remote Operation',
                'verbose_name_plural': 'Remote Operations',
                'ordering': ('-scheduled_at',),
                'unique_together': {('notebook', 'filename')},
            },
        ),
        migrations.CreateModel(
            name='RemoteFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=120)),
                ('content', models.BinaryField(max_length=10485760)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The datetime when the remote file was first created')),
                ('refreshed_at', models.DateTimeField(auto_now_add=True, help_text='The datetime when the remote file was last refreshed at')),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebooks.Notebook')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote.RemoteOperation')),
            ],
            options={
                'verbose_name': 'Remote file',
                'verbose_name_plural': 'Remote files',
                'ordering': ('id',),
                'abstract': False,
                'unique_together': {('notebook', 'filename')},
            },
        ),
    ]