from rest_framework.permissions import BasePermission

class EvaluationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT','PATCH'):
            if request.user == obj.creator:
                return True
            else:
                return False
        else:
            return True