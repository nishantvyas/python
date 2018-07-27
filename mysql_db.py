"""
Simple Program to test MySQL insert and select
"""

import pymysql.cursors

from configparser import ConfigParser

def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()

    try:

        conn = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)

        if conn.open:
            print('Connected to MySQL database')
        else:
            print('connection failed.')

        with conn.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        conn.commit()

        with conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()

            while result is not None:
                print(result)
                result = cursor.fetchone()

    finally:
        conn.close()


if __name__ == '__main__':
    connect()

