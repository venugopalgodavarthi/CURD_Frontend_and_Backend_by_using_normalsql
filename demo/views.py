from django.shortcuts import render
from django.http import HttpResponse
from pro5.dbconnect import cus,db
# Create your views here.

def base(request):
    return render(request,"base.html")

def create(request):
    cus.execute("create table emp(eid int primary key,ename varchar(20), email varchar(20))")
    db.commit()
    return render(request,'create.html')

def insert(request):
    if request.method=='POST':
        eid = request.POST['eid']
        ename = request.POST['ename']
        email = request.POST['email']
        val=[eid,ename,email]
        cus.execute("insert into emp (eid,ename,email) values (%s,%s,%s)",val)
        db.commit()
        return HttpResponse('insert the value')
    return render(request,"insert.html")

def select(request):
    cus.execute("select * from emp")
    res=cus.fetchall()
    return render(request,'select.html',{'res':res})

def update(request):
    if request.method=='POST':
        r=request.POST['eid']
        val=[r]
        cus.execute("select * from emp where eid=%s",val)
        res=cus.fetchone()
        return render(request,'update.html',{'res':res})     
    return render(request,'update.html')

def update_value(request):
    if request.method=='POST':
        eid = request.POST['eid']
        ename = request.POST['ename']
        email = request.POST['email']
        val=[ename,email,int(eid)]
        cus.execute("update emp set ename=%s, email=%s  where eid=%s",val)
        db.commit()
        return HttpResponse("values is update")
    
def delete(request):
    if request.method=='POST':
        r=request.POST['eid']
        val=[r]
        cus.execute("select * from emp where eid=%s",val)
        res=cus.fetchone()
        return render(request,'delete.html',{'res':res})     
    return render(request,'delete.html')

def delete_value(request):
    if request.method=='POST':
        eid = request.POST['eid']
        val=[int(eid)]
        cus.execute("delete from emp where eid=%s",val)
        db.commit()
        return HttpResponse("record is deleted")
    
    
    