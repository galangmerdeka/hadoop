from mrjob.job import MRJob
from mrjob.step import MRStep
import psycopg2

class AggregateOrderDetails(MRJob):
    def mapper_init(self):
        # make postgre database available to mapper
        self.conn = psycopg2.connect(database='postgres', user="root", password="root", host="localhost", port="5432")

    def mapper(self, _, line):
        item = line.strip().split(',')
        date = item[1][-4:]
        
        yield date, int(item[4])

    def reducer(self, key, values):
        yield key, sum(values) 

    def store(self, key, values):
        self.cur = self.conn.cursor()
        self.cur.execute("insert into total_order_yearly(year, total) values(%s,%s)", (key, values))

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init,
                    mapper=self.mapper,
                    reducer=self.reducer),
            MRStep(reducer=self.store)
        ]

    def mapper_final(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    AggregateOrderDetails.run()