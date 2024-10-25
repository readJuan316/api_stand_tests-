import requests
import configuration
import data
#from create_user_tests import get_user_body


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def guardar_token():
    Token_nuevo_usuario = post_new_user(data.user_body)
    token_usuario = Token_nuevo_usuario.json()["authToken"]
    return token_usuario

def post_new_kit(body_kit):
    Mi_token = guardar_token
    headers_token = data.headers.copy()
    headers_token["Autorization"] = f"Bearer {Mi_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=body_kit,
        headers=headers_token)
    return response

def get_users_table(user_body, user_response):
    #return [
        str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
        return str_user
        assert users_table_response.text.count(str_user) == 1

##def test_create_user_2_letter_in_first_name_get_success_response():
  ##  positive_assert("Aa")

# Función de prueba positiva
def positive_assert(firstName):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_users_table(firstName)
    # Enviar la solicitud y obtener la respuesta
    user_response = sender_stand_request.post_new_user(user_body)
    get_users_table(user_response)
    print(user_response)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201, f"Error: se esperaba el código 201 pero se obtuvo {user_response.status_code}"

    # Verificar que el campo authToken esté presente en la respuesta
    response_json = user_response.json()
    assert "authToken" in response_json, "El campo 'authToken' no está presente en la respuesta"
    auth_token = response_json["authToken"]
    assert auth_token !="", "El campo 'authToken' está vacío"
    print(f"AuthToken: {auth_token}")
    #return user_response





