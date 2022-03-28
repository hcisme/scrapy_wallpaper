# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class LinkerPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='81.68.248.232',
            port=3306,
            user='rooter',
            password='emmmm000',
            db='spider',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into imgs(img_src, data_src) values("{}","{}")'.format(item['src'], item['data_src'])
        # 执行
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('读写完毕')
