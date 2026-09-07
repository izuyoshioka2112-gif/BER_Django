from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Staff, Order, OrderItem
import json
from django.http import JsonResponse
from django.contrib import messages

# Create your views here


class ListProductView(ListView):
    template_name = "product/product_list.html"
    queryset = Product.objects.order_by('category')


class DetailListProductView(DetailView):
    template_name = "product/product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quantity_range"] = range(1, 6)
        return context


def add_to_cart_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = str(data.get("product_id"))
        quantity = int(data.get("quantity", 1))
        cart = request.session.get("cart", {})
        cart[product_id] = cart.get(product_id, 0) + quantity
        if cart[product_id] > 15:
            return JsonResponse({"status": "error", "message": "商品一つにつき、15個以上の注文はできません"}, status=400)
        request.session["cart"] = cart
        request.session.modified = True
        return JsonResponse({"status": "ok", "cart": cart})
    return JsonResponse({"status": "error"}, status=400)

def cart_view(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            }
        )
        # リクエストは上のものと同じで自動的にブラウザから送られてくる情報が入っている。returnで使うのは、どこに情報を送ればいいか示すためでもある。しかし、実際に送っているのはrender
    return render(
        request,
        "product/cart.html",
        {
            "cart_items": cart_items,
            "total_price": total_price,
            "quantity_range": range(1, 16),
        },
    )


def update_cart_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = str(data.get("product_id"))
        quantity = int(data.get("quantity", 1))
        cart = request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] = quantity
            request.session["cart"] = cart  # このユーザー専用のデータ保管庫(request.session)に更新点を追加
            request.session.modified = True
        return JsonResponse({"status": "ok", "cart": cart})
    return JsonResponse({"status": "error"}, status=400)


def remove_from_cart_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = str(data.get("product_id"))
        cart = request.session.get("cart", {})
        if product_id in cart:
            del cart[product_id]
            request.session["cart"] = cart
            request.session.modified = True
        return JsonResponse({"status": "ok", "cart": cart})
    return JsonResponse({"status": "error"}, status=400)

def order_confirm_view(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "商品が入っていません")
        return redirect("cart")
    if request.method == "POST":
        table_number = request.POST.get("table_number")
        staff_id = request.POST.get("staff")
        # POST.get＝お客のブラウザから取ってきてる
        staff = Staff.objects.get(id=staff_id)
        # objects.get＝DBから取ってきてる
        order = Order.objects.create(
            table_number = table_number,
            staff=staff,
        )
        for product_id, quantity in cart.items():
            # DBを分けてるからここでくっつけてあげる（親、子）
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
            )
        request.session["cart"] = {}
        request.session.modified = True
        return redirect("order_done")
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append({
            "product":product,
            "quantity": quantity,
            "subtotal":subtotal,
        })
    staff_list = Staff.objects.all()
    table_range = range(1, 21)
    return render(request, "product/order_confirm.html",{
        "cart_items": cart_items,
        "total_price": total_price,
        "staff_list": staff_list,
        "table_range": table_range,
    })

def order_done_view(request):
    return render(request, "product/order_done.html")