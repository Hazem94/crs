# Generated by Django 2.1.5 on 2019-01-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0005_auto_20190106_1635'),
        ('feedback', '0002_auto_20181229_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField()),
                ('email', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rater.Book')),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]