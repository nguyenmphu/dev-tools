import hashlib

from django.http.request import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def md5(request: HttpRequest):
    if request.method == "GET":
        text = request.GET.get("q", "")
    else:
        text = request.data.get("text")
        if not text:
            return Response({"message": "The text must not be empty"}, status=400)
    return Response({"message": hashlib.md5(text.encode("utf-8")).hexdigest()})
