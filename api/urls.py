from django.urls import path,include
from api.views import CarDetailAPIView,AllCarDetailView


urlpatterns =[
    path('cars/',CarDetailAPIView.as_view()),
    path('detail/<int:id>',AllCarDetailView.as_view()),
]