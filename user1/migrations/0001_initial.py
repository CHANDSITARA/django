# Generated by Django 4.1.1 on 2022-10-29 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('auth_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('moblie_no', models.CharField(blank=True, max_length=50, unique=True)),
                ('tenant_id', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('location_tacking', models.CharField(default=0, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('tenant_id', models.CharField(default=0, max_length=20)),
                ('created_at', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user1.user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user1.teams')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user1.user_profile')),
            ],
        ),
    ]
