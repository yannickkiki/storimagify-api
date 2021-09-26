from django.contrib.auth import hashers
from django.db import migrations


def create_super_user(apps, schema_editor):
    User = apps.get_model('user', 'User')
    User.objects.create(
        username='storimagify',
        password=hashers.make_password('storimagify'),
        is_superuser=True,
        is_staff=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_super_user)
    ]
