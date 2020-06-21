from django.shortcuts import render
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'POST':
		inputFname = request.POST['inputFname']
		inputLname = request.POST['inputLname']
		userName = inputFname + inputLname
		email = request.POST['inputEmail1']
		password1 = request.POST['inputPassword2']
		user = User.objects.create_user(username = userName, password = password1, email = email, first_name = inputFname, last_name = inputLname)
		user.save()
		return render(request, 'login.htm')
	else:
		return render(request, 'signup.htm')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			return render(request, 'index.html')
	else:
		return render(request, 'login.htm')
