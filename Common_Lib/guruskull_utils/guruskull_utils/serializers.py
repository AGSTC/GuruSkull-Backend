from rest_framework import serializers
from guruskull_utils.models import UserMaster, TuitionMaster, ResetPassword, RoleMaster, EmailVerification, \
    MobileVerification

class UserMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        fields = '__all__'

class TuitionMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionMaster
        fields = '__all__'

class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = '__all__'

class RoleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = '__all__'

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerification
        fields = '__all__'

class MobileVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileVerification
        fields = '__all__'