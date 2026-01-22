from rest_framework import viewsets, generics, permissions
from django.contrib.auth.models import User
from .models import Hotel
from .serializers import HotelSerializer, UserSerializer

# 1. Le "Cerveau" de tes Hôtels
class HotelViewSet(viewsets.ModelViewSet):
    """
    Cette classe (ViewSet) gère automatiquement :
    - La lecture de la liste (GET /api/hotels/)
    - La création d'un hôtel (POST /api/hotels/)
    - La modification et suppression
    """
    serializer_class = HotelSerializer
    
    # Sécurité : Il faut être connecté pour accéder à ces données
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # LOGIQUE : L'utilisateur (Admin) connecté ne voit QUE SES hôtels.
        # C'est ce qui permet à "Mouhamet Badiane" de ne pas voir les hôtels des autres.
        user = self.request.user
        return Hotel.objects.filter(user=user)

    def perform_create(self, serializer):
        # LOGIQUE : Quand on clique sur "Enregistrer", Django lie 
        # automatiquement l'hôtel à l'utilisateur qui est connecté.
        serializer.save(user=self.request.user)


# 2. La gestion de l'Inscription (Page S'inscrire)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Tout le monde peut accéder à cette vue pour créer un compte
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer