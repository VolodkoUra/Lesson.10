import json
import requests
class MyFirsrPost:
    import requests

    id: 0
    petId: 0
    quantity: 0
    shipDate: str
    status: str
    complete: bool

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k,v)

    def post_to_url(self, url):
        #self.__getattribute__()
        return self.requests.post(url, json =self.__dict__ ).text


d = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-05-28T17:03:27.107Z",
  "status": "placed",
  "complete": True
}

m = MyFirsrPost(**d)
r = m.post_to_url('https://petstore.swagger.io/v2/store/order')
print(r)

print("-"*30)

response_from_post = requests.post(url='https://petstore.swagger.io/v2/store/order',
                                   json=my_body
                                   )
print(response_from_post)

print("="*40)


response = requests.get('https://petstore.swagger.io/v2/store/inventory')
# print(response.status_code)
text = response.text
print(text)
print(type(text))
js = json.loads(text)
print(js)
print("=" * 30)
for k, v in js.items():
    print(k, v)
