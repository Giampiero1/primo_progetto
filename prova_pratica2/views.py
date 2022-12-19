from django.shortcuts import render

def views_a(request):
    auto=["AA123BB","AB345CD","CD456FF"]
    context = {'lista1':auto}
    return render (request, "lista_targhe.html", context)

def views_b(request):
    noleggi= {'AA123BB':[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
                  'AB345CD':[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
                  'CD456FF':[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}

    keys= noleggi.keys()
    context = {'lista2': noleggi, "chiavi": keys} 

    return render(request, "lista_noleggi.html", context)