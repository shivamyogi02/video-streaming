from django.shortcuts import render
from . import pool
import os
import time
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def EpisodeInterface(request):
    return render(request,"EpisodeInterface.html")
@xframe_options_exempt
def SubmitEpisode(request):
    try:
        db,cmd = pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        showid = request.POST['showid']
        episodenumber = request.POST['episodenumber']
        description = request.POST['description']
        poster = request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']
        q = "insert into episode (categoryid,showid,episodenumber,description,poster,trailer,video) values({0},{1},{2},'{3}','{4}','{5}','{6}')".format(categoryid,showid,episodenumber,description,poster.name,trailer.name,video.name)
        print(q)
        cmd.execute(q)

        # wb(write bytes)
        F = open("F:/videostream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()

        F = open("F:/videostream/assets/"+trailer.name, "wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()

        F = open("F:/videostream/assets/"+video.name, "wb")
        for chunk in video.chunks():
            F.write(chunk)
        F.close()

        db.commit()
        db.close()
        return render(request, "EpisodeInterface.html",{'status':True})

    except Exception as e:
        print("errrrrrrrr",e)
        return render(request, "EpisodeInterface.html", {'status': False})



@xframe_options_exempt
def DisplayAllEpisodes(request):
    try:
        db,cmd = pool.ConnectionPooling()
        q = "select * from episode"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request,"DisplayAllEpisode.html",{'rows':rows})
    except Exception as e:
        return render(request, "DisplayAllEpisode.html", {'rows': [] })
        print("error:",e)

@xframe_options_exempt
def EpisodeById(request):
    try:
        eid = request.GET['eid']
        db,cmd = pool.ConnectionPooling()
        q = "select * from episode where episodeid = {} ".format(eid)
        print(q)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request,"EpisodeById.html",{'row':row})
    except Exception as e:
        print("error:",e)
        return render(request, "EpisodeById.html", {'row':[]})

@xframe_options_exempt
def EditDeleteEpisodeData(request):
    try:
        btn = request.GET['btn']
        if(btn == "Edit"):
            episodeid = request.GET['episodeid']
            #categoryid = request.GET['categoryid']
            #showid = request.GET['showid']
            episodenumber = request.GET['episodenumber']
            description = request.GET['description']
            db,cmd = pool.ConnectionPooling()
            q = "update episode set episodenumber={},description='{}' where episodeid={}".format(episodenumber,description,episodeid)
            cmd.execute(q)
            db.commit()
            db.close()
            #time.sleep(5)
            #return DisplayAll(request)
        elif(btn == "Delete"):
            episodeid = request.GET['episodeid']
            db, cmd = pool.ConnectionPooling()
            q = "delete from episode where episodeid={}".format(episodeid)
            cmd.execute(q)
            db.commit()
            db.close()
            #time.sleep(5)
            #return DisplayAll(request)
        return render(request,"EpisodeById.html",{'status':True})
    except Exception as e:
        print("error :", e)
        return render(request, "EpisodeById.html", {'status':False})


@xframe_options_exempt
def EditEpisodePoster(request):
    try:
        db,cmd = pool.ConnectionPooling()
        episodeid = request.POST['episodeid']
        filename = request.POST['filename']
        poster = request.FILES['poster']
        q = "update episode set poster='{0}' where episodeid= '{1}'".format(poster.name,episodeid)
        print(q)
        cmd.execute(q)
        db.commit()

        #wb(write bytes)
        F = open("F:/videostream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("F:/videostream/assets/"+filename)


        db.close()
        #time.sleep(5)
        #return DisplayAll(request)
        return render(request, "EpisodeById.html",{'status':True})

    except Exception as e:
        print("errrrrrrrr",e)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditEpisodeTrailer(request):
    try:
        db,cmd = pool.ConnectionPooling()
        episodeid = request.POST['episodeid']
        filename = request.POST['filename']
        trailer = request.FILES['trailer']
        q = "update episode set trailer='{0}' where episodeid= '{1}'".format(trailer.name,episodeid)
        print(q)
        cmd.execute(q)
        db.commit()

        #wb(write bytes)
        F = open("F:/videostream/assets/"+trailer.name,"wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()
        os.remove("F:/videostream/assets/"+filename)


        db.close()
        #time.sleep(5)
        #return DisplayAll(request)
        return render(request, "EpisodeById.html",{'status':True})

    except Exception as e:
        print("errrrrrrrr",e)
        return render(request, "EpisodeById.html", {'status': False})



@xframe_options_exempt
def EditEpisodeVideo(request):
    try:
        db,cmd = pool.ConnectionPooling()
        episodeid = request.POST['episodeid']
        filename = request.POST['filename']
        video = request.FILES['video']
        q = "update episode set video='{0}' where episodeid= '{1}'".format(video.name,episodeid)
        print(q)
        cmd.execute(q)
        db.commit()

        #wb(write bytes)
        F = open("F:/videostream/assets/"+video.name,"wb")
        for chunk in video.chunks():
            F.write(chunk)
        F.close()
        os.remove("F:/videostream/assets/"+filename)
        db.close()
        #time.sleep(5)
        #return DisplayAll(request)
        return render(request, "EpisodeById.html",{'status':True})
    except Exception as e:
        print("errrrrrrrr",e)
        return render(request, "EpisodeById.html", {'status': False})
