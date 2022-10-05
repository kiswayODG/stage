from odoo import fields, models


class Responsable(models.Model):
    _name="stage.responsable"
    nom=fields.Char("Nom du personnel", required=True)
    prenom=fields.Char("Prenom du personnel", required=True)
    departement=fields.Char("Département", required=True)
    telephone=fields.Integer("Numéro de telephone", required=True)



    
    
