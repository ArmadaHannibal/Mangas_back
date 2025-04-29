from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    priorite_manga = models.CharField(max_length=100)
    categorie_manga = models.CharField(max_length=100, default='Defaut')
    theme_manga = models.CharField(max_length=100, default='Defaut')
    type_manga = models.CharField(max_length=100, default='Defaut')
    saison_manga = models.CharField(max_length=100, default='Defaut')
    genre_manga = models.CharField(max_length=100, default='Defaut')
    public_averti_manga = models.CharField(max_length=100, default='Defaut')
    site_web_manga = models.CharField(max_length=100, default='Defaut')
    vue_manga = models.CharField(max_length=100, default='0')
    langue_manga = models.CharField(max_length=100, default='0')
    cover_image = models.ImageField(upload_to='manga_covers/')
    image_content_1 = models.ImageField(upload_to='manga_covers/', null=True)
    image_content_2 = models.ImageField(upload_to='manga_covers/', null=True)
    image_content_3 = models.ImageField(upload_to='manga_covers/', null=True)
    image_content_4 = models.ImageField(upload_to='manga_covers/', null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Commentaire(models.Model):
    manga = models.ForeignKey(Manga, related_name='commentaires', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    notecomment = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire de {self.utilisateur.username} sur {self.manga.title}'
    

class Favories(models.Model):
    manga = models.ForeignKey(Manga, related_name='favories', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manga.title

class Vue(models.Model):
    manga = models.ForeignKey(Manga, related_name='vue', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manga.title
    
    
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    # Vos autres champs personnalisés ici

    # Spécifiez des related_names différents pour les groupes et les permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Nom personnalisé pour les groupes
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Nom personnalisé pour les permissions
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )