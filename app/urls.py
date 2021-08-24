from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


app_name = 'app'


router = routers.DefaultRouter()
router.register('get-patient-all', PatientModelView)
router.register('get-patient-address-all', PatientAddressModelView)
router.register('get-patient-testing-all', PatientTestingModelView)
router.register('get-patient-reference-all', PatientTypeRefModelView)

router.register('get-specimen-type-reference-all', SpecimenTypeRefModelView)
router.register('get-test-type-reference-all', TestTypeRefModelView)
router.register('get-swab-collection-status-all', SwabCollectionStatusRefModelView)
router.register('get-testing-status-reference-all', TestingStatusRefModelView)

router.register('get-testing-kit-barcode-all', CTestingKitBarcodeModelView)
router.register('get-user-role-reference-all', UserRoleRefModelView)
router.register('get-package-sampling-all', PackageSamplingModelView)
router.register('swab-collection-center-all', SwabCollectionCentreModelView)

router.register('get-tho-all', THOModelView)
router.register('get-dso-all', DSOModelView)
router.register('get-ssu-all', SSUModelView)
router.register('get-testing-lab-facility-all', TestingLabFacilityModelView)

router.register('get-master-zone-all', Master_ZoneModelView)
router.register('get-master-ward-all', Master_WardModelView)
router.register('get-master-village-all', Master_VillageModelView)
router.register('get-master-pachayat-all', Master_PanchayatModelView)
router.register('get-master-block-all', Master_BlockModelView)
router.register('get-district-all', DistrictModelView)
router.register('get-master-lab-all', Master_LabModelView)



urlpatterns = [
    path('', include(router.urls)),


    path('add-patient/', AddPatient.as_view()),
    path('contact-testing-offline/', ContectTestingOffline.as_view()),
    path('contact-testing-date-wise-dump/', ContectTestingDateWiseDump.as_view()),
    path('contact-testing-date-wise-urban-dump/', ContectTestingDateWiseUrbanDump.as_view()),
    path('contact-testing-date-wise-rural-dump/', ContectTestingDateWiseRuralDump.as_view()),
    path('get-otp-details/', GetOTPData.as_view()),
    path('collection-status/', CollectionDetailsAndStatus.as_view()),
    path('get-phc-user-added-patients/', GetPHCUseraddedPatients.as_view()),
    path('get-phc-user-package-samples/', GetPHCUserPackageList.as_view()),
    path('update-patient-collection-status/', UpdatePatientCollectionStatus.as_view()),


    ####################     Packages Urls     ####################
    path('create-package/', CreatePackage.as_view()),
    path('accept-package/', AcceptPackage.as_view()),
    path('get-tho-packages-details/', GetTHOPackageData.as_view()),
    path('get-dso-packages-details/', GetDSOPackageData.as_view()),
    path('get-ssu-packages-details/', GetSSUPackageData.as_view()),
    path('get-tlc-packages-details/', GetTLCPackageData.as_view()),
    path('get-tl-ops-packages-details/', GetTLOPSPackageData.as_view()),
    path('update-dispatch-package-samples/', UpadtePackagetoLabOrHigherOfc.as_view()),
    path('get-all-package-details/', GetAllPackageDetails.as_view()),
    path('get-package-patient-details/', GetPackageSamples.as_view()),
    path('update-package-patient-samples/', AcceptPackagePatientSamples.as_view()),
    path('get-rejected-samples/', GetRejectedSamples.as_view()),

    path('get-phc-user-location-details/', GetPHCUserLocationDetails.as_view()),
    path('get-phc-user-location-village-filter/', GetPHCUserVillageDataFilter.as_view()),
    path('get-phc-user-location-ward-filter/', GetPHCUserWardDataFilter.as_view()),
    path('get-master-table-dropdown/', MasterTableFilterData.as_view()),
    path('get-testing-kits/', GetTestingKitDetails.as_view()),
    path('check-already-tested-patients/', ChackAlreadyTestedPatients.as_view()),
    path('check-contact-tracing-patients/', ChackContactTracingPatients.as_view()),
    path('get-already-tested-patient-details/', GetAlreadyTestedPatientsData.as_view()),
    path('get-contact-tracing-patient-details/', GetContactTracingPatientsData.as_view()), # Two Fun 1
    path('lab-receive-packages/', LabReceivePackage.as_view()),


    ####################     Lab Urls     ####################
    path('dso-update-test-lab/', DSOReferenceTlabData.as_view()),
    path('get-testing-labs/', GetTestingLabs.as_view()),
    path('check-reference-test-lab/', CheckPackageReferenceCheck.as_view()),
    path('update-patient-lab-test-result/', UpdatePatientTestingResult.as_view()),
    path('generate-lab-id/', GenerateLabId.as_view()),
    path('phc-auto-assign-labs/', CheckPHCLabAvailable.as_view()),

    

    path('group-samples/', GroupSmaples.as_view()),
    path('pool-samples/', PoolSmaples.as_view()),


    ####################     User related Urls     ####################
    path('generate-username/', GenerateUsername.as_view()),
    path('create-new-phc-users/', CreateUser.as_view()),
    path('suspend-user/', UserSuspend.as_view()),
    path('get-update-user-details/', GetUserAndUpdateUser.as_view()),    
    path('get-all-mo-phc-users/', GetMOALLUserDetails.as_view()),


    ####################     Filter Urls     ####################
    path('phc-date-filter/', PHCUserDAteFilter.as_view()),
    path('phc-contact-tracing-date-filter/', PHCContactTracingDAteFilter.as_view()),
    path('phc-status-filter/', PHCUseStatusFilter.as_view()),
    path('phc-test-type-filter/', PHCUseTestTypeFilter.as_view()),
    path('get-phc-mobile-swab-collectors/', GetPHCMobileUsers.as_view()),
    
    
    ####################     Contact Tracing Urls     ####################
    path('msc-assigned-contact-tracing/', MSCAssignedData.as_view()),
    path('get-phc-mo-contact-tracing-data/', AllContactTracingData.as_view()),
    path('assign-contact-tracing-data-to-msc-user/', AssignContactTracing.as_view()),
    path('get-contactee-details/', GetContacteePatientDetails.as_view()), # Two Fun 1
    path('get-assigned-completed-pending-msc-count/', GetAssignedCompletedPendingMscCounts.as_view()),


    ####################     Dashboard Urls     ####################
    path('phc-dashboard-count/', GetPHCDashboardDetails.as_view()),
    path('get-tho-dso-ssu-dashboard-details/', GetThoDsoSsuDashboardDetails.as_view()),
   


    ####################     SUU LABS     ####################
    path('get_taluk/', Posttaluk.as_view()),
    path('post_lab/', Postlabs.as_view()),
    path('get-edit-lab/', GetEditLabs.as_view()),
    path('edit-update-lab/', EditUpdateLabs.as_view()),
    path('get_all_lab/', get_all_labs.as_view()),
    path('lab_delete/', Postdelete.as_view()),

    path('add_testing_kit/', Posttestkit.as_view()),
    path('all_testing_kit/', All_testkit.as_view()),

    path('all_patients/', get_all_patients.as_view()),
    path('all_contact_testing/', get_all_contact_testing.as_view()),

    path('all_users/', get_all_user.as_view()),    #pending         #swab collectors    
    path('all_generate_pack/', get_all_generated_package.as_view()),#track packages
    path('all_laballocated/', get_all_lab_allocation.as_view()),    #lab allocation



    ####################     CREATE USERNAME     ####################
    path('create-usernames/', CreatePHCUserNames.as_view()),



    ####################      FilterDSOLabsBasedLocation       ##########################
    path('filter-labs-based-on-distance/', FilterDSOLabsBasedLocation.as_view()),


    ####################      TESTING KIT URLS      ##########################
    path('assign-test-kit-to-phc/', AssignTestKitToPhc.as_view()),
    path('delete-phc-test-kits/', DeletePHCTestKit.as_view()),
    # path('get-phc-test-kits/', GetPhcTestKit.as_view()),
    path('get-phc-all-test-kits/', TestingKitBarcode.as_view()),
    path('get-mo-available-test-kits/', GetAvailableMOTestKits.as_view()),




    ####################      TARGET ASSIGN TO USER      ##########################
    path('target-assign-to-user/', TargetAssigntoUser.as_view()),
    path('user-target-assigned-counts/', UserTargetAssignedCounts.as_view()),

    path('phc-targets/', PHCTargets.as_view()),
    path('get-assigned-user-targets/', GetAssignedUserTargets.as_view()),

    path('get-ssu-dso-details/', GetSSUTargetSetup.as_view()),
    path('target-for-dso/', TargetForDSO.as_view()),
    path('get-dso-target/', GetDSOTarget.as_view()),
    path('target-for-tho/', TargetForTHO.as_view()),
    path('get-tho-target/', GetTHOTarget.as_view()),
    path('target-for-phc/', TargetForPHC.as_view()),





    ####################      REPORTS      ####################
    path('get-phc-user-added-patients-report/', GetPHCUseraddedPatientsReport.as_view()),
    path('phc-date-wise-collection-status-result-count/', PHCDateWiseCollectionStatusAndResultTotalCount.as_view()),
    path('phc-date-wise-contact-testing-status-report-count/', PHCDateWiseContectTestingStatusReport.as_view()),
    path('phc-date-wise-contact-testing-status-individual-user-count-report/', PHCDateWiseContectTestingStatusIndividualUserReport.as_view()),
    path('phc-date-wise-contact-testing-status-individual-user-detail-report/', PHCDateWiseContectTestingStatusIndividualUserDetailReport.as_view()),
    path('phc-date-wise-collection-status-result-count-individual-data/', PHCDateWiseCollectionStatusAndResultTotalCountndividual.as_view()),
    path('phc-date-wise-samples-rejected-counts/', PHCDateWiseSampleRejectedCountReport.as_view()),
    path('phc-date-wise-samples-rejected-indetail-report/', PHCDateWiseSampleRejectedIndetailReport.as_view()),
    path('phc-target-vs-actual-swab-collection/', PHCTargetvsActualSwabCollection.as_view()),
    path('phc-target-vs-actual-swab-collection-date-wise/', PHCTargetvsActualSwabCollectionDateView.as_view()),
    path('phc-swab-collection-by-swab-collector/', SwabCollectionBySwabCollector.as_view()),
    path('phc-swab-collection-by-swab-collector-wise/', SwabCollectionBySwabCollectorSwabcollectorView.as_view()),
    path('phc-swab-package-dispatch-details-count/', SwabPackageDespatchDetailsCount.as_view()),
    path('phc-swab-package-dispatch-indetail/', SwabPackageDespatchDetails.as_view()),
    path('phc-package-lab-wise-report/', PHCPackageLabWiseReport.as_view()),

    path('tho-target-vs-actual-swab-collection/', THOTargetvsActualSwabCollection.as_view()),
    path('tho-swab-dispatch-details/', THOSwabDispatchDetails.as_view()),
    path('tho-package-lab-wise-report/', THOPackageLabWiseReport.as_view()),

    path('dso-target-vs-actual-swab-collection/', DSOTargetvsActualSwabCollection.as_view()),
    path('dso-target-vs-actual-swab-collection-view/', DSOTargetvsActualSwabCollectionView.as_view()),
    path('dso-swab-dispatch-details/', DSOSwabDispatchDetails.as_view()),
    path('dso-package-lab-wise-report/', DSOPackageLabWiseReport.as_view()),

    path('ssu-date-wise-total-target-count-report/', SSUDateWiseTotalTargetCountReport.as_view()),
    path('ssu-date-wise-total-target-count-details-report/', SSUViewTotalTargetCountDetails.as_view()),
    path('ssu-all-swab-collector-team/', SSUSwabCollectorsTeam.as_view()),
    path('ssu-total-samples-collected/', SSUTotalSampleCollected.as_view()),
    path('ssu-get-date-wise-generated-package-report/', SSUDateWiseGeneratedPackageReport.as_view()),
    path('ssu-get-date-wise-generated-package-details-report/', SSUDateWiseGeneratedPackageDetailsReport.as_view()),
    path('ssu-get-lab-wise-delay-report/', SSUGetLabwiseDelayReport.as_view()),
    path('ssu-get-overall-lab-delay-report/', SSUGetOverallLabDelayD4.as_view()),
    path('ssu-get-sysc-asysc-report/', SSUGetMasterSysAsym.as_view()),
    path('ssu-get-rat-rtpcr-positivity-report/', SSUGetMasterRatRtpcrPositivityReport.as_view()),



    ####################      TLAB OPS      ####################
    path('tlab-ops-recieve-package/', UpdatePatientLabId.as_view()),

    path('get-tlab-ops-plate-details/', GetTlabOPSPlateData.as_view()),
    path('get-tlab-ops-plate-patient-details/', GetTlabOPSPlatePatientDetails.as_view()),
    path('update-group-samples-test-result/', UpdateGroupSamplesTestResult.as_view()),
    path('update-patient-pool-lab-id/', UpdatePatientPoolLabId.as_view()),
    path('get-tlab-ops-pool-plate-details/', GetTlabOPSPoolPlateData.as_view()),
    path('get-tlab-ops-pool-patient-details/', GetTlabOPSPoolPlatePatientDetails.as_view()),
    path('update-pool-samples-test-result/', UpdatePoolSamplesTestResult.as_view()),
    path('pool-positive-patient-details/', PatientPoolTestResultView.as_view()),



    path('accept-tho-dso-ssu-package/', AcceptPackageSamples.as_view()),


    path('automate-patient-create/', AutomatePatientCreate.as_view()),
    path('automate-complete-created-samples/', CompleteCreatedSamples.as_view()),

    path('delete-master-phc/', DeleteMasterPHC.as_view()),



    ####################      ICMR      ####################
    path('icmr-add-record/', ICMRAddPatientRecord.as_view()),
    path('icmr-access-token/', ICMRGetAccessToken.as_view()),










    # Lab_Facility
    path('lab_facility/', GetPostTesting_Lab_Facility.as_view(), name="lab_facility"),
    path('lab_facility_by_id/<int:pk>', GetPutPatchTesting_Lab_Facility.as_view(), name="lab_facility_by_id"),

    # SSU
    path('ssu/', GetPostSSU.as_view(), name="ssu"),
    path('ssu_by_id/<int:pk>', GetPutPatchSSU.as_view(), name="ssu_by_id"),

    # DSO
    path('dso/', GetPostDSO.as_view(), name="dso"),
    path('dso_by_id/<int:pk>', GetPutPatchDSO.as_view(), name="dso_by_id"),

    # THO
    path('tho/', GetPostTHO.as_view(), name="tho"),
    path('tho_by_id/<int:pk>', GetPutPatchTHO.as_view(), name="tho_by_id"),

    # Swab_Collection_Centre
    path('swab_coll_center/', GetPostSwab_Collection_Centre.as_view(), name="swab_coll_center"),
    path('swab_coll_center_by_id/<int:pk>', GetPutPatchSwab_Collection_Centre.as_view(), name="swab_coll_center_by_id"),

    # Testing_Kit_Barcode
    path('testing_kit_barcode/', GetPostTesting_Kit_Barcode.as_view(), name="testing_kit_barcode"),
    path('testing_kit_barcode_by_id/<int:pk>', GetPutPatchTesting_Kit_Barcode.as_view(), name="testing_kit_barcode_by_id"),

    # Package_Sampling
    path('package_sampling/', GetPostPackage_Sampling.as_view(), name="package_sampling"),
    path('package_sampling_by_id/<int:pk>', GetPutPatchPackage_Sampling.as_view(), name="package_sampling_by_id"),

    path('auth-login/', CustomAuthToken.as_view()),

]
