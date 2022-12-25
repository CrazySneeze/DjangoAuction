from django.urls import path
from . import views
from .views import user_api, listings_api

urlpatterns = [
    path('api/listings/<str:searchData>', listings_api, name="listings api"),
    path('api/user', user_api),
    path('api/getUsersQuestions/<int:user_id>/', views.getUserQuestions, name='questions'),
    path('api/getQuestion/<int:itemId>', views.getQuestion, name='view question'),
    path('api/postAnswer/<int:question_id>', views.postAnswer, name='submit answer'),
    path('api/postQuestion/<int:item_id>', views.postQuestion, name='submit question'),
    path('api/postItem', views.postItem, name='make listing'),
    path('api/getItem/<int:item_id>', views.getItem, name='view listing'),
    path('api/getQuestionsAskedToUser/<int:user_id>', views.getQuestionsAskedToUser, name='get questions on your items'),
    path('api/placeBid/<int:item_id>', views.placeBid, name='Place Bid'),
    path('health', views.health, name="health"),
]