from django.shortcuts import render,redirect

def pnf(request,exception):
    return redirect("home")

def result(request):
    return redirect("home")

def home(request):
    if request.GET.get("num"):
        try:
            num = float(request.GET.get("num"))
            if num > 0.0:
                res = num ** 0.5
                msg = " Square root = " + str(round(res,2))
                return render(request,"result.html",{"msg":msg})
            else:
                msg = "-ve numbers are not allowed "
                return render(request,"result.html",{"msg":msg})

        except ValueError:
            msg = "Numbers Only"
            return render(request,"result.html",{"msg":msg})
    else:
        return render(request,"home.html")



