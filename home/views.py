from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
 {'name':'pinax-stripe', 'url': 'http://pypi.python.org/pypi/pinax-stripe/4.0.0'},
 {'name':'dj-stripe', 'url': 'http://pypi.python.org/pypi/dj-stripe/1.0.0.post1'},
 {'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-60',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
