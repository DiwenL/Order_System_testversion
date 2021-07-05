import pymysql

class DBConnector:

    def __init__(self,u,passwd,h = 'localhost',p = 3306):
        self.connection = pymysql.connect(
            host = h,
            port = p,
            user = u,
            password = passwd,
            charset = 'utf8'
            )

        self.cursor = self.connection.cursor()
        self.cursor.execute("use cupar_hotel")
        return

    def close_cursor(self):
        self.cursor.close()
        return

    def commit(self):
        self.connection.commit()
        return

    def disconnect(self):
        self.connection.close()
        return

    def close(self):
        closeCursor(self)
        disconnect(self)
        return
        
    def show_table(self,tableName):
        self.cursor.execute("Select * from "+tableName)
        for line in self.cursor:
            print(line)
        return

    def add_product(self,tableName,productInfo):
        '''
        product infor in the form of
        (name,kind,size,int)
        where
        name(string), size(bottle or can), size(int), price(int)
        '''
        
        sql = 'insert into beer(beername,kind,size,price) values(%s,%s,%s,%s)'
        self.cursor.execute(sql,productInfo)
        self.connection.commit()
        return

    def search_product(self,productName,containerKind = "",size = ""):
        result = []
        if containerKind != "" and size != "":
            self.cursor.execute("select * from beer where beername = %s and kind = %s and size = %s",(productName,containerKind,size))
            for product in self.cursor:
                result.append(product)
            return result
        elif containerKind != "" and size == "":
            self.cursor.execute("select * from beer where beername = %s and kind = %s",(productName,containerKind))
            for product in self.cursor:
                result.append(product)
            return result
        elif containerKind == "" and size != "":
            self.cursor.execute("select * from beer where beername = %s and size = %s",(productName,size))
            for product in self.cursor:
                result.append(product)
            return result
        elif containerKind == "" and size == "":
            self.cursor.execute("select * from beer where beername = %s",productName)
            for product in self.cursor:
                result.append(product)
            return result
