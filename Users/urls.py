from django.urls import path
from . import views as v

urlpatterns = [

    path('login/', v.user_login, name='Login'),
    #path('logout/', v.logout_view, name='Logout View'),
    path('signup/', v.signup, name='Signup'),
    path('logout/', v.user_logout, name='Logout'),
    path('profile/', v.user_dashboard, name='User Dashboard'),
    path('profile/edit/', v.edit_profile, name='Edit Profile'),
    path('user/<str:uname>/', v.DynamicUserView, name='Author'),
    path('feedback/', v.feedback, name='Feedback'),

]
