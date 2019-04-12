from core.models import Evenement, EvenementCategory

evenement_category_all = EvenementCategory(name='All')


def get_category_and_posts(category_name):
    evenements = Evenement.objects.filter(published=True)
    if category_name == evenement_category_all.slug():
        category = EvenementCategory(name=category_name)
    else:
        try:
            category = EvenementCategory.objects.get(name__iexact=category_name)
            evenements = evenements.filter(category=category)
        except EvenementCategory.DoesNotExist:
            category = EvenementCategory(name=category_name)
            posts = Evenement.objects.none()

    evenements = evenements.order_by('-created_at')
    return category, evenements


def get_categories():
    categories = list(EvenementCategory.objects.all().order_by('name'))
    categories.insert(0, evenement_category_all)
    return categories