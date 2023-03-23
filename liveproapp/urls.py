from django.urls import path
from liveproapp import views


urlpatterns = [
 
    path("",views.index),
    path("about/",views.about),
    path("services/",views.services),
    path("gallery/",views.gallery),
    path("contact/",views.contact),
    path("single/",views.single),


###############################################################################################################
    path("admin_index/",views.admin_index),
    path("admin_signin/",views.admin_signin),
    path("admin_signup/",views.admin_signup),
    path("admin_signout/",views.admin_signout),
    path("admin_form_product/",views.admin_form_product),
    path("admin_product_display/",views.admin_product_display),
    path("admin_product_update/",views.admin_product_update),
    path("admin_product_delete/",views.admin_product_delete),
    path("admin_form_gallery/",views.admin_form_gallery),
    path("admin_gallery_display/",views.admin_gallery_display),
    path("admin_gallery_update/",views.admin_gallery_update),
    path("admin_gallery_delete/",views.admin_gallery_delete),
]