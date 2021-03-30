""" User urls """
# Django
from django.urls import path

# View
from users import views

urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'),

    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),

    path(
        route='signup/',
        view=views.SignUpView.as_view(),
        name='signup'),

    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'),

    # Posts

    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]
