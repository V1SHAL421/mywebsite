from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

from django.shortcuts import render, redirect
from .forms import WelcomeForm

def start_page(request):
    if request.method == 'POST':
        form = WelcomeForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            # Do something with the data, such as saving it to the database
            
            # Redirect to a success page or another view
            return redirect('success')
    else:
        form = WelcomeForm()
    
    return render(request, 'start_page.html', {'form': form})

def success(request):
    return render(request, 'success.html')
