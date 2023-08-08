#!/usr/bin/env python3
""" Handling authentication """
from flask import request
from Typing import List, TypeVar


class Auth:
    """ Handles all authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None """
        return None
