# Create your models here.from django.db import models

#Python Modules
import os
import uuid


#Django Function
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator,FileExtensionValidator


#Helpers Function and Database Modules
from config.helpers import (random_code,returnFlugFormat,name_message,name_regex,phone_message,phone_regex,get_profile_photo_upload_path)



#!MyAccountManager
class MyAccountManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return 
    
    def create_user(self,email,password=None,**extra_fields):        
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superadmin',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email,password,**extra_fields)
    
    
    
#!Account
class Account(AbstractBaseUser,PermissionsMixin):
    
    #User column fields
    email = models.EmailField(_('email'),max_length=100,unique=True)
    first_name = models.CharField(_('first name'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    last_name = models.CharField(_('last name'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    username = models.CharField(_('username'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    phone = models.CharField(_('phone'),validators=[phone_regex],max_length=12,blank=True,null=True,unique=True,help_text=phone_message)
    registration_number = models.CharField(_('registration number'),max_length=50,db_index=True,null=True,blank=True,unique=True)
    
    #User permissions field
    is_admin = models.BooleanField(_('admin status'),default=False,help_text=_('Designates whether the user is admin or not.'))
    is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'),default=True,help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_superadmin = models.BooleanField(_('superadmin'),default=False,help_text=_('Designates whether the user is admin or not.'))
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
    last_login = models.DateTimeField(_('last login'),auto_now_add=True)
    password_updated_date = models.DateTimeField(_('password updated date'),auto_now_add=True)
    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','phone']#this list in data macthes Account class one-by-one
    
    
    objects = MyAccountManager()
    
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        ordering = ['first_name','last_name','username']
        
    
    #*save
    def save(self,*args,**kwargs):
        #save registration_number
        self.registration_number = random_code()
        super(Account,self).save(*args,**kwargs)
        

    #*clean
    def clean(self) -> None:
        super().clean()
        print('self.__class__ ', self.__class__)
        self.email = self.__class__.objects.normalize_email(self.email)
        
    
    #*get_full_name
    def get_full_name(self) -> str:
        full_name = "{} {} {}".format(self.first_name,self.last_name,self.phone)
        return full_name.strip()
    
        
    #*full_name
    @property
    def full_name(self) -> str:
        return self.get_full_name()
    
    
    #*short_name
    @property
    def short_name(self) -> str:
        return self.get_short_name()
    

    #*name
    @property
    def name(self) -> str:
        name = "{} {}".format(self.first_name,self.last_name)
        return name.strip()
    
    
    #*get_short_name
    def get_short_name(self) -> str:
        return self.first_name
    
    
    #*mobile_phone
    def mobile_phone(self) -> str or None:
        if self.phone:
            return "+" + self.phone
        return None
    
    
    #*set_password
    def set_password(self,raw_password):
        super().set_password(raw_password)
        self.password_updated_date = timezone.now()
        
        
    #*__str__
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name} {self.registration_number}"
    
    
    #*__has_perm__
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    
    #*has_module_perms    
    def has_module_perms(self,add_label):
        return True



#!Profile
class Profile(models.Model):
    account = models.OneToOneField(Account,verbose_name=_('account'),on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('profile picture'),upload_to=get_profile_photo_upload_path,validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    website_links = models.URLField(_('website links'),default='')
    city = models.CharField(_('city'),max_length=20)
    state = models.CharField(_('state'),max_length=20)
    country = models.CharField(_('country'),max_length=20)
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        
        
    def __str__(self):
        return str(self.account.first_name)
    
    
    @property
    def get_full_address(self):
        return f"{self.city} -- {self.country}"
    


