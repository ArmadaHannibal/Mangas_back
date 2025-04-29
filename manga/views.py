from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import CustomLoginForm, CustomSignupForm
from django.http import JsonResponse
from .models import Manga, Commentaire, Favories, Vue
from .serializers import MangaSerializer, CommentaireMangaSerializer, VueMangaSerializer, FavoryMangaSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status


# Create your views here.

# Index le template de la page d'Accueil
def index(request):
    # Récupérer tous les objets Manga de la base de données
    mangas = Manga.objects.all()
    commentaire = Commentaire.objects.all()
    favory = Favories.objects.all()
    vue = Vue.objects.all()
    serializer = MangaSerializer(mangas, many=True)
    serializerCommentaire = CommentaireMangaSerializer(commentaire, many=True)
    serializerfavory = CommentaireMangaSerializer(favory, many=True)
    serializervue = CommentaireMangaSerializer(vue, many=True)

    data = {
        'mangas': serializer.data,
        'commentaires': serializerCommentaire.data,
        'favory': serializerfavory.data,
        'vue': serializervue.data,
    }
    
    return JsonResponse(data, safe=False)
    # return render(request, 'manga/page/index.html', {'mangas': mangas})

# Show le template du contenu de chaque cards (manga)
def show(resquest, book_id):
    # context = {"book": get_object_or_404(Book, pk = book_id)}
    return render(resquest, "manga/sigle.html")

# Connexion le template de connexion pour les utilisateurs déjà inscrit
@csrf_exempt
@api_view(['POST'])
def connexion(request):
    form = CustomLoginForm(data=request.data)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    # if request.method == 'POST':
    #     form = CustomLoginForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             # Redirigez l'utilisateur vers une page appropriée après la connexion
    #             return redirect('manga:index')
    #         # else:
    #         #     form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    # else:
    #     form = CustomLoginForm(request)
    # # context = {"book": get_object_or_404(Book, pk = book_id)}
    # return render(request, "manga/ui/connexion.html", {'form': form})

# Inscription le template de l'inscription pour les nouveaux utilisateurs
def inscription(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Vérifier si le compte existe déjà
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Ce nom d\'utilisateur est déjà pris.')
            else:
                # Créer un nouvel utilisateur
                user = User.objects.create_user(username=username, email=email, password=password)
                # Rediriger vers une page de confirmation ou une autre vue
                return redirect('confirmation')
    else:
        form = CustomSignupForm()
    return render(request, 'manga/ui/inscription.html', {'form': form})

# Compte de l'utilisateur 
# def compte(request, id_compte):
#     context = {"id_compte": get_object_or_404(Book, pk = book_id)}

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        image_file = request.data.get('profile_image')  # Assuming 'profile_image' is the key for the image data

        if image_file:
            user.profile_image = image_file
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No image data provided'}, status=status.HTTP_400_BAD_REQUEST)
