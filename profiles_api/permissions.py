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
        Issue found on 22-Nov-2020.
        NOTE: Now the request.user does not work hence even if we log in as the newly created user we are unable to patch the data.
            Solutions:-
            https://stackoverflow.com/questions/54171931/django-auth-self-request-user-is-always-anonymous-in-viewset
            https://stackoverflow.com/questions/5376985/django-request-user-is-always-anonymous-user
        Issue Resolved on 22-Nov-2020.(# NOTE: Solution is not appropriate)
        Comment out the TokenAuthentication system as if we give this permission we need to write function to get the user id.
        Also we can use the SessionAuthentication so that we will be able to use the request.user.id
        """
        #print('obj.id', obj.id, 'request.user.id', request.user.id)
        #print(request.user)
        return obj.id == request.user.id

class UpdateOwnFeeds(permissions.BasePermission):
    """Only user can update his profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the user only updates his profiles"""

        if request.method in permissions.SAFE_METHODS:
            return True
        #print(request.user.id)
        return obj.user_profile.id == request.user.id
