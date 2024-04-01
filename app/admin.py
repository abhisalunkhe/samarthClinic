from django.contrib import admin
from .models import *

class adminPanelDoctor(admin.ModelAdmin):
    list_display = ['doctorName','doctorDepartment']

class adminPanelAppontment(admin.ModelAdmin):
    list_display = ['patientName','appointmentDoctorName','appointmentDate', 'isDone']

class adminPanelTestimonial(admin.ModelAdmin):
    list_display = ['patientName','patientProfession']

class adminPanelNewsletter(admin.ModelAdmin):
    list_display = ['email']

class adminPanelContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

# Register your models here.
admin.site.register(Doctor, adminPanelDoctor)
admin.site.register(Appointment, adminPanelAppontment)
admin.site.register(Testimonial, adminPanelTestimonial)
admin.site.register(Newsletter, adminPanelNewsletter)
admin.site.register(Contact, adminPanelContact)