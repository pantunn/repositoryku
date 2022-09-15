from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import barang_wishlist #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import barang_wishlist_json
from wishlist.views import kembalikan_data #sesuaikan dengan nama fungsi yang dibuat

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', barang_wishlist, name='barang_wishlist'),
    path('json/', barang_wishlist_json, name='barang_wishlist_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', kembalikan_data, name='kembalikan_data'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', kembalikan_data, name='kembalikan_data')
    
]