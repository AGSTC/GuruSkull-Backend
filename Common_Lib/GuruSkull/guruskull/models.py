from django.db import models
import uuid
from django.utils import timezone as tz
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserMaster(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Use UUIDField for UUID
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey('self', related_name='created_users', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('self', related_name='updated_users', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey('RoleMaster', related_name='users', on_delete=models.SET_NULL, null=True)
    tuition = models.ForeignKey('TuitionMaster', related_name='users', on_delete=models.SET_NULL, null=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'user_master'
        app_label = 'guruskull'

class RoleMaster(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Use UUIDField for UUID
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=tz.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('UserMaster', on_delete=models.SET_NULL, null=True, related_name='created_roles')
    updated_by = models.ForeignKey('UserMaster', on_delete=models.SET_NULL, null=True, related_name='updated_roles')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'role_master'
        app_label = 'guruskull'


class TuitionMaster(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Use UUIDField for UUID
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey('UserMaster',related_name='created_companies', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('UserMaster', related_name='updated_companies', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,  null=True, blank=True)
    tuition_info = models.TextField(null=True, blank=True)
    user = models.ForeignKey('UserMaster', related_name='companies', on_delete=models.CASCADE)
    tuition_type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tuition_master'
        app_label = 'guruskull'


class ResetPassword(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Use UUIDField for UUID
    created_at = models.DateTimeField(default=tz.now)
    user = models.ForeignKey('UserMaster', related_name='reset_passwords', on_delete=models.CASCADE)
    token = models.CharField(max_length=255, null=True, blank=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        db_table = 'reset_password'
        app_label = 'guruskull'

class EmailVerification(models.Model):
    """
          Stores OTPs for email verification
    """
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Use UUIDField for UUID
    email = models.EmailField()
    otp = models.CharField(max_length=6)  # 6-digit OTP
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'email_verification'
        app_label = 'guruskull'


class MobileVerification(models.Model):
    """
    Stores OTPs for mobile number verification
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile = models.CharField(max_length=15)  # store with country code e.g. +91XXXXXXXXXX
    otp = models.CharField(max_length=6)  # 6-digit OTP
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'mobile_verification'
        app_label = 'guruskull'