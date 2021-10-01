from rest_framework.permissions import BasePermission


class IsHREmployee(BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_employee)
        print(request.user.id)
        print(bool(request.user) and (request.user.is_employee==False))
        return bool(request.user) and (request.user.is_employee==False)