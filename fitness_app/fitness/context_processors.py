



menu = [{'title': "About", 'url_name': 'about', 'subcategories':[{'title':'Our Team','url_name':'our_team'},{'title':'Contact','url_name':'contact'}]}]

def get_context_menu(request):
    return {'mainmenu':menu}