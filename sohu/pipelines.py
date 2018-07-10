# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SohuPipeline(object):
    def process_item(self, item, spider):
        context=item["context"]
        for i in range(0,len(context)):
            fh = open("D:/file/python_learning/CH5/news/" + str(i) + ".txt","wb")
            #print(context[i])
            fh.write(context[i])
        return item
