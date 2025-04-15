import requests
import allure
from urls import Urls


class RegisterUserAPI:
    @staticmethod
    @allure.step('Register new user.')
    def register_user(email: str, password: str, name: str):
        response = requests.post(Urls.REGISTER_USER,
                                 json={"email": email, "password": password, "name": name})
        return response


class DeleteUserAPI:
    @staticmethod
    @allure.step('Delete user.')
    def delete_user(token: str):
        headers = {'Authorization': token}
        response = requests.delete(Urls.DELETE_USER, headers=headers)
        return response
