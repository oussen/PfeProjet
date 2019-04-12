from django import forms

from django.contrib.auth.models import User
from .models import Entreprise, Offer, Employe, Evenement, Invitation, Comment, Postule


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ('nom_entreprise', 'mission', 'addresse', 'contact_name',)


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('titre', 'short_description','date_de_debut', 'dete_de_fin', 'salaire')

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ('name', 'fonction', 'contact', 'linkedin')

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ( 'title','category','description', 'lieu', 'sale', 'date_debut', 'date_fin')


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ('sujet', 'liste_email', 'event', 'description')


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text', ]


#####################################
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


########################## postule #########################
class PostuleForm(forms.ModelForm):
    class Meta:
        model = Postule
        fields = ['email', 'upload_cv', 'offre' ]