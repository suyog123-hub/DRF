from rest_framework.permissions import BasePermission

class ContactPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user.is_superuser:
                return True
            else:
                return False
            


       # direct object level permission check garna milxa but it is not recommended for list view because it will be called for each object in the list and it will be very expensive for performance

       
        
    # def has_object_permission(self, request, view, obj):
    #     if request.method == 'GET':
    #         return True
    #     elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
    #         if request.user.is_superuser:
    #             return True
    #         else:
    #             return False