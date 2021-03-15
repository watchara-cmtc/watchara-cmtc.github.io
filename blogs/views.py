from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import testdata

# Create your views here.


def hello(req):
    # return HttpResponse("Hello world ")
    tags = ['น้ำตก', 'น้ำตัก', 'น้ำเต็ก',
            'น้ำตง', 'น้ำตรง', 'น้ำตั้ง', 'น้ำต้ม']
    ratting = 4
    test = testdata.objects.get()
    return render(req, 'index.html',
                  {'testdata': test,
                   'name': 'บทความท่องเที่ยว',
                   'author': 'Guerriers',
                   'tags': tags,
                   'ratting': ratting
                   },
                  )


def layout(req):
    return render(req, 'navbar.html')


def footer(req):
    return render(req, 'footer.html')


def page1(req):
    return render(req, 'page1.html')


def form(req):
    return render(req, 'form.html')


def result(req):
    name = req.POST['name']
    des = req.POST['des']
    return render(req, 'result.html', {'name': name, 'des': des})


def datatest(req):
    test = testdata.objects.get()
    return render(
        req,
        'database.html', {'testdata': test})
