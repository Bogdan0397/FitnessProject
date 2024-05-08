



menu = [{'title': "About", 'url_name': 'about',
        'subcategories':[{'title':'Our Team','url_name':'our_team'},{'title':'Contact','url_name':'contact'}]},
        {'title':"Life Style",'url_name':'lifestyle_home','subcategories':[{'title':'Food Plan’s ','url_name':'foodplans_home'}]}]

def get_context_menu(request):
    return {'mainmenu':menu}