
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
    path('accounts/', include('django.contrib.auth.urls')),


    #######Entreprie function

    path('accounts/login', auth_views.LoginView, name='entreprise-login'),
    path('entreprise/e_signup', views.entreprise_signup, name='entreprise-signup'),
    path('entreprise/', views.entreprise_home, name='entreprise-home'),


    ######### Add offer
    path('entreprise/offer/<int:offer_id>/', views.offer, name='offer'),
    path('entreprise/offer/add', views.add_offer, name='add_offer'),
    path('entreprise/offer/<int:id>/modif', views.modifOffre, name='modif_offre'),

    ###### employee representant entreprise

    path('entreprise/employe/<int:employe_id>/', views.employe, name='employe'),
    path('entreprise/employe/add', views.add_employe, name='add_employe'),

    ######Evenement
    path('entreprise/evenement/<int:evenement_id>/', views.evenement, name='evenement'),
    path('entreprise/evenement/<int:evenement_id>/<str:message>/', views.evenement, name='post-detail-message'), #new



##############################new############################################## le bon commentaire et affichage

    path('entreprise/evenement/', views.evenement_list, name='evenement_list'),
    path('entreprise/evenement/detail/<int:evenement_id>', views.evenement_detail, name='evenement_detail'),

########################################################offre d emploi gestion#############################################

    ######### Add offer

    path('pecos/', views.offer_list, name='offer_list'),
    path('pecos/detail/<int:offer_id>', views.offer_detail, name='offer_detail'),
    #path('<int:offer_id>', views.offer_detail, name='offer_detail'),






##########################################################################################################################
    path('entreprise/evenement/add', views.add_evenement, name='add_evenement'),
    path('entreprise/evenement/<int:id>/modif', views.modifEvents, name='modif_evenement'),
    path('entrepriseDetail/', views.detailEntr, name='detailEntr'),

    ######inviter a un evenement
    path('entreprise/invitation/<int:invitation_id>/', views.invitation, name='invitation'),
    path('entreprise/invitation/add', views.add_invitation, name='add_invitation'),


    #####send email



    path('email/', views.emailView, name='email'),
    # path('success/', views.successView, name='success'),



    ##################### postule a une offre


    path('entreprise/postule', views.postule, name='postule'),

    ]
