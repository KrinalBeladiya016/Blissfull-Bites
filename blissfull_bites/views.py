from django.http import HttpResponse
from django.shortcuts import render,redirect
from User.models import *
from Products.models import *
from django.core.mail import send_mail
from datetime import datetime
from django.db.models import Sum

def login(req):
    invalidMsg = ""
    try:
        if req.method == "POST":
            print("login called!")
            eml = req.POST.get('email')
            password = req.POST.get('password')

            userInfo = userDetails.objects.filter(email=eml)

            for details in userInfo:
                if details.password != password:
                    invalidMsg += 'Invalid Password! Please enter correct password and try again'
                    break
                req.session['email'] = eml
                return redirect("home")
            else:
                invalidMsg = f"The user with email : {eml} is not registered with us. Please Check your email or sign up first."
        else:
            del req.session['email']
    except:
        pass
    return render(req,"index.html",{'invalidMsg':invalidMsg})

def homePage(req):
    cats = Category.objects.all()[:4]
    best_sellers = []
    orders = Order_Products.objects.values('product_id').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')
    for order in orders:
        best_sellers.append(Product.objects.get(pk=order['product_id']))
    return render(req,"home.html/",{'categories':cats, "bestSellers":best_sellers[:10],'loginID': req.session.get('email')})

def showCategories(req):
    cats = Category.objects.all()
    return render(req, "categories.html", {"categories": cats, 'loginID': req.session.get('email')})

def registerUser(req):
    try:
        if req.method == "POST":
            name = req.POST.get('fname') + " " + req.POST.get('lname')
            contact = req.POST.get('contact_no')
            eml = req.POST.get('email')
            address = req.POST.get('house') + ",\n" + req.POST.get('area') + ",\n" + req.POST.get('city') + ",\n" + req.POST.get('state') + " - " + req.POST.get('pincode')
            password = req.POST.get('password')

            info = userDetails(name=name,email=eml,contact_no=contact,password=password,address=address)
            info.save()

            return redirect("indexPage")
    except:
        pass
    return render(req,"register.html")


def getProducts(req,categoryName):
    cats = Category.objects.all()
    prodInfo = Product.objects.filter(category=categoryName)
    return render(req,"products.html",{'prodInfo':prodInfo, 'categories':cats, 'cname':categoryName, 'loginID': req.session.get('email')})

def showProductDetails(req,pid):
    details = Product.objects.get(pk=pid)
    return render(req,"productDetails.html",{'product':details, 'loginID': req.session.get('email')})

def addToCart(req,pid):
    try:
        Cart.objects.get(productId=pid)
        return HttpResponse(False)
    except:
        cart = Cart(email=userDetails.objects.get(pk=req.session['email']), productId=Product.objects.get(pk=pid))
        cart.save()
        return HttpResponse(True)

def deleteCartItem(req,itemId):
    item = Cart.objects.get(pk=itemId)
    item.delete()
    return redirect("openCart")

def updateCart(req,data):
    id = int(data.split("-")[0])
    qty = int(data.split('-')[1])
    print(id,qty)
    obj = Cart.objects.filter(email=req.session.get('email'),productId=id)
    obj.update(quantity=qty)
    return HttpResponse("Updated")

def displayCart(req):
    userMsg = ""
    productsList = []

    productsInCart = Cart.objects.filter(email=req.session.get('email'))
    if len(productsInCart) == 0:
        userMsg = "No Products in your bakery cart!"
    else:
        for p in productsInCart:
            productsList.append(Product.objects.get(pk=p.productId.id))
    data = zip(productsList,productsInCart)
    return render(req,"cart.html",{'msg':userMsg, 'productData':data, 'loginID': req.session.get('email')})

def getUserDetails(req):
    details = userDetails.objects.get(pk=req.session.get('email'))
    return HttpResponse(details.name + " - " + details.contact_no + " - " + details.address)

def placeOrder(req):
    try:
        if req.method == "POST":
            currTime = datetime.now()
            user = userDetails.objects.get(pk=req.session.get('email'))
            totalAmt = req.POST.get('totalAmount')
            try:
                order = User_Orders(email=user,total_amount=totalAmt,order_time=currTime)
            except:
                pass
            order.save()

            items = Cart.objects.filter(email=req.session.get('email'))
            for item in items:
                p = Order_Products(order_id=order,product_id=Product.objects.get(pk=item.productId.id),quantity=item.quantity)
                p.save()
            items.delete()
            # send_mail('Order Details','Your order is placed successfully and will be delivered soon!','blissfullbites0011@gmail.com',[req.session.get('email')],fail_silently=False)
            return redirect("orderHistory")
    except:
        pass
    return render(req,"orderDetails.html")

def getUserOrders(req):
    orders = User_Orders.objects.filter(email=req.session.get("email")).order_by("-id")
    return render(req,"userOrders.html",{'orders':orders, 'loginID': req.session.get('email')})

def getorderDetails(req,oid):
    details = []
    prods = Order_Products.objects.filter(order_id=oid)
    for p in prods:
        prod = Product.objects.get(pk=p.product_id.id)
        details.append({'name':prod.name,'price':prod.price,'image':prod.product_image,'qty':p.quantity})
    return render(req,"orderDetails.html",{"details":details, 'loginID': req.session.get('email')})

def logOut(req):
    del req.session['email']
    return redirect("indexPage")

def signOut(req):
    user = userDetails.objects.get(pk=req.session.get('email'))
    user.delete()
    return redirect("indexPage")

def editUserProfile(req):
    user = userDetails.objects.get(pk=req.session.get('email'))
    try:
        if req.method == "POST":
            name = req.POST.get('fname') + " " + req.POST.get('lname')
            contact = req.POST.get('contact_no')
            address = req.POST.get('house') + ",\n" + req.POST.get('area') + ",\n" + req.POST.get('city') + ",\n" + req.POST.get('state') + " - " + req.POST.get('pincode')
            user = userDetails.objects.filter(email=req.session.get('email'))
            user.update(name=name,contact_no=contact,address=address)
            return redirect("home")
    except:
        pass
    return render(req,"editProfile.html",{'details':user})

def showAboutInfo(req):
    return render(req, "aboutUs.html", {"loginID": req.session.get("email")})

def franchiseDetails(req):
    try:
        if req.method == "POST":
            name = req.POST.get('fname') + req.POST.get('lname')
            email = req.POST.get('email')
            phone = req.POST.get('contact_no')
            state = req.POST.get('state')
            city = req.POST.get('city')
            pin = req.POST.get('pincode')

            f = Franchise(name=name,email=email,contact_no=phone,state=state,city=city,pincode=pin)
            f.save()
            return render(req,"franchise.html",{'msg':"Thanks for applying for franchise"})
    except:
        pass
    return render(req,"franchise.html",{'msg':"","loginID": req.session.get("email")})

def showOutlets(req):
    return render(req,"outlets.html")
