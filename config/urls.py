"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from question_box import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/add/', views.question_add, name='question-add'),
    path('accounts/',include('registration.backends.default.urls')),
    path('', views.question_list, name = 'question-list'),
    path('question/<int:pk>/', views.question_details, name='question-details'),
    path('question/<int:pk>/delete/', views.question_delete, name='question-delete'),
    path('question/<int:question_pk>/favorite/', views.favorite, name='question-favorites'),
    path('question/<slug:slug>/', views.tagged, name= 'question-by-category'),

    # path('answer/', views.answer_add, name='answer-add')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
