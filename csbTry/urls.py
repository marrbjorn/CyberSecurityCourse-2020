from django.contrib import admin
from django.urls import path
from .views import hiddenPageView, formPageView, donePageView, fylkrPageView, previewPageView, csrfinerPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hidden/', hiddenPageView, name='hidden'),
    path('form/', formPageView, name='form'),
    path('done/', donePageView, name='done'),
    path('fylkr/', fylkrPageView, name='fylkr'),
    path('preview/', previewPageView, name='preview'),
    path('CSRFiner/', csrfinerPageView, name='csrfiner')
]
