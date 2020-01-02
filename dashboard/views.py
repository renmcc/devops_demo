from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
import logging
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)

class UsersView(View):
    per_page = 10

    def get_queryset(self):
        return User.objects.values("id","username","email","is_active")

    def get_paginate_queryset(self, queryset):
        paginator = Paginator(queryset, self.get_per_page())
        page_obj = paginator.page(self.get_current_page())
        return page_obj.object_list

    def get_current_page(self):
        try:
            return int(self.request.GET.GET("page", 1))
        except:
            return 1

    def get_per_page(self):
        try:
            per_page = int(self.request.GET.get("per_page", 10))
            return per_page
        except:
            return self.per_page

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.get_paginate_queryset(queryset)
        return JsonResponse(list(queryset), safe=False)

class UserListView(ListView):
    template_name = 'test.html'
    model = User
    paginate_by = 10

class MyView(View):
    def get(self, request, *args, **kwargs):
        logger.debug("第一条日志")
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
