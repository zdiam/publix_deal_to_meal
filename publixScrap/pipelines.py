# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
from itemadapter import ItemAdapter


class PublixscrapPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect('publixScrap.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS publixScrap_tb""")
        self.curr.execute("""create table publixScrap_tb(
        food text,
        dealType text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into publixScrap_tb values (?,?)""",(
            item['food'][0],
            item['dealType'][0]
        ))

        self.conn.commit()