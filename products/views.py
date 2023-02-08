from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Image
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.filter(active=True).prefetch_related("images")
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    images = Image.objects.filter(product=product)

    context = {"product": product, "images": images}

    return render(request, "products/product_details.html", context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        return redirect(reverse("home"))
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist("image")
            product = form.save()
            for image in images:
                if image.name == request.POST.get("primary-image-input"):
                    Image.objects.create(
                        product=product, file_name=image, default=True
                    )
                else:
                    Image.objects.create(
                        product=product, file_name=image, default=False
                    )
            messages.success(request, f"Successfully added {product.name}")
            return redirect(reverse("product_details", args=[product.id]))
        else:
            messages.error(
                request, f"Failed to add Product: {form.errors.as_text()}"
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(
            request, "You are not authorized to remove products as this user."
        )
        return redirect(reverse("products"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Successfully deleted: {product.name}")
    return redirect(reverse("products"))


@login_required
def update_product(request, product_id):
    """A view to update an existing product"""

    if not request.user.is_superuser:
        messages.error(
            request, "You are not authorized to update products as this user."
        )
        return redirect(reverse("products"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}!")
            return redirect(reverse("product_details", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid",
            )
            if form.errors:
                messages.error(request, form.errors.as_text())
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are updating {product.name}")

    template = "products/update_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)
