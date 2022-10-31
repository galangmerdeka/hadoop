
import pandas as pd
# import psycopg2 as pg
import sqlalchemy

path_tr_products = 'dataset/TR_Products.csv'
path_tr_userinfo = 'dataset/TR_UserInfo.csv'
user='root'
password='root'
host='localhost'
port='5432'
database='postgres'
table_name_prod = 'tr_products'
table_name_user = 'tr_userinfo'

data_products = pd.read_csv(path_tr_products)
data_user = pd.read_csv(path_tr_userinfo)

# rename column tr product
col_prod = {"ProductID": "prod_id","ProductName": "prod_name","ProductCategory": "prod_category", "Price": "price"}
data_products = data_products.rename(columns=col_prod)

# rename column tr userinfo
col_usr = {"UserID":"user_id", "UserSex": "user_sex", "UserDevice": "user_device"}
data_user = data_user.rename(columns=col_usr)

# connect to postgres
# engine = engine_sql(f'postgresql://{user}:{password}@{host}:{port}/{database}')
conn = sqlalchemy.create_engine(url='postgresql://root:root@localhost:5432/postgres')

# insert into postgres
data_products.to_sql(table_name_prod, con=conn, index=False, if_exists='replace')
data_user.to_sql(table_name_user, con=conn, index=False, if_exists='replace')