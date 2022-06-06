from django.urls import path
from . import views


app_name='articles'
urlpatterns = [
    path('', views.article_list_or_create), # 전체 아티클을 응답하거나, 새로운 데이터를 만드는 요청
    path('<int:article_pk>', views.article_detail_or_update_or_delete), # 특정 아티클을 조작하는 요청
    path('<int:article_pk>/like/', views.like_article), # 좋아요 누르는 요청
    path('<int:article_pk>/comments/', views.create_comment), # 댓글을 작성하는 요청
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete), # 댓글을 수정하는 요청
    path('search/', views.search), # request에 정보를 담아서 검색하는 요청
    path('news/', views.news_list_or_create), # news 전체를 불러오거나, 새로운 뉴스를 만드는 요청

]