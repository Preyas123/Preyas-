from django.shortcuts import render
from testapp.models import User
from testapp.models import Client
from django.http import HttpResponseRedirect

# Create your views here.

def insertuser(request):
    if request.method=="POST":
        un  = request.POST.get("txt1")
        unm = request.POST.get("txt2")
        uct = request.POST.get("txt3")
        upr = request.POST.get("txt7")
        uas = request.POST.get("txt8")


        use=User()

        use.uno=un
        use.uname = unm
        use.ucity = uct
        use.uproject = upr
        use.uassinged = uas
        use.save()

    else:
        print("this is get request")

    return render(request,"testapp/Add_user_project.html")

def userinfo_view(request):
    users = User.objects.all()
    return render(request, 'testapp/User_project_info.html', {'users':users})


def insertclient(request):
    if request.method=="POST":
        cn  = request.POST.get("txt4")
        cnm = request.POST.get("txt5")
        cct = request.POST.get("txt6")

        cli=Client()

        cli.cno=cn
        cli.cname = cnm
        cli.ccity = cct
        cli.save()

    else:
        print("this is get request")

    return render(request,"testapp/Addclient.html")

def clientinfo_view(request):
    clients = Client.objects.all()
    return render(request, 'testapp/clientinfo.html', {'clients':clients})



def deleteuser(request,id):
    rec=User.objects.get(id=id)
    rec.delete()
    return HttpResponseRedirect('/userinfo/')
    return render(request,'testapp/User_project_info.html')

def updateuserview(request,id):
    if request.method=="POST":
        un  = request.POST.get("txt1")
        unm = request.POST.get("txt2")
        uct = request.POST.get("txt3")

        use = User()
        use.id=id
        use.uno = un
        use.uname = unm
        use.ucity = uct
        use.save()

        return HttpResponseRedirect('/userinfo/')

    else:
        use=User.objects.get(id=id)

        return render(request,'testapp/update_user_project.html',{'use':use})



def deleteclient(request,id):
    rec=Client.objects.get(id=id)
    rec.delete()
    return HttpResponseRedirect('/clientinfo/')
    return render(request,'testapp/clientinfo.html')

def updateclientview(request,id):
    if request.method=="POST":
        cn  = request.POST.get("txt4")
        cnm = request.POST.get("txt5")
        cct = request.POST.get("txt6")

        cli = Client()
        cli.id=id
        cli.cno = cn
        cli.cname = cnm
        cli.ccity = cct
        cli.save()

        return HttpResponseRedirect('/clientinfo/')

    else:
        cli=Client.objects.get(id=id)

        return render(request,'testapp/updateclient.html',{'cli':cli})

