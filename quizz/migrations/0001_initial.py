# Generated by Django 3.1.3 on 2021-05-29 19:31

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=6, unique=True)),
                ('course_name', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=300, null=True, verbose_name='Course Description')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=3, unique=True)),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd', models.DateField(blank=True, null=True)),
                ('no', models.CharField(help_text='10-digit phone number', max_length=10, unique=True)),
                ('joined', models.DateField(blank=True, null=True)),
                ('deptstud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizz.department')),
                ('enrolled', models.ManyToManyField(to='quizz.Course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('total_marks', models.IntegerField(blank=True, default=4, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('time_limit', models.DurationField(help_text='HH:MM:SS format')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=200, verbose_name='Question Description')),
                ('imageq', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Question Image')),
                ('choice_text', models.CharField(max_length=20)),
                ('is_selected', models.BooleanField(blank=True, default=False, null=True, verbose_name='Selected Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
                ('course_exam', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quizz.course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('created', models.DateField(blank=True, null=True)),
                ('course_faculty', models.ManyToManyField(to='quizz.Course')),
                ('dept_faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizz.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.department'),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('submitted', models.DateTimeField(auto_now_add=True, null=True)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizz')),
                ('studenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.student')),
            ],
        ),
    ]
