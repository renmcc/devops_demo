from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.models import User

class MyView(View):
    def get(self, request, *args, **kwargs):
        per = 10

        try:
            page = int(request.GET.get("page", 1))
        except:
            page = 1
        end = page * 10
        start = end - 10

        queryset = User.objects.all()[start:end]
        data = list(queryset.values("id","username", "email"))
        return JsonResponse(data, safe=False)

def articles(request, *args, **kwargs):
    #return HttpResponse(args)
    return HttpResponse(kwargs.values())

def index(request):
    if request.method == "GET":
        print(request.GET)
        data = request.GET.copy()
        data["name"] = 'abc'
        print(data)

        data1 = request.GET.getlist("name")
        print(data1)
    elif request.method == 'POST':
        print(request.POST)

    return HttpResponse("")







def index_template(request):
    context = {"name": "reboot"}
    return render(request, "test.html", context)
