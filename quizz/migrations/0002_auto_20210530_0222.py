# Generated by Django 3.1.3 on 2021-05-29 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizz',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='is_selected',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_selected', models.BooleanField(blank=True, default=False, null=True, verbose_name='Selected Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.quizz')),
            ],
        ),
    ]
