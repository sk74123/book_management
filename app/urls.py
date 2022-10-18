from django.urls import path
from app.views import authorAPI, bookAPI, borrowAPI, borrowbookAPI

urlpatterns = [
    path('author', authorAPI.as_view()),
    path('book', bookAPI.as_view()),
    path('borrow', borrowAPI.as_view()),
    path('borrowbook', borrowbookAPI.as_view())

]

