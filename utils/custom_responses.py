from rest_framework import status
from rest_framework.response import Response


def ok(response_data=None, message="", status_code=status.HTTP_200_OK):
    response_payload = {
        "code": True,
        "statusCode": status_code,
        "message": message or "",
        "result": response_data or None,
    }
    return Response(response_payload, status=status_code)


def success(response_data=None, message="", status_code=status.HTTP_201_CREATED):
    response_payload = {
        "code": True,
        "statusCode": status_code,
        "message": message or "",
        "result": response_data or None,
    }
    return Response(response_payload, status=status_code)


def error(response_data=None, message="Error", status_code=status.HTTP_400_BAD_REQUEST):
    response_payload = {
        "code": False,
        "statusCode": status_code,
        "message": message or "",
        "result": response_data,
    }
    return Response(response_payload, status=status_code)


def unauthorized(
    response_data=None, message="Error", status_code=status.HTTP_401_UNAUTHORIZED
):
    response_payload = {
        "code": False,
        "statusCode": status_code,
        "message": message or "",
        "result": response_data,
    }
    return Response(response_payload, status=status_code)


def bad(response_data=None, message="Error", status_code=status.HTTP_400_BAD_REQUEST):
    response_payload = {
        "code": False,
        "statusCode": status_code,
        "result": response_data,
        "message": message or "",
    }
    return Response(response_payload, status=status_code)


def unknown(
    response_data=None,
    message="Error",
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
):
    response_payload = {
        "code": False,
        "statusCode": status_code,
        "result": response_data,
        "message": message or "",
    }
    return Response(response_payload, status=status_code)
