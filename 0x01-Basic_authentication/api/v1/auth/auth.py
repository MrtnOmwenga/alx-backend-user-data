#!/usr/bin/env python3
""" Handling authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Handles all authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Chacks if path requires authentication """
        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns Authorization header """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None """
        return None
