class Engine:
    """docstring for particular_bot"""
    bots = []

    def __init__(self, arg):
        self.arg = arg

    def start_bot(self, bot):
        self.bots.append(bot)

    def stop_bot(self, bot):
        self.bots.bot.stop()


#####

class Inside_bot:
    """Bot for getting and mangling data"""
    is_inside_bot = True
    is_outside_bot = False
    url = ''

    def __init__(self, *bots):
        self.arg = arg
    def stop(self):
        pass

class Outside_bot:
    """Bot that checks shallow info"""
    is_inside_bot = False
    is_outside_bot = True
    url = ''

    def __init__(self, *bots):
        self.arg = arg

    def stop(self):
        pass

#####

class Csv_bot:
    "Bot for gathering from CSV."
    def __init__(self, arg):
        # CIA TIK PAVYZDIUI, TURBUT SIUOS DUOMENIS GERIAUSIA PADUOTI PER KWARGS-ZODYNA
        self.adresas = "http://www.lakd.lt/files/atviri_duomenys/vmpei.csv"
        self.formatas = "csv"
        self.skyriklis = ";"
        self.atnaujinimo_dažnumas = "1 kartas per dieną"
        self.atnaujinimo_strategija = "skaityti visą failą, susiejant duomenis per pirminį raktą"
        self.laukai_pagaldtcube = {
            "Kelio Nr.": "išorinis raktas į kelio objektą, pirminis raktas",
            "Pradzia km": "lauko tipas km",
            "Pabaiga km": "lauko tipas km",
            "Eismo intensyvumas": "agreguotas kiekis (automobilių skaičius per dieną)",
            "Metai": "lauko tipas metai"}

class Xml_bot:
    """dBot for gathering from CSV"""
    def __init__(self, arg):
        super(Xml_bot, self).__init__()
        self.arg = arg

class Xls_bot:
    """Bot for gathering from XLS"""
    def __init__(self, arg):
        super(Xls_bot, self).__init__()
        self.arg = arg

class Html_table_bot:
    """Bot for gathering from HTML"""
    def __init__(self, arg):
        self.arg = arg

class Doc_table_bot:
    """Bot for gathering from Doc"""
    def __init__(self, arg):
        self.arg = arg
#####


opendatagov_engine = Engine('er')

some_csv_bot = Csv_bot(None)
some_xls_bot = Xls_bot(None)

bots = [some_csv_bot, some_xls_bot]

for bot in bots:
    opendatagov_engine.start_bot(bot)

print(opendatagov_engine.bots)
