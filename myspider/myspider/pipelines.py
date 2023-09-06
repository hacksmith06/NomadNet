# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class H3TagPipeline(object):
    def process_item(self, item, spider):
        # For demonstration purposes, we're just printing the content
        print(item['content'])
        return item
