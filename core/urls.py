from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

app_name="core"

urlpatterns = [
    path('', views.index, name='index'),
    path('financial-audit/audit-coordination/', views.audit_coordination, name='audit_coordination'),
    path('financial-audit/bookkeeping/', views.bookkeeping, name='bookkeeping'),
    path('financial-audit/external-audit/', views.external_audit, name='external_audit'),
    path('financial-audit/internal-audit/', views.internal_audit, name='internal_audit'),
    path('advisory/', views.advisory, name='advisory'),
    path('Taxation_services/', views.Taxation_services, name='Taxationservices'),
    path('contact/', views.contact, name='contact'),
    path('registration-licensing/ngo/', views.ngo_registration_licensing, name='ngo_registration_licensing'),
    path('registration-licensing/corporate/', views.corporate_registration_licensing, name='corporate_registration_licensing'),
    path("companyregistrationwithscep/", views.company_registration_withscep,name='company_registration_withscep')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)