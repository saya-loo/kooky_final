from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import recipe_detail, recipes, index, services, login_user, search, logout_user, myprofile, payment, set_theme, home



urlpatterns = [path('admin/', admin.site.urls),
               path('', index, name='home'),
               path('recipe/', recipes, name='recipes'),
               path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
               path('services/', services, name='services'),
               path('login/', login_user, name='login'),
               path('myprofile/', myprofile, name='myprofile'),
               path('myprofile/logout/', logout_user, name='logout'),
               path('search/', search, name='search'),
               path('payment/', payment, name='payment'),
               path('set-theme/', set_theme, name='set_theme'),
             

               ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
