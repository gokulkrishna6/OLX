from django.contrib import admin
from django.urls import path
from . import views
 

from django.urls import path
from .views import select_location
urlpatterns = [



    
    path('',views.home,name='home'),
    path('ProductsPage/<int:did>',views.ProductsPage,name='ProductsPage'),
    path('poroductsub/<int:did>',views.poroductsub,name='poroductsub'),

   

    path('registration',views.registration,name='registration'),
    path('userLogin',views.userLogin,name='userLogin'),


 
    
    path('OrderData/<int:did>',views.OrderData,name='OrderData'),
    path('add_review/<int:did>',views.add_review,name='add_review'),
 

    path('Chat',views.Chat,name='Chat'),
    path('AdminHome',views.AdminHome,name='adminhome'),
 
    path('login',views.login,name='login'),
    path('AddCategory',views.AddCategory,name='AddCategory'),
    path('AddSubCategory',views.AddSubCategory,name='AddSubCategory'),
    path('addCategoryFunction',views.addCategoryFunction,name='addCategoryFunction'),
    path('addSubCategoryFunction',views.addSubCategoryFunction,name='addSubCategoryFunction'),
    path('addProductFunction',views.addProductFunction,name='addProductFunction'),

    path('editproductpage/<int:did>',views.editproductpage,name='editproductpage'),

    
    path('showRegData',views.showRegData,name='showRegData'),

    path('userHome',views.userHome,name='userHome'),

    path('UserProfile/<int:did>',views.UserProfile,name='UserProfile'),
    
    path('logout',views.logout,name='logout'),
    
    
    path('edit_products/<int:did>',views.edit_products,name="edit_products"),
    # path('edit_customerdetails/<int:did>',views.edit_customerdetails,name="edit_customerdetails"),

    
    path('payment_details/<int:did>',views.payment_details,name='payment_details'),

    path('billing_data/<int:did>',views.billing_data,name='billing_data'),

    path('checkout/<int:did>',views.checkout,name='checkout'),

    path('checkoutcard/<int:did>',views.checkoutcard,name='checkoutcard'),

    path('cart/<int:did>',views.cart,name='cart'),

    path('SellerRegFunction',views.SellerRegFunction,name='SellerRegFunction'),
    path('SellRegPage',views.SellRegPage,name='SellRegPage'),

    path('addProductPage',views.addProductPage,name='addProductPage'),

    path('SellerLoginPage',views.SellerLoginPage,name='SellerLoginPage'),
    path('SellerLogin',views.SellerLogin,name='SellerLogin'),

    path('sellerHome',views.sellerHome,name='sellerHome'),
    path('sellerProfile/<int:did>',views.sellerProfile,name='sellerProfile'),

    path('ProductDetail/<int:did>',views.ProductDetail,name='ProductDetail'),

    path('showBuyerData',views.showBuyerData,name='showBuyerData'),
    path('showSellerData',views.showSellerData,name='showSellerData'),
    path('showPaymentData',views.showPaymentData,name='showPaymentData'),
    path('UserData/<int:bid>',views.UserData,name='UserData'),
    path('ProductData',views.ProductData,name='ProductData'),

    path('EditForAdminBuyer/<int:bid>',views.EditForAdminBuyer,name='EditForAdminBuyer'),

    path('EditForAdminFuctionBuyer/<int:bid>',views.EditForAdminFuctionBuyer,name='EditForAdminFuctionBuyer'),
    path('edit_BuyerData/<int:eid>',views.edit_BuyerData,name='edit_BuyerData'),
 
    path('sellerForAdmin/<int:did>',views.sellerForAdmin,name='sellerForAdmin'),
    path('SellerView/<int:bid>',views.SellerView,name='SellerView'),

    path('buyerForAdmin/<int:bid>',views.buyerForAdmin,name='buyerForAdmin'),

    path('BuyerView/<int:bid>',views.BuyerView,name='BuyerView'),
    

    path('EditProfile/<int:eid>',views.EditProfile,name='EditProfile'),

    path('EditForAdminSeller/<int:bid>',views.EditForAdminSeller,name='EditForAdminSeller'),
  

    path('EditForAdminFuctionSeller/<int:bid>',views.EditForAdminFuctionSeller,name='EditForAdminFuctionSeller'),
    
    path('EditSellerProfile/<int:eid>',views.EditSellerProfile,name='EditSellerProfile'),

   
    path('edit_SellerData/<int:eid>',views.edit_SellerData,name='edit_SellerData'),

    path('OppositeProfile/<int:user_id>',views.OppositeProfile,name='OppositeProfile'),
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),

    path('remove_cart/<int:did>',views.remove_cart,name='remove_cart'),
 

    # path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),

    path('subcatselect',views.subcatselect,name='subcatselect'),
    path('approve',views.approve,name='approve'),

    path('feedback',views.feedback,name='feedback'),
    path('paymentdata',views.paymentdata,name='paymentdata'),

    path('paymentshow/<int:did>',views.paymentshow,name='paymentshow'),
    
    path('passwordchange',views.passwordchange,name='passwordchange'),
    
   

    path('booked',views.booked,name='booked.html'),

 
    
    path('delete_product/<int:did>/', views.delete_product, name='delete_product'),

    path('delete/<int:did>/', views.delete, name='delete'),
 
    path('addcart/<int:did>/', views.addcart, name='addcart'),
    
     

    path('select-location/', select_location, name='select_location'),
    



    path('changepasswordfunforseller',views.changepasswordfunforseller,name='changepasswordfunforseller'),
 
 
    path('test2',views.test2,name='test2'),

    path('approve_products',views.approve_products,name='approve_products'),


    path('search/results/', views.search_results, name='search_results'),
 
 
    path('approve_product/<int:product_id>/', views.approve_product, name='approve_product'),

    path('sellerapprove', views.sellerapprove, name='sellerapprove'),

    path('showorderdata', views.showorderdata, name='showorderdata'),

    path('approve_seller/<int:did>/', views.approve_seller, name='approve_seller'),

    path('soldout/<int:did>/', views.soldout, name='soldout'),

    path('changepasswordfun', views.changepasswordfun, name='changepasswordfun'),

    path('passwordchangepage', views.passwordchangepage, name='passwordchangepage'),
 
] 

 



  



