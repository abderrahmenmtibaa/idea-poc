import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="hello", methods=["GET", "POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            body = req.get_json()
            name = body.get("name")
        except ValueError:
            pass

    if name:
        return func.HttpResponse(
            json.dumps({"message": f"Hello, {name}!", "status": "ok"}),
            mimetype="application/json",
            status_code=200,
        )

    return func.HttpResponse(
        json.dumps({"message": "Hello! Pass a 'name' param or body.", "status": "ok"}),
        mimetype="application/json",
        status_code=200,
    )
