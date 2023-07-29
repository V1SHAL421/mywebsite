from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from .forms import LogInForm, SignUpForm, PostForm
from .models import Post, User

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data
            user = form.save()
            login(request, user)
            # Saves data to the database
            
            # Redirect to a success page or another view
            return redirect('success')
        else:
            print(form.errors)
    else: 
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to a success page or another view
                return redirect('success')
            else:
                # Handle invalid login credentials, e.g., display an error message
                form.add_error(None, "Invalid username or password.")

    else: 
        form = LogInForm()

    return render(request, 'log_in.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a new post object
            post = form.save()
            
            # Redirect to the post detail page or another view
            return redirect('post_submission')
    else:
        form = PostForm()
    
    return render(request, 'post_create.html', {'form': form})



def success(request):
    return render(request, 'success.html')

def post_submission(request):
    return render(request, 'post_submission.html')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'post_delete.html', {'post': post})
