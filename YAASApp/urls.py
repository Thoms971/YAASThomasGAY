from django.urls import path

from . import views

app_name = 'YAASApp'
urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.EditUserView.as_view(), name='userdetail'),
    path('createauction/', views.createauction, name='createauction'),
    path('', views.AuctionIndex.as_view(), name='auctionindex'),
    path('detail/<int:pk>/', views.AuctionDetail.as_view(), name='auctiondetail'),
    path('auctionuser/', views.AuctionUser.as_view(), name='auctionuser'),
    path('editauction/<int:id>', views.EditUserAuction.as_view(), name='edit_user_auction'),
)
