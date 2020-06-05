# ############################################################################### #
# Autoreduction Repository : https://github.com/ISISScientificComputing/autoreduce
#
# Copyright &copy; 2020 ISIS Rutherford Appleton Laboratory UKRI
# SPDX - License - Identifier: GPL-3.0-or-later
# ############################################################################### #
"""
Database Constructor
"""

import mysql.connector


class DatabaseCredentials:
    """Database credentials"""
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""  # need to fill this if root password set locally
        self.database = "system_monitoring"


class DatabaseConnection:
    """Database connection"""
    @staticmethod
    def initial_connection(host_name, user_name, user_password):
        """create connection"""
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Connection to MySQL DB successful")
        except ConnectionError as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def create_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except ConnectionError as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except ConnectionError as e:
            print(f"The error '{e}' occurred")


class CreateDatabase:
    """Database constructor"""
    @staticmethod
    def create_database(connection, query):
        """create database"""
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except ConnectionError as e:
            print(f"The error '{e}' occurred")


class ConstructDatabaseSchema:
    """Construct database and tables"""
    def __init__(self):
        self.instrument_table = "CREATE TABLE IF NOT EXISTS instrument (" \
                                "id int(10) NOT NULL auto_increment, " \
                                "instrument_name VARCHAR(255), " \
                                "PRIMARY KEY(id))"

        self.dates_table = "CREATE TABLE IF NOT EXISTS dates (" \
                           "id int(10) NOT NULL auto_increment, " \
                           "date datetime, " \
                           "PRIMARY KEY(`id`));"

        self.statistics_counts_table = "CREATE TABLE IF NOT EXISTS `system_monitoring` (" \
                                       "id int(10) NOT NULL auto_increment, " \
                                       "total_jobs numeric(9,2), " \
                                       "passed_jobs numeric(9,2), " \
                                       "failed_jobs numeric(9,2), " \
                                       "total_runs numeric(9,2), " \
                                       "passed_runs numeric(9,2), " \
                                       "failed_runs numeric(9,2), " \
                                       "average_execution_time datetime, " \
                                       "started_by_ar numeric(9,2), " \
                                       "started_by_dev numeric(9,2), " \
                                       "started_by_user numeric(9,2), " \
                                       "resolved_runs numeric(9,2), " \
                                       "instrument_id int(10), " \
                                       "date_id int(10), " \
                                       "PRIMARY KEY(id), " \
                                       "FOREIGN KEY(instrument_id) REFERENCES  instrument(id), " \
                                       "FOREIGN KEY(date_id) REFERENCES  dates(id));"

    @staticmethod
    def construct_database():
        """constructs DB"""
        connection = DatabaseConnection().initial_connection(DatabaseCredentials().host,
                                                             DatabaseCredentials().user,
                                                             DatabaseCredentials().password)
        create_database_query = f"CREATE DATABASE {DatabaseCredentials().database}"
        CreateDatabase().create_database(connection, create_database_query)

    def construct_tables(self):
        """constructs db tables"""
        connection = DatabaseConnection().create_connection(DatabaseCredentials().host,
                                                            DatabaseCredentials().user,
                                                            DatabaseCredentials().password,
                                                            DatabaseCredentials().database)
        list_of_tables = [x for x in list(
            ConstructDatabaseSchema().__dict__.keys()) if 'table' in x]
        for table in list_of_tables:
            DatabaseConnection().execute_query(connection, self.__getattribute__(table))


ConstructDatabaseSchema().construct_database()
ConstructDatabaseSchema().construct_tables()
