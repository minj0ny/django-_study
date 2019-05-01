from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'), #url의 이름을 home으로 하겠다, 함수 명과 동일하게 할것
]
