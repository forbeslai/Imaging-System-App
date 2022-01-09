# Generated by Django 3.2 on 2022-01-09 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_system_app', '0003_alter_bill_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='chemical_fixation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='comments_results',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='contrast_staining',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='cpd',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='cryofixation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='dehydration',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='fd',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='first_dilution_time',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='immunolabelling',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='neg_staining',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='resin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='second_dilution_time',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='sem',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='sem_cost',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='sem_mount',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='specimen_procedure',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='tem_embedding_schedule',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='temp_time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
