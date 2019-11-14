#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import ConfigParser
def _get(inifile, section, name): 
    return inifile.get(section, name) 
class SQL_CONF():
    def __init__(self):
        read_inifile = ConfigParser.SafeConfigParser()
        read_inifile.read("../AWS_conf.ini")
        self.db_type = _get(inifile = read_inifile, section="SERVER_CONFIG", name="RDS_TYPE")
        self.server = _get(inifile = read_inifile, section="SERVER_CONFIG", name="RDS_endpoint")
        self.database = _get(inifile = read_inifile, section="SERVER_CONFIG", name="RDS_database_name")
        self.username = _get(inifile = read_inifile, section="SERVER_CONFIG", name="RDS_access_username")
        self.password = _get(inifile = read_inifile, section="SERVER_CONFIG", name="RDS_access_password")
    def db_connection(self):    
        server = self.server
        database =  self.database
        username =  self.username
        password = self.password
        sv=server
        db=database
        un=username
        pw=password
        if self.db_type == "mysql":
            # require mysql-connector-python 
            # pip install mysql-connector-python
            import mysql.connector
            cnxn = mysql.connector.connect(user=un, password=pw, host=server, database=db)
        elif self.db_type == "sqlserver":
            #require odbc driver 
            # you need install SQLSERVER odbc driver
            import pyodbc
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+sv+';DATABASE='+db+';UID='+un+';PWD='+ pw)
        return cnxn