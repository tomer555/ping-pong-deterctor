import pymongo

class PingPongRepository():

    # declare constants 
    CONNECTION_STRING = 'mongodb+srv://sagicoh:e2ulqeFy2iHycuRD@room-monitor.cwpjbul.mongodb.net/?retryWrites=true&w=majority'
    DB_NAME = 'monitors'
    COLLECTION_NAME = 'ping-pong'

    def __init__(self) -> None:
        self.client = pymongo.MongoClient(self.CONNECTION_STRING)
        self.db = self.client[self.DB_NAME]
        self.collection = self.db[self.COLLECTION_NAME]


    def insert (self, time, status):
        monitor = {'statusTime':time, 'status': status}
        self.collection.insert_one(monitor)

    def getAfter (self, time):
        return list(self.collection.find(
            {
                'statusTime': {
                    '$gte': time,
                }
            }
        ))

    def getAll (self):
        return list(self.collection.find({}))


repo = PingPongRepository()

