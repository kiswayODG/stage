{
    
'name':"stage",
'author':"nebrataTeam",
'description':"Module de test permettant d'obtenir les relations entre stagiaires et leur maitre de stage",

'depends': ['base'],
'application': True,
'data':['security/stage_security.xml',
        'security/ir.model.access.csv',
        'views/stage_view.xml', ],

}
