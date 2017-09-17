from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserForm, SignInForm
from blog.models import User, Post
from django.views.generic import View

# Create your views here.
class Indexview(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'Post_objects'
    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/about.html'

class PostCreate(CreateView):
    model = Post
    fields = ['user', 'title', 'content']

class UserFormView(View):
    form_class = UserForm
    template_name = 'blog/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
         # Does not save it to the database
        if form.is_valid():
            user = form.save(commit=False)
             #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

             #returns User Objects if credentials are correct
            #user = authenticate(username=username, password=password)
            #if user is not None:

                 #checking if the account is not banned
                #if user.is_active:
                    #login(request, user)
            return redirect('blog:index')
        #return render(request, self.template_name, {'form': form})

class SignInView(View):
    form_class = SignInForm
    template_name = 'blog/Sign_inForm.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('blog:index')
        else:
            return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blog:sign-in')
    #return render(request, "Sign_inForm.html", {})


        # Return an 'invalid login' error message.
