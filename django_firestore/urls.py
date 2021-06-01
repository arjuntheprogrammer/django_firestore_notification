from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django_firestore.connector import send_message, make_as_read

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('ajax/send-message/', send_message, name='send_message'),
    path('ajax/make-as-read/', make_as_read, name='make_as_read')
]
