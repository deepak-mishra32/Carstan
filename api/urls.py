from django.urls import path,include
from api.views import CarDetailAPIView,AllCarDetailView,ProductDetailView


urlpatterns =[
    path('cars/',CarDetailAPIView.as_view()),
    path('detail/<int:id>',AllCarDetailView.as_view()),
    path('product/<str:name>',ProductDetailView.as_view()),
]