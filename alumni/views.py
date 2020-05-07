from django.shortcuts import render,redirect,reverse,get_object_or_404,HttpResponseRedirect
from .models import Projects
from .forms import UserRegisterForm,ProjectCreateForm,ProjectUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,PostSearchForm,ProjectSearchForm
from .models import Profile
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
#CBV
from django.views.generic import UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Search imports
from search_views.search import SearchListView
from search_views.filters import BaseFilter

#Search class-search capability
class ActorsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['username'] 
        }


class ProjectsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['title'] 
        }



'''def list_view(request,*args,**kwargs):
    obj = Projects.objects.all() 
    template_name = 'alumni/prolist.html' 
    context = {'obj':obj}
    return render(request,template_name,context)'''

class list_view(LoginRequiredMixin,SearchListView): 
    #user = settings.AUTH_USER_MODEL
    model = Projects
    template_name = 'alumni/prolist.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 10
    form_class = ProjectSearchForm
    filter_class = ProjectsFilter

'''def profilelist(request,*args,**kwargs):
    pro = Profile.objects.all() 
    template_name = 'alumni/porfilelist.html'
    context = {'pro':pro}''' 

class profilelist(LoginRequiredMixin,SearchListView):
    model = Profile
    template_name = 'alumni/profilelist.html'
    context_object_name = 'posts'
    paginate_by = 10 
    form_class = PostSearchForm
    filter_class = ActorsFilter


class profileldetailsview(LoginRequiredMixin,DetailView):
    model = Profile 


@login_required
def create_view(request,*args,**kwargs):
    form = ProjectCreateForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
        messages.success(request,f"The project is posted!")
        return HttpResponseRedirect('/prolist')
        
    template_name = 'alumni/procreate.html'
    context = {'form':form}
    return render(request,template_name,context)


@login_required
def detail_view(request,project_id,*args,**kwargs):
    objects =  Projects.objects.get(id=project_id) 
    pro = Profile.objects.get(user=request.user)
    #pro1 = Profile.objects.get(user=objects.student1)
    #pro2 = Profile.objects.get(user=objects.student2)
    #pro3 = Profile.objects.get(user=objects.student3) 
    template_name = 'alumni/prodetails.html'
    if request.method == 'POST':
        if pro in objects.mentor.all():
            objects.mentor.remove(pro)
            messages.success(request,f"You are no longer the mentor of this project")
        else:
            objects.mentor.add(pro)
            messages.success(request,f"You have been assigned as the mentor for this project!")
        objects.save()
        
    context = {'objects':objects,'pro':pro}
    return render(request,template_name,context)


class update_view(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Projects
    fields = ['title','description','tech_stack','working_ss']
    success_message = "The project has been updated successfully!"
    def form_valid(self, form):
        #form.instance.author = self.request.user
        #messages.success(self.request,f'The project has been updated successfully!')
        return super().form_valid(form) 
        
   
    def test_func(self):
        post = self.get_object()
        print(post.student1)
        #path = obj.get_absolute_url()
        if self.request.user == post.student1 or self.request.user == post.student2 or self.request.user == post.student3:
            return True
        return False

    success_url = "/prolist"


class DeleteView(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model = Projects 
    success_url = "/prolist"
    success_message = "Project has been deleted!"


#def delete_view()


'''def update_view(request,project_id):
    template_name = 'alumni/proupdate.html'
    obj = Projects.objects.get(id=project_id)
    form = ProjectUpdateForm(request.POST,request.FILES,instance=obj)
    if form.is_valid():
        form.save() 
        messages.success(request,f'The Project details has been updated!')
    context = {'form':form} 
    return render(request,template_name,context)'''

@login_required
def mentor_view(request,project_id,*args,**kwargs):
    objects = Projects.objects.get(id=project_id)
    template_name = "alumni/mentor.html"
    context = {'objects':objects}

    return render(request,template_name,context)

def author_view(request,project_id,*args,**kwargs):
    objects = Projects.objects.get(id=project_id)
    template_name = "alumni/author.html"
    context = {'objects':objects}

    return render(request,template_name,context)


def Register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'alumni/register.html', {'form': form})   



@login_required
def profile(request,*args,**kwargs):
    pro = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        pro.username = str(request.user.username)
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            #u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        pro.save()

    else:
        pro.username = str(request.user) 
        pro.save()
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'pro':pro,
        'p_form': p_form
    }
    return render(request, 'alumni/profile.html', context)

