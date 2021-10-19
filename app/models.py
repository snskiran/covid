from hashlib import blake2b, blake2s
from random import sample
from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.contrib.auth.models import  User,Group
from django.db.models import base
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.db.models.query import BaseIterable

import json

from django.utils import timezone
from django.utils.translation import TranslatorCommentWarning

# from ckeditor.fields import RichTextField

class Roles(models.Model):
    role_name = models.CharField(max_length=150, blank=True, null=True)
    role_description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.role_name)



class Patient_Type_Ref(models.Model):
    
    # patient_type_id                 =   models.CharField(max_length=150, blank=True, null=True)
    patient_type_name               =   models.CharField(max_length=150, blank=True, null=True)
    patient_type_desc               =   models.CharField(max_length=150, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    


class Specimen_Type_Ref(models.Model):
    
    # specimen_type_id                =   models.CharField(max_length=250, blank=True, null=True)
    specimen_type_name              =   models.CharField(max_length=150, blank=True, null=True)
    specimen_type_desc              =   models.CharField(max_length=150, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    


class Test_Type_Ref(models.Model):
    
    # test_type_id                    =   models.CharField(max_length=250, blank=True, null=True)
    test_type_name                  =   models.CharField(max_length=150, blank=True, null=True)
    test_type_desc                  =   models.CharField(max_length=150, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)        



class Swab_Collection_Status_Ref(models.Model):
    
    # swab_collection_status_id       =   models.CharField(max_length=250, blank=True, null=True)
    swab_collection_status_name     =   models.CharField(max_length=150, blank=True, null=True)
    swab_collection_status_desc     =   models.CharField(max_length=150, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
        


class Testing_Status_Ref(models.Model):

    # testing_status_id               =   models.CharField(max_length=50, blank=True, null=True)
    testing_status_name             =   models.CharField(max_length=50, blank=True, null=True)
    testing_status_desc             =   models.CharField(max_length=50, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
        
 

class Master_Zone(models.Model):
    district_code = models.CharField(max_length=50, blank=True, null=True)
    district_name_kan = models.CharField(max_length=150, blank=True, null=True)
    district_name_eng = models.CharField(max_length=150, blank=True, null=True)
    bbmp_zone_no_ksrsac = models.IntegerField(blank=True, null=True)
    software_zone_no = models.CharField(max_length=150, blank=True, null=True)
    zone_name = models.CharField(max_length=150, blank=True, null=True)
    ksrsac_ward_no = models.CharField(max_length=150, blank=True, null=True)
    new_ward_no =models.CharField(max_length=10, blank=True, null=True)
    ward_name = models.CharField(max_length=150, blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.zone_name)



class Master_Ward(models.Model):
     
    district_code = models.IntegerField(blank=True, null=True)
    district_name_kan = models.CharField(max_length=150, blank=True, null=True)
    district_name_eng = models.CharField(max_length=150, blank=True, null=True)

    bbmp_zone_no_ksrsac = models.IntegerField(blank=True, null=True)
    software_zone_no = models.CharField(max_length=150, blank=True, null=True)
    zone_name = models.CharField(max_length=150, blank=True, null=True)
    ksrsac_ward_no = models.IntegerField(blank=True, null=True)
    ward_no = models.CharField(max_length=150, blank=True, null=True)
    ward_name = models.CharField(max_length=150, blank=True, null=True)
    ksrsac_dist_code = models.CharField(max_length= 10,blank=True, null=True)
    ksrsac_town_code = models.IntegerField(blank=True, null=True)
    new_town_code = models.CharField(max_length=10, blank=True, null=True)
    town_name = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.ward_name)



class Master_Village(models.Model):
    district_code = models.IntegerField(blank=True, null=True)
    block_code = models.CharField(max_length= 120,blank=True, null=True)
    panchayat_code = models.CharField(max_length= 120, blank=True, null=True)
    village_code = models.CharField(max_length= 150,blank=True, null=True)
    village_name_kan = models.CharField(max_length=150, blank=True, null=True)
    village_name_eng = models.CharField(max_length=150, blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.village_name_eng)



class Master_Panchayat(models.Model):
    district_code = models.IntegerField(blank=True, null=True)
    block_code = models.IntegerField(blank=True, null=True)
    panchayat_code = models.IntegerField(blank=True, null=True)
    panchayat_name_kan = models.CharField(max_length=150, blank=True, null=True)
    panchayat_name_eng = models.CharField(max_length=150, blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.panchayat_name_eng)



class Master_Block(models.Model):
    district_code = models.IntegerField(blank=True, null=True)
    block_code = models.IntegerField(blank=True, null=True)
    block_name_kan = models.CharField(max_length=150, blank=True, null=True)
    block_name_eng = models.CharField(max_length=150, blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.block_name_eng)



class Master_District(models.Model):
    icmr_district_code = models.IntegerField(blank=True, null=True)
    district_code = models.IntegerField(blank=True, null=True)
    district_name_kan = models.CharField(max_length=150,blank=True, null=True)
    district_name_eng = models.CharField(max_length=150,blank=True, null=True)

    district_lat = models.CharField(max_length=150,blank=True, null=True)
    district_lon = models.CharField(max_length=150,blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (self.district_name_eng)
    
    

class Master_PHC(models.Model):

    sys_id = models.CharField(max_length=20, blank=True, null=True)
    district_name_eng = models.CharField(max_length=120, blank=True, null=True)
    block_name_eng = models.CharField(max_length=120, blank=True, null=True)
    panchayat_name_eng = models.CharField(max_length=150, blank=True, null=True)
    village_name_eng = models.CharField(max_length=120, blank=True, null=True)
    ward_name_eng = models.CharField(max_length=120, blank=True, null=True)
    zone_name_eng = models.CharField(max_length=120, blank=True, null=True)
    district_code = models.IntegerField(blank=True, null=True)
    block_code = models.CharField(max_length=30, blank=True, null=True)
    panchayat_code = models.CharField(max_length=30, blank=True, null=True)
    village_code = models.CharField(max_length=120, blank=True, null=True)
    zone_code = models.CharField(max_length=120, blank=True, null=True)
    ward_code = models.CharField(max_length=120, blank=True, null=True)
    phc_name = models.CharField(max_length=220, blank=True, null=True)
    phc_code = models.CharField(max_length=120, blank=True, null=True)
    phc_type = models.CharField(max_length=20, blank=True, null=True)



class Testing_Lab_Master(models.Model):

    lab_name = models.CharField(max_length=250, blank=True, null=True)
    district_code                   =   models.CharField(max_length=150, blank=True, null=True)
    district_name                   =   models.CharField(max_length=150, blank=True, null=True)
    lab_type                   =   models.CharField(max_length=150, blank=True, null=True)
    rat_rt_pcr                   =   models.CharField(max_length=150, blank=True, null=True)

    current_count                   =   models.IntegerField(blank=True, null=True)
    availability_limit              =   models.IntegerField(blank=True, null=True)




class Master_Labs(models.Model):

    lab_name = models.CharField(max_length=250, blank=True, null=True)
    district_code                   =   models.CharField(max_length=150, blank=True, null=True)
    district_name                   =   models.CharField(max_length=150, blank=True, null=True)
    lab_type                   =   models.CharField(max_length=150, blank=True, null=True)
    rat_rt_pcr                   =   models.CharField(max_length=150, blank=True, null=True)
    lab_id = models.CharField(max_length=120, blank=True, null=True)

    current_count                   =   models.IntegerField(blank=True, null=True)
    availability_limit              =   models.IntegerField(blank=True, null=True)

    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    district_id = models.CharField(max_length=250,blank=True, null=True)
    karnataka_districts_id = models.IntegerField(blank=True, null=True)
    karnataka_blocks_id = models.IntegerField(blank=True, null=True)
    lab_type_id = models.CharField(max_length= 150,blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    pincode = models.CharField(max_length=250, blank=True, null=True)
    gps_lat = models.CharField(max_length=250, blank=True, null=True)
    gps_lon = models.CharField(max_length=250, blank=True, null=True)
    max_capacity = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    test_type = models.CharField(max_length=150, blank=True, null=True)
    lab_classification_id = models.CharField(max_length=150, blank=True, null=True)
    closing_balance = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default= 1, blank=True, null=True)

    last_genearte_individual_lab_id = models.CharField(max_length=120 ,blank=True, null=True)
    last_genearte_pool_lab_id = models.CharField(max_length=120 ,blank=True, null=True)

    # def __str__(self):
    #     return '%s' % (str(self.address)+'     '+str(self.lab_type_id))






#!===================================================================================================================================================================

class Testing_Lab_Facility(models.Model):
   
    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # user_role_id                    =   models.CharField(max_length=50, blank=True, null=True)

    # package_sampling_id             =   models.CharField(max_length=50, blank=True, null=False)
    # testing_lab_facility_id         =   models.CharField(max_length=50, blank=True, null=True)

    testing_lab_facility_name       =   models.CharField(max_length=50, blank=True, null=True)
    testing_lab_facility_desc       =   models.CharField(max_length=50, blank=True, null=True)
    address_line_1                  =   models.CharField(max_length=150, blank=True, null=True)
    address_line_2                  =   models.CharField(max_length=150, blank=True, null=False)

    # district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    # city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    # village_name                    =   models.CharField(max_length=50, blank=True, null=True)

    testing_lab_master = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, null=True, blank=True)
    lab_name = models.CharField(max_length=250, blank=True, null=True)
    district_code                   =   models.CharField(max_length=150, blank=True, null=True)
    district_name                   =   models.CharField(max_length=150, blank=True, null=True)
    lab_type                   =   models.CharField(max_length=150, blank=True, null=True)
    rat_rt_pcr                   =   models.CharField(max_length=150, blank=True, null=True)


    zone = models.ForeignKey(Master_Zone, on_delete=models.CASCADE, blank=True, null=True)
    district                   =   models.ForeignKey(Master_District, on_delete=models.CASCADE, blank=True, null=True)
    city                       =   models.ForeignKey(Master_Block, on_delete=models.CASCADE ,blank=True, null=True)
    ward                       =   models.ForeignKey(Master_Ward, on_delete=models.CASCADE,blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat                  =   models.ForeignKey(Master_Panchayat, on_delete=models.CASCADE,blank=True, null=True)
    village                    =   models.ForeignKey(Master_Village, on_delete=models.CASCADE,blank=True, null=True)

    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    current_count                   =   models.CharField(max_length=50, blank=True, null=True)
    availability_limit              =   models.CharField(max_length=50, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    def __str__(self):
        return '%s' % (self.testing_lab_facility_name)
    

    
class SSU(models.Model):
   
    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    test_lab                        =   models.ForeignKey(Testing_Lab_Facility,on_delete=models.CASCADE,blank=True,null=True)
    role                    =   models.ForeignKey(Roles, on_delete=models.CASCADE, blank=True, null=True)

    # username                        =   models.CharField(max_length=150, blank=True, null=True)
    # password                        =   models.CharField(max_length=150, blank=True, null=True)

    ssu_name                        =   models.CharField(max_length=50, blank=True, null=True)
    ssu_desc                        =   models.CharField(max_length=50, blank=True, null=True)
    address_line_1                  =   models.CharField(max_length=150, blank=True, null=True)
    address_line_2                  =   models.CharField(max_length=150, blank=True, null=True)
    zone = models.ForeignKey(Master_Zone, on_delete=models.CASCADE, blank=True, null=True)
    # district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    district                   =   models.ForeignKey(Master_District, on_delete=models.CASCADE, blank=True, null=True)
    # city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    city                       =   models.ForeignKey(Master_Block, on_delete=models.CASCADE ,blank=True, null=True)
    # ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    ward                       =   models.ForeignKey(Master_Ward, on_delete=models.CASCADE,blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    # panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    panchayat                  =   models.ForeignKey(Master_Panchayat, on_delete=models.CASCADE,blank=True, null=True)
    # village_name                    =   models.CharField(max_length=50, blank=True, null=True)
    village                    =   models.ForeignKey(Master_Village, on_delete=models.CASCADE,blank=True, null=True)
    pincode                         =   models.CharField(max_length=50, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    def __str__(self):
        return '%s' % (self.ssu_name)
    

    
class DSO(models.Model):

    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    test_lab                        =   models.ForeignKey(Testing_Lab_Facility,on_delete=models.CASCADE,blank=True,null=True)
    ssu                             =   models.ForeignKey(SSU,on_delete=models.CASCADE,blank=True,null=True)
    role                    =   models.ForeignKey(Roles,on_delete=models.CASCADE, blank=True, null=True)
    
    dso_name                        =   models.CharField(max_length=50, blank=True, null=True)
    dso_desc                        =   models.CharField(max_length=50, blank=True, null=True)
    address_line_1                  =   models.CharField(max_length=150, blank=True, null=True)
    address_line_2                  =   models.CharField(max_length=150, blank=True, null=True)
    # district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    # city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    # panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    # village_name                    =   models.CharField(max_length=50, blank=True, null=True)

    zone = models.ForeignKey(Master_Zone, on_delete=models.CASCADE, blank=True, null=True)
    district                   =   models.ForeignKey(Master_District, on_delete=models.CASCADE, blank=True, null=True)
    city                       =   models.ForeignKey(Master_Block, on_delete=models.CASCADE ,blank=True, null=True)
    ward                       =   models.ForeignKey(Master_Ward, on_delete=models.CASCADE,blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat                  =   models.ForeignKey(Master_Panchayat, on_delete=models.CASCADE,blank=True, null=True)
    village                    =   models.ForeignKey(Master_Village, on_delete=models.CASCADE,blank=True, null=True)

    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    def __str__(self):
        return '%s' % (self.dso_name)
    
    
    
class THO(models.Model):

    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    test_lab                        =   models.ForeignKey(Testing_Lab_Facility,on_delete=models.CASCADE,blank=True,null=True)
    dso                             =   models.ForeignKey(DSO,on_delete=models.CASCADE,blank=True,null=True)
    role                    =   models.ForeignKey(Roles,on_delete=models.CASCADE, blank=True, null=True)

    tho_name                        =   models.CharField(max_length=50, blank=True, null=True)
    tho_desc                        =   models.CharField(max_length=50, blank=True, null=True)
    address_line_1                  =   models.CharField(max_length=150, blank=True, null=True)
    address_line_2                  =   models.CharField(max_length=150, blank=True, null=True)
    # district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    # city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    # panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    # village_name                    =   models.CharField(max_length=50, blank=True, null=True)

    zone = models.ForeignKey(Master_Zone, on_delete=models.CASCADE, blank=True, null=True)
    district                   =   models.ForeignKey(Master_District, on_delete=models.CASCADE, blank=True, null=True)
    city                       =   models.ForeignKey(Master_Block, on_delete=models.CASCADE ,blank=True, null=True)
    ward                       =   models.ForeignKey(Master_Ward, on_delete=models.CASCADE,blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat                  =   models.ForeignKey(Master_Panchayat, on_delete=models.CASCADE,blank=True, null=True)
    village                    =   models.ForeignKey(Master_Village, on_delete=models.CASCADE,blank=True, null=True)

    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    def __str__(self):
        return '%s' % (self.tho_name)
    
    
    
class Swab_Collection_Centre(models.Model):

    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    test_lab                        =   models.ForeignKey(Testing_Lab_Facility,on_delete=models.CASCADE,blank=True,null=True)
    tho                             =   models.ForeignKey(THO,on_delete=models.CASCADE,blank=True,null=True)
    role                    =   models.ForeignKey(Roles,on_delete=models.CASCADE, blank=True, null=True)

    swab_collection_centre_name     =   models.CharField(max_length=50, blank=True, null=True)
    swab_collection_centre_desc     =   models.CharField(max_length=50, blank=True, null=True)
    address_line_1                  =   models.CharField(max_length=150, blank=True, null=True)
    address_line_2                  =   models.CharField(max_length=150, blank=True, null=True)
    # district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    # city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    # taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    # panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    # village_name                    =   models.CharField(max_length=50, blank=True, null=True)
    phc_master =models.ForeignKey(Master_PHC, on_delete=models.CASCADE, blank=True, null=True)

    zone = models.ForeignKey(Master_Zone, on_delete=models.CASCADE, blank=True, null=True)
    district                   =   models.ForeignKey(Master_District, on_delete=models.CASCADE, blank=True, null=True)
    city                       =   models.ForeignKey(Master_Block, on_delete=models.CASCADE ,blank=True, null=True)
    ward                       =   models.ForeignKey(Master_Ward, on_delete=models.CASCADE,blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat                  =   models.ForeignKey(Master_Panchayat, on_delete=models.CASCADE,blank=True, null=True)
    village                    =   models.ForeignKey(Master_Village, on_delete=models.CASCADE,blank=True, null=True)

    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    def __str__(self):
        return '%s' % (self.swab_collection_centre_name +'     '+ self.role.role_name)
    
    
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Testing_Kit_Barcode(models.Model):
    
    # testing_kit_barcode_id          =   models.CharField(max_length=50, blank=True, null=True)
    testing_kit_barcode_name        =   models.CharField(max_length=250, blank=True, null=True)
    testing_kit_barcode_value       =   models.CharField(max_length=50, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    active           =   models.IntegerField(default=1,blank=True,null=True)
        


class RTPCR_Test_Kits(models.Model):
    rtpcr_test_kit_name = models.CharField(max_length=250, blank=True, null=True)
    rtpcr_testing_kit_barcode_value       =   models.CharField(max_length=50, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False ,blank=True,null=True)
    active           =   models.IntegerField(default=1,blank=True,null=True)




class Package_Sampling(models.Model):
    
    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    swab_cc                         =   models.ForeignKey(Swab_Collection_Centre,on_delete=models.CASCADE,blank=True,null=True)
    master_phc                         =   models.ForeignKey(Master_PHC,on_delete=models.CASCADE,blank=True,null=True)
    tho                             =   models.ForeignKey(THO,on_delete=models.CASCADE,blank=True,null=True)
    dso                             =   models.ForeignKey(DSO,on_delete=models.CASCADE,blank=True,null=True)
    ssu                             =   models.ForeignKey(SSU,on_delete=models.CASCADE,blank=True,null=True)
    test_lab                        =   models.ForeignKey(Testing_Lab_Facility,on_delete=models.CASCADE,blank=True,null=True)
    lab_master                      =   models.ForeignKey(Master_Labs,on_delete=models.CASCADE,blank=True,null=True)

    package_sampling_name           =   models.CharField(max_length=50, blank=True, null=True)
    package_sampling_barcode        =   models.CharField(max_length=150, blank=True, null=True)
    testing_kit_barcodes_list       =   models.CharField(max_length=100, blank=True, null=True)
    dispatch_status                 =   models.CharField(max_length=50, blank=True, null=True)
    sympto_indication                    =   models.CharField(max_length=200, blank=True, null=True)
    samples_count                   =   models.IntegerField(blank=True, null=True)
    package_type_status             =   models.IntegerField(blank=True, null=True)
    package_type_action             =   models.IntegerField(blank=True, null=True)
    
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    dso_disptch_status = models.CharField(max_length=20, blank=True, null=True, default='Dispatch')
    ssu_disptch_status = models.CharField(max_length=20, blank=True, null=True, default='Dispatch')
    test_lab_disptch_status = models.CharField(max_length=20, blank=True, null=True, default='Dispatch')

    reference_tlab = models.CharField(max_length=12, blank=True, null=True, default=0)
    lab_received_datetime = models.DateTimeField(auto_now_add=False, blank=True,null=True)
    lab_ops_received_datetime = models.DateTimeField(auto_now_add=False, blank=True,null=True)

    created_group_pool_data = models.IntegerField(default=0, blank=True, null=True)

    lab_accept_reject_status = models.IntegerField(default=0, blank=True, null=True)
       


class User_Role_Ref(models.Model): 
    user                            =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, blank=True, null=True)
    user_role_name                  =   models.CharField(max_length=50, blank=True, null=True)
    user_role_desc                  =   models.CharField(max_length=50, blank=True, null=True)
    mobile_number                  =   models.CharField(max_length=12, blank=True, null=True)
    suspend                         = models.BooleanField(default=False)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
       


class Reason_For_Testing(models.Model):
    reason_name = models.CharField(max_length=150, blank=True, null=True)



class Patient(models.Model):
    
    swab_collection = models.ForeignKey(Swab_Collection_Centre, on_delete=models.CASCADE, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    patient_type                 =   models.ForeignKey(Patient_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    patient_name                    =   models.CharField(max_length=50, blank=True, null=True)
    mobile_number                   =   models.CharField(max_length=15, blank=True, null=True)
    mobile_number_belongs_to        =   models.CharField(max_length=50, blank=True, null=True)
    gender                          =   models.CharField(max_length=10, blank=True, null=True)
    age                             =   models.IntegerField( blank=True, null=True)
    age_type = models.CharField(max_length=10, blank=True, null=True)
    id_proof_type                   =   models.CharField(max_length=120, blank=True, null=True)
    aadhar_number                   =   models.CharField(max_length=120, blank=True, null=True)
    ration_card_number              =   models.CharField(max_length=15, blank=True, null=True)
    vaccine_status                  =   models.CharField(max_length=10, blank=True, null=True)
    vaccine_mobile_registered       =   models.CharField(max_length=150, blank=True, null=True)
    specimen_type                =   models.ForeignKey(Specimen_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    specimen_collection_date        =   models.DateField(auto_now_add=True, blank=True, null=True)
    testing_kit_barcode             =   models.ForeignKey(Testing_Kit_Barcode, on_delete=models.CASCADE, blank=True, null=True)
    patient_status                  =   models.CharField(max_length=50, blank=True, null=True)
    symptoms_list                   =   models.CharField(max_length=50, blank=True, null=True)
    test_type                    =   models.ForeignKey(Test_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    srf_id                         =   models.CharField(max_length=50, blank=True, null=True)
    barcode                         =   models.CharField(max_length=150, blank=True, null=True)
    # swab_collection_status       =   models.CharField(max_length=50, blank=True, null=True, default='Pending')
    # swab_collection_result       =   models.CharField(max_length=50, blank=True, null=True, default='Not Dispached')
    swab_collection_status       =   models.IntegerField(blank=True, null=True, default=31)
    swab_collection_result       =   models.IntegerField(blank=True, null=True,)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    patient_testing_id              =   models.CharField(max_length=50, blank=True, null=True)
    co_morbidity              =   models.CharField(max_length=50, blank=True, null=True)
    co_morbidity_type              =   models.CharField(max_length=250, blank=True, null=True)
    old_srf_id = models.CharField(max_length=20, blank=True, null=True)
    pre_contact_person = models.CharField(max_length=20, blank=True, null=True)
    package_sampling = models.ForeignKey(Package_Sampling, on_delete=models.CASCADE, blank=True, null=True)

    rat_srf_id = models.CharField(max_length=50, blank=True, null=True)
    sample_status = models.CharField(max_length=150, blank=True, null=True)
    sample_rejected_reason = models.CharField(max_length=150, blank=True, null=True)

    reason_for_testing = models.TextField(blank=True, null=True)
    reason_for_testing_description = models.TextField(blank=True, null=True)

    test_lab_id = models.CharField(max_length=120, blank=True, null=True)
    lab_master = models.ForeignKey(Master_Labs, on_delete=models.CASCADE ,blank=True, null=True)
    lab_accepted_datetime = models.DateTimeField(auto_now_add=False, blank=True,null=True)
    lab_ops_received_datetime = models.DateTimeField(auto_now_add=False, blank=True,null=True)

    rat_created_id = models.CharField(max_length=120, blank=True, null=True)

    arrival_date = models.CharField(max_length=120, blank=True, null=True)
    
    submit_for_individual_testing = models.IntegerField(default=0, blank=True, null=True)
    submit_for_pool_testing = models.IntegerField(default=0, blank=True, null=True)

    group_samples = models.IntegerField(default=0, blank=True, null=True)
    pool_samples = models.IntegerField(default=0, blank=True, null=True)

    group_samples_result = models.IntegerField(default=0, blank=True, null=True)
    pool_samples_result = models.IntegerField(default=0, blank=True, null=True)

    samples_rejected = models.IntegerField(default=0, blank=True, null=True)
    samples_inconclusive = models.IntegerField(default=0, blank=True, null=True)

    father_name = models.CharField(max_length= 150, blank=True, null=True)
    occupation = models.CharField(max_length= 150, blank=True, null=True)
    mode_of_transport = models.CharField(max_length= 150, blank=True, null=True)
    arogya_setu_app = models.CharField(max_length= 150, blank=True, null=True)
    vaccine_type = models.CharField(max_length= 150, blank=True, null=True)
    driver_license = models.CharField(max_length= 150, blank=True, null=True)
    passport = models.CharField(max_length= 150, blank=True, null=True)
    sample_collected_from = models.CharField(max_length= 150, blank=True, null=True)


    first_dose_date = models.DateField(auto_now_add=False, blank=True, null=True)

    hospitalized = models.CharField(max_length= 150, blank=True, null=True)

    sero_category = models.CharField(max_length= 250, blank=True, null=True)
    igg_sample = models.CharField(max_length= 50, blank=True, null=True)
    speciman_type_scan = models.CharField(max_length= 50, blank=True, null=True)
    speciman_typeRFID_scan = models.CharField(max_length= 50, blank=True, null=True)
    contact_with_lab_confirmed_patient = models.CharField(max_length= 50, blank=True, null=True)
    speciman_type_blood_test_scan = models.CharField(max_length= 50, blank=True, null=True)
    speciman_type_nasal_throat_scan = models.CharField(max_length= 50, blank=True, null=True)
    

    priority = models.IntegerField(default= 0, blank=False, null=False)
    retest = models.IntegerField(default= 0, blank=False, null=False)

    de_pool = models.IntegerField(default= 0, blank=False, null=False)

    icmr_added = models.IntegerField(default= 0, blank= True, null= True)

    

class Patient_Address(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    state_name                      =   models.CharField(max_length=50, blank=True, null=True)
    district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    village_name                    =   models.CharField(max_length=50, blank=True, null=True)
    resident_type                   =   models.CharField(max_length=50, blank=True, null=True)
    zone_type                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_type                       =   models.CharField(max_length=50, blank=True, null=True)
    flat_door_no                    =   models.CharField(max_length=50, blank=True, null=True)
    main_road_no                    =   models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=250, blank=True, null=True)
    landmark = models.CharField(max_length=250, blank=True, null=True)
    # address_line1                   =   models.CharField(max_length=150, blank=True, null=True)
    # address_line2                   =   models.CharField(max_length=150, blank=True, null=True)
    ct_latitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    ct_longitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    


class Outside_Patient_Address(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    state_name                      =   models.CharField(max_length=50, blank=True, null=True)
    district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    village_name                    =   models.CharField(max_length=50, blank=True, null=True)
    resident_type                   =   models.CharField(max_length=50, blank=True, null=True)
    zone_type                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_type                       =   models.CharField(max_length=50, blank=True, null=True)
    flat_door_no                    =   models.CharField(max_length=50, blank=True, null=True)
    main_road_no                    =   models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=250, blank=True, null=True)
    landmark = models.CharField(max_length=250, blank=True, null=True)
    # address_line1                   =   models.CharField(max_length=150, blank=True, null=True)
    # address_line2                   =   models.CharField(max_length=150, blank=True, null=True)
    ct_latitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    ct_longitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)



class Patient_Testing(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    lab_received_date               =   models.DateField(auto_now_add=True)
    # testing_kit_id                =   models.CharField(max_length=50, blank=True, null=True)
    rtpcr_test = models.IntegerField(default=0, blank=True, null=True)
    testing_status               =   models.CharField(max_length=50, blank=True, null=True)
    ct_value                        =   models.IntegerField(  blank=True, null=True)
    comments                        =   models.CharField(max_length=150, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)

    

class Contact_Tracing(models.Model):

    covid_id = models.CharField(max_length=20, blank= False, null=False)
    name = models.CharField(max_length=150, blank=True, null=True)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    category = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    district_name_eng = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    city_name_eng = models.CharField(max_length=150, blank=True, null=True)
    block = models.CharField(max_length=150, blank=True, null=True)
    block_name_eng = models.CharField(max_length=150, blank=True, null=True)
    panchayat = models.CharField(max_length=150, blank=True, null=True)
    panchayat_name_eng = models.CharField(max_length=150, blank=True, null=True)
    village = models.CharField(max_length=150, blank=True, null=True)
    village_name_eng = models.CharField(max_length=150, blank=True, null=True)
    town = models.CharField(max_length=150, blank=True, null=True)
    town_name_eng = models.CharField(max_length=150, blank=True, null=True)
    ward_type = models.CharField(max_length=150, blank=True, null=True)
    ward = models.CharField(max_length=150, blank=True, null=True)
    ward_name_eng = models.CharField(max_length=150, blank=True, null=True)
    taluk = models.CharField(max_length=150, blank=True, null=True)
    taluk_name_eng = models.CharField(max_length=150, blank=True, null=True)
    bbmp_zone = models.CharField(max_length=150, blank=True, null=True)
    bbmp_zone_name_eng = models.CharField(max_length=150, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    building = models.CharField(max_length=150, blank=True, null=True)
    door_no = models.CharField(max_length=150, blank=True, null=True)

    ct_latitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    ct_longitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    date_of_contact_created = models.DateTimeField(auto_now_add=True)
    assigned_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # assigned_phc = models.ForeignKey(Master_PHC, on_delete=models.CASCADE ,blank=True, null=True)
    assigned_phc = models.CharField(max_length=150 ,blank=True, null=True)
    assigned_msc_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sample_collected = models.IntegerField(default=0, blank=True, null=True)



class ILI(models.Model):

    covid_id = models.CharField(max_length=20, blank= False, null=False)
    name = models.CharField(max_length=150, blank=True, null=True)
    mobile_number = models.CharField(max_length=12, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    category = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    block = models.CharField(max_length=150, blank=True, null=True)
    panchayat = models.CharField(max_length=150, blank=True, null=True)
    village = models.CharField(max_length=150, blank=True, null=True)
    town = models.CharField(max_length=150, blank=True, null=True)
    ward = models.CharField(max_length=150, blank=True, null=True)
    taluk = models.CharField(max_length=150, blank=True, null=True)
    bbmp_zone = models.CharField(max_length=150, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    building = models.CharField(max_length=150, blank=True, null=True)
    door_no = models.CharField(max_length=150, blank=True, null=True)

    ct_latitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    ct_longitude = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    date_of_contact_created = models.DateTimeField(auto_now_add=True)
    assigned_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # assigned_phc = models.ForeignKey(Master_PHC, on_delete=models.CASCADE ,blank=True, null=True)
    assigned_phc = models.CharField(max_length=150 ,blank=True, null=True)
    assigned_msc_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sample_collected = models.IntegerField(default=0, blank=True, null=True)    



class New_Entry_Contact_Tracing(models.Model):

    swab_collection = models.ForeignKey(Swab_Collection_Centre, on_delete=models.CASCADE, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    patient_type                 =   models.ForeignKey(Patient_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    contactee_name                    =   models.CharField(max_length=50, blank=True, null=True)
    contactee_mobile_number                    =   models.CharField(max_length=50, blank=True, null=True)
    # patient_name                    =   models.CharField(max_length=50, blank=True, null=True)
    patient_name                    =   models.CharField(max_length=50, blank=True, null=True)
    mobile_number                   =   models.CharField(max_length=15, blank=True, null=True)
    mobile_number_belongs_to        =   models.CharField(max_length=50, blank=True, null=True)
    gender                          =   models.CharField(max_length=10, blank=True, null=True)
    age                             =   models.IntegerField( blank=True, null=True)
    id_proof_type                   =   models.CharField(max_length=120, blank=True, null=True)
    aadhar_number                   =   models.CharField(max_length=12, blank=True, null=True)
    ration_card_number              =   models.CharField(max_length=15, blank=True, null=True)
    vaccine_status                  =   models.CharField(max_length=10, blank=True, null=True)
    vaccine_mobile_registered       =   models.CharField(max_length=150, blank=True, null=True)
    specimen_type                =   models.ForeignKey(Specimen_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    specimen_collection_date        =   models.DateField(auto_now_add=True, blank=True, null=True)
    testing_kit_barcode             =   models.ForeignKey(Testing_Kit_Barcode, on_delete=models.CASCADE, blank=True, null=True)
    patient_status                  =   models.CharField(max_length=50, blank=True, null=True)
    symptoms_list                   =   models.CharField(max_length=50, blank=True, null=True)
    test_type                    =   models.ForeignKey(Test_Type_Ref, on_delete=models.CASCADE,blank=True, null=True)
    srf_id                         =   models.CharField(max_length=50, blank=True, null=True)
    # swab_collection_status       =   models.CharField(max_length=50, blank=True, null=True, default='Pending')
    # swab_collection_result       =   models.CharField(max_length=50, blank=True, null=True, default='Not Dispached')
    swab_collection_status       =   models.IntegerField(blank=True, null=True, default=0)
    swab_collection_result       =   models.IntegerField(blank=True, null=True,)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)
    patient_testing_id              =   models.CharField(max_length=50, blank=True, null=True)
    co_morbidity              =   models.CharField(max_length=50, blank=True, null=True)
    co_morbidity_type              =   models.CharField(max_length=250, blank=True, null=True)
    old_srf_id = models.CharField(max_length=20, blank=True, null=True)
    pre_contact_person = models.CharField(max_length=20, blank=True, null=True)
    package_sampling = models.ForeignKey(Package_Sampling, on_delete=models.CASCADE, blank=True, null=True)

    rat_srf_id = models.CharField(max_length=50, blank=True, null=True)
    sample_status = models.CharField(max_length=150, blank=True, null=True)
    sample_rejected_reason = models.CharField(max_length=150, blank=True, null=True)

    reason_for_testing = models.TextField(blank=True, null=True)
    reason_for_testing_description = models.TextField(blank=True, null=True)

    rat_created_id = models.CharField(max_length=120, blank=True, null=True)

    arrival_date = models.CharField(max_length=120, blank=True, null=True)



class New_Entry_Contact_Tracing_Address(models.Model):

    new_entry_contact_tracing = models.ForeignKey(New_Entry_Contact_Tracing, on_delete=models.CASCADE, null=True, blank=True)
    state_name                      =   models.CharField(max_length=50, blank=True, null=True)
    district_name                   =   models.CharField(max_length=50, blank=True, null=True)
    city_name                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_name                       =   models.CharField(max_length=50, blank=True, null=True)
    taluk_name                      =   models.CharField(max_length=50, blank=True, null=True)
    panchayat_name                  =   models.CharField(max_length=50, blank=True, null=True)
    village_name                    =   models.CharField(max_length=50, blank=True, null=True)
    resident_type                   =   models.CharField(max_length=50, blank=True, null=True)
    zone_type                       =   models.CharField(max_length=50, blank=True, null=True)
    ward_type                       =   models.CharField(max_length=50, blank=True, null=True)
    flat_door_no                    =   models.CharField(max_length=50, blank=True, null=True)
    main_road_no                    =   models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=250, blank=True, null=True)
    # address_line1                   =   models.CharField(max_length=150, blank=True, null=True)
    # address_line2                   =   models.CharField(max_length=150, blank=True, null=True)
    pincode                         =   models.CharField(max_length=10, blank=True, null=True)
    create_timestamp                =   models.DateTimeField(auto_now_add=True,verbose_name="Create_TimeStamp",blank=True,null=True)
    last_update_timestamp           =   models.DateTimeField(auto_now_add=False,verbose_name="Last_Update_TimeStamp",blank=True,null=True)



class Phc_Id_Test_Kit_Id(models.Model):

    phc_id = models.IntegerField(blank=True, null=True)
    test_kit_id = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=1, blank=True, null=True)




class PHCTargetAssignment(models.Model):

    district_code = models.CharField(max_length=150, blank=True, null=True)
    dso = models.ForeignKey(DSO, on_delete=models.CASCADE, blank=True, null=True)
    dso_target = models.IntegerField(blank=True, null=True)
    dso_created_datetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    tho = models.ForeignKey(THO, on_delete=models.CASCADE, blank=True, null=True)
    tho_target = models.IntegerField(blank=True, null=True)
    tho_created_datetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    phc = models.ForeignKey(Master_PHC, on_delete=models.CASCADE, blank=True, null=True)
    phc_target = models.IntegerField(blank=True, null=True)
    phc_created_datetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    contact_tracing_target = models.IntegerField(blank=True, null=True)
    ili_target = models.IntegerField(blank=True, null=True)
    random_other_target = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)



class TargetAssignToUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    contact_tracing_target = models.IntegerField(blank=True, null=True)
    ili_target = models.IntegerField(blank=True, null=True)
    random_other_target = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class PHCLikedLabs(models.Model):
    phc_master = models.ForeignKey(Master_PHC, on_delete=models.CASCADE, blank=True, null=True)
    lab_master = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)



class GroupPlate(models.Model):

    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    plate_no = models.CharField(max_length= 150,blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class GroupSamples(models.Model):

    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    plate = models.ForeignKey(GroupPlate, on_delete=models.CASCADE, blank=True, null=True)
    # plate_no = models.IntegerField(blank=True, null=True)
    test_result = models.IntegerField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class PoolPlate(models.Model):

    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    plate_no = models.CharField(max_length= 150,blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class PoolSamples(models.Model):

    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    plate = models.ForeignKey(PoolPlate, on_delete=models.CASCADE, blank=True, null=True)
    pool_id = models.CharField(max_length=150, blank=True, null=True)
    # plate_no = models.IntegerField(blank=True, null=True)
    test_result = models.IntegerField(blank=True, null=True)
    submit_for_pool_testing = models.IntegerField(default=0, blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class ICMRDataPush(models.Model):

    patient_id = models.CharField(max_length= 250, blank= True, null= True)
    patient_name = models.CharField(max_length= 250, blank= True, null= True)
    gender = models.CharField(max_length= 250, blank= True, null= True)
    age = models.CharField(max_length= 250, blank= True, null= True)
    age_in = models.CharField(max_length= 250, blank= True, null= True)
    contact_number = models.CharField(max_length= 250, blank= True, null= True)
    contact_number_belongs_to = models.CharField(max_length= 250, blank= True, null= True)
    nationality = models.CharField(max_length= 250, blank= True, null= True)
    state = models.CharField(max_length= 250, blank= True, null= True)
    district = models.CharField(max_length= 250, blank= True, null= True)
    pincode = models.CharField(max_length= 250, blank= True, null= True)
    aadhar_number = models.CharField(max_length= 250, blank= True, null= True)
    passport_number = models.CharField(max_length= 250, blank= True, null= True)
    patient_category = models.CharField(max_length= 250, blank= True, null= True)
    address = models.CharField(max_length= 250, blank= True, null= True)
    patient_area = models.CharField(max_length= 250, blank= True, null= True)
    occupation = models.CharField(max_length= 250, blank= True, null= True)
    aarogya_setu_app_downloaded = models.CharField(max_length= 250, blank= True, null= True)
    contact_with_lab_confirmed_patient = models.CharField(max_length= 250, blank= True, null= True)
    srf_id = models.CharField(max_length= 250, blank= True, null= True)
    sample_cdate = models.CharField(max_length= 250, blank= True, null= True)
    sample_rdate = models.CharField(max_length= 250, blank= True, null= True)
    sample_type = models.CharField(max_length= 250, blank= True, null= True)
    sample_id = models.CharField(max_length= 250, blank= True, null= True)
    sample_collected_from = models.CharField(max_length= 250, blank= True, null= True)
    status = models.CharField(max_length= 250, blank= True, null= True)
    symptoms = models.CharField(max_length= 250, blank= True, null= True)
    date_of_onset_of_symptoms = models.CharField(max_length= 250, blank= True, null= True)
    underlying_medical_condition = models.CharField(max_length= 250, blank= True, null= True)
    vaccine_recevied = models.CharField(max_length= 250, blank= True, null= True)
    vaccine_type = models.CharField(max_length= 250, blank= True, null= True)
    vaccine_dose1_date = models.CharField(max_length= 250, blank= True, null= True)
    vaccine_dose2_date = models.CharField(max_length= 250, blank= True, null= True)
    hospitalized  = models.CharField(max_length= 250, blank= True, null= True)
    hospital_name  = models.CharField(max_length= 250, blank= True, null= True)
    hospitalization_date  = models.CharField(max_length= 250, blank= True, null= True)
    hospital_state  = models.CharField(max_length= 250, blank= True, null= True)
    hospital_district  = models.CharField(max_length= 250, blank= True, null= True)
    sample_tdate = models.CharField(max_length= 250, blank= True, null= True)
    testing_kit_used  = models.CharField(max_length= 250, blank= True, null= True)
    covid19_result_egene  = models.CharField(max_length= 250, blank= True, null= True)
    ct_value_screening  = models.CharField(max_length= 250, blank= True, null= True)
    orf1b_confirmatory  = models.CharField(max_length= 250, blank= True, null= True)
    ct_value_orf1b  = models.CharField(max_length= 250, blank= True, null= True)
    rdrp_confirmatory  = models.CharField(max_length= 250, blank= True, null= True)
    ct_value_rdrp  = models.CharField(max_length= 250, blank= True, null= True)
    final_result_of_sample = models.CharField(max_length= 250, blank= True, null= True)
    repeat_sample = models.CharField(max_length= 250, blank= True, null= True)
    transport_mode_used_to_visit_testing_facility  = models.CharField(max_length= 250, blank= True, null= True)
    remarks = models.CharField(max_length= 250, blank= True, null= True)
    lab_id  = models.CharField(max_length= 250, blank= True, null= True)
    lab_code = models.CharField(max_length= 250, blank= True, null= True)

    updated_samples_status = models.IntegerField(default=0, blank=True, null=True)
                    



class Phc_MSC_Id_Test_Kit_Id(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    phc_id = models.IntegerField(blank=True, null=True)
    test_kit_id = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=1, blank=True, null=True)




class Lab_RTPCR_Test_Kit_Id(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    master_labs = models.ForeignKey(Master_Labs, on_delete= models.CASCADE, blank=True, null=True)
    test_kit_id = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=1, blank=True, null=True)




class MergedPlateDetails(models.Model):
    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    plate_no = models.CharField(max_length= 150,blank=True, null=True)
    testing_status = models.IntegerField(default= 0, blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)





class MergedPlateSamples(models.Model):
    test_lab = models.ForeignKey(Testing_Lab_Facility, on_delete=models.CASCADE, blank=True, null=True)
    master_lab = models.ForeignKey(Master_Labs, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    merge_plate = models.ForeignKey(MergedPlateDetails, on_delete=models.CASCADE, blank=True, null=True)
    ind_pool_id = models.CharField(max_length=150, blank=True, null=True)
    # plate_no = models.IntegerField(blank=True, null=True)
    test_result = models.IntegerField(blank=True, null=True)
    submit_for_testing = models.IntegerField(default=0, blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)


