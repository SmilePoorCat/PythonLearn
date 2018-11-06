# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MystockspiderPipeline(object):
    def process_item(self, item, spider):
        return item


# 处理spider返回的item对象
class StockSavingPipeline(object):

    # 初始化方法
    def __init__(self):
        print("\n" * 5, "StockSavingPipeline __init__")

    # 处理spider返回的item对象
    # item = 爬虫提交过来的数据模型
    # spider = 提交item的爬虫实例
    def process_item(self, item, spider):
        print("\n" * 5, "StockSavingPipeline process_item")

        # 提取数据
        data = item['data']
        file_name = "./files/" + item['name'] + ".csv"

        # 向文件中写入数据
        with open(file_name, "a") as file:
            file.write(data)

        # 如果有多个pipeline，继续向下一个pipeline传递
        # 不返回则传递终止
        # 这里主要体现一个分工、分批处理的思想
        return item

    # 对象被销毁时调用
    def __del__(self):
        print("\n" * 5, "StockSavingPipeline __del__")
