from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import *
from .models import UserLocation
from django.contrib.auth.decorators import login_required
from random import randrange
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.conf import settings 
from django.urls import reverse

def chat_with_user(request, user_id):
    
    user=SellerData.objects.get(user_id=request.user)
    user1=SellerData.objects.get(user=user_id)
    receiver = get_object_or_404(User, id=user_id)


    messages = ChatMessage.objects.filter(
        (models.Q(sender=request.user, receiver=receiver)) |
        (models.Q(sender=receiver, receiver=request.user))
    ).order_by('timestamp')

   

    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        if message_text.strip():
      
        
      
            ChatMessage.objects.create(sender=request.user, receiver=receiver, message=message_text 
             )
            
            return redirect('chat_with_user', user_id=user_id)
        
    user=SellerData.objects.filter(user_id=user_id)
   
    products = ProductModel.objects.prefetch_related('productimage_set').filter(seller_id=user1.id).filter(approved=True)

    popular_prd = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=4).filter(approved=True)

    return render(request, 'chat1.html', {'receiver': receiver, 'messages': messages,'user':user,'user1':user1,'products':products,'popular_prd':popular_prd})

def ProductsPage (request,did):
    products = ProductModel.objects.filter(Category_id=did).filter(approved=True)
    cate=SubCategoryModel.objects.filter(Category_id=did).all()
    images=ProductImage.objects.filter(id=did).all()
    return render (request,'ProductsPage.html',{'products':products,'cate':cate,'images':images})

def poroductsub (request,did):
    products = ProductModel.objects.filter(SubCategory_id=did).filter(approved=True)
    cate=SubCategoryModel.objects.filter(Category_id=did).all()
    images=ProductImage.objects.filter(id=did).all()
    return render (request,'productsub.html',{'products':products,'cate':cate,'images':images})

def OppositeProfile(request,user_id):
    user=SellerData.objects.filter(user_id=user_id)
    products = ProductModel.objects.prefetch_related('productimage_set').filter(seller_id=user_id).filter(approved=True)

    popular_prd = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=4).filter(approved=True)
    return render (request,'OppositeProfile.html',{'user':user,'products':products,'popular_prd':popular_prd})

def subcatselect(request):
    data=CategoryModel.objects.all()
    current_user=request.user
    userid=current_user.id
    users=SellerData.objects.get(id=userid)
    return render(request,"subcatselect.html",{'data':data,'users':users})

 

def addSubCategoryFunction(request):
    if request.method=='POST':

        SubCategory = request.POST['SubCategory']
        select=request.POST.get('select2')
        category=CategoryModel.objects.get(id=select)
        
        category=SubCategoryModel(SubCategory_Name=SubCategory,Category=category)
        category.save()
        messages.info(request,'Subcategory is successfully added')
        
    return redirect ('AddSubCategory')

def cart(request,did):
   
    ca=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    seller=SellerData.objects.get(user_id=uid)
  
    data=CartModel.objects.filter(Customer=seller)
    print(data)



    return render(request,"cart.html",{'data':data, 'ca':ca })


from django.shortcuts import get_object_or_404

def add_review(request, did):
    current_user = request.user
    uid = current_user.id
    billing = PaymentData.objects.get(id=did)
    seller = SellerData.objects.get(user=uid)
    print(billing)
    if request.method == 'POST':
        review = request.POST['review']
        star = request.POST['rating[]']


        product = billing.product 
        image = billing.image

        data = ReviewData(star=star, review=review, product=product, seller=seller, payment=billing, image=image)
        data.save()

    return redirect('OrderData', seller.id)
 
def ProductDetail(request, did):
    cate = SubCategoryModel.objects.filter(Category=did)
    data = ProductModel.objects.filter(id=did, approved=True)
    images = ProductImage.objects.filter(Product_id=did)

    current = request.user
    uid = current.id
    seller = SellerData.objects.get(user=uid)
    
    saved_location = UserLocation.objects.filter(Prod=did).first()
    review= ReviewData.objects.filter(product=did)
 

    vall = {
        'latitude': saved_location.latitude if saved_location else None,
        'longitude': saved_location.longitude if saved_location else None,
    }

    return render(request, 'ProductDetail.html', {'data': data, 'cate': cate, 'images': images, 'seller': seller, 'vall': vall,'review':review})



def userHome(request ):
    data=CategoryModel.objects.all()     
    current_user=request.user                         
    userid=current_user.id
    chat = ChatMessage.objects.filter(receiver_id=userid)
    users=SellerData.objects.get(user=userid)
    buyer=SellerData.objects.all()
    print(userid)
    products = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=4).filter(approved=True)
    fashions = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=5).filter(approved=True)
    cars = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=3).filter(approved=True)
    
    categories=CategoryModel.objects.all()
    subcategories =SubCategoryModel.objects.all()
    return render(request,"userHome.html",{'categories':categories,'subcategories':subcategories,'data':data,'users':users,'products':products,'fashions':fashions,'cars':cars,'chat':chat ,'buyer':buyer})





 
def home (request):
    products = ProductModel.objects.prefetch_related('productimage_set').all().filter(approved=True)
    return render (request,'home.html',{'products':products})


    
 
    
    
 




def registration (request):
    return render (request,'registration.html')

def SellRegPage (request):
    return render (request,'SellRegPage.html')

def userLogin (request):
    return render (request,'userLogin.html')

def SellerProfile (request):
   
    return render (request,'SellerProfile.html' )



def Chat (request):
    return render (request,'Chat.html')

def AdminHome (request):
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)



    # for product in products:
    #     id = product.user_id
    #     print(id)

    # seller= SellerData.objects.filter(user_id=id)
    
    return render (request,'AdminHome.html',{'products':products,'sellers':sellers })


def showorderdata(request):
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)
    products1 = ProductModel.objects.prefetch_related('productimage_set').filter(approved=True)

    data= PaymentData.objects.all()
    data1= SellerData.objects.all()
    
    
  
    
    return render (request,'showorderdata.html',{'data':data,'data1':data1,'products':products})

def AddCategory (request):
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)

    return render (request,'AddCategory.html',{'sellers':sellers,'products':products,})



def AddSubCategory (request):
    category=CategoryModel.objects.all()
 

    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)
    return render (request,'AddSubCategory.html',{'sellers':sellers,'products':products,'category':category})

def edit_BuyerData(request,eid):
    if request.method=='POST':
        customer=SellerData.objects.get(id=eid)
        old=customer.img
        new=request.FILES.get('img')
        if old!=None and new==None:
            customer.img=old
        else:
            customer.img=new
        customer.user.first_name=request.POST.get('first_name')
        customer.user.last_name=request.POST.get('last_name')
        customer.user.email=request.POST.get('email')
        customer.number=request.POST.get('number')
        customer.user.username=request.POST.get('username')
        customer.country=request.POST.get('country')
        customer.state=request.POST.get('state')
        customer.save()
        customer.user.save()
        return redirect('UserProfile', customer.id )    

def EditProfile(request,eid):
    current_user=request.user
    userid=current_user.id
    data=SellerData.objects.get(user_id=userid)
    return render(request,"EditProfile.html",{'data':data})

def UserProfile (request,did):
    data=SellerData.objects.get(user_id=did)
    products = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=4).filter(approved=True)
    return render (request,'UserProfile.html',{'data':data,'products':products})

def OrderData (request,did):
    user=SellerData.objects.get(id=did)
    current_user = request.user
    uid=current_user.id
    
    payment_history = PaymentData.objects.filter(user_id=uid)
    return render (request,'OrderData.html',{'user':user,'payment_history':payment_history})

def paymentshow (request,did):
    data=SellerData.objects.get(user=did)
    user = request.user

  
    payment_history = PaymentData.objects.filter(seller_id=data.id)
    return render (request,'paymentshow.html',{'data':data,'payment_history':payment_history})


 

def EditSellerProfile(request,eid):
    data=SellerData.objects.get(id=eid)
    return render(request,"EditSellerProfile.html",{'data':data})
 


            
def SellerRegFunction(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        number = request.POST['number']
        country = request.POST['country']
        state = request.POST['state']
        address=request.POST['address']
        img = request.FILES.get('img')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken')
            return redirect('SellRegPage')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('SellRegPage')
        else:
           
            password = str(randrange(100000, 1000000))

       
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

      
            seller = SellerData(number=number, img=img, country=country, state=state, user=user,address=address)
            seller.save()

            messages.info(request, 'Thank you for your submission! 🎉 Your request is now awaiting approval from our admin team. Once approved, you will receive a confirmation email with further instructions. We appreciate your patience and look forward to welcoming you soon! If you have any urgent queries, feel free to reach out to our support team. Happy exploring!         thank you TEAM ALTOS"')
            return redirect('SellerLoginPage')
            


 


def edit_SellerData(request,eid):
    if request.method=='POST':
        customer=SellerData.objects.get(id=eid)
        old=customer.img
        new=request.FILES.get('img')
        if old!=None and new==None:
            customer.img=old

        else:
            customer.img=new
        
        customer.user.first_name=request.POST.get('first_name')
        customer.user.last_name=request.POST.get('last_name')
        customer.user.email=request.POST.get('email')
        customer.number=request.POST.get('number')
        customer.user.username=request.POST.get('username')
        customer.country=request.POST.get('country')
        customer.state=request.POST.get('state')
        customer.save()
        customer.user.save()
        return redirect('sellerProfile', customer.user.id )


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            if request.user.is_staff==1:              
                return redirect('adminhome')
          
            else:
              return redirect('userHome')             
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('userLogin')
    else:
        return redirect('userLogin')


# seller details -----------------------------------------------------------------------------------------------------
def sellerHome(request):
    data=CategoryModel.objects.all()
    current_user=request.user
    userid=current_user.id
    users=SellerData.objects.get(user=userid)
    chat = ChatMessage.objects.filter(receiver_id=userid)
    products = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=4).filter(approved=True)
    fashions = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=5).filter(approved=True)
    cars = ProductModel.objects.prefetch_related('productimage_set').filter(Category_id=3).filter(approved=True)

    return render(request,"sellerHome.html",{'data':data,'users':users,'products':products,'fashions':fashions,'cars':cars,'chat':chat})

def SellerLoginPage(request):

    return render(request,"SellerLoginPage.html")

def SellerLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            if request.user.is_staff==1:              
                return redirect('adminhome')                
            else:
              return redirect('userHome')
     
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('SellerLoginPage')
    else:
      
        return redirect('SellerLoginPage')
    
def sellerProfile (request,did):
    data=SellerData.objects.get(user=did)
    products = ProductModel.objects.prefetch_related('productimage_set').filter(seller_id=data.id).all()

    products2 = ProductModel.objects.prefetch_related('productimage_set').filter(approved=True)
    return render (request,'sellerProfile.html',{'data':data ,'products':products,'products2':products2})


 

def addCategoryFunction(request):
    if request.method=='POST':
        MainCategory = request.POST['MainCategory']
        category=CategoryModel(Category_Name=MainCategory)
        category.save()
        messages.info(request,'Category is successfully added')
    return redirect ('AddCategory')



 




  
    


 

def addcart(request, did):
    data = ProductModel.objects.get(id=did)
    current_user = request.user
    uid = current_user.id
    user = SellerData.objects.get(user=uid)
 
    image = ProductImage.objects.filter(Product_id=did).first()
 

    cart = CartModel(Customer=user, Product=data, Image=image) 
    cart.save()
    messages.info(request,'Product addded to card')
    return redirect('ProductDetail', data.id)




# admin data-------------------------------------------------------------------------------------------------------

def showRegData(request):
    data=SellerData.objects.all()
    data={'data':data}
    return render (request,'showRegData.html',data)

def showBuyerData(request):
    data=BillingData.objects.all()
    data1= SellerData.objects.all()

    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)
    return render (request,'showBuyerData.html',{'sellers':sellers,'products':products,'data': data,'data1':data1})





def paymentdata(request):
    
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers2= SellerData.objects.filter(approved=False)
    sellers= SellerData.objects.all()
    data=PaymentData.objects.all()
    
    return render (request,'paymentdata.html',{'data':data,'sellers':sellers,'products':products,'sellers2':sellers2})

def showSellerData(request):
    data=SellerData.objects.filter(approved=True)
 

    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)
    return render (request,'showSellerData.html',{'sellers':sellers,'products':products,'data': data})

def showPaymentData(request):
    data=SellerData.objects.all()
    data={'data':data}
    return render (request,'showRegData.html',data)

def UserData(request,bid):
    data=SellerData.objects.get(id=bid)
    
    return render (request,'UserData.html',{'data':data})

def SellerView(request,bid):
    data=SellerData.objects.get(id=bid)
    return render (request,'SellerView.html',{'data':data})

def BuyerView(request,bid):
    data=SellerData.objects.get(id=bid)
    return render (request,'BuyerView.html',{'data':data})

 

def ProductData(request):
    products2 = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)
    products = ProductModel.objects.prefetch_related('productimage_set').all()
    return render (request,'ProductData.html',{ 'products':products ,'sellers':sellers,'products2':products2})





def EditForAdminBuyer(request,bid):
    data=SellerData.objects.get(id=bid)
    data={'data':data}
    return render (request,'EditForAdminBuyer.html',data)

def EditForAdminSeller(request,bid):
    data=SellerData.objects.get(id=bid)
    data={'data':data}
    return render (request,'EditForAdminSeller.html',data)



 

def EditForAdminFuctionSeller(request,bid):
    customer=SellerData.objects.get(id=bid)
    old=customer.img
    new=request.FILES.get('img')
    if old!=None and new==None:
        customer.img=old
    else:
        customer.img=new
    customer.user.first_name=request.POST.get('first_name')
    customer.user.last_name=request.POST.get('last_name')
    customer.user.email=request.POST.get('email')
    customer.number=request.POST.get('number')
    customer.user.username=request.POST.get('username')
    customer.country=request.POST.get('country')
    customer.state=request.POST.get('state')
    customer.save()
    customer.user.save()
    return redirect ('SellerView',customer.id  )

def EditForAdminFuctionBuyer(request,bid):
    customer=SellerData.objects.get(id=bid)
    old=customer.img
    new=request.FILES.get('img')
    if old!=None and new==None:
        customer.img=old
    else:
        customer.img=new
    customer.user.first_name=request.POST.get('first_name')
    customer.user.last_name=request.POST.get('last_name')
    customer.user.email=request.POST.get('email')
    customer.number=request.POST.get('number')
    customer.user.username=request.POST.get('username')
    customer.country=request.POST.get('country')
    customer.state=request.POST.get('state')
    customer.save()
    customer.user.save()
    return redirect ('BuyerView',customer.id  )
 
# ----------------------------------------------------------------------------------------------------------------




def logout(request):
	auth.logout(request)
	return redirect('home')





def checkout(request,did):
    data=CartModel.objects.filter(Customer=did)
    ca=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    user=SellerData.objects.get(user=uid)
    
    return render (request,'checkout.html',{'data':data,'user':user,'ca':ca })

def checkoutcard(request,did):
    data=CartModel.objects.filter(Customer=did)
    ca=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    user=SellerData.objects.get(user=uid)
    return render (request,'checkoutcard.html',{'data':data,'user':user,'ca':ca })




def remove_cart(request,did):
   
    cart=CartModel.objects.get(id=did)
    cart.delete()
    current_user=request.user
    uid=current_user.id
    user=SellerData.objects.get(user=uid)
    messages.info(request,'Product Removed Successfully!')
    return redirect('cart' ,user.id)

def approve(request):
    return render (request,'approve.html')



def sellerForAdmin(request,did):
    customer=SellerData.objects.get(id=did)
    customer.delete()
 
    return redirect('showSellerData')

def buyerForAdmin(request,did):
    customer=SellerData.objects.get(id=did)
    customer.delete()
 
    return redirect('showBuyerData')


 

def booked(request):
    return render (request,'booked.html')


def test2(request):
    return render (request,'test2.html')


# def buynow(request,did):
#     data=ProductModel.objects.get(id=did)
#     current_user=request.user
#     uid=current_user.id
#     print(uid)
#     user=BuyerData.objects.get(user=uid)

#     product=OrderModel(Category=data.Category,SubCategory=data.SubCategory,Customer=user,Product=data)
#     product.save()
#     print("shoping complited")
#     return redirect('success')

def addProductPage(request):
    current_user = request.user
    uid = current_user.id  
    user = SellerData.objects.get(user=current_user)
    categories = CategoryModel.objects.all()
    print(uid)

    return render(request, "addProductPage.html", {'categories': categories, 'user': user})

  

    

def editproductpage(request,did):
    product=ProductModel.objects.prefetch_related('productimage_set').get(id=did)
    
    categories = CategoryModel.objects.all()
    location= UserLocation.objects.get(Prod=did)
    return render(request,'editproduct.html',{'product':product,'categories': categories,'location':location}) 
 
from django.shortcuts import render, redirect
from .models import ProductModel, SubCategoryModel, ProductImage, UserLocation

def edit_products(request, did):
    cu = request.user
    cuid = cu.id

    if request.method == 'POST':
        product = ProductModel.objects.get(id=did)
        pn = request.POST['prtname']
        pd = request.POST['prtdispription']
        pp = request.POST['prtprice']
        select = request.POST.get('select')
        scategory = SubCategoryModel.objects.get(id=select)    
        product.Product_Name = pn
        product.Product_Discription = pd
        product.Product_Price = pp
        product.SubCategory = scategory
        product.Category = scategory.Category   
        product.save()    
        if 'images' in request.FILES:
            new_images = request.FILES.getlist('images')        
            ProductImage.objects.filter(Product=product).delete()            
            for image in new_images:
                ProductImage.objects.create(Product=product, image=image)
        if 'latitude' in request.POST and 'longitude' in request.POST:
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            UserLocation.objects.filter(Prod=product).update(latitude=latitude, longitude=longitude)

    return redirect('sellerProfile', cuid)


def addProductFunction(request):
    if request.method == 'POST':
        pn = request.POST['prtname']
        pd = request.POST['prtdispription']
        pp = request.POST['prtprice']
        select = request.POST.get('select')
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        images = request.FILES.getlist('images')

        cuser = request.user
        sid = cuser.id
        user = SellerData.objects.get(user=sid)



        scategory = get_object_or_404(SubCategoryModel, id=select)

        data = ProductModel(
            Product_Name=pn,
            Product_Discription=pd,

            Product_Price=pp,
            SubCategory=scategory,
            Category=scategory.Category,
            seller=user,
            approved=False,
            stock=True
        )
        data.save()

        for image in images:
            ProductImage.objects.create(Product=data, image=image)

        UserLocation.objects.create(Prod=data, latitude=latitude, longitude=longitude)
        messages.info(request, 'Thank you for your submission! 🎉 Your request is now awaiting approval from our admin team. Once approved, you will receive a confirmation email with further instructions. We appreciate your patience and look forward to welcoming you soon! If you have any urgent queries, feel free to reach out to our support team. Happy exploring!         thank you TEAM ALTOS')
        return redirect('sellerProfile' , user.user.id)
 

    

def billing_data(request, did):
    current_user = request.user
    uid = current_user.id
    data = SellerData.objects.get(user=uid)
    if request.method=='POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        comapny_name = request.POST['company_name']
        house_number = request.POST['house_number']
        post_code = request.POST['post_code']
        land_mark = request.POST['land_mark']

        
     
        
     

        cart = CartModel.objects.filter(Customer_id=did)
        
  
        for cart in cart:
            product = cart.Product
            image = cart.Image
            seller = cart.Product.seller

            values = BillingData(
                firstname=first_name,
                lastname=last_name,
                companyname=comapny_name,
                housenumber=house_number,
                pincode=post_code,
                landmark=land_mark,
                seller=seller,
            
           
                product=product,
                image=image
            )
            values.save()
    return redirect('checkoutcard', data.id)
        
def payment_details(request,did):
    current_user = request.user
    uid = current_user.id
    data = SellerData.objects.get(user=uid)
    user=data.user
    
    print(uid)
    if request.method=='POST':
        
 
        card_number = request.POST['cardnumber']
        card_name = request.POST['cardname']
        day = request.POST['day']
        year = request.POST['year']
        security_code = request.POST['securitycode']

         
       
        carts = CartModel.objects.filter(Customer_id=did)
        
     
        for cart in carts:
            product = cart.Product
            image = cart.Image
            seller=cart.Product.seller


            values = PaymentData(
                cardnumber=card_number,
                cardname=card_name,
                day=day,
                year=year,
                securitycode=security_code,
                seller=seller,
                user=user,
                
    

                product=product,
                image=image 
            )
            values.save()

    return redirect('OrderData', data.id)

def feedback(request):
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)
    data = ReviewData.objects.all()
    return render (request,'feedback.html',{'data':data,'sellers':sellers,'products':products,})






def select_location(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        UserLocation.objects.create(latitude=latitude, longitude=longitude)
  
    return render(request, 'select_location.html')

 

def search_view(request):
    return render(request, 'search.html')




 
 
 

def search_results(request):
    query = request.GET.get('query', '')

  
   


    query_filter = (
        Q(Category__Category_Name__icontains=query) |
        Q(SubCategory__SubCategory_Name__icontains=query) |
        Q(Product_Name__icontains=query)
    )


 


    results = ProductModel.objects.filter(query_filter).filter(approved=True)

    return render(request, 'search_results.html', {'results': results, 'query': query})



def approve_products(request):
    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)
    sellers= SellerData.objects.filter(approved=False)
    return render(request, 'approve_products.html',{'products':products,'sellers':sellers})

def approve_product(request, product_id):
    product = ProductModel.objects.get(pk=product_id)
    product.approved=True
    product.save()
    return redirect('ProductData')

def sellerapprove(request):

    products = ProductModel.objects.prefetch_related('productimage_set').filter(approved=False)

    sellers= SellerData.objects.filter(approved=False)

 
    return render(request, 'sellerapprove.html',{'sellers':sellers,'products':products,} )

def approve_seller(request, did):
    seller_data = SellerData.objects.get(pk=did)
    seller_data.approved = True
    seller_data.save()

    username = seller_data.user.username
    email = seller_data.user.email
    password = str(randrange(100000, 1000000))

 
    seller_data.user.set_password(password)
    seller_data.user.save()

    subject = 'Password Recovery OTP'
    message = f'Dear {username},\n\n'\
              f'Recover your password for your Altos classified account.\n\n'\
              f'Here is your One-Time Password (OTP): {password}\n\n'\
              f'If you did not initiate this password recovery request, please ignore this email.\n\n\n\n'\
              f'Thank you, Altos classified Team'

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    messages.info(request, 'Successfully Approved')
    return redirect('sellerapprove')


def delete_product(request,did):
    product=ProductModel.objects.get(id=did)
    product.delete()
    messages.info(request,'Product deleted successfully')
    return redirect('ProductData')




def soldout(request,did):
    current_user=request.user
    uid=current_user.id
    product=ProductModel.objects.get(id=did)
    product.stock= False
    product.save()
    return redirect ('sellerProfile', uid)

def delete(request,did):
    current_user=request.user
    uid=current_user.id
    product=ProductModel.objects.get(id=did)
    product.delete()
    messages.info(request,'Product deleted successfully')
    return redirect('sellerProfile', uid)

def passwordchange(request):
 
	return render (request,'passwordchange.html')


def passwordchangepage(request):
 
	return render (request,'passwordchangepage.html')

def changepasswordfun(request):
 
    current_user=request.user
    uid=current_user.id
    val=SellerData.objects.get(user=uid)
    if request.method=='POST':
        username=request.POST['username']
        newpass=request.POST['password']
        
        if val.user.username==username:
            
            data=User.objects.get(id=val.user.id)
            data.set_password(newpass)
            data.save()
            messages.info(request, 'password is changed')
            return redirect('userLogin')
        else:
            return redirect('passwordchange')
        
def changepasswordfunforseller(request):
 
    current_user=request.user
    uid=current_user.id
    val=SellerData.objects.get(user=uid)
    if request.method=='POST':
        username=request.POST['username']
        newpass=request.POST['password']
        
        if val.user.username==username:
            
            data=User.objects.get(id=val.user.id)
            data.set_password(newpass)
            data.save()
            messages.info(request, 'password is changed')
            return redirect('SellerLoginPage')
        else:
            return redirect('passwordchangepage')

    
 
    
    return redirect('passwordchange')


