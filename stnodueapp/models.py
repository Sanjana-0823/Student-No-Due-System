
from pickle import FALSE, TRUE
from django.db import models

class student(models.Model): 
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course=models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    pass1 = models.CharField(max_length=20)
    pass2 = models.CharField(max_length=20)

    @staticmethod
    def get_student_by_studreg(regno):
        try:
            return student.objects.get(regno=regno)
        except:
            return False
    def get_student_by_year(year):
        try:
            return student.objects.get(year=year)
        except:
            return False

    class Meta:
        db_table = "student"
    @staticmethod
    def get_all_by_frstyear(year_name,course_name):
        return student.objects.filter(year=year_name,course=course_name)   
    def get_all_by_scondyear(year_name,course_name):
        return student.objects.filter(year=year_name,course=course_name) 
    def get_all_by_thirdyear(year_name,course_name):
        return student.objects.filter(year=year_name,course=course_name)  
    def get_all_by_course(course_name):
        return student.objects.filter(course=course_name)

    def __str__(self):
        return 'student: {self.name}'


class faculty(models.Model): 
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    department=models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    conpassword = models.CharField(max_length=20)

    class Meta:
        db_table = "faculty"
        
    def __str__(self):
        return 'faculty: {self.name}'


        

class hallticket(models.Model):
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    course=models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    date=models.DateField(auto_now=True)
    noduereasons=models.CharField(max_length=100)
    library=models.CharField(max_length=20,null=True,default=None)
    libraryremark=models.CharField(max_length=200,null=True,default=None)
    accounts=models.CharField(max_length=20,null=True,default=None)
    accountsremark=models.CharField(max_length=200,null=True,default=None)
    sports=models.CharField(max_length=20,null=True,default=None)
    sportsremark=models.CharField(max_length=200,null=True,default=None)
    hod=models.CharField(max_length=20,null=True,default=None)
    hodremark=models.CharField(max_length=200,null=True,default=None)
    admin=models.CharField(max_length=20,null=True,default=None)
    
    class Meta:
        db_table="hallticket"


    @staticmethod
    
    def get_all_by_c(course_name):
        return hallticket.objects.filter(course=course_name)
    @staticmethod
    def get_file_by_year(regno):
        try:
            return hallticket.objects.filter(regno=regno)
        except:
            return False


class tc_db(models.Model):
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob=models.DateField()
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    addate=models.DateField()
    course=models.CharField(max_length=10)
    dateofapply=models.DateField(auto_now=True)
    noduereasons=models.CharField(max_length=100)
    accounts=models.CharField(max_length=20,null=True,default=None)
    accountsremark=models.CharField(max_length=200,null=True,default=None)
    hod=models.CharField(max_length=20,null=True,default=None)
    hodremark=models.CharField(max_length=200,null=True,default=None)
    admin=models.CharField(max_length=20,null=True,default=None)
    
    class Meta:
        db_table="tc_db"       


    @staticmethod
    def get_all_by_c(course_name):
        return tc_db.objects.filter(course=course_name) 
    @staticmethod
    def get_file_by_year(regno):
        try:
            return tc_db.objects.filter(regno=regno)
        except:
            return False


class tc(models.Model):
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob=models.DateField()
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    addate=models.DateField()
    course=models.CharField(max_length=10)
    dateofapply=models.DateField(auto_now=True)
    noduereasons=models.CharField(max_length=100)
    accounts=models.CharField(max_length=20,null=True,default=None)
    accountsremark=models.CharField(max_length=200,null=True,default=None)
    hod=models.CharField(max_length=20,null=True,default=None)
    hodremark=models.CharField(max_length=200,null=True,default=None)
    admin=models.CharField(max_length=20,null=True,default=None)
    
    class Meta:
        db_table="tc"       


    @staticmethod
    def get_all_by_c(course_name):
        return tc.objects.filter(course=course_name) 
    @staticmethod
    def get_file_by_year(regno):
        try:
            return tc.objects.filter(regno=regno)
        except:
            return False

class librarydb(models.Model):
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    course=models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    date=models.DateField(auto_now=True)
    noduereasons=models.CharField(max_length=100)
    library=models.CharField(max_length=20,null=True,default=None)
    libraryremark=models.CharField(max_length=200,null=True,default=None)
    admin=models.CharField(max_length=20,null=True,default=None)
    class Meta:
        db_table="librarydb"       
    @staticmethod
    def get_all_by_c(course_name):
        return librarydb.objects.filter(course=course_name) 
    @staticmethod
    def get_file_by_year(regno):
        try:
            return librarydb.objects.filter(regno=regno)
        except:
            return False

class sportsdb(models.Model):
    regno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    course=models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    date=models.DateField(auto_now=True)
    noduereasons=models.CharField(max_length=100)
    sports=models.CharField(max_length=20,null=True,default=None)
    sportsremark=models.CharField(max_length=200,null=True,default=None)
    admin=models.CharField(max_length=20,null=True,default=None)
    
    class Meta:
        db_table="sportsdb"


    @staticmethod
    def get_all_by_c(course_name):
        return sportsdb.objects.filter(course=course_name)
    @staticmethod
    def get_file_by_year(regno):
        try:
            return sportsdb.objects.filter(regno=regno)
        except:
            return False

class contactus(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=50)
    remark=models.CharField(max_length=200)
    class Meta:
        db_table="contactus"