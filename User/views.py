from datetime import date

from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from CreateEvent.models import Event, AttendEvent
from User.forms import StudentForm, TeacherForm
from User.models import Account, Student, Teacher


class HomePageView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)

class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = Account.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('User:index'))
        except Account.DoesNotExist:
            user = None

        return render(request, self.template_name, {'msg':'Incorrect username or password'})

class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect(reverse('User:index'))

class RegisterStudentView(View):
    template_name = 'createStudent.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('User:index'))
        return render(request, self.template_name, {'form': form})

class RegisterTeacherView(View):
    template_name = 'createTeacher.html'

    def get(self, request):
        form = TeacherForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('User:index'))
        return render(request, self.template_name, {'form': form})

class EditProfileView(View):
    template_name = 'editProfile.html'

    def get(self, request):
        if request.session['type'] == 'S':
            student = Student.objects.get(pk=request.session['username'])
            form = StudentForm(instance=student)
        else:
            teacher = Teacher.objects.get(pk=request.session['username'])
            form = TeacherForm(instance=teacher)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.session['type'] == 'S':
            student = Student.objects.get(pk=request.session['username'])
            form = StudentForm(request.POST, instance=student)
        else:
            teacher = Teacher.objects.get(pk=request.session['username'])
            form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})

class DisplayEventsView(View):
    template = 'displayEvents.html'

    def get(self, request):
        studentLoggedIn = Student.objects.get(pk=request.session['username'])
        not_attended_events = Event.objects.exclude(student=studentLoggedIn)
        print(not_attended_events)
        return render(request, self.template, {'events': not_attended_events})

class AttendEventView(View):
    template = 'attendEvent.html'

    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        return render(request, self.template, {'event': event})

    def post(self, request, event_id):
        status = int(request.POST.get('status'))

        if status == 1:
            student_id = request.session['username']
            date_today = date.today()

            with connection.cursor() as cursor:
                cursor.callproc('RegisterStudent', [student_id, event_id, date_today])

        return redirect('User:display_available_events')

        # event = Event.objects.get(pk=event_id)
        # number_of_participants = AttendEvent.objects.filter(event=event).count()
        # status = bool(int(request.POST.get('status')))
        # if status == 1 and number_of_participants < event.max_participants:
        #     student = Student.objects.get(pk=request.session['username'])
        #     attend_event = AttendEvent.objects.get_or_create(event=event, student=student, date_registered=date.today())
        #     print(attend_event)
        # return redirect('User:display_available_events')