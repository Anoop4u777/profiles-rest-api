"""https://www.django-rest-framework.org/api-guide/permissions/"""

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own data only."""

    def has_object_permission(self, request, view, obj):
        """
        To check whether the current user is only updating his own profile.
        SAFE_METHODS is a tuple containing ('GET', 'OPTIONS', 'HEAD').
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        """
        Just in case for check.
        NOTE: Now the request.user does not work hence even if we log in as the newly created user we are unable to patch the data.
            Solutions:-
            https://stackoverflow.com/questions/54171931/django-auth-self-request-user-is-always-anonymous-in-viewset
            https://stackoverflow.com/questions/5376985/django-request-user-is-always-anonymous-user
        """
        print('obj.id', obj.id, 'request.user.id', request.user.id)
        print(request.user)
        return obj.id == request.user.id
