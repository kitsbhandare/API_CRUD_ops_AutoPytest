import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()

######get user
def test_get_user(apis):
    response=apis.get('users')
    print("Boddy",response.json())
    assert response.status_code==200,"status code should be 200"
    assert len(response.json()) > 0,"Body should not empty"

######create user
def test_create_user(apis):
    user_data={
        "name":"Kiran",
        "username":"QA",
        "email":"kiran@gmail.com"
    }
    response=apis.post('users',user_data)
    print("Boddy",response.json())
    print("id is:",response.json()['id'])
    assert response.status_code==201,"status code should be 201"
    assert response.json()['name']=="Kiran"
    assert response.json()['username']=="QA"

    ######get newly created user
    #id=response.json()['id'] # i want to pass this id in next line ASK DIPALI
    response_get = apis.get("users/1") #now randomly took existing id, in real you have to fetch newly created id
    print(response_get.json())
    assert response_get.json()['name'] == 'Leanne Graham'

######update user
def test_update_user(apis):
    user_data={
        "name":"Akira",
        "username":"QA",
        "email":"kiran123@gmail.com"
    }
    response=apis.put('users/1',user_data)
    print("Boddy",response.json())
    assert response.status_code==200,"status code should be 200"
    assert response.json()['name']=="Akira"

######delete user
def test_delete_user(apis):
    response=apis.delete('users/1')
    print("Boddy",response.json())
    assert response.status_code==200,"status code should be 200"

