from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('', views.login, name='login'),
    path('overview/', views.overview, name='overview'),
    path('record-visitor/', views.record_visitor, name='record_visitor'),
    path('check-out-visitor/<int:visitor_id>/', views.check_out_visitor, name='check_out_visitor'),
    path('visitor-list/', views.visitor_list, name='visitors'),
    path('visitor-list/details/<int:visitor_id>/', views.details, name='details'),
    path('approve/<int:visitor_id>/', views.approve_visitor, name='approve_visitor'),
    path('movements/', views.movements, name='movements'),
    path('search/', views.search_visitors, name='search_visitors'),
    path('logout/', views.logout_view, name='logout'),
    path('checkout-visitor/', views.checkout_visitor, name='checkout_visitor'),  # New URL pattern for card reader checkout
    path('card-reader-interaction/', views.card_reader_interaction, name='card_reader_interaction'),  # New URL pattern for card reader interaction
]
