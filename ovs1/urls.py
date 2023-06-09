from django.contrib import admin
from django.urls import path,include
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nacos/', admin.site.urls, name='nater'),
    path('', include('contact.urls')),
    path('register/', views.registrationView, name='registration'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('logout/', views.logoutView, name='logout'),
    path('position/', views.positionView, name='position'),
    path('position/vote', views.vote, name='vote'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
    path('list/', views.resultView1, name='result1'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editProfileView, name='editprofile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Online Voting System"
admin.site.index_title = "Welcome to online voting system admin panel"
admin.site.site_title = "OVS"


