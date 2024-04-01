from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'doctors': doctors,
        'testimonials': testimonials
    }
    return render(request,'index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        record = Contact.objects.create(name = name, email = email, subject = subject, message = message)
        record.save()
        messages.success(request, 'Your response is saved. We will get back to you soon!!!')
        return redirect('/')
    else:
        return render(request,'contact.html')

def appointment(request):
    if request.method == "POST":
        patientName = request.POST['name']
        patientEmail = request.POST['email']
        patientPhone = request.POST['phone']
        appointmentDoctorName = request.POST['doctor']
        appointmentDate = request.POST['date']
        appointmentTime = request.POST['time']
        patientProblem = request.POST['problem']

        appointment = Appointment.objects.filter(appointmentTime = appointmentTime, appointmentDate = appointmentDate)
        if appointment:
            messages.error(request, 'Please select another time for the appointment as this slot is engaged!!!')
            return redirect('/')
        else:
            record = Appointment.objects.create(patientName = patientName,patientEmail = patientEmail,patientPhone = patientPhone,appointmentDoctorName = appointmentDoctorName,appointmentDate = appointmentDate,appointmentTime = appointmentTime,patientProblem = patientProblem)
            record.save()
            messages.success(request, 'Appointment is successfully made! Reach the location on time!!!')
            return redirect('/')
    else:
        return render('/')
    

def newsletter(request):
    if request.method == "POST":
        email = request.POST['email']

        record = Newsletter.objects.create(email = email)
        record.save()
        messages.success(request, 'Successfully subscribed to our newsletter. You will receive our latest updates on email!!!')
        return redirect('/')