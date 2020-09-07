# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose,TakeFirst
from w3lib.html import replace_escape_chars, remove_tags,replace_entities




class SFitnessItem(scrapy.Item):
    
    title=scrapy.Field(
        input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars),

        )
    link= scrapy.Field(
          input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars),

          )
    price = scrapy.Field(
          input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars,remove_tags)
            )
    not_in_stock = scrapy.Field(
          input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars,remove_tags)
            )
    in_stock = scrapy.Field(
          input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars,remove_tags)
            )
    estimated_date_available = scrapy.Field(
          input_processor=MapCompose(lambda v: v.strip(), replace_escape_chars,remove_tags)
            )
    
    