from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

from cart.webhook import webhook
from cart.views import cart_detail, success
from core.views import frontpage, about
from order.views import admin_order_pdf
from store.views import product_detail, category_detail, search, delete_product, my_listings,  addproducts, ProductUpdateView
from userprofile.views import signup, myaccount, profile, seller_profile, create_profile, contact_view
from django.views.generic.edit import UpdateView

from newsletter.api import api_add_subscriber
from coupon.api import api_can_use
from store.api import api_add_to_cart, api_remove_from_cart, create_checkout_session, validate_payment

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('add/', addproducts, name='addProducts'),
    path('mylistings/', my_listings,name='mylistings'),
    path('delete/<int:id>/', delete_product,name='delete_product'),
    path('update/<int:pk>/',ProductUpdateView.as_view(),name='update_product'),
    path('search/', search, name='search'),
    path('cart/', cart_detail, name='cart'),
    path('hooks/', webhook, name='webhook'),
    path('success/', success, name='success'),

    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),


    # Auth

    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('sellerprofile/<int:id>/',seller_profile,name='sellerprofile'),
    path('createprofile/',create_profile,name='createprofile'),
    path('contact/', contact_view, name='contact'),




    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # API

    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api/validate_payment/', validate_payment, name='validate_payment'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

    # Store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
