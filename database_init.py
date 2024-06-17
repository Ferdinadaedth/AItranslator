import mysql.connector
import configparser

class MySQLConnector:
    def __init__(self, config_file):
        self.host, self.database, self.user, self.password = self.read_database_config(config_file)
        self.connection = self.connect_mysql()

    def read_database_config(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        host = config.get('mysql', 'host')
        database = config.get('mysql', 'database')
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'password')
        return host, database, user, password

    def connect_mysql(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print('Connected to MySQL database')
                return connection
        except mysql.connector.Error as error:
            print(f"Failed to connect to MySQL database: {error}")
            return None


mysql_config = "database.ini"
mysql_connector = MySQLConnector(mysql_config)
connection = mysql_connector.connection
