from django.shortcuts import render
from django.http import HttpResponse
from pro5.dbconnect import cus,db


def sample(request):
    return render(request,'sample.html')


def create(request):
    cus.execute("create table student(sid int primary key,sname varchar(20))")
    db.commit()
    return HttpResponse("create the table")

def insert(request,id,name):
    val=[int(id),name]
    cus.execute("insert into student (sid,sname) values (%s,%s)",val)
    db.commit()
    return HttpResponse('insert the value')

def select(request):
    cus.execute("select * from student")
    res=cus.fetchall()
    return HttpResponse(res)

def delete(request,id):
    val=[int(id)]
    cus.execute("delete from student where sid = %s",val)
    db.commit()
    return HttpResponse("delete the record")

def update(request,id,name):
    val=[name,int(id)]
    cus.execute("update student set sname=%s where sid=%s",val)
    db.commit()
    return HttpResponse("update the value")
    