"""scanX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views.register_APIView import RegisterView
from .views.login_APIView import LoginView
from .views.logout_APIView import LogoutView
from .views.upload_APIView import UploadView
from .views.get_users_APIView import GetUsersView
from .views.getUserEmail_APIView import GetUserEmailView
from .views.delete_user_APIView import DeleteUserView
from .views.update_user_APIView import UpdateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('file-upload/', UploadView.as_view(), name='file-upload'),
    path('get-users/', GetUsersView.as_view(), name='get-users'),
    path('get-user-email/', GetUserEmailView.as_view(), name='get-user-email'),
    path('delete-user/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
]
