from.import views
from django.urls import path


urlpatterns = [
    path('', views.article_list),
]
