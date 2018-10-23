"""
Definition of urls for DjangoCrudApplication.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views as auth_views
from django.contrib import admin
admin.autodiscover()
from app.forms import authentication_forms
from app.views import main_views
from app.views import product_views
# Examples:
urlpatterns = [
    url(r'', include('app.urls.product_urls')),
    url(r'^$', main_views.home, name='home'),
    url(r'^contact$', main_views.contact, name='contact'),
    url(r'^about$', main_views.about, name='about'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="app/login.html",
                                                                authentication_form = authentication_forms.BootstrapAuthenticationForm,
                                                                extra_context = 
                                                                {
                                                                    'title': 'Log in',
                                                                    'year': datetime.now().year
                                                                 }),name='login'),

    url(r'^logout$',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),

   
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls)
]
