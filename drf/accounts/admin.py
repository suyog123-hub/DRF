from django.contrib import admin
from django.contrib.auth.models import Group , Permission
from django.contrib.contenttypes.models import ContentType
from crud.models import Contact

# Register your models here.

group , created =Group.objects.get_or_create(name='Contactmanager')
content_type = ContentType.objects.get_for_model(Contact)
permission = Permission.objects.filter(content_type=content_type)
group.permissions.set(permission)
group.save()
