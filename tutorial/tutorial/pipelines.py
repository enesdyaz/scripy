from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, XmlItemExporter, JsonItemExporter

class CsvPipeline(object):
    def __init__(self):
        self.file = open("assets/movies.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class JsonPipeline(object):
    def __init__(self):
        self.file = open("assets/movies.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class XmlPipeline(object):
    def __init__(self):
        self.file = open("assets/movies.xml", 'wb')
        self.exporter = XmlItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item