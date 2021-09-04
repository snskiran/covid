from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class ChangePasswordSerializer(serializers.ModelSerializer):
    password        = serializers.CharField(write_only=True, required=True)#, validators=[validate_password])
    password2       = serializers.CharField(write_only=True, required=True)
    old_password    = serializers.CharField(write_only=True, required=True)

    class Meta:
        model   = User
        fields  = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance



class PatientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Patient
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class PatientAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient_Address
        fields ="__all__"



class PatientTestingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient_Testing
        fields = '__all__'


class PatientTypeRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient_Type_Ref
        fields = '__all__'



class SpecimenTypeRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specimen_Type_Ref
        fields = '__all__'


class TestTypeRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test_Type_Ref
        fields = '__all__'


class SwabCollectionStatusRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swab_Collection_Status_Ref
        fields = '__all__'


class TestingStatusRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing_Status_Ref
        fields = '__all__'


class TestingKitBarcodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing_Kit_Barcode
        fields = '__all__'


class UserRoleRefSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Role_Ref
        fields = '__all__'


class PackageSamplingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package_Sampling
        fields = '__all__'


class SwabCollectionCentreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swab_Collection_Centre
        fields = '__all__'


class THOSerializer(serializers.ModelSerializer):

    class Meta:
        model = THO
        fields = '__all__'


class DSOSerializer(serializers.ModelSerializer):

    class Meta:
        model = DSO
        fields = '__all__'


class SSUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SSU
        fields = '__all__'


class TestingLabFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing_Lab_Facility
        fields = '__all__'                                                






class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Patient
        fields = '__all__' 

class Patient_AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Patient_Address
        fields = '__all__' 

class Patient_TestingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Patient_Testing
        fields = '__all__' 

class Patient_Type_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Patient_Type_Ref
        fields = '__all__' 

class Specimen_Type_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Specimen_Type_Ref
        fields = '__all__' 

class Test_Type_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Test_Type_Ref
        fields = '__all__' 

class Swab_Collection_Status_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Swab_Collection_Status_Ref
        fields = '__all__' 

class Testing_Status_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Testing_Status_Ref
        fields = '__all__' 

class Testing_Kit_BarcodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Testing_Kit_Barcode
        fields = '__all__' 

class User_Role_RefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   User_Role_Ref
        fields = '__all__' 

class Package_SamplingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Package_Sampling
        fields = '__all__' 

class Swab_Collection_CentreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Swab_Collection_Centre
        fields = '__all__'

class THOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   THO
        fields = '__all__'

class DSOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   DSO
        fields = '__all__'

class SSUSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   SSU
        fields = '__all__'



class Testing_Lab_FacilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Testing_Lab_Facility
        fields = '__all__'

        
        

class Master_LabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Labs
        fields = '__all__'        





class Master_ZoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Zone
        fields = '__all__'


class Master_WardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Ward
        fields = '__all__'



class Master_VillageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Village
        fields = '__all__'


class Master_PanchayatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Panchayat
        fields = '__all__'


class Master_BlockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Block
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_District
        fields = '__all__'




class MasterLabsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Master_Labs
        fields = '__all__'





