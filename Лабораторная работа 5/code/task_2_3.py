from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")



class MongoManager:
    def __init__(self, client, user, pwd):
        self.client = client
        self.user = user
        self.pwd = pwd
        self.connection = None
    
    def __enter__(self):
        self.connection = MongoClient(
            self.client,
            username=self.user,
            password=self.pwd
            )

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

def main():
    mongo_context = MongoManager(
        client = "mongodb://localhost:27017/",
        user = "Admin",
        pwd = "Admin"
    )

    with mongo_context:
        users = mongo_context.connection['mongo-db']['user']

        found = users.find()

        print("Found all users:")
        for user in found:
            print(user)

        found = users.find({"name": "Ada Lovelace"})
        print("\nFound Ada Lovelace:")
        for user in found:
            print(user)

if __name__ == "__main__":
    main()