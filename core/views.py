from django.shortcuts import render
from store.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def frontpage(request):
    products = Product.objects.filter(is_featured=True)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]
    page_number = request.GET.get('page')
    paginator = Paginator(products,4)

    try:
       products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products

    }

    return render(request, 'frontpage.html', context)





def about(request):
    return render(request, 'about.html')

