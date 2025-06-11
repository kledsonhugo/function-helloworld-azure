import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="{version}", methods=["GET"])
def version_base(req: func.HttpRequest) -> func.HttpResponse:
    version = req.route_params.get('version')
    return func.HttpResponse(
        f"API {version} está ativa. Consulte os endpoints específicos, como /api/{version}/hello.",
        status_code=200
    )

@app.route(route="{version}/hello", methods=["GET"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Função HTTP Python acionada processou uma requisição.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Olá, {name}. Esta função HTTP foi executada com sucesso.")
    else:
        return func.HttpResponse(
             "Esta função HTTP foi executada com sucesso. Passe um nome na query string ou no corpo da requisição para uma resposta personalizada.",
             status_code=200
        )