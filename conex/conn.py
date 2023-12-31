import mysql.connector

class Conex:

    def __init__(self,  host, user="Diego", passwd="!gklTjM3zU_E5XjM", database="mydb"):
        try:
            self.__myconn = mysql.connector.connect(host=host, \
                                             user=user, \
                                             passwd=passwd, \
                                             database=database)

        except Exception as ex:
            print(ex)
            self.__myconn.rollback()
            return None

    def closeConex(self):
        self.__myconn.close()

    def getConex(self):
        return self.__myconn
    