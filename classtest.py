def test(**kwargs):
    result = {}
    if "name" in kwargs:
        result["name"] = kwargs.get("name")
    if "age" in kwargs:
        result["age"] = kwargs.get("age")
    return result

def wrapper(**kwargs):
    print(test(**kwargs))

wrapper(name="SumanDeb", age=32)