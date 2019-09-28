from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from studentMarks.models import User
import studentMarks.urls as sMURLS  
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'dateOfBirth', 'currentStream', 'currentClass']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(sMURLS)),
    path('drf', include('rest_framework.urls', namespace='rest_framework'))
]
