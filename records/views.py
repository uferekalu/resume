from django.shortcuts import render, redirect, get_object_or_404
from .models import Details, Profile
from .forms import *
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            messages.success(request, "Account has been created for " + username)
            return redirect('records:login')
    context = {
        'form': form
    }
    return render(request, 'records/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('records:details')
        else:
            message.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'records/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('records:login')

@login_required(login_url='account_login')
def home(request):
    details = Details.objects.all().order_by('-id')
    total_details = details.count()
    mech = details.filter(dept='ME').count()
    elect = details.filter(dept='EE').count()
    civil = details.filter(dept='CE').count()
    agric = details.filter(dept='AE').count()
    chem = details.filter(dept='CHE').count()
    comp_sci = details.filter(dept='CS').count()
    comp_engr = details.filter(dept='CTE').count()
    sci_lab = details.filter(dept='SLT').count()
    food_sci = details.filter(dept='FST').count()
    pharm_tech = details.filter(dept='PT').count()
    dispensary = details.filter(dept='DOP').count()
    total = Details.objects.aggregate(Sum('total'))['total__sum']
    
    paginator = Paginator(details, 10)

    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'mech': mech,
        'elect': elect,
        'civil': civil,
        'agric': agric,
        'chem': chem,
        'comp_sci': comp_sci,
        'comp_engr': comp_engr,
        'sci_lab': sci_lab,
        'food_sci': food_sci,
        'pharm_tech': pharm_tech,
        'dispensary': dispensary,
        'total': total,
        'page_obj': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'records/index.html', context)

@login_required(login_url='account_login')
def courses(request):
    courses_registered = CoursesRegistered.objects.all().order_by('id')
    
    paginator = Paginator(courses_registered, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'page_obj': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'records/courses.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def addDetails(request):
    form = AddForm
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:details')
    
    context = {
        'form': form
    }
    return render(request, 'records/add_detail.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def addCourses(request):
    form = AddCourses
    if request.method == 'POST':
        form = AddCourses(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records:courses')
    
    context = {
        'form': form
    }
    return render(request, 'records/add_courses.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def deleteDetail(request, pk):
    detail = Details.objects.get(id=pk)
    if request.method == 'POST':
        detail.delete()
        return redirect('records:details')
    context = {
        'item': detail
    }
    return render(request, 'records/delete.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def deleteCourse(request, pk):
    course = CoursesRegistered.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('records:courses')
    context = {
        'course': course
    }
    return render(request, 'records/delete_course.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def updateDetail(request, pk):
    detail = Details.objects.get(id=pk)
    form = UpdateForm(instance=detail)
    
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('records:details')
    context = {
        'form': form
    }
    return render(request, 'records/update.html', context)

@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admin'])
def updateCourse(request, pk):
    course = CoursesRegistered.objects.get(id=pk)
    form = UpdateCourse(instance=course)
    
    if request.method == 'POST':
        form = UpdateCourse(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('records:courses')
    context = {
        'form': form
    }
    return render(request, 'records/update_course.html', context)

def unauthorized(request):
    context = {}
    return render(request, 'records/unauthorized.html', context)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(name__icontains=query) | Q(phone__icontains=query) | Q(payment__icontains=query) | Q(balance__icontains=query) | Q(total__icontains=query) | Q(dept__icontains=query)
            details = Details.objects.filter(lookups)
            context = {
                'details': details
            }
            return render(request, 'records/search.html', context)
        else:
            return render(request, 'records/search.html')
    else:
        return render(request, 'records/index.html')

def profile(request, pk):
    detail = Details.objects.get(id=pk)
    context = {
        'detail': detail
    }
    return render(request, 'records/dashboard.html', context)

