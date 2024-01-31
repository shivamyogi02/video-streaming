from django.shortcuts import render
from . import pool
from django.http import JsonResponse
import os
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def ShowInterface(request):
    return render(request,"ShowInterface.html")
@xframe_options_exempt
def SubmitShow(request):
 try:
    db,cmd=pool.ConnectionPooling()

    categoryid=request.POST['categoryid']
    showname = request.POST['showname']
    type = request.POST['type']
    description=request.POST['description']
    year = request.POST['year']
    rating = request.POST['rating']
    artist = request.POST['artist']
    status= request.POST['status']
    showstatus = request.POST['showstatus']
    episodes = request.POST['episodes']
    poster=request.FILES['poster']
    trailerurl = request.FILES['trailerurl']
    videourl = request.FILES['videourl']

    q="insert into shows(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster,trailerurl,videourl)values('{0}','{1}','{2}','{3}','{4}',{5},'{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster.name,trailerurl.name,videourl.name)
    print(q)
    cmd.execute(q)
    db.commit()
    # wb(write bytes)
    F = open("F:/VideoStream/assets/" + poster.name, "wb")
    for chunk in poster.chunks():
        F.write(chunk)
    F.close()
    F = open("F:/VideoStream/assets/" + trailerurl.name, "wb")
    for chunk in trailerurl.chunks():
        F.write(chunk)
    F.close()
    F = open("F:/VideoStream/assets/" + videourl.name, "wb")
    for chunk in videourl.chunks():
        F.write(chunk)
    F.close()

    db.close()
    return render(request,"ShowInterface.html",{'status':True})

 except Exception as e:
    print("error:", e)
    return render(request, "ShowInterface.html",{'status':False})
@xframe_options_exempt
def DisplayAllShow(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,"DisplayAllShows.html",{'rows':rows})
    except Exception as e:
        print("error:",e)
        return render(request, "DisplayAllShows.html", {'rows': []})
@xframe_options_exempt
def ShowById(request):
    try:
        sid=request.GET['sid']
        db, cmd = pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid)  from shows S where S.showid={}".format(sid)
        cmd.execute(q)
        print(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"ShowById.html",{'row':row})
    except Exception as e:
        print("errror:",e)
        return render(request, "ShowById.html", {'row': []})
@xframe_options_exempt
def EditDeleteShowData(request):
    try:
        btn=request.GET["btn"]
        if(btn=="Edit"):
            categoryid = request.GET['categoryid']
            showid=request.GET['showid']
            showname = request.GET['showname']
            type = request.GET['type']
            description = request.GET['description']
            year = request.GET['year']
            rating = request.GET['rating']
            artist = request.GET['artist']
            status = request.GET['status']
            showstatus = request.GET['showstatus']
            episodes = request.GET['episodes']
            db, cmd = pool.ConnectionPooling()
            q="update shows set categoryid='{}',showname='{}',type='{}',description='{}',year='{}',rating='{}',artist='{}',status='{}',showstatus='{}',episodes='{}' where showid='{}'".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,showid)

            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            db, cmd = pool.ConnectionPooling()
            showid=request.GET['showid']
            q="delete from shows where showid={}".format(showid)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request,"ShowById.html",{'status':True})
    except Exception as e:
        print("errror:",e)
        return render(request, "ShowById.html", {'status':False})
@xframe_options_exempt
def EditPoster(request):
 try:
    db,cmd=pool.ConnectionPooling()

    showid=request.POST['showid']
    filename = request.POST['filename']
    poster=request.FILES['poster']
    q="update shows set poster='{0}' where showid={1}".format(poster.name,showid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    F=open("F:/VideoStream/assets/"+poster.name,"wb")
    for chunk in poster.chunks():
        F.write(chunk)
    F.close()
    os.remove("F:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"ShowById.html",{'status':True})

 except Exception as e:
    print("error",e)
    return render(request, "ShowById.html",{'status':True})
@xframe_options_exempt
def EditTrailer(request):
 try:
    db,cmd=pool.ConnectionPooling()

    showid=request.POST['showid']
    filename = request.POST['filename']
    trailerurl=request.FILES['trailerurl']
    q="update shows set trailerurl='{0}' where showid={1}".format(trailerurl.name,showid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    F=open("F:/VideoStream/assets/"+trailerurl.name,"wb")
    for chunk in trailerurl.chunks():
        F.write(chunk)
    F.close()
    os.remove("F:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"ShowById.html",{'status':True})

 except Exception as e:
    print("error",e)
    return render(request, "ShowById.html",{'status':True})
@xframe_options_exempt
def EditVideo(request):
 try:
    db,cmd=pool.ConnectionPooling()

    showid=request.POST['showid']
    filename = request.POST['filename']
    videourl=request.FILES['videourl']
    q="update shows set videourl='{0}' where showid={1}".format(videourl.name,showid)
    print(q)
    cmd.execute(q)
    db.commit()
    #wb(write bytes)
    F=open("F:/VideoStream/assets/"+videourl.name,"wb")
    for chunk in videourl.chunks():
        F.write(chunk)
    F.close()
    os.remove("F:/VideoStream/assets/"+filename)
    db.close()
    return render(request,"ShowById.html",{'status':True})

 except Exception as e:
    print("error",e)
    return render(request, "ShowById.html",{'status':True})
@xframe_options_exempt
def DisplayAllShowJSON(request):
     try:
         cid=request.GET["cid"]

         db, cmd = pool.ConnectionPooling()
         q = "select * from shows where categoryid={}".format(cid)
         cmd.execute(q)
         rows = cmd.fetchall()
         db.close()
         return JsonResponse(rows, safe=False)
     except Exception as e:
         return JsonResponse([], safe=False)