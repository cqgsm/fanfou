from rest_framework.permissions import BasePermission

class ParticipantPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            if request.user == obj.creator:
                return True
            else:
                return False
        elif request.method in ("PUT", "PATCH"):
            #审核申请人只能由活动创建人审核
            if obj.dating.creator == request.user:
                return True
            else:
                return False
        else:
            return True

class DatingPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            if request.user == obj.creator:
                return True
            else:
                return False