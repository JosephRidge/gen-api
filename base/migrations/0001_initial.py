# Generated by Django 5.2.2 on 2025-06-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewGeneratorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_switch_position', models.CharField(blank=True, max_length=20, null=True)),
                ('genset_state', models.CharField(blank=True, max_length=30, null=True)),
                ('current_fault', models.IntegerField(blank=True, null=True)),
                ('current_fault_severity', models.CharField(blank=True, max_length=20, null=True)),
                ('genset_l1_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l2_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l3_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l1_l2_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l2_l3_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l3_l1_rms_voltage', models.FloatField(blank=True, null=True)),
                ('genset_l1_rms_current', models.FloatField(blank=True, null=True)),
                ('genset_l2_rms_current', models.FloatField(blank=True, null=True)),
                ('genset_l3_rms_current', models.FloatField(blank=True, null=True)),
                ('genset_l1_kw', models.FloatField(blank=True, null=True)),
                ('genset_l2_kw', models.FloatField(blank=True, null=True)),
                ('genset_l3_kw', models.FloatField(blank=True, null=True)),
                ('genset_total_kw', models.FloatField(blank=True, null=True)),
                ('genset_l1_kvar', models.FloatField(blank=True, null=True)),
                ('genset_l2_kvar', models.FloatField(blank=True, null=True)),
                ('genset_l3_kvar', models.FloatField(blank=True, null=True)),
                ('genset_total_kvar', models.FloatField(blank=True, null=True)),
                ('genset_l1_kva', models.FloatField(blank=True, null=True)),
                ('genset_l2_kva', models.FloatField(blank=True, null=True)),
                ('genset_l3_kva', models.FloatField(blank=True, null=True)),
                ('genset_total_kva', models.FloatField(blank=True, null=True)),
                ('genset_frequency', models.FloatField(blank=True, null=True)),
                ('battery_voltage', models.FloatField(blank=True, null=True)),
                ('oil_pressure', models.FloatField(blank=True, null=True)),
                ('coolant_temperature', models.FloatField(blank=True, null=True)),
                ('average_engine_speed', models.FloatField(blank=True, null=True)),
                ('start_attempts', models.IntegerField(blank=True, null=True)),
                ('utility_l1_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('utility_l2_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('utility_l3_n_rms_voltage', models.FloatField(blank=True, null=True)),
                ('utility_l1_l2_rms_voltage', models.FloatField(blank=True, null=True)),
                ('utility_l2_l3_rms_voltage', models.FloatField(blank=True, null=True)),
                ('utility_l3_l1_rms_voltage', models.FloatField(blank=True, null=True)),
                ('charging_alternator_voltage', models.FloatField(blank=True, null=True)),
                ('modbus_remote_start', models.CharField(blank=True, max_length=10, null=True)),
                ('modbus_fault_reset', models.CharField(blank=True, max_length=10, null=True)),
                ('network_shutdown_modbus_command', models.CharField(blank=True, max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
