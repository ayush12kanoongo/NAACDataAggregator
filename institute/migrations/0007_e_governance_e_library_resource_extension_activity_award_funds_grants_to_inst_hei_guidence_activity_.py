# Generated by Django 3.2.5 on 2022-11-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0006_category_seat_reservation_exam_result_mou_mou_activity_program_revision'),
    ]

    operations = [
        migrations.CreateModel(
            name='E_governance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('implementation_year', models.IntegerField(blank=True, null=True)),
                ('doc_link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='E_library_resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('subscription_details', models.CharField(blank=True, max_length=100, null=True)),
                ('subscription_expenditure', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('doc_link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Extension_activity_award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(blank=True, max_length=50, null=True)),
                ('award_name', models.CharField(blank=True, max_length=50, null=True)),
                ('awarding_agency_name', models.CharField(blank=True, max_length=50, null=True)),
                ('year_of_awarding', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funds_grants_to_inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(blank=True, max_length=50, null=True)),
                ('grant_purpose', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('fund_amount', models.IntegerField(blank=True, null=True)),
                ('audit_doc_link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hei_guidence_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(blank=True, max_length=50, null=True)),
                ('year_of_conduction', models.IntegerField(blank=True, null=True)),
                ('number_of_students_enrolled', models.IntegerField(blank=True, null=True)),
                ('number_of_students_placed', models.IntegerField(blank=True, null=True)),
                ('document_link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prof_dev_skill_enhan_ext_outrch_prog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_title', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('no_of_participants', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('agency_or_organizing_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('outrch_prog_scheme_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sports_cultural_event_by_intitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=50, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop_seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_workshop_seminar', models.CharField(blank=True, max_length=50, null=True)),
                ('year_of_conduction', models.IntegerField(blank=True, null=True)),
                ('no_of_participants', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('activity_report_link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]