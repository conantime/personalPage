import pymongo

class conn():
    client = None
    def __init__(self):
        self.client = pymongo.MongoClient('localhost',27017 )
    def get_list(self,m,l):
       db = self.client[m] # dynamic connect mongodb
       if l not in db.collection_names() :
          db.create_collection(l)
          col = db[l]  #dynamic connect collection
          return col
       else:
           col = db[l]
           return col


if __name__ == "__main__":
    conn = conn()

    col = conn.get_list(m="test",l="test").save({"uname":"paul@163.com"})


