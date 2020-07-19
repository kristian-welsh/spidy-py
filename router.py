import responder

class Router:
    def findResponder(self, request):
        return {
            "/": responder.Responder()
        }[request.route()]

