from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose
import re

class QuoteItem(Item):
    text = Field()
    tags = Field()
    author = Field()
    test = Field()

def not_found_result(value):
    if value == None:
        return "No especificado"
    else:
        return value.strip()

def default_value_if_empty(value, default="-"):
    return value if value else default

def price_process(p):
    text = p.strip().lower()
    if text == "consulte":
        return None
    else:
        patron = r'(\d[\d,.]*)'
        text = text.replace(".", "")
        text = re.search(patron, text)
        if text:
            text = text.group(1)
            text = text.replace(",", ".")
            return text  

def codigo_process(c):
    text = c.strip()
    text = text.split("-")[1].strip()
    return text
    
       



class Caracteristicas(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
