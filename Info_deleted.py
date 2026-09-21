user_info = {
    "username": 'ashish99',
    "password": "@123ap",
    "email": "asaaa@gmail.com",
    "address": "aaaaa, 111111",
    "country": "india"
}

secret_info = ["password", "address", "phone"]

for item in secret_info:
    if item in user_info:
        print(f"Deleted=> Key: {item} , Value: {user_info[item]}")
        user_info.pop(item)
    else:
        print(f"{item} is not present")

print(user_info)
