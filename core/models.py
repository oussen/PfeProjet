from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Entreprise(models.Model):
    SECTEUR_ACTIVITE = (
        ('1', 'Services'),
        ('2', 'Education'),
        ('3', 'Banque'),
        ('4', 'Assurances'),
        ('5', 'Medical')
    )

    nom_entreprise = models.CharField(max_length=500)
    mission = models.TextField(max_length=1000)
    addresse = models.CharField(max_length=500)
    contact_name = models.CharField(max_length=500)
    join_date = models.DateField(default=timezone.now)
    email = models.EmailField()
    secteur_activite = models.CharField(max_length=1000, choices=SECTEUR_ACTIVITE)
    urls_en = models.CharField(max_length=500)
    urls_linkedin = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str___(self):
        return self.nom



class EvenementCategory(models.Model):
    name = models.CharField(max_length=50)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name



class Evenement(models.Model):

    hunter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('EvenementCategory',
                                  null=True,
                                  blank=True,
                                  on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=1500)
    lieu = models.CharField(max_length=500)
    sale = models.CharField(max_length=500)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    #created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500, default='ETSMTL')



    def __str___(self):
        return self.lieu

class Joindre(models.Model):
    nombre_representant = models.CharField(max_length=500)
    description =  models.CharField(max_length=1500)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)

    def __str___(self):
        return self.description

class OfferCategory(models.Model):
    name = models.CharField(max_length=50)

    def slug(self):
        return (self.name)

    def __str__(self):
        return self.name



class Offer(models.Model):

    hunter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=500)
    short_description = models.TextField(max_length=1000)
    date_de_debut = models.CharField(max_length=500)
    dete_de_fin = models.CharField(max_length=500)
    salaire = models.CharField(max_length=500)
    evenement = models.ManyToManyField(Evenement)
    category = models.ForeignKey('OfferCategory',
                                 null=True,
                                 blank=True,
                                 on_delete=models.DO_NOTHING)

    def __str___(self):
        return self.name


class Employe(models.Model):

    hunter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    fonction = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    evenement = models.ManyToManyField(Evenement)


    def __str___(self):
        return self.name




class Invitation(models.Model):
    hunter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    evenement = models.ForeignKey('Evenement',
                                  on_delete=models.CASCADE,
                                  related_name='invitation')
    sujet = models.CharField(max_length=500)
    liste_email = models.CharField(max_length=500)
    event = models.CharField(max_length=500)
    description = models.CharField(max_length=1500)

    def __str___(self):
        return self.sujet


#### ajout de commentaire
class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERATED, 'Moderated'),
    )

    evenement = models.ForeignKey('Evenement',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20,
                              default=STATUS_VISIBLE,
                              choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.text


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='participant')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str___(self):
        return self.user.get_full_name()



#####################################################################################

class Postule(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERATED, 'Moderated'),
    )




    #hunter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    offre = models.ForeignKey('Offer',
                                  on_delete=models.CASCADE,
                                  related_name='postules')
    status = models.CharField(max_length=20,
                              default=STATUS_HIDDEN,
                              choices=STATUS_CHOICES)
    date_postulation = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=500)
    upload_cv = models.FileField(upload_to='documents/', blank=True)
    #upload_doc = commentaire = models.TextField(max_length=500)


    def __str___(self):
        return self.date_postulation