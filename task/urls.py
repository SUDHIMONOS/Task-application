from django.urls import path
from task import views

urlpatterns=[
    path("task/add",views.TaskCreateView.as_view(),name="task-create"),
    path("task/all",views.TaskListView.as_view(),name="task-list"),
    path("task/<int:pk>",views.TaskDetailView.as_view(),name="task-detail"),
    path("task/<int:pk>/remove",views.TaskDeleteView.as_view(),name="task-delete"),
    path("",views.IndexView.as_view(),name="home"),
    path("register",views.SignUpView.as_view(),name="sign-up"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("logout",views.sign_out,name="signout")



]