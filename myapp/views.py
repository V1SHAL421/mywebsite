from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignUpForm, PostForm
from .models import Post

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['Your Name']
            surname = form.cleaned_data['Your Surname']
            surname = form.cleaned_data['Userrname']
            bio = form.cleaned_data['Bio']
            email = form.cleaned_data['Your Email']
            new_password = form.cleaned_data['Password']
            password_confirmation = form.cleaned_data['Confirm Password']
            
            # Do something with the data, such as saving it to the database
            
            # Redirect to a success page or another view
            return redirect('success')
    else:
        form = SignUpForm()
    
    return render(request, 'sign_up.html', {'form': form})

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
