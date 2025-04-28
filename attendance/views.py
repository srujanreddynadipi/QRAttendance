import datetime

from django.http import FileResponse
from django.shortcuts import render

from attendance.forms import FacultyForm,StudentForm
from attendance.service import postObject, FireBaseObject
from attendance import firebase
import pyqrcode

firebase = firebase.FirebaseApplication('https://qrattendance-4e21a-default-rtdb.firebaseio.com/', None)

def facultyregistration(request):
    if request.method == "POST":

        registrationForm = FacultyForm(request.POST)

        if registrationForm.is_valid():

            name = registrationForm.cleaned_data["name"]
            email = registrationForm.cleaned_data["email"]
            mobile = registrationForm.cleaned_data["mobile"]
            department = registrationForm.cleaned_data["department"]
            username = registrationForm.cleaned_data["username"]
            password = registrationForm.cleaned_data["password"]

            data = {'name': name, 'email': email, 'mobile': mobile
                , "department": department, "username": username, "password": password}

            result = firebase.get('/faculty/', '')
            isRegistred = False
            if result is not None:
                for id, obj in result.items():
                    object = FireBaseObject()
                    object.id = id
                    for param, value in obj.items():
                        if param in "username" and username in value:
                            isRegistred = True

            if isRegistred:
                return render(request, 'facultyregistration.html', {"message": "User All Ready Exist"})
            else:
                try:
                    result = postObject(data, "faculty")
                    print(result)
                    return render(request, 'facultyregistration.html', {"message": "Faculty Added Successfully"})
                except:
                    return render(request, 'facultyregistration.html', {"message": "Faculty Registration Failed"})
        else:
            return render(request, 'facultyregistration.html', {"message": "Invalid Form"})

    return render(request, 'facultyregistration.html', {"message": "Invalid Request"})


def deletefaculty(request):
    faculty = request.GET['facultyid']
    firebase.delete('/faculty/', faculty)

    objects = []
    result = firebase.get('/faculty/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "name":
                    object.name = value
                if param in "email":
                    object.email = value
                if param in "mobile":
                    object.mobile = value
                if param in "department":
                    object.department = value
                if param in "username":
                    object.username = value
                if param in "password":
                    object.password = value
            objects.append(object)

    return render(request, "facultys.html", {"facultys": objects})

def getfacultys(request):
    objects = []
    result = firebase.get('/faculty/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "name":
                    object.name = value
                if param in "email":
                    object.email = value
                if param in "mobile":
                    object.mobile = value
                if param in "department":
                    object.department = value
                if param in "username":
                    object.username = value
                if param in "password":
                    object.password = value
            objects.append(object)

    return render(request, "facultys.html", {"facultys": objects})

def studentregistration(request):

    if request.method == "POST":

        registrationForm = StudentForm(request.POST)

        if registrationForm.is_valid():
            name = registrationForm.cleaned_data["name"]
            email = registrationForm.cleaned_data["email"]
            mobile = registrationForm.cleaned_data["mobile"]
            department = registrationForm.cleaned_data["department"]
            username = registrationForm.cleaned_data["username"]
            password = registrationForm.cleaned_data["password"]
            year = registrationForm.cleaned_data["year"]
            section = registrationForm.cleaned_data["section"]
            status = "no"

            result = firebase.get('/student/', '')
            isRegistred = False
            if result is not None:
                for id, obj in result.items():
                    object = FireBaseObject()
                    object.id = id
                    for param, value in obj.items():
                        if param in "username" and username in value:
                            isRegistred = True

            if isRegistred:
                return render(request, 'studentregistration.html', {"message": "User All Ready Exist"})
            else:
                try:
                    data = {'name': name, 'email': email, 'mobile': mobile
                        , "department": department, "username": username, "password": password, "year": year,
                            "section": section, "status": status}
                    result = postObject(data, "student")
                    print(result)
                    return render(request, 'studentregistration.html', {"message": "Student Added Successfully"})
                except:
                    return render(request, 'studentregistration.html', {"message": "Registration Failed"})
        else:
            return render(request, 'studentregistration.html', {"message": "Invalid Form"})

    return render(request, 'studentregistration.html', {"message": "Invalid Request"})

#===============================================================================================
def deletestudent(request):
    student = request.GET['studentid']
    firebase.delete('/student/', student)

    objects = []
    result = firebase.get('/student/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "name":
                    object.name = value
                if param in "email":
                    object.email = value
                if param in "mobile":
                    object.mobile = value
                if param in "department":
                    object.department = value
                if param in "username":
                    object.username = value
                if param in "password":
                    object.password = value
                if param in "year":
                    object.year = value
                if param in "section":
                    object.section = value
                if param in "status":
                    object.status = value
            objects.append(object)

    return render(request, "students.html", {"students": objects})


#===============================================================================================
def getstudents(request):
    objects = []
    result = firebase.get('/student/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "name":
                    object.name = value
                if param in "email":
                    object.email = value
                if param in "mobile":
                    object.mobile = value
                if param in "department":
                    object.department = value
                if param in "username":
                    object.username = value
                if param in "password":
                    object.password = value
                if param in "year":
                    object.year = value
                if param in "section":
                    object.section = value
                if param in "status":
                    object.status = value
            objects.append(object)

    return render(request, "students.html", {"students": objects})

#===============================================================================================
def login(request):

    uname = request.GET["username"]
    upass = request.GET["password"]
    type = request.GET["type"]

    if type in "admin":

        if uname == "admin" and upass == "admin":

            request.session['username'] = "admin"
            request.session['role'] = "admin"

            objects = []
            result = firebase.get('/student/', '')
            if result is not None:
                for id, obj in result.items():
                    object = FireBaseObject()
                    object.id = id
                    for param, value in obj.items():
                        if param in "name":
                            object.name = value
                        if param in "email":
                            object.email = value
                        if param in "mobile":
                            object.mobile = value
                        if param in "department":
                            object.department = value
                        if param in "username":
                            object.username = value
                        if param in "password":
                            object.password = value
                        if param in "year":
                            object.year = value
                        if param in "section":
                            object.section = value
                        if param in "status":
                            object.status = value
                    objects.append(object)

            return render(request, "students.html", {"students": objects})

        else:
            return render(request, 'index.html', {"message": "Invalid Credentials"})

    if type in "faculty":

        isValidUser = False
        result = firebase.get('/faculty/', '')

        if result is not None:

            for id, obj in result.items():

                object = FireBaseObject()

                object.id = id

                dbusername = ""

                dbpassword = ""

                for param, value in obj.items():

                    if param in "username":
                        dbusername = value

                    if param in "password":
                        dbpassword = value

                    if param in "department":
                        department = value

                if dbusername in uname and dbpassword in upass:
                    isValidUser = True

                    break

        if isValidUser:

            request.session['username'] = uname
            request.session['role'] = "faculty"
            return render(request, "generateqr.html")

        else:
            return render(request, 'index.html', {"message": "Invalid Credentials"})

    return render(request, 'index.html', {"message": "Invalid Request"})

def activateAccount(request):
    username = request.GET['username']
    status = request.GET['status']

    firebase.put('/student/' + username, 'status', status)
    print('Record Updated')
    objects = []
    result = firebase.get('/student/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "name":
                    object.name = value
                if param in "email":
                    object.email = value
                if param in "mobile":
                    object.mobile = value
                if param in "department":
                    object.department = value
                if param in "username":
                    object.username = value
                if param in "password":
                    object.password = value
                if param in "year":
                    object.year = value
                if param in "section":
                    object.section = value
                if param in "status":
                    object.status = value
            objects.append(object)

    return render(request, "students.html", {"students": objects})


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

#======================================================================================================
def generateqr(request):
    return render(request, "generateqr.html")

import os  # Add this at the top with other imports
def generateqraction(request):
    department = request.GET["department"].upper()  # Convert to uppercase
    year = request.GET["year"]
    sem = request.GET["sem"]
    section = request.GET["section"]
    subject = request.GET["subject"].upper()  # Convert to uppercase
    cdate = datetime.datetime.now()

    strdt = str(cdate.day)+"-"+str(cdate.month)+"-"+str(cdate.year)+"-"+str(cdate.hour)+"-"+str(cdate.minute)
    info = str(department+"_"+year+"_"+sem+"_"+section+"_"+subject+"_"+strdt)
    
    # Generate QR code
    url = pyqrcode.create(info)
    
    # Save QR code with absolute path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(base_dir, 'static', 'qrcodes')
    
    # Create directory if it doesn't exist
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    qr_filename = f"{info}.png"
    full_path = os.path.join(static_dir, qr_filename)
    url.png(full_path, scale=6)
    
    context = {
        'qr_path': f'/static/qrcodes/{qr_filename}',
        'department': department,  # Will now be uppercase
        'year': year,
        'semester': sem,
        'section': section,
        'subject': subject,  # Will now be uppercase
        'datetime': cdate.strftime("%d-%m-%Y %H:%M")
    }
    
    return render(request, "displayqr.html", context)

def viewattendanceaction(request):

    username=request.GET['username']
    subject = request.GET['subject']

    count=0

    objects = []
    result = firebase.get('/attendance/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "username":
                    object.username = value
                if param in "subject":
                    object.subject = value
                if param in "date":
                    object.date = value

            if object.username==username and object.subject==subject:
                objects.append(object)
                count=count+1

    return render(request, "viewattendance.html", {"attendances": objects,"count":count})

#==============================================================================================
def addQuestion(request):
    if request.method == 'POST':  # Check if request method is POST
        question_text = request.POST.get('question')  # Use POST instead of GET and use get() method
        if question_text:  # Check if question exists
            objects = []
            result = firebase.get('/question/', '')
            if result is not None:
                for id, obj in result.items():
                    object = FireBaseObject()
                    object.id = id
                    for param, value in obj.items():
                        if param in "question":
                            object.question = value
                        if param in "qid":
                            object.qid = value
                    objects.append(object)

            data = {"qid": str(len(objects) + 1), "question": question_text}
            result = postObject(data, "question")
            print(result)

            # Refresh the questions list
            objects = []
            result = firebase.get('/question/', '')
            if result is not None:
                for id, obj in result.items():
                    object = FireBaseObject()
                    object.id = id
                    for param, value in obj.items():
                        if param in "question":
                            object.question = value
                    objects.append(object)

            return render(request, "questions.html", {"questions": objects, "message": "Question added successfully"})
        else:
            return render(request, "addquestion.html", {"message": "Question cannot be empty"})
    
    return render(request, "addquestion.html")  # For GET requests, just show the form

def getquestions(request):
    objects = []
    result = firebase.get('/question/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "question":
                    object.question = value
            objects.append(object)

    return render(request, "questions.html", {"questions": objects})

def deletequestion(request):
    question = request.GET['questionid']
    firebase.delete('/question/', question)

    objects = []
    result = firebase.get('/question/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param in "question":
                    object.question = value
            objects.append(object)

    return render(request, "questions.html", {"questions": objects})

def getfeedback(request):

    good = 0
    average = 0
    bad = 0

    try:
        faculty=request.GET['fid']
    except Exception as e:
        print(e)
        faculty=request.session['username']

    result = firebase.get('/result/', '')

    if result is not None:

        for id, obj in result.items():

            fid = ""
            feedback = ""

            for param, value in obj.items():
                print("Param", param, "-", "value", value)
                if param == "fid":
                    fid = value
                if param == "result":
                    feedback = value

            print("fid", fid)
            print("feedback", feedback)

            if fid == faculty:
                if feedback == "good":
                    good = good + 1
                elif feedback == "average":
                    average = average + 1
                elif feedback == "bad":
                    bad = bad + 1

    objects = []
    result = firebase.get('/question/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param == "question":
                    object.question = value
                if param == "qid":
                    object.qid = value
            objects.append(object)

    return render(request, "viewfeedback.html", {"good": good, "bad": bad, "average": average, "faculty": faculty,"questions":objects})


def getquestionfeedback(request):

    good = 0
    average = 0
    bad = 0

    faculty = request.GET['fid']
    questionid = request.GET['qid']

    result = firebase.get('/result/', '')

    if result is not None:

        for id, obj in result.items():

            fid = ""
            feedback = ""
            qid=""

            for param, value in obj.items():
                #print("Param", param, "-", "value", value)
                if param == "fid":
                    fid = value
                if param == "result":
                    feedback = value
                if param == "qid":
                    qid = value

            print("fid", fid,faculty)
            print("qid", qid,questionid)
            print("feedback", feedback)

            if fid ==faculty and qid == questionid:
                if feedback == "good":
                    good = good + 1
                elif feedback == "average":
                    average = average + 1
                elif feedback == "bad":
                    bad = bad + 1

    print("final", good, bad, average)
    objects = []
    result = firebase.get('/question/', '')
    if result is not None:
        for id, obj in result.items():
            object = FireBaseObject()
            object.id = id
            for param, value in obj.items():
                if param == "question":
                    object.question = value
                if param == "qid":
                    object.qid = value
            objects.append(object)

    return render(request, "viewfeedback.html",{"good": good, "bad": bad, "average": average, "faculty": faculty, "questions": objects})