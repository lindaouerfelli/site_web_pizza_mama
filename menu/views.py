from django.shortcuts import render #permet de chercher un template et faire le rendu
from django.http import HttpResponse
from .models import Pizza
# Create your views here.
# index est le nom de ma vue !

# faut dire que cette vue on peut l'accéder par  /menu ---> config d'URLS
# la vue est déclenché une fois que je tape un url /menu par exemple !
#  on dirait toutes mes pages web sont des vues chacune !     # Logique pour la page d'accueil      # Logique pour la liste des articles      # Logique pour la page de détail d'un article
#Une Vue pour Gérer Plusieurs Pages

def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.nom + " : " + str(pizza.prix) + "£" for pizza in pizzas]
    pizzas_names_and_price_str = ",".join(pizzas_names_and_price)
    return HttpResponse("Les pizzas : "+ pizzas_names_and_price_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas' : pizzas})
