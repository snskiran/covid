from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(Patient)

@admin.register(Patient)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'mobile_number', 'group_samples', 'pool_samples', 'test_type', 'test_lab_id')



# admin.site.register(Patient_Address)

@admin.register(Patient_Address)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'patient', )

admin.site.register(Patient_Testing)
admin.site.register(Patient_Type_Ref)
admin.site.register(Specimen_Type_Ref)
admin.site.register(Test_Type_Ref)
admin.site.register(Swab_Collection_Status_Ref)
admin.site.register(Testing_Status_Ref)
# admin.site.register(Testing_Lab_Facility)
# admin.site.register(SSU)
# admin.site.register(DSO)
# admin.site.register(THO)

# admin.site.register(SSU)
# admin.site.register(DSO)
# admin.site.register(THO)

@admin.register(SSU)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id','ssu_name')

@admin.register(DSO)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'dso_name')

@admin.register(THO)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'tho_name')
# admin.site.register(Swab_Collection_Centre)
# admin.site.register(Testing_Kit_Barcode)
# admin.site.register(Package_Sampling)
# admin.site.register(User_Role_Ref)

@admin.register(User_Role_Ref)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'user_role_name', 'user')


@admin.register(Testing_Lab_Facility)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'testing_lab_facility_name', 'district_name', 'lab_type', 'rat_rt_pcr',)


@admin.register(Swab_Collection_Centre)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'swab_collection_centre_name','role')



@admin.register(Package_Sampling)
class TestingLabAdmin(ImportExportModelAdmin):
	list_display = ('id', 'package_sampling_name', 'package_type_status', 'package_type_action', 'test_lab_id', 'created_group_pool_data', 'samples_count', 'package_sampling_barcode')



@admin.register(Master_Zone)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'district_code', 'district_name_kan', 'district_name_eng', 'bbmp_zone_no_ksrsac', 'software_zone_no', 'zone_name', 'ksrsac_ward_no', 'ward_name')



@admin.register(Master_Ward)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'district_code', 'district_name_kan', 'district_name_eng', 'software_zone_no', 'zone_name', 'ksrsac_ward_no', 'ward_no', 'ward_name', 'ksrsac_dist_code', 'ksrsac_town_code', 'new_town_code', 'town_name')



@admin.register(Master_Village)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'district_code', 'block_code', 'panchayat_code', 'village_code', 'village_name_kan', 'village_name_eng')



@admin.register(Master_Panchayat)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'district_code', 'block_code', 'panchayat_code', 'panchayat_name_kan', 'panchayat_name_eng')



@admin.register(Master_Block)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'district_code', 'block_code', 'block_name_kan', 'block_name_eng')



@admin.register(Master_District)
class WardMasterAdmin(ImportExportModelAdmin):
	# list_display = ('id', 'district_code', 'district_lat', 'district_lon', 'district_name_kan', 'district_name_eng',)
	list_display = ('id', 'district_code', 'district_name_eng',)



admin.site.register(Roles)
admin.site.register(Outside_Patient_Address)


@admin.register(Contact_Tracing)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'name', 'mobile_number', 'age', 'gender',)




@admin.register(Master_PHC)
class PHCMaterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'sys_id', 'district_name_eng', 'block_name_eng', 'village_name_eng', 'block_code', 'panchayat_code', 'village_code', 'phc_name', 'phc_code')


@admin.register(Master_Labs)
class TestingLabMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'lab_name', 'gps_lat', 'gps_lon', 'district_name', 'lab_type', 'rat_rt_pcr',)
	


@admin.register(Testing_Kit_Barcode)
class TestingKitBarcodeAdmin(ImportExportModelAdmin):
	list_display = ('id', 'testing_kit_barcode_name',)


@admin.register(RTPCR_Test_Kits)
class RTPCRTestingKitBarcodeAdmin(ImportExportModelAdmin):
	list_display = ('id', 'rtpcr_test_kit_name',)



admin.site.register(New_Entry_Contact_Tracing)
admin.site.register(New_Entry_Contact_Tracing_Address)

admin.site.register(Testing_Lab_Master)

# admin.site.register(Testing_Lab_Master_One)
# admin.site.register(Master_Labs)

admin.site.register(Phc_Id_Test_Kit_Id)
# admin.site.register(PHCTargetAssignment)
# admin.site.register(TargetAssignToUser)


admin.site.register(ILI)



admin.site.register(GroupPlate)
admin.site.register(GroupSamples)
admin.site.register(PoolPlate)
# admin.site.register(PoolSamples)

@admin.register(PoolSamples)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'plate', 'pool_id', 'test_result', 'create_datetime',)



@admin.register(TargetAssignToUser)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'user', 'contact_tracing_target', 'ili_target', 'random_other_target', 'created_datetime')


# admin.site.register(PHCTargetAssignment)

@admin.register(PHCTargetAssignment)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'created_datetime', 'dso_target', 'tho', 'tho_target', 'phc', 'phc_target', 'contact_tracing_target', 'ili_target', 'random_other_target', )





# admin.site.register(ICMRDataPush)

@admin.register(ICMRDataPush)
class WardMasterAdmin(ImportExportModelAdmin):
	list_display = ('id', 'patient_id')




admin.site.register(MergedPlateDetails)
admin.site.register(MergedPlateSamples)



