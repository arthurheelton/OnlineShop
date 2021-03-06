from django.conf.urls import url
from footspace.views import (
	base_view,
	category_view,
	product_view,
	cart_view,
	add_to_cart_view,
	remove_from_cart_view,
	change_item_quantity,
	checkout_view,
	order_create_view
	)

urlpatterns = [
	 url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
	 url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
	 url(r'^add_to_cart/$', add_to_cart_view, name='add_to_cart'),
	 url(r'^remove_from_cart/$', remove_from_cart_view, name='remove_from_cart'),
	 url(r'^change_item_quantity/$', change_item_quantity, name='change_item_quantity'),
	 url(r'^cart/$', cart_view, name='cart'),
	 url(r'^checkout/$', checkout_view, name='checkout'),
	 url(r'^order/$', order_create_view, name='create_order'),
    url(r'^$', base_view, name='base'), 
]