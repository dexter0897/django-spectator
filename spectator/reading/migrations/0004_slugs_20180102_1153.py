# Generated by Django 2.0 on 2018-01-02 11:53

from django.db import migrations, models
from django.conf import settings
from hashids import Hashids


def generate_slug(value):
    "A copy of spectator.core.models.SluggedModelMixin._generate_slug()"
    alphabet = 'abcdefghijkmnopqrstuvwxyz23456789'
    salt = 'Django Spectator'

    if hasattr(settings, 'SPECTATOR_SLUG_ALPHABET'):
        alphabet = settings.SPECTATOR_SLUG_ALPHABET

    if hasattr(settings, 'SPECTATOR_SLUG_SALT'):
        salt = settings.SPECTATOR_SLUG_SALT

    hashids = Hashids(alphabet=alphabet, salt=salt, min_length=5)

    return hashids.encode(value)


def set_slug(apps, schema_editor, class_name):
    """
    Create a slug for each Object already in the DB.
    """
    Cls = apps.get_model('spectator_reading', class_name)

    for obj in Cls.objects.all():
        obj.slug = generate_slug(obj.pk)
        obj.save(update_fields=['slug'])


def set_publication_slug(apps, schema_editor):
    set_slug(apps, schema_editor, 'Publication')

def set_publicationseries_slug(apps, schema_editor):
    set_slug(apps, schema_editor, 'PublicationSeries')


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_reading', '0003_publication_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(blank=True, default='a', max_length=10),
            preserve_default=False,
        ),
        migrations.RunPython(set_publication_slug),
        migrations.AlterField(
            model_name='publicationseries',
            name='slug',
            field=models.SlugField(blank=True, default='a', max_length=10),
            preserve_default=False,
        ),
        migrations.RunPython(set_publicationseries_slug),
    ]