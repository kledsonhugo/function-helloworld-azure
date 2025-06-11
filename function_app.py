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
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )