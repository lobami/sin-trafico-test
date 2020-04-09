from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Generate:
    New token session.
    """
    serializer_class = MyTokenObtainPairSerializer
