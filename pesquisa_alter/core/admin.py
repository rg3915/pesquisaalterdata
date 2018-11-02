from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone','cdalterdata')
    search_fields = ('cdalterdata','name', 'email')
    #list_filter = ('gender',)