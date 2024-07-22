import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code) # con esto se muestra el codigo de status como 201, 400, 200
print(response.json()) #para que muestre el token de autorizacion para crear una cuenta

def get_docs():
    return requests.get(configuration.URL_SERVICE +configuration.LOG_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)
