from django.urls import path,include
from api.views import (CarDetailAPIView,AllCarDetailView,
            ProductDetailView,CompanyProductView,CarTypeView
            ,PriceView,TransmissionTypeView,FilterView)


urlpatterns =[
    path('cars/',CarDetailAPIView.as_view()),
    path('detail/<int:id>',AllCarDetailView.as_view()),
    path('product/<str:name>',ProductDetailView.as_view()),
    path('company/<str:company>',CompanyProductView.as_view()),
    path('category/<str:type>',CarTypeView.as_view()),
    path('transmission/<str:type>',TransmissionTypeView.as_view()),
    path('filter/<str:type>/<str:category>/<str:company>/<int:price>/<str:fuel>',FilterView.as_view()),
    path('filter-price/<int:price>',PriceView.as_view()),
]