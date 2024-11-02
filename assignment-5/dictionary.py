# dictionary 
person = {
    "name": {
        "firstName": "Anik",
        "lastName": "Sarker"
    },
    "age": 25,
    "profession": ("Software Developer", "Programmer", "Tech Enthusiast"),
    "test_set": {1, 5, 3, 5, 3, 5}
}

print(type(person), person['age'], person['name']['firstName'], type(person["profession"]), person["test_set"])