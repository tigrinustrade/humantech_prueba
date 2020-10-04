"""User Permissions"""
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):

    def has_objects_permission(self, request, view, obj):
        return request.user == obj
