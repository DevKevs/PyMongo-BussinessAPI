def bussinesModel(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "typeOf": item["typeOf"],
        "photo": item["photo"],
        "address": item["address"],
        "lat": item["lat"],
        "lgn": item["lgn"]
    }
def bussinesModel_list(entity) -> list:
   return [bussinesModel(item) for item in entity]
    