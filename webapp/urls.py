from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('my_profile', views.my_profile, name='my profile'),
    path('edit_profile', views.edit_profile, name='edit profile'),
    path('update', views.update, name='update'),
    path('home', views.home, name='home'),
    path('python', views.python, name='python'),
    path('machine_learning', views.machine, name='machine learning'),
    path('data_science', views.data_science, name='data science'),
    path('php', views.php, name='php'),
    path('aws', views.aws, name='aws'),
    path('data_structure', views.data_str, name='data structure'),
    path('java', views.java, name='java'),
    path('angular', views.angular, name='angular'),
    path('full_stack', views.full_stack, name='full stack'),
    path('front_end', views.front_end, name='front end'),
    path('tcs', views.tcs, name='tcs'),
    path('capgemini', views.capgemini, name='capgemini'),
    path('accenture', views.accenture, name='accenture'),
    path('tech_mahindra', views.mahindra, name='tech mahindra'),
    path('infosys', views.infosys, name='infosys'),
]