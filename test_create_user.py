import pytest
import requests

class userSignUpModel():
    def __init__(self,name,last_name,email,password,repeatPassword):
        self.name = name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.repeatPassword = repeatPassword

def test_check_succsessful_user_login():
    user_to_signup = userSignUpModel("John", "Dou", "andrii.2kurochkin+3@nure.ua", "Qwerty123451", "Qwerty123451")
    session = requests.session()
    get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
    post_new_user = session.post("https://qauto2.forstudy.space/api/auth/signup", json=user_to_signup.__dict__)
    get_current_user_after_post = session.get("https://qauto2.forstudy.space/api/users/current")
    assert post_new_user.status_code == 201

user_data = [
    ("Andrey", "Kurochkin", "andrii.kurochkin+5@nure.ua", "Sara123", "Sara123"),
    ("Andrey", "Kozurov", "andrii.kozurov+1@nure.ua", "SonyST123", "SonyaST123"),
    ("Ruslan", "Nikulchenko", "ruslan.nikulchenko+3@nure.ua", "Sofa123", "Sofa123"),
]
@pytest.mark.parametrize("name,last_name,email,password,repeat_password",user_data)
def test_registr_user(name,last_name,email,password,repeat_password):
    some_user_data = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": repeat_password
    }
    session = requests.session()
    post_new_user = session.post(url = "https://qauto2.forstudy.space/api/auth/signup", json = some_user_data)

    assert post_new_user.status_code == 201