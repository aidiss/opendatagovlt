# coding: utf-8

import colander
import datetime

class Resource(colander.MappingSchema):
    code = colander.SchemaNode(colander.Int(), validator=colander.Range(0, 1000))
    name = colander.SchemaNode(colander.String())
    alt_name = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())
    keywords = colander.SchemaNode(colander.SequenceSchema) # limited choice?
    tvarkytojas = colander.SchemaNode(colander.String())
    contacts = colander.SchemaNode(colander.SequenceSchema)
    data_type = colander.SchemaNode(colander.String()) 
    data_format = colander.SchemaNode(colander.String())
    start_of_rinkmena = colander.SchemaNode(colander.Date()) # datetime ?
    end_of_rinkmena = colander.SchemaNode(colander.Date()) # datetime ?
    update_frequency = colander.SchemaNode(colander.String()) # limited choice?
    internet_address = colander.SchemaNode(colander.String()) # validator=colander.url ? does not work 
    teikimo_salygos = colander.SchemaNode(colander.String())
    data_reliability = colander.SchemaNode(colander.String()) # limited choice?
    data_depth = colander.SchemaNode(colander.String()) # limited choice?
    rinkmenos_aprasymo_publikavimo_duomenys = colander.SchemaNode(colander.String())
