from django.shortcuts import render


def home(request):
    if request.GET.get("num"):
        try:
            num = int(request.GET.get("num"))
            if num % 2 == 0 :
                msg = "Num " + str(num) + "  is even "

            else:
                msg = "Num " + str(num) + "  is odd "
            return render(request,"home.html",{"msg":msg})
        except ValueError:
            msg = "You should enter integers only "
            return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")



