# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-01 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import share.models.fields
import share.models.ingest
import share.models.jobs


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0048_auto_20171113_1852'),
    ]

    operations = [
        # Operations that don't require database changes, but Django would make changes anyway.
        migrations.SeparateDatabaseAndState(state_operations=[

            # Rename RawDatum.logs to RawDatum.jobs, without renaming anything in the database.
            # Django would not allow adding a model for the auto-generated through table.
            migrations.RenameField(
                model_name='rawdatum',
                old_name='logs',
                new_name='jobs',
            ),
            migrations.CreateModel(
                name='RawDatumJob',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('datum', models.ForeignKey(db_column='rawdatum_id', on_delete=django.db.models.deletion.CASCADE, to='share.RawDatum')),
                    ('job', models.ForeignKey(db_column='harvestlog_id', on_delete=django.db.models.deletion.CASCADE, to='share.HarvestLog')),
                ],
                options={
                    'db_table': 'share_rawdatum_logs',
                },
            ),
            migrations.AlterField(
                model_name='rawdatum',
                name='jobs',
                field=models.ManyToManyField(related_name='raw_data', through='share.RawDatumJob', to='share.HarvestLog'),
            ),

            # Rename SourceConfig.harvest_logs to harvest_jobs.
            # Django would drop/add the FK index.
            migrations.AlterField(
                model_name='harvestlog',
                name='source_config',
                field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='harvest_jobs', to='share.SourceConfig'),
            ),

            # Rename model without renaming table.
            # Django would drop/add RawDatumJob.job FK index.
            migrations.AlterModelTable(
                name='harvestlog',
                table='share_harvestlog',
            ),
            migrations.RenameModel('HarvestLog', 'HarvestJob'),
        ]),

        migrations.CreateModel(
            name='IngestJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField(null=True)),
                ('status', models.IntegerField(choices=[(0, 'Enqueued'), (1, 'In Progress'), (2, 'Failed'), (3, 'Succeeded'), (4, 'Rescheduled'), (6, 'Forced'), (7, 'Skipped'), (8, 'Retrying'), (9, 'Cancelled')], db_index=True, default=0)),
                ('claimed', models.NullBooleanField()),
                ('error_type', models.TextField(blank=True, db_index=True, null=True)),
                ('error_message', models.TextField(blank=True, db_column='message', null=True)),
                ('error_context', models.TextField(blank=True, db_column='context', default='')),
                ('completions', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('share_version', models.TextField(default=share.models.jobs.get_share_version, editable=False)),
                ('source_config_version', models.PositiveIntegerField()),
                ('transformer_version', models.PositiveIntegerField()),
                ('regulator_version', models.PositiveIntegerField()),
                ('transformed_datum', share.models.fields.DateTimeAwareJSONField(null=True)),
                ('regulated_datum', share.models.fields.DateTimeAwareJSONField(null=True)),
                ('retries', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegulatorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('node_id', models.TextField(null=True)),
                ('rejected', models.BooleanField()),
                ('ingest_job', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='regulator_logs', to='share.IngestJob')),
            ],
        ),
        migrations.AlterModelManagers(
            name='sourceconfig',
            managers=[
                ('objects', share.models.ingest.SourceConfigManager('label')),
            ],
        ),

        # Rename field without altering db column
        migrations.AlterField(
            model_name='harvestjob',
            name='context',
            field=models.TextField(blank=True, db_column='context', default=''),
        ),
        migrations.RenameField(
            model_name='harvestjob',
            old_name='context',
            new_name='error_context',
        ),

        migrations.AddField(
            model_name='harvestjob',
            name='claimed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='harvestjob',
            name='error_message',
            field=models.TextField(blank=True, db_column='message', null=True),
        ),
        migrations.AddField(
            model_name='harvestjob',
            name='error_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rawdatum',
            name='datestamp',
            field=models.DateTimeField(help_text='The most relevant datetime that can be extracted from this RawDatum. This may be, but is not limited to, a deletion, modification, publication, or creation datestamp. Ideally, this datetime should be appropriate for determining the chronological order its data will be applied.', null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='home_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sourceconfig',
            name='full_harvest',
            field=models.BooleanField(default=False, help_text='Whether or not this SourceConfig should be fully harvested. Requires earliest_date to be set. The schedule harvests task will create all jobs necessary if this flag is set. This should never be set to True by default. '),
        ),
        migrations.AddField(
            model_name='ingestjob',
            name='raw',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='ingest_jobs', to='share.RawDatum'),
        ),
        migrations.AddField(
            model_name='ingestjob',
            name='source_config',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='ingest_jobs', to='share.SourceConfig'),
        ),
        migrations.AddField(
            model_name='ingestjob',
            name='suid',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='ingest_jobs', to='share.SourceUniqueIdentifier'),
        ),
        migrations.AddField(
            model_name='ingestjob',
            name='ingested_normalized_data',
            field=models.ManyToManyField(related_name='ingest_jobs', to='share.NormalizedData'),
        ),
        migrations.AlterUniqueTogether(
            name='ingestjob',
            unique_together=set([('raw', 'source_config_version', 'transformer_version', 'regulator_version')]),
        ),
    ]
