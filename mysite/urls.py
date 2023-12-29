# from django.views.generic import RedirectView

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('polls/', include('polls.urls')),
#     path('admin/', admin.site.urls),
#     # path('/', admin.site.urls),
#     path('', RedirectView.as_view(url='C:\\Users\\rjr89\\Desktop\\teste__juninho\\Projeto-Django\polls\\templates\\polls\\home.html'), name='home'),
# ]



from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='/polls/templates/polls/home.html'), name='home'),
    path('', TemplateView.as_view(template_name='polls/home.html'), name='home'),
]
