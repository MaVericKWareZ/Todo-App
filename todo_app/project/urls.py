"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import include, path

import todo_app.accounts.urls
import todo_app.task.urls
import todo_app.todoapp.urls
from todo_app.authentication.views.login import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include(todo_app.todoapp.urls)),
    # path('api/', include(todo_app.api.urls)),
    path('api/', include(todo_app.accounts.urls)),
    path('api/', include(todo_app.task.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
