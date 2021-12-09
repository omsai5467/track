from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import product
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
	if request.method == "POST":
		user = authenticate(username = request.POST['fname'],  password=request.POST['pass'])
		if user is not None:
			t = product.objects.all()
			return render(request,'product.html',{'t':t})
		    
		else:
		    return HttpResponse('alert("not corrct passs")')
			
	return render(request,'index.html')
def sign(request):
	if  request.method == 'POST':
		try:

			user = User.objects.create_user(username = request.POST['fname'],  password=request.POST['pass'])
			print(user)
			user.save()
			return redirect('/')
		except:
			return HttpResponse('user regi')

		
	return render(request,'sign.html')


@csrf_exempt

def addproduct(request):
	if request.method == 'POST':
		x = product(Pid= request.POST['pid'] ,Pname =request.POST['Pname'],Pstatus = request.POST['Pstatus'])
		x.save()
		print(x.Pid)
		# t = product.objects.all()
		t = serialize('json', product.objects.all())
		return JsonResponse({'t': t})

@csrf_exempt

def update(request):
	if request.method == "POST":
		x = product.objects.get(id = request.POST['id'])
		x.Pstatus = request.POST['Pstatus']
		x.save()
		return JsonResponse({'t': 't'})

