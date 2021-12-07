from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import *
import random
from django.db.models import Q
import math


# Create your views here.
# home page
def index(request):
    tech = Category.objects.filter(subtype='tech')
    company = Category.objects.filter(subtype='company')
    aptitude = Category.objects.filter(subtype='aptitude')
    other = Category.objects.filter(subtype='other')
    context = {'tech': tech, 'company': company, 'aptitude': aptitude, 'other': other}
    return render(request, 'webapp/index.html', context)


# user registration
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        email = request.POST.get('email', False)
        username = request.POST.get('username', False)
        password1 = request.POST.get('password', False)
        password2 = request.POST.get('password2', False)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists..!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already taken!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username, password=password1)
                user.save()
                messages.info(request, "User created successfully!")
                return redirect('login')
        else:
            messages.info(request, "Password does not match!")
            return redirect('register')
    else:
        return render(request, 'webapp/register.html')


# user login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if Candidate.objects.filter(user_id=user).exists():
                tech = Category.objects.filter(subtype='tech')
                company = Category.objects.filter(subtype='company')
                aptitude = Category.objects.filter(subtype='aptitude')
                other = Category.objects.filter(subtype='other')
                data = Candidate.objects.filter(user_id=request.user)
                context = {'tech': tech, 'company': company, 'aptitude': aptitude, 'other': other, 'data': data}
                return render(request,  'webapp/canhome.html', context)
            else:
                messages.info(request, 'Please create your profile!')
                return render(request, 'webapp/new_profile.html')
        else:
            messages.info(request, "Invalid credentials....")
            return redirect('login')

    else:
        return render(request, 'webapp/login.html')


# user logout
def logout(request):
    auth.logout(request)
    return redirect('/')


# create new profile
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            email = request.POST.get('email')
            contact1 = request.POST.get('contact1')
            contact2 = request.POST.get('contact2')
            address = request.POST.get('address')
            ssc_col = request.POST.get('ssc_col')
            ssc_uni = request.POST.get('ssc_uni')
            ssc_pass = request.POST.get('ssc_pass')
            ssc_per = request.POST.get('ssc_per')
            hsc_col = request.POST.get('hsc_col')
            hsc_uni = request.POST.get('hsc_uni')
            hsc_pass = request.POST.get('hsc_pass')
            hsc_per = request.POST.get('hsc_per')
            dip_col = request.POST.get('hsc_col')
            dip_spl = request.POST.get('dip_spl')
            dip_uni = request.POST.get('dip_uni')
            dip_pass = request.POST.get('dip_pass')
            dip_per = request.POST.get('dip_per')
            grad_col = request.POST.get('grad_col')
            grad_spl = request.POST.get('grad_spl')
            grad_uni = request.POST.get('grad_uni')
            grad_pass = request.POST.get('grad_pass')
            grad_per = request.POST.get('grad_per')
            pg_col = request.POST.get('pg_col')
            pg_spl = request.POST.get('pg_spl')
            pg_uni = request.POST.get('pg_uni')
            pg_pass = request.POST.get('pg_pass')
            pg_per = request.POST.get('pg_per')
            gradp_title = request.POST.get('gp_title')
            gradp_detail = request.POST.get('gp_detail')
            linkedin = request.POST.get('linkedin')
            tech_skills = request.POST.get('tech_skills')
            soft_skills = request.POST.get('soft_skills')
            cert1 = request.POST.get('cert1')
            cert2 = request.POST.get('cert2')
            cert3 = request.POST.get('cert3')
            exp1_title = request.POST.get('exp1_title')
            exp2_title = request.POST.get('exp2_title')

            candidate = Candidate.objects.create(user_id=request.user, Name=name, Gender=gender, DOB=dob, Email=email,
                                                 Contact1=contact1, Contact2=contact2, Address=address, SSC_col=ssc_col,
                                                 SSC_uni=ssc_uni, SSC_pass=ssc_pass, SSC_per=ssc_per, HSC_col=hsc_col,
                                                 HSC_uni=hsc_uni, HSC_pass=hsc_pass, HSC_per=hsc_per, Dip_col=dip_col,
                                                 Dip_spl=dip_spl, Dip_uni=dip_uni, Dip_pass=dip_pass, Dip_per=dip_per,
                                                 Grad_col=grad_col, Grad_spl=grad_spl, Grad_uni=grad_uni,
                                                 Grad_pass=grad_pass, Grad_per=grad_per, Grad_project_title=gradp_title,
                                                 Pg_col=pg_col, Pg_spl=pg_spl, Pg_uni=pg_uni, Pg_pass=pg_pass,
                                                 Pg_per=pg_per,
                                                 Grad_project_detail=gradp_detail, Linkedin=linkedin,
                                                 Tech_skills=tech_skills, Soft_skills=soft_skills, Certification1=cert1,
                                                 Certification2=cert2, Certification3=cert3,
                                                 Experience1_title=exp1_title, Experience2_title=exp2_title)
            candidate.save()
            tech = Category.objects.filter(subtype='tech')
            company = Category.objects.filter(subtype='company')
            aptitude = Category.objects.filter(subtype='aptitude')
            other = Category.objects.filter(subtype='other')
            data = Candidate.objects.filter(user_id=request.user)
            context = {'tech': tech, 'company': company, 'aptitude': aptitude, 'other': other, 'data': data}
            messages.info(request, 'Profile created successfully!')
            return render(request, 'webapp/canhome.html', context)
        else:
            return render(request, 'webapp/new_profile.html')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# user profile
def my_profile(request):
    if request.user.is_authenticated:
        data = Candidate.objects.filter(user_id=request.user)
        if len(data) == 0:
            messages.info(request, 'Please create your profile!')
            return render(request, 'webapp/new_profile.html')
        else:
            return render(request, 'webapp/profile.html', {'data': data})
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# edit profile
def edit_profile(request):
    var = request.GET.get('user')
    data = Candidate.objects.filter(candidate_id=var)
    return render(request, 'webapp/edit_profile.html', {'data': data})


# update profile
def update(request):
    if request.user.is_authenticated:
        candidate = Candidate.objects.get(user_id=request.user)
        if request.method == 'POST':
            name = request.POST.get('name')
            if len(request.POST.get('name')) == 0:
                name = candidate.Name
            gender = request.POST.get('gender')
            if len(request.POST.get('gender')) == 0:
                gender = candidate.Gender
            dob = request.POST.get('dob')
            if len(request.POST.get('dob')) == 0:
                dob = candidate.DOB
            email = request.POST.get('email')
            if len(request.POST.get('email')) == 0:
                email = candidate.Email
            contact1 = request.POST.get('contact1')
            if len(request.POST.get('contact1')) == 0:
                contact1 = candidate.Contact1
            contact2 = request.POST.get('contact2')
            if len(request.POST.get('contact2')) == 0:
                contact2 = candidate.Contact2
            address = request.POST.get('address')
            if len(request.POST.get('address')) == 0:
                address = candidate.Address
            ssc_col = request.POST.get('ssc_col')
            if len(request.POST.get('ssc_col')) == 0:
                ssc_col = candidate.SSC_col
            ssc_uni = request.POST.get('ssc_uni')
            if len(request.POST.get('ssc_uni')) == 0:
                ssc_uni = candidate.SSC_uni
            ssc_pass = request.POST.get('ssc_pass')
            if len(request.POST.get('ssc_pass')) == 0:
                ssc_pass = candidate.SSC_pass
            ssc_per = request.POST.get('ssc_per')
            if len(request.POST.get('ssc_per')) == 0:
                ssc_per = candidate.SSC_per
            hsc_col = request.POST.get('hsc_col')
            if len(request.POST.get('hsc_col')) == 0:
                hsc_col = candidate.HSC_col
            hsc_uni = request.POST.get('hsc_uni')
            if len(request.POST.get('hsc_uni')) == 0:
                hsc_uni = candidate.HSC_uni
            hsc_pass = request.POST.get('hsc_pass')
            if len(request.POST.get('hsc_pass')) == 0:
                hsc_pass = candidate.HSC_pass
            hsc_per = request.POST.get('hsc_per')
            if len(request.POST.get('hsc_per')) == 0:
                hsc_per = candidate.HSC_per
            dip_col = request.POST.get('hsc_col')
            if len(request.POST.get('hsc_col')) == 0:
                dip_col = candidate.Dip_col
            dip_spl = request.POST.get('dip_spl')
            if len(request.POST.get('dip_spl')) == 0:
                dip_spl = candidate.Dip_spl
            dip_uni = request.POST.get('dip_uni')
            if len(request.POST.get('dip_uni')) == 0:
                dip_uni = candidate.Dip_uni
            dip_pass = request.POST.get('dip_pass')
            if len(request.POST.get('dip_pass')) == 0:
                dip_pass = candidate.Dip_pass
            dip_per = request.POST.get('dip_per')
            if len(request.POST.get('dip_per')) == 0:
                dip_per = candidate.Dip_per
            grad_col = request.POST.get('grad_col')
            if len(request.POST.get('grad_col')) == 0:
                grad_col = candidate.Grad_col
            grad_spl = request.POST.get('grad_spl')
            if len(request.POST.get('grad_spl')) == 0:
                grad_spl = candidate.Grad_spl
            grad_uni = request.POST.get('grad_uni')
            if len(request.POST.get('grad_uni')) == 0:
                grad_uni = candidate.Grad_uni
            grad_pass = request.POST.get('grad_pass')
            if len(request.POST.get('grad_pass')) == 0:
                grad_pass = candidate.Grad_pass
            grad_per = request.POST.get('grad_per')
            if len(request.POST.get('grad_per')) == 0:
                grad_per = candidate.Grad_per
            pg_col = request.POST.get('pg_col')
            if len(request.POST.get('pg_col')) == 0:
                pg_col = candidate.Pg_col
            pg_spl = request.POST.get('pg_spl')
            if len(request.POST.get('pg_spl')) == 0:
                pg_spl = candidate.Pg_spl
            pg_uni = request.POST.get('pg_uni')
            if len(request.POST.get('pg_uni')) == 0:
                pg_uni = candidate.Pg_uni
            pg_pass = request.POST.get('pg_pass')
            if len(request.POST.get('pg_pass')) == 0:
                pg_pass = candidate.Pg_pass
            pg_per = request.POST.get('pg_per')
            if len(request.POST.get('pg_per')) == 0:
                pg_per = candidate.Pg_per
            gradp_title = request.POST.get('gp_title')
            if len(request.POST.get('gp_title')) == 0:
                gradp_title = candidate.Grad_project_title
            gradp_detail = request.POST.get('gp_detail')
            if len(request.POST.get('gp_detail')) == 0:
                gradp_detail = candidate.Grad_project_detail
            linkedin = request.POST.get('linkedin')
            if len(request.POST.get('linkedin')) == 0:
                linkedin = candidate.Linkedin
            tech_skills = request.POST.get('tech_skills')
            if len(request.POST.get('tech_skills')) == 0:
                tech_skills = candidate.Tech_skills
            soft_skills = request.POST.get('soft_skills')
            if len(request.POST.get('soft_skills')) == 0:
                soft_skills = candidate.Soft_skills
            cert1 = request.POST.get('cert1')
            if len(request.POST.get('cert1')) == 0:
                cert1 = candidate.Certification1
            cert2 = request.POST.get('cert2')
            if len(request.POST.get('cert2')) == 0:
                cert2 = candidate.Certification2
            cert3 = request.POST.get('cert3')
            if len(request.POST.get('cert3')) == 0:
                cert3 = candidate.Certification3
            exp1_title = request.POST.get('exp1_title')
            if len(request.POST.get('exp1_title')) == 0:
                exp1_title = candidate.Experience1_title
            exp2_title = request.POST.get('exp2_title')
            if len(request.POST.get('exp2_title')) == 0:
                exp2_title = candidate.Experience2_title

            candidate.Name = name
            candidate.Gender = gender
            candidate.DOB = dob
            candidate.Email = email
            candidate.Contact1 = contact1
            candidate.Contact2 = contact2
            candidate.Address = address
            candidate.SSC_col = ssc_col
            candidate.SSC_uni = ssc_uni
            candidate.SSC_pass = ssc_pass
            candidate.SSC_per = ssc_per
            candidate.HSC_col = hsc_col
            candidate.HSC_uni = hsc_uni
            candidate.HSC_pass = hsc_pass
            candidate.HSC_per = hsc_per
            candidate.Dip_col = dip_col
            candidate.Dip_spl = dip_spl
            candidate.Dip_uni = dip_uni
            candidate.Dip_pass = dip_pass
            candidate.Dip_per = dip_per
            candidate.Grad_col = grad_col
            candidate.Grad_spl = grad_spl
            candidate.Grad_uni = grad_uni
            candidate.Grad_pass = grad_pass
            candidate.Grad_per = grad_per
            candidate.Pg_col = pg_col
            candidate.Pg_spl = pg_spl
            candidate.Pg_uni = pg_uni
            candidate.Pg_pass = pg_pass
            candidate.Pg_per = pg_per
            candidate.Grad_project_title = gradp_title
            candidate.Grad_project_detail = gradp_detail
            candidate.Linkedin = linkedin
            candidate.Tech_skills = tech_skills
            candidate.Soft_skills = soft_skills
            candidate.Certification1 = cert1
            candidate.Certification2 = cert2
            candidate.Certification3 = cert3
            candidate.Experience1_title = exp1_title
            candidate.Experience2_title = exp2_title

            candidate.save()

            tech = Category.objects.filter(subtype='tech')
            company = Category.objects.filter(subtype='company')
            aptitude = Category.objects.filter(subtype='aptitude')
            other = Category.objects.filter(subtype='other')
            data = Candidate.objects.filter(user_id=request.user)
            context = {'tech': tech, 'company': company, 'aptitude': aptitude, 'other': other, 'data': data}
            messages.info(request, 'Profile updated successfully!')
            return render(request, 'webapp/canhome.html', context)

    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# user home
def home(request):
    if request.user.is_authenticated:
        tech = Category.objects.filter(subtype='tech')
        company = Category.objects.filter(subtype='company')
        aptitude = Category.objects.filter(subtype='aptitude')
        other = Category.objects.filter(subtype='other')
        data = Candidate.objects.filter(user_id=request.user)
        context = {'tech': tech, 'company': company, 'aptitude': aptitude, 'other': other, 'data': data}
        return render(request, 'webapp/canhome.html', context)
    else:
        return redirect('/')


# python test
def python(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Python.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Python', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Python')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Python.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/python.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/python.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Machine learning test
def machine(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Machine.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Machine Learning', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Machine Learning')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Machine.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/machine.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/machine.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Data science test
def data_science(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Dscience.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Data Science', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Data Science')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Dscience.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/dscience.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/dscience.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# PHP test
def php(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Php.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Php', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Php')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Php.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/php.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/php.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Aws test
def aws(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Aws.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Aws', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Aws')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Aws.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/aws.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/aws.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Data structure test
def data_str(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Dstructure.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Data Structure', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Data Structure')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Dstructure.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/dstructure.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/dstructure.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Java test
def java(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Java.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Java', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Java')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Java.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/java.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/java.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Angular test
def angular(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Angular.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Angular', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Angular')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Angular.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/angular.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/angular.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Full stack test
def full_stack(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Fullstack.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Fullstack', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Fullstack')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Fullstack.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/fullstack.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/fullstack.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Front end test
def front_end(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Front.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Front End', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Front End')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Front.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/front.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/front.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Tcs test
def tcs(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Tcs.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Tcs', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Tcs')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Tcs.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/tcs.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/tcs.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# capgemini test
def capgemini(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Capgemini.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Capgemini', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Capgemini')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Capgemini.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/capgemini.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/capgemini.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Accenture test
def accenture(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Accenture.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Accenture', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Accenture')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Accenture.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/accenture.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/accenture.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Infosys test
def infosys(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Infosys.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Infosys', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Infosys')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Infosys.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/infosys.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/infosys.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# Tech mahindra test
def mahindra(request):
    if request.user.is_authenticated:
        can = Candidate.objects.filter(user_id=request.user)
        if len(can) != 0:
            if request.method == 'POST':
                questions = Mahindra.objects.filter(question__in=Test.objects.filter(user=request.user).values('question'))

                total_correct = correct(request, questions)
                total_attempt = attempt(request, questions)
                if total_attempt == 0:
                    accuracy = 0
                else:
                    accuracy = (total_correct/total_attempt)*100
                scores = Result.objects.create(user_id=request.user, tech='Mahindra', score=total_correct,
                                               attempt=total_attempt, accuracy=accuracy)
                scores.save()
                result = Result.objects.filter(user_id=request.user).order_by('-time')[:1]

                freq = len(Result.objects.filter(Q(user_id=request.user) & Q(tech='Mahindra')))

                return render(request, 'webapp/canhome.html', {'result': result, 'data': can, 'freq': freq})
            else:
                pquestions = list(Mahindra.objects.all())
                questions = random.sample(pquestions, 10)
                user1 = Test.objects.filter(user=request.user)
                if len(user1) == 0:
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/mahindra.html', {'questions': questions})
                else:
                    Test.objects.filter(user=request.user).delete()
                    for que in questions:
                        var = Test.objects.create(question=que.question, user=request.user)
                        var.save()
                    return render(request, 'webapp/mahindra.html', {'questions': questions})
        else:
            messages.info(request, 'Please login or create your profile!')
            return redirect('/')
    else:
        messages.info(request, 'Login required!')
        return redirect('/')


# to calculate score
def correct(request, questions):
    total_correct = 0
    for i in questions:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_correct += 1
    return total_correct


# to calculate ques attempted
def attempt(request, questions):
    total_attempt = 0
    for i in questions:
        user_answer = request.POST.get(str(i.answer))
        if user_answer is not None:
            total_attempt += 1
    return total_attempt
