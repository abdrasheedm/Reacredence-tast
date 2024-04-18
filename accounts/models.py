from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, name, email, phone_number, password=None):

        if not email:
            raise TypeError("User must have an email address")

        if not phone_number:
            raise ValueError("User must have a phone number")

        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, email, phone_number, password=None):
       user = self.create_user(
        email=self.normalize_email(email),
        phone_number=phone_number,
        password=password,
        name=name,

       )
       user.is_admin = True
       user_type = 'Admin'
       user.user_type = user_type
       user.is_active = True
       user.is_staff = True
       user.is_superuser = True
       user.is_verified = True
       user.save(using=self._db)
       
       return user
    


class Account(AbstractBaseUser):
    name = models.CharField(max_length=50, default="")
    user_type = models.CharField(max_length=50, default="customer")
    email = models.EmailField(unique=True, db_index=True, null=False)
    phone_number = models.CharField(unique=True, blank=True, max_length=10)

    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email



    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
