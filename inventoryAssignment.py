inventory = {
    "Butter":{
        "quantity": 2,
        "price": 2.25
    },
    "Yogurt":{
        "quantity": 24,
        "price": 0.75
    },
    "Bread":{
        "quantity": 1,
        "price": 1.5
    },
    "Water":{
        "quantity": 15,
        "price": 1.0
    }
}

def check_low_stock(threshold):
    for k in inventory:
        if inventory[k]["quantity"] <= threshold:
            print(f"{k}'s stock is low")

check_low_stock(2)