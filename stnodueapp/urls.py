from django.urls import path
from stnodueapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('main',views.main,name='main'),
    path('contact',views.contact,name='contact'),
    path('contactview',views.contactview,name='contactview'),
    path('accountscontact',views.accountscontact,name='accountscontact'),
    path('bcacontact',views.bcacontact,name='bcacontact'),
    path('bcomcontact',views.bcomcontact,name='bcomcontact'),
    path('bsccontact',views.bsccontact,name='bsccontact'),
    path('libcontact',views.libcontact,name='libcontact'),
    path('sportscontact',views.sportscontact,name='sportscontact'),

    path('a',views.a,name='a'),


    path('adminlogin',views.adminlogin,name='adminlogin'), 
    path('home',views.home,name='home'),
    path('addstud',views.addstud, name='addstud'),
    #stud logout
    path('signout',views.signout,name="signout"),

    #bcalist
    path('bcalist',views.bcalist,name='bcalist'),
    path('delete1/<int:id>', views.delete1,name='delete1'),
    path('bcaedit/<int:id>', views.bcaedit,name='bcaedit'),
    path('update1/<int:id>', views.update1,name='update1'),
    path('bcasecndyear',views.bcasecndyear),
    path('bcafrstyear',views.bcafrstyear),
    path('bcathirdyear',views.bcathirdyear),

    #bcomlist
    path('bcomlist',views.bcomlist,name='bcomlist'),
    path('delete2/<int:id>', views.delete2,name='delete2'),
    path('bcomedit/<int:id>', views.bcomedit,name='bcomedit'),
    path('update2/<int:id>', views.update2,name='update2'),
    path('bcomsecndyear',views.bcomsecndyear),
    path('bcomfrstyear',views.bcomfrstyear),
    path('bcomthirdyear',views.bcomthirdyear),

    #bsclist
    path('bsclist',views.bsclist,name='bsclist'),
    path('delete3/<int:id>', views.delete3,name='delete3'),
    path('bscedit/<int:id>', views.bscedit,name='bscedit'),
    path('update3/<int:id>', views.update3,name='update3'),
    path('bscsecndyear',views.bscsecndyear),
    path('bscfrstyear',views.bscfrstyear),
    path('bscthirdyear',views.bscthirdyear),


    #faculty register
    path('addfaculty',views.addfaculty,name='addfaculty'),
    path('faclist',views.faclist,name='faclist'),
    path('facdelete/<int:id>', views.facdelete,name='facdelete'),
    path('facedit/<int:id>', views.facedit,name='facedit'),
    path('facupdate/<int:id>', views.facupdate,name='facupdate'),

    #stud login
    path('studlogin',views.studlogin,name='studlogin'),
    #faclogin
    path('faclogin',views.faclogin,name='faclogin'),    
    path('libraryhome',views.libraryhome,name='libraryhome'),
    path('accountshome',views.accountshome,name='accountshome'),
    path('sportshome',views.sportshome,name='sportshome'),
    path('hodbcahome',views.hodbcahome,name='hodbcahome'),
    path('hodbcomhome',views.hodbcomhome,name='hodbcomhome'),
    path('hodbschome',views.hodbschome,name='hodbschome'),

    #bcastud home
    path('bcahome',views.bcahome,name='bcahome'),

    #bcom stud home
    path('bcomhome',views.bcomhome,name='bcomhome'),

    #bsc stud home
    path('bschome',views.bschome,name='bschome'),

    path('nodue',views.nodue,name='nodue'),

    path('noduestatus',views.noduestatus,name='noduestatus'),
    path('noduestatusdeletehall/<str:regno>',views.noduestatusdeletehall,name='noduestatusdeletehall'),
    path('noduestatusdeletelibrary/<str:regno>',views.noduestatusdeletelibrary,name='noduestatusdeletelibrary'),
    path('noduestatusdeletetc/<str:regno>',views.noduestatusdeletetc,name='noduestatusdeletetc'),
    path('noduestatusdeletesports/<str:regno>',views.noduestatusdeletesports,name='noduestatusdeletesports'),

    path('hallviewdetails/<int:id>',views.hallviewdetails),
    path('halldetailsupdate/<int:id>', views.halldetailsupdate),
    path('sportsviewdetails/<int:id>',views.sportsviewdetails),
    path('sportsdetailsupdate/<int:id>', views.sportsdetailsupdate,name='sportsdetailsupdate'),
    path('libraryviewdetails/<int:id>',views.libraryviewdetails),
    path('librarydetailsupdate/<int:id>', views.librarydetailsupdate),
    path('tcviewdetails/<int:id>',views.tcviewdetails),
    path('tcdetailsupdate/<int:id>', views.tcdetailsupdate),
    



    path('hallnodue',views.hallnodue,name='hallnodue'),
    path('tcnodue',views.tcnodue,name='tcnodue'),
    path('librarynodue',views.librarynodue,name='librarynodue'),
    path('sportsnodue',views.sportsnodue,name='sportsnodue'),

    #accounts
    # path('accountshalldelete/<int:id>', views.accountshalldelete,name='accountshalldelete'),
    path('accountshalledit/<int:id>', views.accountshalledit,name='accountshalledit'),
    path('accountshallupdate/<int:id>', views.accountshallupdate,name='accountshallupdate'),
    path('bcomaccountshall',views.bcomaccountshall,name='bcomaccountshall'),
    path('bcaaccountshall',views.bcaaccountshall,name='bcaaccountshall'),
    path('bscaccountshall',views.bscaccountshall,name='bscaccountshall'),


    # path('bscsecndyearh',views.bscsecndyearh),
    # path('bscfrstyearh',views.bscfrstyearh),
    # path('bscthirdyearh',views.bscthirdyearh),
    # path('accountstcdelete/<int:id>', views.accountstcdelete,name='accountstcdelete'),
    path('accountstcedit/<int:id>', views.accountstcedit,name='accountstcedit'),
    path('accountstcupdate/<int:id>', views.accountstcupdate,name='accountstcupdate'),
    path('bcomaccountstc',views.bcomaccountstc,name='bcomaccountstc'),
    path('bcaaccountstc',views.bcaaccountstc,name='bcaaccountstc'),    
    path('bscaccountstc',views.bscaccountstc,name='bscaccountstc'),


    #library
    path('bcalibhall',views.bcalibhall,name='bcalibhall'),
    path('bcomlibhall',views.bcomlibhall,name='bcomlibhall'),
    path('bsclibhall',views.bsclibhall,name='bsclibhall'),
    # path('libhalldelete/<int:id>', views.libhalldelete,name='libhalldelete'),
    path('libhalledit/<int:id>', views.libhalledit,name='libhalledit'),
    path('libhallupdate/<int:id>', views.libhallupdate,name='libhallupdate'),

    path('bcalib',views.bcalib,name='bcalib'),
    path('bcomlib',views.bcomlib,name='bcomlib'),
    path('bsclib',views.bsclib,name='bsclib'),
    # path('libdelete/<int:id>', views.libdelete,name='libdelete'),
    path('libedit/<int:id>', views.libedit,name='libedit'),
    path('libupdate/<int:id>', views.libupdate,name='libupdate'),

 

    #sports
    path('bcasportshall',views.bcasportshall,name='bcasportshall'),
    path('bcomsportshall',views.bcomsportshall,name='bcomsportshall'),
    path('bscsportshall',views.bscsportshall,name='bscsportshall'),
    # path('sportshalldelete/<int:id>', views.sportshalldelete,name='sportshalldelete'),
    path('sportshalledit/<int:id>', views.sportshalledit,name='sportshalledit'),
    path('sportshallupdate/<int:id>', views.sportshallupdate,name='sportshallupdate'),



    path('bcasports',views.bcasports,name='bcasports'),
    path('bcomsports',views.bcomsports,name='bcomsports'),
    path('bscsports',views.bscsports,name='bscsports'),
    # path('sportsdelete/<int:id>', views.sportsdelete,name='sportsdelete'),
    path('sportsedit/<int:id>', views.sportsedit,name='sportsedit'),
    path('sportsupdate/<int:id>', views.sportsupdate,name='sportsupdate'),


    #hod
    path('hodbcahall',views.hodbcahall,name='hodbcahall'),
    # path('hodbcahalldelete/<int:id>', views.hodbcahalldelete,name='hodbcahalldelete'),
    path('hodbcahalledit/<int:id>', views.hodbcahalledit,name='hodbcahalledit'),
    path('hodbcahallupdate/<int:id>', views.hodbcahallupdate,name='hodbcahallupdate'),

    path('hodbcatc',views.hodbcatc,name='hodbcatc'),
    # path('hodbcatcdelete/<int:id>', views.hodbcatcdelete,name='hodbcatcdelete'),
    path('hodbcatcedit/<int:id>', views.hodbcatcedit,name='hodbcatcedit'),
    path('hodbcatcupdate/<int:id>', views.hodbcatcupdate,name='hodbcatcupdate'),

    path('hodbcomhall',views.hodbcomhall,name='hodbcomhall'),
    # path('hodbcomhalldelete/<int:id>', views.hodbcomhalldelete,name='hodbcomhalldelete'),
    path('hodbcomhalledit/<int:id>', views.hodbcomhalledit,name='hodbcomhalledit'),
    path('hodbcomhallupdate/<int:id>', views.hodbcomhallupdate,name='hodbcomhallupdate'),


    path('hodbcomtc',views.hodbcomtc,name='hodbcomtc'),
    # path('hodbcomtcdelete/<int:id>', views.hodbcomtcdelete,name='hodbcomtcdelete'),
    path('hodbcomtcedit/<int:id>', views.hodbcomtcedit,name='hodbcomtcedit'),
    path('hodbcomtcupdate/<int:id>', views.hodbcomtcupdate,name='hodbcomtcupdate'),



    path('hodbschall',views.hodbschall,name='hodbschall'),
    # path('hodbschalldelete/<int:id>', views.hodbschalldelete,name='hodbschalldelete'),
    path('hodbschalledit/<int:id>', views.hodbschalledit,name='hodbschalledit'),
    path('hodbschallupdate/<int:id>', views.hodbschallupdate,name='hodbschallupdate'),

    path('hodbsctc',views.hodbsctc,name='hodbsctc'),
    # path('hodbsctcdelete/<int:id>', views.hodbsctcdelete,name='hodbsctcdelete'),
    path('hodbsctcedit/<int:id>', views.hodbsctcedit,name='hodbsctcedit'),
    path('hodbsctcupdate/<int:id>', views.hodbsctcupdate,name='hodbsctcupdate'),
    
    #hallticket admin
    path('ahallticketnodue',views.ahallticketnodue,name='ahallticketnodue'),
    path('hallticketnodueedit/<int:id>', views.hallticketnodueedit,name='hallticketnodueedit'),
    path('hallticketnodueupdate/<int:id>', views.hallticketnodueupdate,name='hallticketnodueupdate'),

    
    #tc admin
    path('atcnodue',views.atcnodue,name='atcnodue'), 
    path('tcnodueedit/<int:id>', views.tcnodueedit,name='tcnodueedit'),
    path('tcnodueupdate/<int:id>', views.tcnodueupdate,name='tcnodueupdate'),
  
     #library admin
    path('alibrarynodue',views.alibrarynodue,name='alibrarynodue'), 
    path('librarynodueedit/<int:id>', views.librarynodueedit,name='librarynodueedit'),
    path('librarynodueupdate/<int:id>', views.librarynodueupdate,name='librarynodueupdate'),  
     #sports admin
    path('asportsnodue',views.asportsnodue,name='asportsnodue'),
    path('sportsnodueedit/<int:id>', views.sportsnodueedit,name='sportsnodueedit'),
    path('sportsnodueupdate/<int:id>', views.sportsnodueupdate,name='sportsnodueupdate'),


    path('some_view/<str:regno>',views.some_view),



    path('vish',views.vish),
    path('vishlogin',views.vishlogin),
    path('vishstudlogin',views.vishstudlogin),
    path('vishadmin',views.vishadmin),
    path('vinav',views.vinav),



]