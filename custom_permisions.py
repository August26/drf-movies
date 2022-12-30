from rest_framework.permissions import BasePermission


class IsAnonCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" and not request.user.is_authenticated:
            return False
        elif request.method == "PUT" and not request.user.is_authenticated:
            return False
        elif request.method == "PATCH" and not request.user.is_authenticated:
            return False
        elif request.method == "DELETE" and not request.user.is_authenticated:
            return False
        else:
            return True
