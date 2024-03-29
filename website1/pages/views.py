from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Contact,Register,Product,Cart,Order

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    

    return HttpResponse(template.render({},request))

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render({},request))

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render({},request))

def addproduct(request):
    template = loader.get_template("addproduct.html")
    return HttpResponse(template.render({},request))

def product(request):

    products=Product.objects.all().values()

    context={
        'products':products
    }

    template = loader.get_template("product.html")
    return HttpResponse(template.render(context,request))



def account(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/login")
    template = loader.get_template("account.html")
    return HttpResponse(template.render({},request))
def login(request):
    if 'user' in request.session:
        return HttpResponseRedirect("/account")
    if request.method=='POST':
        log_user=request.POST["login_username"]
        log_pass=request.POST["login_password"]

        login=Register.objects.filter(reg_username=log_user,reg_password=log_pass)

        if(login):
            request.session["user"]=log_user
            return HttpResponseRedirect("/account")

    template = loader.get_template("login.html")
    return HttpResponse(template.render({},request))
 

def register(request):
    if 'user' in request.session:
        return HttpResponseRedirect("/account")
    if request.method =='POST':
        reg_name =request.POST['reg_name']
        reg_email = request.POST['reg_email']
        reg_phone = request.POST['reg_phone']
        reg_username = request.POST['reg_username']
        reg_password = request.POST['reg_password']



        register = Register(reg_name=reg_name,
                        reg_email=reg_email,
                        reg_phone=reg_phone,
                        reg_username=reg_username,
                        reg_password=reg_password)
        
        register.save()


    template = loader.get_template("register.html")
    return HttpResponse(template.render({},request))

def contact(request):
    if request.method =='POST':
        contact_name =request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_msg =request.POST['contact_msg']

        contact = Contact(con_name=contact_name,
                        con_email=contact_email,
                        con_msg=contact_msg)
        
        contact.save()


    template = loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
    

def logout(request):
    if 'user' in request.session:
        del request.session["user"]
    return HttpResponseRedirect("/login")


def addproduct(request):
    if request.method =='POST':
        product_name =request.POST['pro_name']
        product_price = request.POST['pro_price']
        product_image = request.FILES['pro_image']
        

        product = Product(pro_name=product_name,
                        pro_price=product_price,
                        pro_image=product_image)
                        
        product.save()


    template = loader.get_template("addproduct.html")
    return HttpResponse(template.render({},request))

def addtocart(request,id):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')
    

    exist = Cart.objects.filter(cart_proid=id)
    if exist:
        exstcart = Cart.objects.filter(cart_proid=id)[0]
        exstcart.cart_qty+=1
        exstcart.cart_amount = exstcart.cart_qty * exstcart.cart_price
        exstcart.save()
    else:    
    
        pro = Product.objects.filter(id=id)[0]

        cart = Cart(cart_user =request.session["user"],
                    cart_proid = pro.id,
                    cart_name=pro.pro_name,
                    cart_price=pro.pro_price,
                    cart_image=pro.pro_image,
                    cart_qty=1,
                    cart_amount=pro.pro_price)
        cart.save()
    return HttpResponseRedirect("/cart")
    

def cart(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')
    

    #delete cart item
    if 'del' in request.GET:
        id = request.GET['del']
        delcart = Cart.objects.filter(id=id)[0]
        delcart.delete()

    #change cart quantity    

    
    if 'q' in request.GET:
        q = request.GET['q']
        cp = request.GET['cp']
        cart3=Cart.objects.filter(id=cp)[0]

        if q=='inc':
            cart3.cart_qty+=1
        elif q=='dec':
            if(cart3.cart_qty>1):
                cart3.cart_qty-=1
                
        cart3.cart_amount = cart3.cart_qty * cart3.cart_price
        cart3.save()        
    

    user = request.session["user"]
    cart=Cart.objects.filter(cart_user=user).values()
    cart2=Cart.objects.filter(cart_user=user)


    tot = 0
    for x in cart2:
        tot+=x.cart_amount

    shp = tot * 10/100
    gst = tot * 18/100

    gtot = tot+shp+gst    


    context={

        'cart':cart,
        'tot':tot,
        'shp':shp,
        'gst':gst,
        'gtot':gtot
    }

    template = loader.get_template("cart.html")
    return HttpResponse(template.render(context,request))


def checkout(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/login')
    co = 0
    adrs = dtype = ""
    if 'dlv_adrs' in request.POST:
        adrs = request.POST["dlv_adrs"]
        dtype = request.POST["dlv_type"]
        co=1

    user = request.session["user"]   

    #delete old data from orders
    oldodr=Order.objects.filter(ord_user=user) 
    oldodr.delete()

    #add cart data to order table
    cart=Cart.objects.filter(cart_user=user)
    for x in cart:
        odr = Order(ord_user = x.cart_user,
                    ord_name = x.cart_name,
                    ord_price =x.cart_price,
                    ord_image =x.cart_image,
                    ord_qty=x.cart_qty,
                    ord_amount=x.cart_amount,
                    ord_address=adrs,
                    ord_dlvtype=dtype,
                    )
        odr.save()
    
    #display order data
    order=Order.objects.filter(ord_user=user).values()
    order2=Order.objects.filter(ord_user=user)   
    
    

    tot = 0
    for x in order2:
        tot+=x.ord_amount
        
        

    shp = tot * 10/100
    gst = tot * 18/100

    gtot = tot+shp+gst    


    context={

        'order':order,
        'tot':tot,
        'shp':shp,
        'gst':gst,
        'gtot':gtot,
        'co':co
    }

    template = loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))

def confirmorder(request):
    user = request.session["user"]
    order=Order.objects.filter(ord_user=user)
    for x in order:
        x.ord_status=1
        x.save()
    template = loader.get_template("confirmorder.html")
    return HttpResponse(template.render({},request))    

def myorders(request):
    user = request.session["user"]
    order=Order.objects.filter(ord_user=user,ord_status=1)
    context = {
        'order':order
    }
    template = loader.get_template("myorders.html")
    return HttpResponse(template.render(context,request))



