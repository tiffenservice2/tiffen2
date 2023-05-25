from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('home/',views.homeview),
    path('blogdetail/<int:id>',views.blogdetailview),
    path('reg/',views.regview),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('breakfast/',views.breakfast.as_view()),
    path('contact/',views.contactview.as_view()),
    path('about/',views.aboutusview.as_view()),
    path('insertcontect/',views.insertcontect),

    path('blog/',views.blogsview),
    path('services/',views.servicesview),
    path('serviceitem/<int:id>', views.serviceitemview),
    path('cusion/',views.cusionsview),
    path('typecusion/<int:id>',views.typecusionsview),
    path('serviceitemdetail/<int:id>', views.serviceitemdetailview),

     
]
