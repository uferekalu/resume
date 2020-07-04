from django.urls import path
from . import views

app_name ='records'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('unauthorized/', views.unauthorized, name='restricted'),
    path('', views.home, name='details'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('add_details/', views.addDetails, name='add-details'),
    path('add_courses', views.addCourses, name='add-courses'),
    path('courses', views.courses, name='courses'),
    # path('<int:pk>/', views.detail, name='record-detail'),
    path('delete_detail/<int:pk>/', views.deleteDetail, name='delete-detail'),
    path('delete_course/<int:pk>/', views.deleteCourse, name='delete-course'),
    path('update_detail/<int:pk>/', views.updateDetail, name='update-detail'),
    path('update_course/<int:pk>/', views.updateCourse, name='update-course'),
    path('search/', views.search, name='search'),
]
