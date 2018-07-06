from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from OnlineShop.settings import MEDIA_ROOT

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin

from goods.views import GoodsListViewSet, CategoryViewset, BannerViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset



router = DefaultRouter()

# Set up goods URL
router.register(r'goods', GoodsListViewSet, base_name="goods")

# Set up category URL
router.register(r'categorys', CategoryViewset, base_name="categorys")

# Favourite
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# Comment
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# Address
router.register(r'address', AddressViewset, base_name="address")

# Cart url
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# Order url
router.register(r'orders', OrderViewset, base_name="orders")

# Banners url
router.register(r'banners', BannerViewset, base_name="banners")

urlpatterns = [
    url(r'^', include((router.urls))),

    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),



    url(r'xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls("OnlineShop")),



]
