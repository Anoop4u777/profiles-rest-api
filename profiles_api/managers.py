from django.contrib.auth.models import BaseUserManager


"""Manager for user profiles"""
class UserProfileManager(BaseUserManager):


    """Creating a new user"""
    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('All the users must have a Email')

        """used to normalize the email ie, https://stackoverflow.com/questions/27936705/what-does-it-mean-to-normalize-an-email-address"""
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        """
        User to hash the password ie,to make the email in hashed format so no one other than the django understands it.
        Also this is used to encrypt the data ie, we need to always encrypt the sensitive data.
        """
        user.set_password(password)
        """Added is_staff here which is not included in the course as a staff user can only log in to the admin"""
        user.is_staff = True

        """Standard procedure to save to a specific Database(or table), we can add multiple models if needed """
        user.save(using=self._db)

        return user

    """Used to create and save a new super user with the details"""
    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)
        user.is_superuser = True
        #user.is_staff = True
        user.save(using=self._db)
        return user
