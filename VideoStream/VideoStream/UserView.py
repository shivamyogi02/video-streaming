from django.shortcuts import render
from . import pool
from django.http import JsonResponse
def UserView(request):
    try:
        ses = ''
        user = ''

        try:
         if (request.session['USER']):
            ses = True
            user = request.session['USER']
         else:
            ses: False
            user = []
            print("USER",user)
         print("xxxxxxxxxxxxxx", ses)
        except Exception as e:
          print("Session Error:",e)
        db, cmd = pool.ConnectionPooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        q = "select * from shows where status='Trending'"
        cmd.execute(q)
        trows = cmd.fetchall()


        q = "select * from shows where categoryid in(select categoryid from  category where categoryname='TV Shows')"
        cmd.execute(q)
        tvrows = cmd.fetchall()
        db.close()
        return render(request,"UserInterface.html",{'rows': rows,'trows':trows,'tvrows':tvrows,'ses':ses,'user':user})
    except Exception as e:
        print(e)
        return render(request, "UserInterface.html", {'rows': []})
def Preview(request):
    ses = ''
    user = ''

    try:
         if (request.session['USER']):
            ses = True
            user = request.session['USER']
         else:
            ses: False
            user = []
         print("USER",user)
    except:
          pass
    row=request.GET['row']
    row=eval(row)
    #Main Menu
    db, cmd = pool.ConnectionPooling()
    q = "select * from category"
    cmd.execute(q)
    rows = cmd.fetchall()
    #Movies
    q = "select * from shows where categoryid=5"
    cmd.execute(q)
    movies = cmd.fetchall()

    db.close()
    return render(request, "Preview.html", {'row': row,'rows':rows,'movies':movies,'ses':ses,'user':user})

def TvPreview(request):
    row=request.GET['row']
    row=eval(row)
    #Main Menu
    db, cmd = pool.ConnectionPooling()
    q = "select * from category"
    cmd.execute(q)
    rows = cmd.fetchall()

    # Episodes
    q = "select * from episode where categoryid=7 and showid={}".format(row[1])
    cmd.execute(q)
    episodes = cmd.fetchall()

    #TvShows
    q = "select * from shows where categoryid=7"
    cmd.execute(q)
    tvshows = cmd.fetchall()

    db.close()
    return render(request, "TvPreview.html", {'row': row,'episodes':episodes,'tvshows':tvshows})

def UserDetailsSubmit(request):
   try:
    mobileno=request.GET['mobileno']
    db, cmd = pool.ConnectionPooling()
    username= request.GET['username']
    age= request.GET['age']
    gender = request.GET['gender']
    status= request.GET['status']
    q="insert into clientdetails (mobilenumber,username,age,gender,status) values('{0}','{1}','{2}','{3}','{4}')".format(mobileno,username,age,gender,status)
    print(q)
    cmd.execute(q)
    db.commit()
    db.close()
    return JsonResponse("Registration Completed Successfully", safe=False)
   except Exception as e:
     return JsonResponse("Fail to Submit Record", safe=False)

def CheckMobileNumber(request):
   try:
    mobileno=request.GET['mobileno']
    db, cmd = pool.ConnectionPooling()

    q="select *  from clientdetails where mobilenumber='{}'".format(mobileno)
    print(q)
    cmd.execute(q)
    row=cmd.fetchone()
    return JsonResponse(row, safe=False)

    db.close()

   except Exception as e:
     return JsonResponse(null, safe=False)

def UserSession(request):
   try:
    mobileno=request.GET['mobileno']
    username = request.GET['username']

    request.session["USER"]=[mobileno,username]
    print("Session Created",mobileno,username)
    return JsonResponse(True, safe=False)




   except Exception as e:
     return JsonResponse(False, safe=False)

def UserLogout(request):
   try:
    del request.session['USER']

    return UserView(request)

   except Exception as e:
    print(e)

def Searching(request):
    try:
        st = request.GET['st']
        db, cmd = pool.ConnectionPooling()

        q = "select *  from shows where showname like '%{}%'".format(st)
        print(q)
        cmd.execute(q)
        rows = cmd.fetchall()
        return JsonResponse(rows, safe=False)

        db.close()

    except Exception as e:
        return JsonResponse(null, safe=False)

