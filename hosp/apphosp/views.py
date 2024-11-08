from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'signup.html')


def SignUpAction(request):
    if request.method == "POST":
        nm = request.POST['name']
        em = request.POST['email']
        usr = request.POST['un']
        pwd = request.POST['pas']
        gen = request.POST['gender']
        ph = request.POST['phone']
        data1 = newmember.objects.filter(email=em)
        if data1:
            messages.info(request, 'email already exists')
            return redirect(signUp)
        else:
            data = newmember.objects.create(name=nm, email=em, username=usr, password=pwd, phone_number=ph, gender=gen)
            data.save()
        return HttpResponse("record added!!")


def loginCheck(request):
    if request.method == 'POST':
        em = request.POST['email']
        pwd = request.POST['pass']
        # d = newmember.objects.all()
        # for i in d:
        #     if usr == i.username and pwd == i.password:
        #         return redirect(index)
        # return HttpResponse("Wrong username or password")
        data = newmember.objects.filter(email=em)
        if data:
            data1 = newmember.objects.get(email=em)
            if data1.password == pwd:
                request.session['id'] = em
                return redirect(homepg)
            else:
                messages.info(request, 'invalid E-mail or password')
                return redirect(login)
        else:
            messages.info(request, 'invalid E-mail or password')
            return redirect(login)


def appointmentAction(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        date = request.POST['setTodaysDate']
        dept = request.POST['dpt']
        gn = request.POST['gender']
        ph = request.POST['phone']
        add = request.POST['message']
        pymnt = request.POST['paymentdone']
        data = appointments.objects.create(name=nm, email=em, date=date, department=dept, gender=gn, phone_number=ph,
                                           additional_comments=add, payment=pymnt)
        data.save()

        return HttpResponse("record added!!")


def homepg(request):
    return render(request, 'home.html')


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(index)


def adminlog(request):
    return render(request, 'adminLogin.html')


def bookingdet(request):
    pending_bookings = []
    history = []
    d = appointments.objects.filter(bk_status='pending')
    for i in d:
        if i.email == request.session['id']:
            pending_bookings.append(i)
    d1 = appointments.objects.filter(bk_status='approve')
    for j in d1:
        if j.email == request.session['id']:
            history.append(j)
    return render(request, 'bookingdetails.html', {'data': pending_bookings, 'data1': history})


def adminHomePage(request):
    d = newmember.objects.all()
    return render(request, 'adminHome.html', {'data': d})


def adminloginCheck(request):
    if request.method == 'POST':
        em = request.POST['name']
        pwd = request.POST['pass']
        # d = newmember.objects.all()
        # for i in d:
        #     if usr == i.username and pwd == i.password:
        #         return redirect(index)
        # return HttpResponse("Wrong username or password")
        data = admin_log.objects.filter(adName=em)
        if data:
            data1 = admin_log.objects.get(adName=em)
            if data1.adPass == pwd:
                request.session['id'] = em
                return redirect(adminHomePage)
            else:
                messages.info(request, 'invalid E-mail or password')
                return redirect(adminlog)
        else:
            messages.info(request, 'invalid E-mail or password')
            return redirect(adminlog)


def adappointmentpage(request):
    d = appointments.objects.filter(bk_status='pending')
    return render(request, 'adAppointment.html', {'data': d})


def appointment_approve(request, id):
    appointments.objects.filter(pk=id).update(bk_status='approve')
    messages.info(request, 'appointment approved')
    return redirect(adappointmentpage)


def appointment_reject(request, id):
    appointments.objects.filter(pk=id).delete()
    messages.info(request, 'appointment rejected')
    return redirect(adappointmentpage)


def doctorsform(request):
    return render(request, 'doctors.html')


def doctorsAction(request):
    if request.method == 'POST':
        name = request.POST['name']
        docId = request.POST['id']
        docPhoto = request.FILES['photo']
        dept = request.POST['dpt']
        check = doctorAdd.objects.filter(docId=docId)
        if (check):
            messages.info(request, 'doctor already exist!!')
        else:
            data = doctorAdd.objects.create(name=name, docId=docId, photoDoc=docPhoto, department=dept)
            data.save()
            messages.info(request, 'doctor information Added!')

        return redirect(doctorsform)


def docdisplay(request):
    d = doctorAdd.objects.all()
    return render(request, 'regdocdisplay.html', {'data': d})


def doctorDelete(request, id):
    doctorAdd.objects.filter(pk=id).delete()
    messages.info(request, 'doctor information deleted')
    return redirect(docdisplay)
