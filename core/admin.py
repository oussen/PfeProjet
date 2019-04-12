from django.contrib import admin

from .models import Entreprise, Offer, Employe, Evenement, Invitation, Joindre, Comment, Participant, EvenementCategory, OfferCategory, Postule
# Register your models here.

from . import models


admin.site.register(Entreprise)
admin.site.register(Offer)
admin.site.register(Employe)
admin.site.register(OfferCategory)
admin.site.register(Invitation)
admin.site.register(Joindre)
admin.site.register(Participant)
admin.site.register(EvenementCategory)
admin.site.register(Postule)




class CommentInline(admin.StackedInline):
    model = models.Comment

class EvenementAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
    ]

admin.site.register(Evenement, EvenementAdmin)
admin.site.register(Comment)