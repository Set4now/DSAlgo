import requests
def getdata(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 404:
            raise Exception("The url doesnot exists")
        if resp.status_code == 200 and resp.json():
            data = resp.json()
            output = []
            for entry in data:
                userdata = {}
                userdata["userID"] = entry["userId"]
                userdata["tilte"] = entry["title"]
                output.append(userdata)
            return output
    except Exception as e:
        return ("Something went wrong", str(e))

url = "https://jsonplaceholder.typicode.com/posts"
#url = "https://jsonplaceholder.typicode.com/post"

print(getdata(url))
