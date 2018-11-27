from django.conf.urls import url
from pabd.views import home,lista


urlpatterns=[
	url(r'^$', home),
	url(r'^lista-todos/$',lista),]