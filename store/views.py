from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import random
from django.contrib import messages


# Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Add to Cart
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

# View Cart

def view_cart(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login and register to access the cart")
        return redirect('user_login')
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.subtotal() for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

# Checkout
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.subtotal() for item in cart_items])

    if request.method == "POST":
        # Fake order creation
        order = Order.objects.create(
            user=request.user,
            total_price=total,
            is_paid=True,
            payment_id="FAKE-DEMO-" + str(order_id_generator())
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
        cart_items.delete()
        return redirect('payment_success')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

# Demo order ID generator

def order_id_generator():
    return random.randint(100000, 999999)

# Payment Success (Redirect from Razorpay)
@login_required
def payment_success(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum([item.subtotal() for item in cart_items])
    
    order = Order.objects.create(user=request.user, total_price=total, is_paid=True)
    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )
    cart_items.delete()
    return render(request, 'payment_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})

# User Auth Views
def user_login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_register(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        User.objects.create_user(username=u, password=p)
        return redirect('user_login')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=query) if query else []
    return render(request, 'search.html', {'results': results, 'query': query})