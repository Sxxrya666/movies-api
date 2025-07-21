from fastapi import FastAPI, Body
from uuid import uuid4, UUID


app = FastAPI()

#dummy in memory db
fake_items_db = [ ]


@app.get("/")
def home():
    return {"message": "Welcome to the Items API!"}

@app.get("/items") 
def get_items(offset: int = 0, limit: int = 10):
    return fake_items_db[offset: limit]

@app.post("/send-item")
def send_item(items=Body()):
    if "item_name" not in items:
        return {"message": "Invalid item name. Please try again loser", "status": "fail"}
    return fake_items_db.append({"id": str(uuid4()), "item_name": items['item_name']})

@app.put('/update-item')
def update_item(items=Body()):
    for i in range(len(fake_items_db)):
        if items['id'] == fake_items_db[i]['id']:
            fake_items_db[i] = items 
            return {
                "status": "success",
                "message": f"updated '{items["id"]}' id successfully!",
                "data": fake_items_db
            }
    return {
        "status": "fail",
        "message": "updation failed due to invalid id! please try again" 
    }

    
@app.delete('/delete-item/{item_id}')
def delete_item(item_id):
    for i in range(len(fake_items_db)):
        if item_id[i] in fake_items_db[i]["id"]:
            # fake_items_db.remove(item_id)
            fake_items_db.remove(fake_items_db[i])
            return {
                "status": "success",
                "message": f"deleted '{item_id}' id successfully!",
                "data": fake_items_db
            }
    return {
        "status": "fail",
        "message": "invalid id! please try again with an existing id"
    }

@app.delete("/delete-all")
def delete_all_items(user: str = "guest"):
    if user == "admin":
        fake_items_db.clear() 
        return {
            "status": "success", 
            "message": "in memory db cleared successfully!",
            "data": fake_items_db
        }
    else:
        return {
            "You are not allowed to perform this action!"
        }
