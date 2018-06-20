from requests import Request, Session
import json
import ast


class RestClient:

    def __init__(self, params):
        if("url" not in params):
            raise Exception("You must set the URL to make a request")
        else:
            self.url = params["url"]

        if("parameters" in params):
            self.parameters = params["parameters"]

        if("method" in params):
            self.method = params["method"]

        if("headers" in params):
            self.headers += params["headers"]
        print(self.headers)

        if(hasattr(self, 'method')):
            self.request = Request(
                self.method,
                self.url,
                data=json.dumps(self.parameters),
                headers=self.headers)

    def run(self):
        request = self.request.prepare()
        try:
            response = Session().send(request)
        except Exception as error:
            raise Exception("error: {}".format(error))
        return {
            "code": response.status_code,
            "body": ast.literal_eval(json.dumps(response.text))
        }
