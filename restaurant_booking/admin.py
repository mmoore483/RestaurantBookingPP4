from django.contrib import admin
from .models import Customer, Reservation, Table
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')