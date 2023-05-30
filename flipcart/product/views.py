from django.http import HttpResponse
from django.shortcuts import render, redirect

from .import category
from .category import Category
from .models import Product, Customer
from django.contrib.auth.hashers import make_password,check_password

def index(request):

    product = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        product = Product.objects.filter(category=category_id)
    else:
        product = Product.get_all_product()
    s={"product":product,'categories':categories}

    product=request.POST.get('product')
    cart=request.POST.get('cart')
    if cart:
        quantity=cart.get(product)
        if quantity:
            cart[product]=quantity+1
        else:
            cart[product]=1
    else:
        cart={}
        cart[product]=1
    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'index.html',s)
def signup(request):
    if request.method=="GET":
        return render(request,'category.html')
    else:
        a=request.POST
        fn=a.get('fn') #fn=request.POST['fn']
        ln=a.get('ln')#ln=request.POST['ln']
        email=a.get('email')
        mobile=a.get('phone')
        password=a.get('password')

        customerdata=Customer(first_name=fn,last_name=ln,email=email,mobile=mobile,password=password)
        values={'first_name':fn,'last_name':ln,'phone':mobile,'password':password,'email':email}
    error_message=None
    if (not fn):
        error_message="firstname should not to be empty"
    elif (len(fn)<4):
        error_message='minimum 4 characters are required for first name'
    elif (not ln):
        error_message="lastname should not to be empty"
    elif (len(ln)<4):
        error_message='minimum 4 characters are required for last name'
    elif (not email):
        error_message="This field is mandatory"
    elif (not mobile):
        error_message='This field is required'
    elif (len(mobile)<10 and len(mobile)>10):
        error_message='mobile number must be 10 digit number'
    elif (not password):
        error_message='password should not be empty'
    elif (not password):
        error_message='password should not be empty'
    elif(len(password)<5):
        error_message = 'password should contains minimum 4 characters are required'
    elif customerdata.isexists():
        error_message="your Email is already exists"

    if (not error_message):
        customerdata.password=make_password(customerdata.password)
        customerdata.save()
        return redirect('/')
    else:
        msg={'values':values,'error':error_message}
        return render(request,'category.html',msg)

def login(request):

    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_email(email)
        error_message=None
        if customer:
            check=check_password(password,customer.password)
            if check:
                request.session['u_id']=customer.id
                request.session['u_email'] = customer.email
                print("your logged in:", request.session['u_email'])
                return redirect('/')
            else:
                error_message='your password is wrong'
        else:
            error_message='email doesnot exists'
    return render(request, 'login.html',{'error':error_message})



