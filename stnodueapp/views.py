import email
from http.client import HTTPResponse
from sre_constants import SUCCESS
from django.shortcuts import render,redirect
from stnodueapp import urls
from django.contrib.auth import logout
import mysql.connector as sql
from django.contrib import messages
from stnodueapp.forms import studentform,facultyform,hallform,tcform,libform,spform,contactform
from .models import student,faculty,hallticket,sportsdb,librarydb,tc_db,contactus


def index(request):
    return render(request,"index.html")

def signout(request):
    logout(request)
    request.session.flush()
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')

def main(request):
    return render(request,'main.html')


def contact(request):
    if request.method=="POST":
        form = contactform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect()
            except:
                pass
    else:
        form=contactform()
    return render(request,'contact.html')

def contactview(request):
    c = contactus.objects.all()
    return render(request,'contactview.html' , {'contactus': c })
def accountscontact(request):
    c = contactus.objects.all()
    return render(request,'accounts/accountscontact.html' , {'contactus': c })
def bcacontact(request):
    c = contactus.objects.all()
    return render(request,'hod/bcacontact.html' , {'contactus': c })
def bcomcontact(request):
    c = contactus.objects.all()
    return render(request,'hod/bcomcontact.html' , {'contactus': c })
def bsccontact(request):
    c = contactus.objects.all()
    return render(request,'hod/bsccontact.html' , {'contactus': c })
def libcontact(request):
    c = contactus.objects.all()
    return render(request,'library/libcontact.html' , {'contactus': c })
def sportscontact(request):
    c = contactus.objects.all()
    return render(request,'sports/sportscontact.html' , {'contactus': c })
#adminlogin
def adminlogin(request):
    if request.method=="POST":
        m=sql.connect(host='127.0.0.1',user='root',password='0823',database='stnodue_db')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                username=value
            if key=="password":
                password=value            
        c="select * from adminlog where username='{}' and password='{}'".format(username,password)  
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Wrong Credentials")
            return redirect('adminlogin') 
        else:
            return redirect('/home')     
    return render(request,'admin/adminlogin.html')

def home(request):
    return render(request,'admin/home.html')

#add stud
def addstud(request):
    if request.method=="POST":
        form = studentform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HTTPResponse(SUCCESS)
                return redirect()
            except:
                pass
    else:
        form=studentform()
    return render(request,'admin/addstud.html')    

#stud list BCA
def bcalist(request):
    c_year = student.get_all_by_course("BCA")
    return render(request,'admin/bcalist.html' , {'student': c_year })
def bcaedit(request, id):
    stud = student.objects.get(id=id)
    return render(request,"admin/bcaedit.html",{ 'student': stud })
def update1(request, id):
    stud = student.objects.get(id=id)
    form=studentform(request.POST, instance=stud)
    if form.is_valid():
        form.save()
        return redirect ('/bcalist')
    return render(request,"admin/addstud.html",{ 'student' : stud })    
def delete1(request, id):
    stud = student.objects.get(id=id)
    stud.delete()
    return redirect ('/bcalist')    
def bcafrstyear(request):
    c_year = student.get_all_by_frstyear('1st Year','BCA')
    return render(request, "admin/bcalist.html" , {'student': c_year })
def bcasecndyear(request):
    c_year = student.get_all_by_scondyear("2nd Year",'BCA')
    return render(request, "admin/bcalist.html" , {'student': c_year })
def bcathirdyear(request):
    c_year = student.get_all_by_thirdyear("3rd Year",'BCA')
    return render(request, "admin/bcalist.html" , {'student': c_year }) 


#bcom studlist
def bcomlist(request):
    bc_year = student.get_all_by_course("BCom")
    return render(request,'admin/bcomlist.html' , {'student': bc_year })
def bcomedit(request, id):
    stud = student.objects.get(id=id)
    return render(request,"admin/bcomedit.html",{ 'student': stud })
def update2(request, id):
    stud = student.objects.get(id=id)
    form=studentform(request.POST, instance=stud)
    if form.is_valid():
        form.save()
        return redirect ('/bcomlist')
    return render(request,"addstud.html",{ 'student' : stud })    
def delete2(request, id):
    stud = student.objects.get(id=id)
    stud.delete()
    return redirect ('/bcomlist')    
def bcomfrstyear(request):
    c_year = student.get_all_by_frstyear('1st Year','BCom')
    return render(request, "admin/bcomlist.html" , {'student': c_year })
def bcomsecndyear(request):
    c_year = student.get_all_by_scondyear("2nd Year",'BCom')
    return render(request, "admin/bcomlist.html" , {'student': c_year })
def bcomthirdyear(request):
    c_year = student.get_all_by_thirdyear("3rd Year",'BCom')
    return render(request, "admin/bcomlist.html" , {'student': c_year })
   
#bsc studist
def bsclist(request):
    c_year = student.get_all_by_course("BSc")
    return render(request,'admin/bsclist.html' , {'student': c_year })
def bscedit(request, id):
    stud = student.objects.get(id=id)
    return render(request,"admin/bscedit.html",{ 'student': stud })
def update3(request, id):
    stud = student.objects.get(id=id)
    form=studentform(request.POST, instance=stud)
    if form.is_valid():
        form.save()
        return redirect ('/bsclist')
    return render(request,"admin/addstud.html",{ 'student' : stud })    
def delete3(request, id):
    stud = student.objects.get(id=id)
    stud.delete()
    return redirect ('/bsclist') 
def bscfrstyear(request):
    c_year = student.get_all_by_frstyear('1st Year','BSc')
    return render(request, "admin/bsclist.html" , {'student': c_year })
def bscsecndyear(request):
    c_year = student.get_all_by_scondyear("2nd Year", 'BSc')
    return render(request, "admin/bsclist.html" , {'student': c_year })
def bscthirdyear(request):
    c_year = student.get_all_by_thirdyear("3rd Year", 'BSc')
    return render(request, "admin/bsclist.html" , {'student': c_year }) 

#addfac
def addfaculty(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        department=request.POST['department']
        password=request.POST['password']
        conpassword=request.POST['conpassword']

        form=faculty(username=username,name=name,contact=contact,email=email,department=department,password=password,conpassword=conpassword)
        form.save()
        messages.success(request,'success')
        return redirect('addfaculty')    
    else:
        messages.error(request,'error')
       
    return render(request,'admin/addfaculty.html')    
#faclist
def faclist(request):
    fac= faculty.objects.all()
    return render(request,'admin/faclist.html' , {'faculty': fac })
def facedit(request, id):
    fac = faculty.objects.get(id=id)
    return render(request,"admin/facedit.html",{ 'faculty': fac })
def facupdate(request, id):
    fac = faculty.objects.get(id=id)
    form=facultyform(request.POST, instance=fac)
    if form.is_valid():
        form.save()
        return redirect ('/faclist')
    return render(request,"admin/addfaculty.html",{ 'faculty' : fac })    
def facdelete(request, id):
    fac = faculty.objects.get(id=id)
    fac.delete()
    return redirect ('/faclist')


#stud login
def studlogin(request):
    if request.method=="POST":
        m=sql.connect(host='127.0.0.1',user='root',password='0823',database='stnodue_db')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="regno":
                regno=value
            if key=="course":
                course=value
            if key=="pass1":
                pass1=value
            
        c="select * from student where regno='{}' and course='{}'and pass1='{}'".format(regno,course,pass1)  
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        stu=student.get_student_by_studreg(regno)
        if t==():
            messages.error(request,"Wrong Credentials")
            return redirect('studlogin')
        if t!=():
            request.session['student_regno']= stu.regno
            request.session['student_year']=stu.year
            request.session['student_name']=stu.name
            request.session['student_course']=stu.course
            key=="course"
            if course=="BCA":
                return redirect('/bcahome')
            elif course=="BCom":
                return redirect('/bcomhome')  
            elif course=="BSc":
                return redirect('/bschome')  
    return render(request, "index.html")

#bca stud
def bcahome(request):
    print(request.session.get('student_regno'))
    print(request.session.get('student_name'))
    print(request.session.get('student_year'))
    print(request.session.get('student_course'))
    return render(request,'bcastud/bcahome.html')    


    #bcomstudent

def bcomhome(request):
    print(request.session.get('student_regno'))
    print(request.session.get('student_name'))
    print(request.session.get('student_year'))
    print(request.session.get('student_course'))
    return render(request,'bcomstud/bcomhome.html')


    #bscstudent
def bschome(request):
    print(request.session.get('student_regno'))
    print(request.session.get('student_name'))
    print(request.session.get('student_year'))
    print(request.session.get('student_course'))
    return render(request,'bscstud/bschome.html')

   
# def bcahallticketnodue(request):
#     apply=hallticket.get_all_by_c("BCA")
#     return render(request, "library/bcomlibrarynodue.html" , { 'hallticket': apply }) 

# def bcatcnodue(request):
#     apply=tc.get_all_by_c("BCA")
#     return render(request, "library/bcomlibrarynodue.html" , { 'hallticket': apply }) 

def nodue(request):
    return render(request,'nodue.html')
    
def noduestatus(request):
    stud=(request.session.get('student_regno'))
    print(request.session.get('student_regno'))
    apply = hallticket.get_file_by_year(stud)
    apply1 = tc_db.get_file_by_year(stud)
    apply2 = sportsdb.get_file_by_year(stud)
    apply3= librarydb.get_file_by_year(stud)
    return render(request, "noduestatus.html" , { 'hallticket': apply,'tc_db':apply1,'sportsdb':apply2 ,'librarydb':apply3  }) 


def noduestatusdeletehall(request, regno):
    if hallticket==hallticket:
        apply = hallticket.objects.get(regno=regno)
        apply.delete()
    return redirect ('/noduestatus')    
def noduestatusdeletetc(request, regno):
    if tc_db==tc_db:
        apply1 = tc_db.objects.get(regno=regno)
        apply1.delete()
    return redirect ('/noduestatus')    
def noduestatusdeletesports(request, regno):
    if sportsdb==sportsdb:
        apply2 = sportsdb.objects.get(regno=regno)
        apply2.delete()
    return redirect ('/noduestatus')    
def noduestatusdeletelibrary(request, regno):
    if librarydb==librarydb:
        apply3 = librarydb.objects.get(regno=regno)
        apply3.delete()
    return redirect ('/noduestatus')    



def hallnodue(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        name = request.POST['name']
        course=request.POST['course']
        year=request.POST['year']
        date=request.POST['date']
        noduereasons=request.POST['noduereasons']

        form=hallticket(regno=regno,name=name,course=course,year=year,date=date,noduereasons=noduereasons)
        form.save()
        messages.success(request,'success')
        return redirect('hallnodue')    
    else:
        messages.error(request,'error')
    return render(request, "nodue.html")

def tcnodue(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        name = request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        father_name=request.POST['father_name']
        mother_name=request.POST['mother_name']
        nationality=request.POST['nationality']
        addate=request.POST['addate']
        course=request.POST['course']
        dateofapply=request.POST['dateofapply']
        noduereasons=request.POST['noduereasons']
        form=tc_db(regno=regno,name=name,gender=gender,dob=dob,father_name=father_name,mother_name=mother_name,nationality=nationality,addate=addate,course=course,dateofapply=dateofapply,noduereasons=noduereasons)
        form.save()
        messages.success(request,'success')
        return redirect('tcnodue')    
    else:
        messages.error(request,'error')
    return render(request, "nodue.html")

def librarynodue(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        name = request.POST['name']
        course=request.POST['course']
        year=request.POST['year']
        date=request.POST['date']
        noduereasons=request.POST['noduereasons']
        form=librarydb(regno=regno,name=name,course=course,year=year,date=date,noduereasons=noduereasons)
        form.save()
        messages.success(request,'success')
        return redirect('librarynodue')    
    else:
        messages.error(request,'error')
    return render(request, "nodue.html")

def sportsnodue(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        name = request.POST['name']
        course=request.POST['course']
        year=request.POST['year']
        date=request.POST['date']
        noduereasons=request.POST['noduereasons']
        form=sportsdb(regno=regno,name=name,course=course,year=year,date=date,noduereasons=noduereasons)
        form.save()
        messages.success(request,'success')
        return redirect('sportsnodue')    
    else:
        messages.error(request,'error')
    return render(request, "nodue.html")    

# def hallviewdetails(request,id):
#     stu=student.get_student_by_studid(id)
#     request.session['student_id']= stu.id
#     apply = hallticket.objects.get(id=id)
#     return render(request,"hallviewdetails.html",{ 'hallticket': apply }) 
def hallviewdetails(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"hallviewdetails.html",{ 'hallticket': apply })
def halldetailsupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/noduestatus')
    return render(request,"noduestatus.html",{ 'hallticket':apply })   

def sportsviewdetails(request, id):
    apply = sportsdb.objects.get(id=id)
    # return redirect ('/nodustatus')
    return render(request,"sportsviewdetails.html",{ 'sportsdb': apply })
def sportsdetailsupdate(request, id):
    apply =sportsdb.objects.get(id=id)
    form=spform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/noduestatus')
    return render(request,"noduestatus.html",{ 'sportsdb':apply })   

def tcviewdetails(request, id):
    apply = tc_db.objects.get(id=id)
    # return redirect ('/nodustatus')
    return render(request,"tcviewdetails.html",{ 'tc_db': apply })
def tcdetailsupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/noduestatus')
    return render(request,"noduestatus.html",{ 'tc_db':apply }) 
    
def libraryviewdetails(request, id):
    apply = librarydb.objects.get(id=id)
    # return redirect ('/nodustatus')
    return render(request,"libraryviewdetails.html",{ 'librarydb': apply })
def librarydetailsupdate(request, id):
    apply =librarydb.objects.get(id=id)
    form=libform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/noduestatus')
    return render(request,"noduestatus.html",{ 'librarydb':apply }) 
#faclogin
def faclogin(request):
    if request.method=="POST":

        m=sql.connect(host='127.0.0.1',user='root',password='0823',database='stnodue_db')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():

            if key=="username":
                username=value
            if key=="department":
                department=value
            if key=="password":
                password=value
            
        c="select * from faculty where username='{}'and department='{}' and password='{}'".format(username,department,password)  
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request,"Wrong Credentials")
            return redirect('faclogin')
        if t!=():
            key=="department"
            if department=="LIBRARY":
                return redirect('libraryhome')
            elif department=="ACCOUNTS":
                return redirect('accountshome')  
            elif department=="BCA":
                return redirect('hodbcahome')  
            elif department=="BSc":
                return redirect('hodbschome')                   
            elif department=="BCom":
                return redirect('hodbcomhome')  
            elif department=="SPORTS":
                return redirect('sportshome') 
    return render(request, "index.html")

 #accounts
def accountshome(request):
    return render(request,'accounts/accountshome.html') 
#accounts hallticket
def bcaaccountshall(request):
    apply= hallticket.get_all_by_c("BCA")
    return render(request, "accounts/accountshall.html" , { 'hallticket': apply }) 
def bcomaccountshall(request):
    apply= hallticket.get_all_by_c("BCom")
    return render(request, "accounts/accountshall.html" , { 'hallticket': apply })    
def bscaccountshall(request):
    apply= hallticket.get_all_by_c("BSc")
    return render(request, "accounts/accountshall.html" , { 'hallticket': apply })
    
def accountshalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"accounts/accountshalledit.html",{ 'hallticket': apply })
def accountshallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/accountshome')
    return render(request,"accounts/accountshall.html",{ 'hallticket':apply })    
# def accountshalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect ('/accountshome') 
# def bscfrstyearh(request):
#     c_year = hallticket.get_all_by_frstyear('1st Year','BSc')
#     return render(request, "accounts/accountshall.html" , {'hallticket': c_year })
# def bscsecndyearh(request):
#     c_year = hallticket.get_all_by_scondyear("2nd Year", 'BSc')
#     return render(request, "accounts/accountshall.html" , {'hallticket': c_year })
# def bscthirdyearh(request):
#     c_year = hallticket.get_all_by_thirdyear("3rd Year", 'BSc')
#     return render(request, "accounts/accountshall.html" , {'hallticket': c_year }) 


#accounts tc
def accountstcedit(request, id):
    apply = tc_db.objects.get(id=id)
    return render(request,"accounts/accountstcedit.html",{ 'tc_db': apply })
def accountstcupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/accountshome')
    return render(request,"accounts/accountstc.html",{ 'tc_db':apply })    
# def accountstcdelete(request, id):
#     apply = tc.objects.get(id=id)
#     apply.delete()
#     return redirect ('/accountshome') 

def bcaaccountstc(request):
    apply= tc_db.get_all_by_c("BCA")
    return render(request, "accounts/accountstc.html" , { 'tc_db': apply })   
def bcomaccountstc(request):
    apply= tc_db.get_all_by_c("BCom")
    return render(request, "accounts/accountstc.html" , { 'tc_db': apply }) 
def bscaccountstc(request):
    apply= tc_db.get_all_by_c("BSc")
    return render(request, "accounts/accountstc.html" , { 'tc_db': apply }) 



    #library
def libraryhome(request):
    return render(request,'library/libraryhome.html')

#library hallticket

def bcalibhall(request):
    apply= hallticket.get_all_by_c("BCA")
    return render(request, "library/libhall.html" , { 'hallticket': apply })

def bcomlibhall(request):
    apply= hallticket.get_all_by_c("BCom")
    return render(request, "library/libhall.html" , { 'hallticket': apply }) 

def bsclibhall(request):
    apply= hallticket.get_all_by_c("BSc")
    return render(request, "library/libhall.html" , { 'hallticket': apply }) 
def libhalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"library/libhalledit.html",{ 'hallticket': apply })
def libhallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/libraryhome')
    return render(request,"library/libhall.html",{ 'hallticket':apply })    
# def libhalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect ('/libraryhome')

#library 
def bcalib(request):
    apply= librarydb.get_all_by_c("BCA")
    return render(request, "library/lib.html" , { 'librarydb': apply })
def bcomlib(request):
    apply= librarydb.get_all_by_c("BCom")
    return render(request, "library/lib.html" , { 'librarydb': apply })
def bsclib(request):
    apply= librarydb.get_all_by_c("BSc")
    return render(request, "library/lib.html" , { 'librarydb': apply }) 

def libedit(request, id):
    apply = librarydb.objects.get(id=id)
    return render(request,"library/libedit.html",{ 'librarydb': apply })
def libupdate(request, id):
    apply =librarydb.objects.get(id=id)
    form=libform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/libraryhome')
    return render(request,"library/lib.html",{ 'librarydb':apply })    
# def libdelete(request, id):
#     apply = librarydb.objects.get(id=id)
#     apply.delete()
#     return redirect ('/libraryhome')



    #sports
def sportshome(request):
    return render(request,'sports/sportshome.html')

#sports halltickt
def bcasportshall(request):
    apply= hallticket.get_all_by_c("BCA")
    return render(request, "sports/sportshall.html" , { 'hallticket': apply })  
def bcomsportshall(request):
    apply= hallticket.get_all_by_c("BCom")
    return render(request, "sports/sportshall.html" , { 'hallticket': apply })  
def bscsportshall(request):
    apply= hallticket.get_all_by_c("BSc")
    return render(request, "sports/sportshall.html" , { 'hallticket': apply }) 

def sportshalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"sports/sportshalledit.html",{ 'hallticket': apply })
def sportshallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/sportshome')
    return render(request,"sports/sportsnodue.html",{ 'hallticket':apply })    
# def sportshalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect('/sportshome')

 #sports 
def bcasports(request):
    apply= sportsdb.get_all_by_c("BCA")
    return render(request, "sports/sports.html" , { 'sportsdb': apply })  
def bcomsports(request):
    apply= sportsdb.get_all_by_c("BCom")
    return render(request, "sports/sports.html" , { 'sportsdb': apply })  
def bscsports(request):
    apply= sportsdb.get_all_by_c("BSc")
    return render(request, "sports/sports.html" , { 'sportsdb': apply })  
def sportsedit(request, id):
    apply = sportsdb.objects.get(id=id)
    return render(request,"sports/sportsedit.html",{ 'sportsdb': apply })
def sportsupdate(request, id):
    apply =sportsdb.objects.get(id=id)
    form=spform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/sportshome')
    return render(request,"sports/sportsnodue.html",{ 'sportsdb':apply })    
# def sportsdelete(request, id):
#     apply = sportsdb.objects.get(id=id)
#     apply.delete()
#     return redirect('/sportshome')


   #hod
def hodbcahome(request):
    return render(request,'hod/hodbcahome.html')
def hodbcahall(request):
    apply= hallticket.get_all_by_c("BCA")
    return render(request, "hod/hodbcahall.html" , { 'hallticket': apply }) 
def hodbcahalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"hod/hodbcahalledit.html",{ 'hallticket': apply })
def hodbcahallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbcahall')
    return render(request,"hod/hodbcahall.html",{ 'hallticket':apply })    
# def hodbcahalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbcahall')    


def hodbcatc(request):
    apply= tc_db.get_all_by_c("BCA")
    return render(request, "hod/hodbcatc.html" , { 'tc_db': apply }) 
def hodbcatcedit(request, id):
    apply = tc_db.objects.get(id=id)
    return render(request,"hod/hodbcatcedit.html",{ 'tc_db': apply })
def hodbcatcupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbcatc')
    return render(request,"hod/hodbcatc.html",{ 'tc_db':apply })    
# def hodbcatcdelete(request, id):
#     apply = tc.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbcatc')    
    

def hodbcomhome(request):
    return render(request,'hod/hodbcomhome.html')
def hodbcomhall(request):
    apply= hallticket.get_all_by_c("BCom")
    return render(request, "hod/hodbcomhall.html" , { 'hallticket': apply })  
def hodbcomhalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"hod/hodbcomhalledit.html",{ 'hallticket': apply })
def hodbcomhallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbcomhall')
    return render(request,"hod/hodbcomhall.html",{ 'hallticket':apply })    
# def hodbcomhalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbcomhall')    


def hodbcomtc(request):
    apply= tc_db.get_all_by_c("BCom")
    return render(request, "hod/hodbcomtc.html" , { 'tc_db': apply }) 
def hodbcomtcedit(request, id):
    apply = tc_db.objects.get(id=id)
    return render(request,"hod/hodbcomtcedit.html",{ 'tc_db': apply })
def hodbcomtcupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbcomtc')
    return render(request,"hod/hodbcomtc.html",{ 'tc_db':apply })    
# def hodbcomtcdelete(request, id):
#     apply = tc.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbcomtc')    
    

def hodbschome(request):
    return render(request,'hod/hodbschome.html')
def hodbschall(request):
    apply= hallticket.get_all_by_c("BSc")
    return render(request, "hod/hodbschall.html" , { 'hallticket': apply })  
def hodbschalledit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"hod/hodbschalledit.html",{ 'hallticket': apply })
def hodbschallupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbschall')
    return render(request,"hod/hodbschall.html",{ 'hallticket':apply })    
# def hodbschalldelete(request, id):
#     apply = hallticket.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbschall')    


def hodbsctc(request):
    apply= tc_db.get_all_by_c("BSc")
    return render(request, "hod/hodbsctc.html" , { 'tc_db': apply })  
def hodbsctcedit(request, id):
    apply = tc_db.objects.get(id=id)
    return render(request,"hod/hodbsctcedit.html",{ 'tc_db': apply })
def hodbsctcupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/hodbsctc')
    return render(request,"hod/hodbsctc.html",{ 'tc_db':apply })    
# def hodbsctcdelete(request, id):
#     apply = tc.objects.get(id=id)
#     apply.delete()
#     return redirect ('/hodbsctc')    
    



#admin hallticket nodue


def ahallticketnodue(request):
    apply= hallticket.objects.all()
    return render(request, "admin/ahallticketnodue.html" , { 'hallticket': apply }) 
def hallticketnodueedit(request, id):
    apply = hallticket.objects.get(id=id)
    return render(request,"admin/hallticketnodueedit.html",{ 'hallticket': apply })
def hallticketnodueupdate(request, id):
    apply =hallticket.objects.get(id=id)
    form=hallform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/ahallticketnodue')
    return render(request,"admin/ahallticketnodue.html",{ 'hallticket':apply }) 

    
#admin tc nodue
def atcnodue(request):
    apply= tc_db.objects.all()
    return render(request, "admin/atcnodue.html" , { 'tc_db': apply }) 
def tcnodueedit(request, id):
    apply = tc_db.objects.get(id=id)
    return render(request,"admin/tcnodueedit.html",{ 'tc_db': apply })
def tcnodueupdate(request, id):
    apply =tc_db.objects.get(id=id)
    form=tcform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/atcnodue')
    return render(request,"admin/atcnodue.html",{ 'tc_db':apply }) 


#admin sports nodue
def asportsnodue(request):
    apply= sportsdb.objects.all()
    return render(request, "admin/asportsnodue.html" , { 'sportsdb': apply }) 
def sportsnodueedit(request, id):
    apply = sportsdb.objects.get(id=id)
    return render(request,"admin/sportsnodueedit.html",{ 'sportsdb': apply })
def sportsnodueupdate(request, id):
    apply =sportsdb.objects.get(id=id)
    form=spform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/asportsnodue')
    return render(request,"admin/asportsnodue.html",{ 'sportsdb':apply }) 


#admin library nodue
def alibrarynodue(request):
    apply= librarydb.objects.all()
    return render(request, "admin/alibrarynodue.html" , { 'librarydb': apply }) 
def librarynodueedit(request, id):
    apply = librarydb.objects.get(id=id)
    return render(request,"admin/librarynodueedit.html",{ 'librarydb': apply })
def librarynodueupdate(request, id):
    apply =librarydb.objects.get(id=id)
    form=libform(request.POST, instance=apply)
    if form.is_valid():
        form.save()
        return redirect ('/alibrarynodue')
    return render(request,"admin/alibrarynodue.html",{ 'librarydb':apply }) 




import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def some_view(request,regno):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFontSize(22)
    p.drawString(170, 800, "Acharya Bangalore B School")
    p.setFontSize(14)
    p.drawString(220, 760, "No due Certificate")
    p.setFontSize(13)
    p.drawString(40, 720, "This is to certify that this particular student is cleared all the dues that ")
    p.drawString(40, 700, "is to be paid to the organisation ")
    p.drawString(150, 610, "Register Number : ")
    p.drawString(255, 612, request.session.get('student_regno'))
    p.drawString(150, 590, "Name :")
    p.drawString(255, 590, request.session.get('student_name'))
    p.drawString(150, 570, "Course :")
    p.drawString(255, 570, request.session.get('student_course'))
    p.drawString(150, 550, "Year :")
    p.drawString(255, 550, request.session.get('student_year'))


 
    p.setFont("Courier", 16)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')



def a(request):
    return render(request,"a.html")


def vish(request):
    return render(request,'vish.html')
def vishlogin(request):
    return render(request,'vishlogin.html')
def vishstudlogin(request):
    return render(request,'vishstudlogin.html')
def vishadmin(request):
    return render(request,'vishadmin.html')
def vinav(request):
    return render(request,'vinav.html')