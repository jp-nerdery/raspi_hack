# -*- coding: utf-8 -*-

import psycopg2
import mysql.connector
import base64
import codecs
from datetime import datetime
 
import pandas as pd
import numpy as np
import pandas as psql

from  jerp_src.db import sql_db_config 



class My_pg_Access():
    def connect():
        ''' Connection Method 
            provide postgreSQL Only
            SQL_CONFIG Class is define SQL Connection Setting of server enviroment value or specify installed postgreSQL DB param
        '''
        db_flg =0
        conn =None
        h,pt ,dn, u, ps ,_= sql_db_config.SQL_CONFIG.configs()
        
        if db_flg ==0:
            conn = mysql.connector.connect(user=u, password=ps, host=h, database=dn)
        else:
            conn = psycopg2.connect(host= h,port=pt ,dbname=dn, user=u, password=ps)
        cur = conn.cursor()
        print('Connect Success')
        return conn,cur
    def select_data(SQL_COM,dataparam=None):
        ''' SELECT DB TABLE 
        '''
        conn ,_ = My_pg_Access.connect()
        if dataparam is None:
            sql_data = psql.read_sql(SQL_COM, conn) 
            print('SELECT Success')
            conn.close
            columns_name = [(item,item) if isinstance(item,str) else (item,item.decode("utf-8")) for item in sql_data.columns.values]
            sql_data = sql_data.rename(columns=dict(columns_name)) 
            return sql_data
        else:
            sql_data = psql.read_sql(SQL_COM, conn,params=dataparam)
            print('SELECT Success')
            conn.close
            columns_name = [(item,item) if isinstance(item,str) else (item,item.decode("utf-8")) for item in sql_data.columns.values]
            sql_data = sql_data.rename(columns=dict(columns_name))
            return sql_data
        
    def insert_data(table_name,dataparam):
        ''' INSERT DB table data 
            table_name = Specify DataBase Table Name
            dataparam = Specify column names and data of SQL syntax Insert statement in dictionary format
        '''
        conn ,cur = My_pg_Access.connect()
        
       

        SQL_COM = ''
        SQL_COM = 'INSERT INTO ' + table_name
        SQL_COM += ' ( '
              
        for i,(key, val) in enumerate(dataparam.items()):
            if len(dataparam.items()) != i +1 :
                SQL_COM += key + ','
            else:
                SQL_COM += key 
        SQL_COM += ' ) VALUES( '
        for i,(key, val) in enumerate(dataparam.items()):
            if len(dataparam.items()) !=  i +1 :
                SQL_COM += '%(' + key + ')s' + ','
            else:
                SQL_COM += '%(' + key + ')s'
        SQL_COM += ')'
        cur.execute(SQL_COM,dataparam)
        conn.commit()
        conn.close
        print('INSERT Success')
    def update_data(table_name,dataparam,whereparam =None):
        ''' UPDATE DB table data
            table_name = Specify DataBase Table Name
            dataparam  = Specify column names and data of SQL syntax Update statement in dictionary format
            whereparam = Specify column names and data in the WHERE section of the Update statement of SQL syntax in dictionary format
        '''
        conn ,cur = My_pg_Access.connect()
         
        _,_,_, _, _,scm = sql_db_config.SQL_CONFIG.configs()

        SQL_COM = ''
        SQL_COM = 'UPDATE ' + table_name
        SQL_COM += ' SET '
        for i,(key, val) in enumerate(dataparam.items()):
            if len(dataparam.items()) !=  i +1 :
                SQL_COM +=  key  + '=' + '%(' + key + ')s' + ','
            else:
                SQL_COM +=  key  + '=' + '%(' + key + ')s'
        if whereparam is not None:
            SQL_COM += ' WHERE  '
            for i,(key, val) in enumerate(whereparam.items()):
                if len(whereparam.items()) !=  i +1 :
                    SQL_COM +=  key  + '=' + '%(' + key + ')s' + ' AND '
                else:
                    SQL_COM +=  key  + '=' + '%(' + key + ')s'
            dataparam.update(whereparam)
        cur.execute(SQL_COM,dataparam)
        conn.commit()
        conn.close
        print('UPDATE Success')
    def delete_data(table_name,dataparam):
        ''' DELETE DB table data
            dataparam = SQL Define WHERE param
        '''
        conn ,cur = My_pg_Access.connect()
         
        _,_,_, _, _,scm = sql_db_config.SQL_CONFIG.configs()

        SQL_COM = ''
        SQL_COM = 'DELETE FROM ' + table_name
        SQL_COM += ' WHERE  '
        for i,(key, val) in enumerate(dataparam.items()):
            if len(dataparam.items()) !=  i +1 :
                SQL_COM +=  key  + '=' + '%(' + key + ')s' + ' AND '
            else:
                SQL_COM +=  key  + '=' + '%(' + key + ')s'
        SQL_COM += ''
        cur.execute(SQL_COM,dataparam)
        conn.commit()
        conn.close
        print('DELETE Success')
    def truncate_data(table_name):
        '''
        You can truncate DB Table in using this method to easily. 
        '''
        conn ,cur = My_pg_Access.connect()
         
        _,_,_, _, _,scm = sql_db_config.SQL_CONFIG.configs()

        SQL_COM = ''
        SQL_COM = 'TRUNCATE TABLE ' + scm + '.' + table_name
             
        cur.execute(SQL_COM)
        conn.commit()
        conn.close
        print('TRUNCATE Success')