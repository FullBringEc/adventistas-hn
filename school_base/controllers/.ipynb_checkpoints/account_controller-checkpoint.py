# -*- coding: utf-8 -*-

from odoo import http
from . import base_controller as base

import json
from datetime import datetime
from datetime import date


#controlador encargado de devolver data de estudiantes, para insertarlo en FACTS
class StudentController(http.Controller):
    
    #definiendo la url desde donde va ser posible acceder, tipo de metodo, cors para habiltiar accesos a ip externas.
    @http.route("/account/dataAccount", auth="public", methods=["GET"], cors='*')
    # define una funcion principal
    def get_adm_uni(self, **params): 
        #crea una variable con el modelo desde donde se va a tomar la información 
        # adm_uni.application
        # status_type
        students = http.request.env['adm_uni.application']        
        
        #filtro del modelo basados en parametros de la url 
        search_domain = [("status_type","=","stage")]
        #search_domain = [("status_type","=","fact_integration")] #,("country_id", "=", int(params['country_id']))] if "country_id" in params else []
        #search_domain = [("status_type","=","fact_integration"),("country_id", "=", int(params['country_id']))] 
        
        #Tomar informacion basado en el modelo y en el domain IDS
        students_record = students.search(search_domain)      
        
        #Obtienes la información basada en los ids anteriores y tomando en cuenta los campos definifos en la funcion posterior
        students_values = students_record.read(["id","city","country_id","state_id", "street_address","zip","first_name","middle_name","last_name","name","email", "birthdate","gender","phone", "status_id","status_type","current_school","current_school_address","create_date","create_uid","write_date","write_uid"])

        # Se recorre por cada estudiante
        for record in students_values: 
            # Convertir fechas a string
            if record["birthdate"]:
                record["birthdate"] = record["birthdate"].strftime('%m/%d/%Y')
            else:
                record["birthdate"] = '' 
            # Es lo mismo que:
            # date_of_birth = record["birthdate"]
            # date_of_birth = date_of_birth.strftime('%m/%d/%Y')
            # record["birthdate"] = date_of_birth 
            
            if record["create_date"]:
                record["create_date"] = record["create_date"].strftime('%m/%d/%Y')
            else:
                record["create_date"] = ''                
            
            if record["write_date"]:
                record["write_date"] = record["write_date"].strftime('%m/%d/%Y')
            else:
                record["write_date"] = ''
                
            # record["__last_update"] = record["__last_update"].strftime('%m/%d/%Y')
            # record["create_date"] = record["create_date"].strftime('%m/%d/%Y')
            # record["write_date"] = record["write_date"].strftime('%m/%d/%Y')   
            
            #crea una variable con el modelo desde donde se va a tomar la información
            attachments = http.request.env['ir.attachment']        
        
            #filtro del modelo basados en parametros de la url
            search_domain_attach = [("res_model", "=", "adm_uni.application"),("res_id","=",record["id"])]
        
            #Tomar informacion basado en el modelo y en el domain IDS
            attachments_record = attachments.search(search_domain_attach)      
        
            #Obtienes la información basada en los ids anteriores y tomando en cuenta los campos definifos en la funcion posterior
            attachments_values = attachments_record.read(["id","name"])    
            record["attachIds"] = json.dumps(attachments_values)
            
        #students_values.append("test")
        #pintar la información obtenida, esto lo utilizamos para parsearlo en el ajax.         
        return json.dumps(students_values)

    #definiendo la url desde donde va ser posible acceder, tipo de metodo, cors para habiltiar accesos a ip externas.
    @http.route("/account/adm_insertId", auth="public", methods=["POST"], cors='*', csrf=False)
    # define una funcion principal 
    def insertId(self, **kw):  
        data = json.loads(kw["data"])
        for itemData in data: 
            #itemData["odooId"]
            #itemData["factsId"]
            application = http.request.env['adm_uni.application']
          
            search_domain = [("id","=",itemData["odooId"])]
            
            #Tomar informacion basado en el modelo y en el domain IDS
            application_record = application.search(search_domain)      
        
            #Obtienes la información basada en los ids anteriores y tomando en cuenta los campos definifos en la funcion posterior
            application_values = application_record.partner_id
        
            application_values.sudo().write({'x_facts_id': itemData["factsId"]})
            #tomamos el modelo de application
            #application = http.request.env['adm_uni.application']        
            #obtenemos el contacto de odoo
            #contact = http.request.env['res.partner'] 
            #obj = contact.sudo().browse(application_values[0]["id"])
            #actualizamos campo
            #obj.sudo().write({'x_facts_id': itemData["factsId"]}) 
        
        return json.dumps(data)
    
    
    #definiendo la url desde donde va ser posible acceder, tipo de metodo, cors para habiltiar accesos a ip externas.
    @http.route("/account/getDataOdooFromFamilyID", auth="public", methods=["POST"], cors='*', csrf=False)
    # define una funcion principal 
    def insertId(self, **kw):  
        data = json.loads(kw["data"])
        
        students = http.request.env['account.move']        
        
        #filtro del modelo basados en parametros de la url 
        search_domain = [("partner_id","=",data["id"])]
        #search_domain = [("status_type","=","fact_integration")] #,("country_id", "=", int(params['country_id']))] if "country_id" in params else []
        #search_domain = [("status_type","=","fact_integration"),("country_id", "=", int(params['country_id']))] 
        
        #Tomar informacion basado en el modelo y en el domain IDS
        students_record = students.search(search_domain)      
        
        #Obtienes la información basada en los ids anteriores y tomando en cuenta los campos definifos en la funcion posterior
        students_values = students_record.read(["access_token","amount_total","invoice_date"])
        
        
        return json.dumps(students_values)