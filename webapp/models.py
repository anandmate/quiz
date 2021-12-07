from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def gen_candidate_id():
    last_candidate = Candidate.objects.all().order_by('candidate_id').last()
    if not last_candidate:
        return '00101'
    candidate_id = last_candidate.candidate_id
    custom_int = int(candidate_id[:7])
    new_custom_int = custom_int+1
    new_candidate_id = str(new_custom_int).zfill(6)
    return new_candidate_id


class Candidate(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_id = models.IntegerField(default=gen_candidate_id, editable=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    DOB = models.DateField()
    Email = models.EmailField()
    Contact1 = models.BigIntegerField()
    Contact2 = models.BigIntegerField(null=True, blank=True)
    Address = models.CharField(max_length=300)
    SSC_col = models.CharField(max_length=100, null=True, blank=True)
    SSC_uni = models.CharField(max_length=100, null=True, blank=True)
    SSC_pass = models.CharField(max_length=10, null=True, blank=True)
    SSC_per = models.FloatField(null=True, blank=True)
    HSC_col = models.CharField(max_length=100, null=True, blank=True)
    HSC_uni = models.CharField(max_length=100, null=True, blank=True)
    HSC_pass = models.CharField(max_length=10, null=True, blank=True)
    HSC_per = models.FloatField(null=True, blank=True)
    Dip_col = models.CharField(max_length=100, null=True, blank=True)
    Dip_spl = models.CharField(max_length=100, null=True, blank=True)
    Dip_uni = models.CharField(max_length=100, null=True, blank=True)
    Dip_pass = models.CharField(max_length=10, null=True, blank=True)
    Dip_per = models.FloatField(null=True, blank=True)
    Grad_col = models.CharField(max_length=100, null=True, blank=True)
    Grad_spl = models.CharField(max_length=100, null=True, blank=True)
    Grad_uni = models.CharField(max_length=100, null=True, blank=True)
    Grad_pass = models.CharField(max_length=10, null=True, blank=True)
    Grad_per = models.FloatField(null=True, blank=True)
    Pg_col = models.CharField(max_length=100, null=True, blank=True)
    Pg_spl = models.CharField(max_length=100, null=True, blank=True)
    Pg_uni = models.CharField(max_length=100, null=True, blank=True)
    Pg_pass = models.CharField(max_length=10, null=True, blank=True)
    Pg_per = models.FloatField(null=True, blank=True)
    Grad_project_title = models.CharField(max_length=100, null=True, blank=True)
    Grad_project_detail = models.CharField(max_length=500, null=True, blank=True)
    Linkedin = models.CharField(max_length=100, null=True, blank=True)
    Tech_skills = models.CharField(max_length=500, null=True, blank=True)
    Soft_skills = models.CharField(max_length=500, null=True, blank=True)
    Certification1 = models.CharField(max_length=100, null=True, blank=True)
    Certification2 = models.CharField(max_length=100, null=True, blank=True)
    Certification3 = models.CharField(max_length=100, null=True, blank=True)
    Experience1_title = models.CharField(max_length=100, null=True, blank=True)
    Experience2_title = models.CharField(max_length=100, null=True, blank=True)


class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tech = models.CharField(max_length=30)
    score = models.IntegerField()
    attempt = models.IntegerField()
    accuracy = models.FloatField(null=True)
    time = models.DateTimeField(auto_now=True)


class Python(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Machine(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Dscience(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Aws(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Front(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Fullstack(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Dstructure(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Java(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Angular(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Php(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Tcs(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Accenture(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Capgemini(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Mahindra(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Infosys(models.Model):
    question = models.CharField(max_length=500, unique=True)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explain = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Test(models.Model):
    question = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class Category(models.Model):
    subtype_choices = [
        ('tech', 'tech'),
        ('company', 'company'),
        ('aptitude', 'aptitude'),
        ('other', 'other')
    ]
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='webapp/logo')
    subtype = models.CharField(max_length=50, choices=subtype_choices)