from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthen(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(self.__dict__)
        print(obj)
        if request.method in SAFE_METHODS:
            return True
        return False
