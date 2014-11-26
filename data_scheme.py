# coding: utf-8

import colander
import datetime

class Resource(colander.MappingSchema):
    code = colander.SchemaNode(colander.Int(), validator=colander.Range(0, 1000))
    name = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=20))
    alt_name = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=20))
    description = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=500))
    keywords = colander.SchemaNode(colander.Sequence(), validator=colander.Length(min=5, max=20))
    tvarkytojas = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=20))
    contacts = colander.SchemaNode(colander.Sequence(), validator=colander.Length(min=5, max=20))
    data_type = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=20))
    data_format = colander.SchemaNode(colander.String(), validator=colander.Length(min=5, max=20))
    start_of_rinkmena = colander.SchemaNode(colander.Date())  # datetime and string are other choice.
    end_of_rinkmena = colander.SchemaNode(colander.Date())  # datetime and string are other choice.
    update_frequency = colander.SchemaNode(colander.Tuple())  # tuple (times, per_time_unit
    internet_address = colander.SchemaNode(colander.String())  # validator=colander.url ? does not work
    teikimo_salygos = colander.SchemaNode(colander.String())
    data_reliability = colander.SchemaNode(colander.Int(), validator=colander.Range(0, 5))
    data_depth = colander.SchemaNode(colander.String(), validator=colander.Range(0, 5))
    rinkmenos_aprasymo_publikavimo_duomenys = colander.SchemaNode(colander.String())
