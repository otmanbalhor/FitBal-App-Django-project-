from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('add-customer',views.AddCustomerView.as_view(), name='add-customer'),
    path('add-coach',views.AddCoachView.as_view(), name='add-coach'),
    path('add-invoice',views.AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/<int:pk>',views.InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf/<int:pk>',views.get_invoice_pdf, name="invoice-pdf"),
    path('signup',views.signUp, name='signup'),
    path('login',views.login, name='login'),
    path('userpage',views.userpage, name='userpage')
]
