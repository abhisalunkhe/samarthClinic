from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctorName = models.CharField(max_length = 100)
    doctorDepartment = models.CharField(max_length = 100)
    doctorProfileImage = models.ImageField(upload_to='Doctors')
    facebookLink = models.CharField(max_length = 100)
    twitterLink = models.CharField(max_length = 100)
    instagramLink = models.CharField(max_length = 100)

class Appointment(models.Model):
    patientName = models.CharField(max_length = 100)
    patientEmail = models.CharField(max_length = 100)
    patientPhone = models.CharField(max_length = 10)
    appointmentDoctorName = models.CharField(max_length = 100)
    appointmentDate = models.CharField(max_length = 50)
    appointmentTime = models.CharField(max_length = 50)
    patientProblem = models.TextField()
    isDone = models.BooleanField(default = False)


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    message = models.TextField()

class Testimonial(models.Model):
    patientName = models.CharField(max_length = 100)
    patientProfession = models.CharField(max_length = 100)
    patientImage = models.ImageField(upload_to='Patient Testimonial')
    patientComments = models.TextField()


class Newsletter(models.Model):
    email = models.CharField(max_length = 100)