# Generated by Django 2.0 on 2018-01-25 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_reading', '0004_slugs_20180102_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicationrole',
            options={'ordering': ('role_order', 'role_name'), 'verbose_name': 'Publication role'},
        ),
        migrations.AlterModelOptions(
            name='publicationseries',
            options={'ordering': ('title_sort',), 'verbose_name': 'Publication series', 'verbose_name_plural': 'Publication series'},
        ),
    ]
