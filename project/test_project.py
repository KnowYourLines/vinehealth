from flask import request

from project import app


def test_smoke():
    with app.test_request_context("/licence", method="POST"):
        assert request.method == "POST"
