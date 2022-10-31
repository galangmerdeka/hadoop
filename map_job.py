from mrjob.job import MRJob
import psycopg2

class FilterProduct(MRJob):
    def mapper_init(self):
        # make postgre database available to mapper
        self.conn = psycopg2.connect(database='postgres', user="root", password="root", host="localhost", port="5432")

    def mapper(self, _, line):
        self.cur = self.conn.cursor()
        item = line.strip().split(',')
        # yield _, type(int(item[3]))
        if int(item[3]) > 10:
            self.cur.execute("insert into products(product_id, product_name, product_category, price) values(%s,%s,%s,%s)", (item[0], item[1], item[2], item[3]))
            yield item[1], item[3]

    def mapper_final(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    FilterProduct.run()