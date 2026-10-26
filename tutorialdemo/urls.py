from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, footer, user, contact, product_create, product_list, product_delete,update_data,student_form,file_upload,set_session,get_session,delete_session,set_cookie,get_cookie,delete_cookie,tracker

urlpatterns = [
    path("", home, name="home"),
    path("footer/", footer, name="footer"),
    path("user/", user, name="user"),
    path("contact/", contact, name="contact"),
    path("product/", product_create, name="product_create"),
    path("student/", student_form,name="student_form"),
    path("list/", product_list, name="product"),
    path("delete/,<int:id>/", product_delete, name="delete_product"),
    path("update/,<int:id>/", update_data, name="data_update"),
    path("upload/",file_upload,name="file_upload"),
    path("session/set/",set_session),
    path("session/get/",get_session),
    path("session/delete/",delete_session),
    path("cookie/set/",set_cookie),
    path("cookie/get/",get_cookie),
    path("cookie/delete/",delete_cookie),
    path("tracker/", tracker, name="tracker")
]

urlpatterns+static(
    settings.MEDIA_URL,
    documents_root=settings.MEDIA_ROOT
)