
from django.contrib import admin
from django.urls import path
from Grade_manager import views
from Grade_manager.views import Class_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.insert),
    path('', views.show,name = "show"),
    path('delete/<id>', views.delete,name = "delete"),
    path('update/<id>', views.update,name = "update"),
    path('class_view/<id>', Class_view.as_view(),name = "class_view"),
]
