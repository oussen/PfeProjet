import json

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import UserForm, EntrepriseForm, OfferForm, EmployeForm, EvenementForm, InvitationForm, PostuleForm, \
    CreateCommentForm
from .models import Offer, Employe, Invitation, Evenement, Comment, Postule, EvenementCategory
from . import model_helpers

# Create your views here.
# entreprise

def home(request):
    evenement = Evenement.objects.all()
    return render(request, 'home.html', {
        'evenement': evenement
    })

def detailEntr(request):
    return render(request, 'entreprise/detail-entreprise.html', {})

#### entreprise
#@login_required()
def entreprise_home(request):
    evenement = Evenement.objects.all()
    offre = Offer.objects.all()
    if request.method == 'SUPPRIME':
        id = json.loads(request.body)['id']
        evenement = get_object_or_404(Evenement, id=id)

        evenement.delete()

        return HttpResponse('')
    
    if request.method == 'SUPPRIMEJOB':
        id = json.loads(request.body)['id']
        job = get_object_or_404(Offer, id=id)

        job.delete()

        return HttpResponse('')



    return render(request, 'entreprise/entreprise_home.html',
                  {'evenement': evenement,
                   'offre' : offre})


######## entreprise signup



def entreprise_signup(request):
    user_form = UserForm()
    entreprise_form = EntrepriseForm()
    #entreprise_form = EntrepriseForm(request.POST)


    if request.method == "POST":
        user_form = UserForm(request.POST)
        entreprise_form = EntrepriseForm(request.POST)
        if user_form.is_valid() and entreprise_form.is_valid():
        #if  entreprise_form.is_valid():

            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_entreprise = entreprise_form.save(commit=False)
            new_entreprise.user = new_user
            new_entreprise.save()
            return redirect('home')

            login(request, authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            ))


    return render(request, "entreprise/e_signup.html", {
        "user_form": user_form,
        "entreprise_form": entreprise_form
    })



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message( request, messages.SUCCESS, 'votre compte a été crée avec succès')
        else:
            messages.error(request, 'votre compte n a pas été crée')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })



#@login_required
def offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    #offers=Offer.Objects.filter(entreprise = request.user.entreprise).order_by("-id")

    return render(request, 'entreprise/offer.html', {
        'offer':offer
        #'offers':offers
    })


#@login_required
def add_offer(request):
    offer_form = OfferForm(request.POST)
    offer=Offer()

    if request.method == 'POST':
        offer_form = OfferForm(request.POST)
        if offer_form.is_valid():
            offer = offer_form.save(commit=False)
            #offer.entreprise = request.entreprise
            offer.hunter_user = request.user
            offer.save()
            return redirect('entreprise-home')
            #return redirect('/entreprise/offer/' + str(offer.id))
    else:
        offer_form = OfferForm()
    return render(request, 'entreprise/add_offer.html', {
        'offer_form': offer_form
    })

#@login_required
def modifOffre(request, id):
    offre = get_object_or_404(Offer, id=id)
    form = OfferForm(request.POST or None, instance=offre)
    if form.is_valid():
         form.save()

         #return redirect(request, 'entreprise/entreprise_home.html', {'evenements': event})
         return redirect('entreprise-home')

    return render(request, 'entreprise/modif_offre.html', {'form': form})

########Employe
#@login_required
def employe(request, employe_id):
    employe = get_object_or_404(Employe, pk=employe_id)
    return render(request, 'entreprise/employe.html', {
        'employe': employe
    })
#@login_required
def add_employe(request):
    employe_form = EmployeForm(request.POST)
    employe=Employe()

    if request.method == 'POST':
        employe_form = EmployeForm(request.POST)
        if employe_form.is_valid():
            employe = employe_form.save(commit=False)
            #offer.entreprise = request.entreprise
            employe.hunter_user = request.user
            employe.save()
            return redirect('/entreprise/employe/' + str(employe.id))
    else:
        employe_form = EmployeForm()
    return render(request, 'entreprise/add_employe.html', {
        'employe_form': employe_form
    })



########Evenement

#@login_required

def evenement(request, evenement_id):
    from django.shortcuts import render, get_object_or_404, reverse
    evenement = get_object_or_404(Evenement, pk=evenement_id)
    comment_form = CreateCommentForm(request.POST)
    comments = evenement.comments.exclude(status=Comment.STATUS_HIDDEN).order_by('created_at') #new

    if request.method == 'POST':
         comment_form = CreateCommentForm(request.POST)
         if comment_form.is_valid():
             comment = comment_form.save(commit=False)
             comment.post = evenement
             comment.save()

             args = [evenement.pk, 'Your comment has been posted!']
             return HttpResponseRedirect(reverse('post-detail-message', args=args) + '#comments')
         else:
             comment_form = CreateCommentForm()

    return render(request, 'entreprise/evenement.html', {
        'evenement': evenement,
        'comments': comments,
        'comment_form': comment_form,
    })

#@login_required
def add_evenement(request):
    evenement_form = EvenementForm(request.POST)
    evenement = Evenement()
    cat = EvenementCategory.objects.all()

    if request.method == 'POST':
        evenement_form = EvenementForm(request.POST)
        if evenement_form.is_valid():
            evenement = evenement_form.save(commit=False)
            #offer.entreprise = request.entreprise
            evenement.hunter_user = request.user
            evenement.save()
            return redirect('entreprise-home')

    else:
        evenement_form = EvenementForm()
    return render(request, 'entreprise/add_evenement.html', {
        'evenement_form': evenement_form,
        'cat': cat
    })

#@login_required
def modifEvents(request, id):
    event = get_object_or_404(Evenement, id=id)
    form = EvenementForm(request.POST or None, instance=event)
    if form.is_valid():
         form.save()

         #return redirect(request, 'entreprise/entreprise_home.html', {'evenements': event})
         return redirect('entreprise-home')

    return render(request, 'entreprise/modif_events.html', {'form': form})

########Invitation
#@login_required
def invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, pk=invitation_id)

    return render(request, 'entreprise/invitation.html', {
        'invitation': invitation
    })


#@login_required
def add_invitation(request):
    invitation_form = InvitationForm(request.POST)
    invitation=Invitation()

    if request.method == 'POST':
        invitation_form = InvitationForm(request.POST)
        if invitation_form.is_valid():
            invitation = invitation_form.save(commit=False)
            invitation.hunter_user = request.user
            invitation.save()
            return redirect('/entreprise/invitation/' + str(invitation.id))
    else:
        invitation_form = InvitationForm()
    return render(request, 'entreprise/add_invitation.html', {
        'invitation_form': invitation_form
    })


##############send email
# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                #send_mail(subject, message, from_email, ['guymonthe2003@gmail.com'])
                #send_mail(subject, message, from_email, ['guymonthe2003@gmail.com'])
                 send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.add_message(request, messages.SUCCESS, 'Votre Invitation a été envoyer')
            #return redirect('success')
    return render(request, "email.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')






#######################################   Postule a une offre
def postule(request):
    postule_form = PostuleForm(request.POST)
    postule=Postule()

    if request.method == 'POST':
        postule_form = PostuleForm(request.POST)
        if postule_form.is_valid():
            postule = postule_form.save(commit=False)
            postule.hunter_user = request.user
            postule.save()
            return redirect('home')
    else:
        postule_form = PostuleForm()
    return render(request, 'entreprise/postule.html', {
        'postule_form': postule_form
    })

###################################################################################################################################


def evenement_list(request):
    evenements = Evenement.objects.all()



    context = {

        'evenements': evenements
    }

    return render(request, 'entreprise/evenement_list.html', context )







def evenement_detail(request, evenement_id):
    evenement = get_object_or_404(Evenement, pk=evenement_id)

    comments = evenement.comments.exclude(status=Comment.STATUS_HIDDEN)  # new

    if request.method== 'POST':
        comment_form = CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.evenement = evenement
            comment.save()
    else:
        comment_form = CreateCommentForm






    context = {

        'evenement':evenement,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'entreprise/evenement_detail.html', context  )


############################################################################################################################################################################
################################ gestion des offres
def offer_list(request):

    offers = Offer.objects.all()


    context = {
        'offers': offers
    }

    return render(request, 'entreprise/offer_list.html', context )



def offer_detail(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    test = Offer.objects.all()

    postules = offer.postules.exclude(status=Postule.STATUS_HIDDEN)  # new

    if request.method== 'POST':
        postule_form = PostuleForm(request.POST)
        if postule_form.is_valid():
            postule=postule_form.save(commit=False)
            postule.offer = offer
            postule.save()
            messages.add_message(request, messages.SUCCESS, 'Votre CV a été envoyé avec succès')

    else:
        postule_form = PostuleForm
        #messages.error(request, 'Votre Cv n a pas été soumis')





    context = {
        'offer':offer,
        'test':test,
        'postules': postules,
        'postule_form': postule_form
    }
    #return render(request, offer_id, context  )
    return render(request, 'entreprise/offer_detail.html', context  )

