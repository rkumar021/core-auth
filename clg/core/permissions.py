from os import name
from django.db.models.query import QuerySet
from rest_framework import permissions
from .models import User

class ViewPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        userobj = User.objects.get(id=request.user.id).roles.all()
        user1 = userobj.values()
        role = []
        for i in user1:
            role.append(i['id'])
        print(role)
        if 3 in role or 2 in role or 1 in role:
            return True
        return False

class CreatePermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        userobj = User.objects.get(id=request.user.id).roles.all()
        user1 = userobj.values()
        role = []
        for i in user1:
            role.append(i['id'])
        print(role)
        if 3 in role or 2 in role:
            return True
        return False

class DeletePermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        userobj = User.objects.get(id=request.user.id).roles.all()
        user1 = userobj.values()
        role = []
        for i in user1:
            role.append(i['id'])
        print(role)
        if 3 in role:
            return True
        return False
        # rolelist = list(userobj) 
        # print(type(userobj[0]))
        # alll =str(userobj)
        # no = len(alll)
        # print(alll, no)
        # roless = str(userobj[0])
        # # roles2 = str(userobj[1])
        # print(roless)
        # if roless=='admin':
        #     return True
        # return False

class UpdatePermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        userobj = User.objects.get(id=request.user.id).roles.all()
        user1 = userobj.values()
        role = []
        for i in user1:
            role.append(i['id'])
        print(role)
        if 3 in role or 2 in role:
            return True
        return False