from django.conf.urls import include, url
from django.contrib import admin
from api import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'task', views.TaskListView)
urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^index/', views.IndexVIew.as_view()),
]
urlpatterns += router.urls
