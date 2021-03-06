import datetime
from functools import partial
from django.core.checks import messages
from django.db import models
from rest_framework import response
from .serializers import *
from .models import *

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.db.models import Q, F, Count, Sum
from django.http import JsonResponse, request

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics,viewsets
from rest_framework.generics import GenericAPIView, RetrieveAPIView

import requests
from datetime import datetime as asdatetime
from datetime import timedelta
# import datetime as dttm
from datetime import date as dt
import json
import os
from django.http import Http404
from django.db.models import Q

import random

import ast
import base64

from math import radians, cos, sin, asin, sqrt

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from app.urls_variables import *


class AccessENVData(APIView):

    def get(self, request):

        print("HELLOOOO     ", token_url)



# Create your views here.

class PatientModelView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Patient.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientAddressModelView(viewsets.ModelViewSet):
    queryset = Patient_Address.objects.all()
    serializer_class = PatientAddressSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Patient_Address.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientTestingModelView(viewsets.ModelViewSet):
    queryset = Patient_Testing.objects.all()
    serializer_class = PatientTestingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Patient_Testing.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientTypeRefModelView(viewsets.ModelViewSet):
    queryset = Patient_Type_Ref.objects.all()
    serializer_class = PatientTypeRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Patient_Type_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecimenTypeRefModelView(viewsets.ModelViewSet):
    queryset = Specimen_Type_Ref.objects.all()
    serializer_class = SpecimenTypeRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Specimen_Type_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestTypeRefModelView(viewsets.ModelViewSet):
    queryset = Test_Type_Ref.objects.all()
    serializer_class = TestTypeRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Test_Type_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SwabCollectionStatusRefModelView(viewsets.ModelViewSet):
    queryset = Swab_Collection_Status_Ref.objects.all()
    serializer_class = SwabCollectionStatusRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Swab_Collection_Status_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestingStatusRefModelView(viewsets.ModelViewSet):
    queryset = Testing_Status_Ref.objects.all()
    serializer_class = TestingStatusRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Testing_Status_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class CTestingKitBarcodeModelView(viewsets.ModelViewSet):
    queryset = Testing_Kit_Barcode.objects.all()
    serializer_class = TestingKitBarcodeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Testing_Kit_Barcode.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRoleRefModelView(viewsets.ModelViewSet):
    queryset = User_Role_Ref.objects.all()
    serializer_class = UserRoleRefSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = User_Role_Ref.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class PackageSamplingModelView(viewsets.ModelViewSet):
    queryset = Package_Sampling.objects.all()
    serializer_class = PackageSamplingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Package_Sampling.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SwabCollectionCentreModelView(viewsets.ModelViewSet):
    queryset = Swab_Collection_Centre.objects.all()
    serializer_class = SwabCollectionCentreSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Swab_Collection_Centre.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class THOModelView(viewsets.ModelViewSet):
    queryset = THO.objects.all()
    serializer_class = THOSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = THO.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class DSOModelView(viewsets.ModelViewSet):
    queryset = DSO.objects.all()
    serializer_class = DSOSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = DSO.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SSUModelView(viewsets.ModelViewSet):
    queryset = SSU.objects.all()
    serializer_class = SSUSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = SSU.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestingLabFacilityModelView(viewsets.ModelViewSet):
    queryset = Testing_Lab_Facility.objects.all()
    serializer_class = TestingLabFacilitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Testing_Lab_Facility.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



class Master_LabModelView(viewsets.ModelViewSet):
    queryset = Master_Labs.objects.all()
    serializer_class = Master_LabSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Labs.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    

class Master_ZoneModelView(viewsets.ModelViewSet):
    queryset = Master_Zone.objects.all()
    serializer_class = Master_ZoneSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Zone.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



class Master_WardModelView(viewsets.ModelViewSet):
    queryset = Master_Ward.objects.all()
    serializer_class = Master_WardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Ward.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



class Master_VillageModelView(viewsets.ModelViewSet):
    queryset = Master_Village.objects.all()
    serializer_class = Master_VillageSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Village.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



class Master_PanchayatModelView(viewsets.ModelViewSet):
    queryset = Master_Panchayat.objects.all()
    serializer_class = Master_PanchayatSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Panchayat.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



class Master_BlockModelView(viewsets.ModelViewSet):
    queryset = Master_Block.objects.all()
    serializer_class = Master_BlockSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_Block.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)




class DistrictModelView(viewsets.ModelViewSet):
    queryset = Master_District.objects.all()
    serializer_class = DistrictSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            id = instance.id

            self.perform_destroy(instance)
            user_data = Master_District.objects.filter(id=id).delete()

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
    

def paginatorCreation(query_data, page_no):

    paginator = Paginator(query_data, 10)
    try:
        paginator_data = paginator.page(page_no)
    except PageNotAnInteger:
        paginator_data = paginator.page(1)
    except EmptyPage:
        paginator_data = paginator.page(paginator.num_pages)

    return paginator_data    
    

    
    
    
def getToken():

    acc_url = auth_token_url
    token_body = {'grant_type': auth_token_grant_type ,'username': auth_token_username, 'password': auth_token_password}
    acc_json_data = json.dumps(token_body)
    acc_tok_res = requests.post(acc_url, data= token_body)

    acc_token_res = acc_tok_res.json()
    body_hdr = acc_token_res['access_token']


    header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
    json_header = json.dumps(header)

    return header    

    


#########################          LOGIN          #########################
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        data = request.data
        print(data)

        serializer = self.serializer_class(data=request.data, context={'request': request})
                                               
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] 
        print("USERRRRR", user.pk)
        
        
        if user:

                user_master_data = User_Role_Ref.objects.get(Q(user_id = user.pk))

                print(user_master_data.role_id)

                roles = Roles.objects.get(id= user_master_data.role_id)
                if user_master_data.suspend == False:
                
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({
                        'token': token.key,
                        'user_id': user.pk, 
                        'username':user.username,
                        'first_name': user.first_name,
                        'user_role_id':roles.role_name,
                        'user_role_name':user_master_data.user_role_name, 
                        'message':'Login Successful'
                    }, status= status.HTTP_200_OK)
                else:
                    return Response({'message':'User Suspended'}, status= status.HTTP_401_UNAUTHORIZED)
        
        else:
             return Response({'message':"Something Went Wrong"})




#########################          ADD PATIENT          #########################
class AddPatient(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print("DATA", data)

        reason_testing = data.get('reason_testing')
        reason = data.get('reason')
        patient_type = data.get('patient_type')
        patient_name = data.get('patient_name')
        mobile_number_belongs_to = data.get('mobile_number_belongs_to')
        mobile_number = data.get('mobile_number')
    
        otp_no = data.get('otp_no')
        states = data.get('states')
        district_name = data.get('district_name')
        resident_type = data.get('resident_type')
        ward_type = data.get('ward_type')
        city_name = data.get('city_name')
        taluk_name = data.get('taluk_name')
        village_name = data.get('village_name')
        panchayat_name = data.get('panchayat_name')
        zone_name = data.get('zone_name')
        ward_name = data.get('ward_name')
        flat_door_no = data.get('flat_door_no')
        main_road_no = data.get('main_road_no')
        pincode = data.get('pincode')
        gender = data.get('gender')
        age = data.get('age')
        age_type = data.get('age_type')
        idProof_type = data.get('idProof_type')

        aadhar_number = data.get('aadhar_number')
        ration_card_number = data.get('ration_card_number')
        speciman_type = data.get('speciman_type')
        speciman_collection_date = data.get('speciman_collection_date')
        patient_status_type = data.get('patient_status_type')
        symptoms = data.get('symptoms')
        co_morbidity = data.get('co_morbidity')
        co_morbidity_type = data.get('co_morbidity_type')
        test_type = data.get('test_type')
        old_srf_id = data.get('old_srf_id')
        
        vaccine_status = data.get('vaccine_status')
        con_mobile_number = data.get('con_mobile_number')
        existing_mobile_number = data.get('existing_mobile_number')
        user_id = data.get('user_id')

        locality = data.get('locality')
        landmark = data.get('landmark')

        arrival_date = data.get('arrival_date')

        rat_created_id_data = data.get('rat_created_id')

        generate_srf = random.randint(100000000, 999999999)

        barcode = data.get('barcode')


        father_name = data.get('father_name')
        occupation = data.get('occupation')
        mode_of_transport = data.get('mode_of_transport')
        arogya_setu_app = data.get('arogya_setu_app')
        vaccine_type = data.get('vaccine_type')
        first_dose_date = data.get('first_dose_date')
        hospitalized = data.get('hospitalized')
        driver_license = data.get('driver_license')
        passport = data.get('passport')

        sample_collected_from = data.get('sample_collected_from')

        # Encode
        aadhar_bytes = str(aadhar_number).encode('ascii')
        base64_bytes = base64.b64encode(aadhar_bytes)
        encriptrd_aadhar = base64_bytes.decode('ascii')
        
        # Decode
        # base64_message = encriptrd_aadhar
        # base64_bytes = base64_message.encode('ascii')
        # aadhar_bytes = base64.b64decode(base64_bytes)
        # aadhar_number = aadhar_bytes.decode('ascii')

        print(reason_testing)
        print(reason)
        print(patient_type)
        print(patient_name)
        print(mobile_number_belongs_to)
        print(mobile_number)
        print(otp_no)
        print(states)
        print(district_name)
        print(resident_type)
        print(ward_type)
        print(city_name)
        print(taluk_name)
        print(village_name)
        print(panchayat_name)
        print(zone_name)
        print(ward_name)
        print(flat_door_no)
        print(main_road_no)
        print(pincode)
        print(gender)
        print(age)
        print(idProof_type)
        print(aadhar_number)
        print(ration_card_number)
        print(speciman_type)
        print(speciman_collection_date)
        print(patient_status_type)
        print(symptoms)
        print(co_morbidity)
        print(co_morbidity_type)
        print(test_type)
        print(old_srf_id)
        print(vaccine_status)
        print(con_mobile_number)
        print(existing_mobile_number)
        print(user_id)
        print(locality)
        print(landmark)
        print(arrival_date)
        print(rat_created_id_data)
        print(generate_srf)
        print(barcode)

        patient_type_ref_data = Patient_Type_Ref.objects.get(patient_type_name= patient_type)
        specimen_type_ref_data = Specimen_Type_Ref.objects.get(specimen_type_name= speciman_type)
        # testing_type_ref_data = Testing_Kit_Barcode.objects.get(testing_kit_barcode_name= testing_kit_barcode)
        test_type_ref_data = Test_Type_Ref.objects.get(test_type_name= test_type)
       
        symptoms_list = []
        if symptoms:
            for i in symptoms:
                print(i)
                if isinstance(i, str):
                    dist_type = ast.literal_eval(i)
                    symptoms_list.append(dist_type['name'])
                else:
                    symptoms_list.append(i['name'])
        
        co_morbidity_type_list = []
        for i in co_morbidity_type:
            print(i)
            # print(i['name'])
            if isinstance(i, str):
                dist_type = ast.literal_eval(i)
                co_morbidity_type_list.append(dist_type['name'])
            else:
                co_morbidity_type_list.append(i['name'])

        


        record_create_timestamp = ''

        rat_created_id = 0


        user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

        get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

        srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

        yr = str(asdatetime.now().year)[2:]
        mn = str(asdatetime.now().month).zfill(2)
        dd = str(asdatetime.now().day)

        srf_data = srf_dist_code+yr+mn+dd

        last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

        if last_srf_id:
            srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
            print(srf_data)
        else:
            srf_data = srf_data + '1'.zfill(5)

        if rat_created_id_data:
            get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
            srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
            print("RAT SRF ID")
            print(srf_data)

        if data.get('id'):
                Contact_Tracing.objects.filter(id= data.get('id')).update(sample_collected= 1)

        patients_data = Patient.objects.create(reason_for_testing= reason_testing, reason_for_testing_description= reason, patient_type_id= patient_type_ref_data.id,
                                        added_by_id= user_id,
                                        patient_name= patient_name, 
                                        mobile_number= mobile_number, 
                                        mobile_number_belongs_to= mobile_number_belongs_to,

                                        gender= gender, 
                                        age= age,
                                        age_type= age_type,
                                        id_proof_type= idProof_type,
                                        aadhar_number= encriptrd_aadhar,
                                        ration_card_number= ration_card_number, 
                                        vaccine_status= vaccine_status, 
                                        # vaccine_mobile_registered= vaccine_mobile_registered,
                                        specimen_type_id= specimen_type_ref_data.id, 
                                        co_morbidity= co_morbidity,
                                        co_morbidity_type= co_morbidity_type_list,
                                        patient_status = patient_status_type,
                                        # specimen_collection_date= specimen_collection_date, 
                                        #testing_kit_barcode_id= testing_type_ref_data.id,
                                        # symptoms_list= symptoms, 
                                        symptoms_list= symptoms_list, 
                                        test_type_id= test_type_ref_data.id, 
                                        srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                        # barcode= barcode,
                                        barcode= srf_data,
                                        rat_created_id= rat_created_id_data, arrival_date= arrival_date,

                                        father_name = father_name,
                                        occupation = occupation,
                                        mode_of_transport = mode_of_transport,
                                        arogya_setu_app = arogya_setu_app,
                                        vaccine_type = vaccine_type,
                                        first_dose_date = first_dose_date,
                                        hospitalized = hospitalized,
                                        driver_license= driver_license,
                                        passport= passport,
                                        sample_collected_from= sample_collected_from,



                                    )
        record_create_timestamp = str(patients_data.create_timestamp)
        
        rat_created_id = patients_data.id
        if resident_type == 'Other-state':
            Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                            state_name= states, 
                                            district_name= district_name, #district_type= district_type, 
                                            city_name= city_name,
                                            zone_type= zone_name, 
                                            ward_name= ward_name, 
                                            taluk_name= taluk_name, 
                                            panchayat_name= panchayat_name, 
                                            village_name= village_name, 
                                            resident_type= resident_type, 
                                            ward_type= ward_type, 
                                            flat_door_no= flat_door_no, 
                                            main_road_no= main_road_no,
                                            pincode= pincode,
                                            locality= locality,
                                            landmark= landmark
                                            )
        else:
            Patient_Address.objects.create(patient_id= patients_data.id, 
                                            state_name= states, 
                                            district_name= district_name, #district_type= district_type, 
                                            city_name= city_name,
                                            zone_type= zone_name, 
                                            ward_name= ward_name, 
                                            taluk_name= taluk_name, 
                                            panchayat_name= panchayat_name, 
                                            village_name= village_name, 
                                            resident_type= resident_type, 
                                            ward_type= ward_type, 
                                            flat_door_no= flat_door_no, 
                                            main_road_no= main_road_no,
                                            pincode= pincode,
                                            locality= locality,
                                            landmark= landmark)
                         
        res_data = [{'patient_name':patient_name, 'mobile_number':mobile_number, 'gender': gender, 'age':age, 'speciman_type':speciman_type,'patient_status_type':patient_status_type, 'test_type':test_type, 'added_date':record_create_timestamp, 'srf_id': srf_data, 'rat_created_id':rat_created_id}]
        return Response({'result': res_data,'message':"Patient Data added Sucessfully"}, status= status.HTTP_200_OK)








#########################          TLAB ADD PATIENT           #########################
class LabAddPatient(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        reason_testing = data.get('reason_testing')
        reason = data.get('reason')
        patient_type = data.get('patient_type')
        patient_name = data.get('patient_name')
        mobile_number_belongs_to = data.get('mobile_number_belongs_to')
        mobile_number = data.get('mobile_number')
    
        otp_no = data.get('otp_no')
        states = data.get('states')
        district_name = data.get('district_name')
        resident_type = data.get('resident_type')
        ward_type = data.get('ward_type')
        city_name = data.get('city_name')
        taluk_name = data.get('taluk_name')
        village_name = data.get('village_name')
        panchayat_name = data.get('panchayat_name')
        zone_name = data.get('zone_name')
        ward_name = data.get('ward_name')
        flat_door_no = data.get('flat_door_no')
        main_road_no = data.get('main_road_no')
        pincode = data.get('pincode')
        gender = data.get('gender')
        age = data.get('age')
        age_type = data.get('age_type')
        idProof_type = data.get('idProof_type')

        aadhar_number = data.get('aadhar_number')
        ration_card_number = data.get('ration_card_number')
        speciman_type = data.get('speciman_type')
        speciman_collection_date = data.get('speciman_collection_date')
        patient_status_type = data.get('patient_status_type')
        symptoms = data.get('symptoms')
        co_morbidity = data.get('co_morbidity')
        co_morbidity_type = data.get('co_morbidity_type')
        test_type = data.get('test_type')
        old_srf_id = data.get('old_srf_id')
        
        vaccine_status = data.get('vaccine_status')
        con_mobile_number = data.get('con_mobile_number')
        existing_mobile_number = data.get('existing_mobile_number')
        user_id = data.get('user_id')

        locality = data.get('locality')
        landmark = data.get('landmark')

        arrival_date = data.get('arrival_date')

        rat_created_id_data = data.get('rat_created_id')

        generate_srf = random.randint(100000000, 999999999)

        barcode = data.get('barcode')

        father_name = data.get('father_name')
        occupation = data.get('occupation')
        mode_of_transport = data.get('mode_of_transport')
        arogya_setu_app = data.get('arogya_setu_app')
        vaccine_type = data.get('vaccine_type')
        first_dose_date = data.get('first_dose_date')
        hospitalized = data.get('hospitalized')
        driver_license = data.get('driver_license')
        passport = data.get('passport')

        # Encode
        aadhar_bytes = str(aadhar_number).encode('ascii')
        base64_bytes = base64.b64encode(aadhar_bytes)
        encriptrd_aadhar = base64_bytes.decode('ascii')
        
        # Decode
        # base64_message = encriptrd_aadhar
        # base64_bytes = base64_message.encode('ascii')
        # aadhar_bytes = base64.b64decode(base64_bytes)
        # aadhar_number = aadhar_bytes.decode('ascii')


        patient_type_ref_data = Patient_Type_Ref.objects.get(patient_type_name= patient_type)
        specimen_type_ref_data = Specimen_Type_Ref.objects.get(specimen_type_name= speciman_type)
        # testing_type_ref_data = Testing_Kit_Barcode.objects.get(testing_kit_barcode_name= testing_kit_barcode)
        test_type_ref_data = Test_Type_Ref.objects.get(test_type_name= test_type)
       
        symptoms_list = []
        if symptoms:
            for i in symptoms:
                print(i)
                if isinstance(i, str):
                    dist_type = ast.literal_eval(i)
                    symptoms_list.append(dist_type['name'])
                else:
                    symptoms_list.append(i['name'])
        
        co_morbidity_type_list = []
        for i in co_morbidity_type:
            print(i)
            # print(i['name'])
            if isinstance(i, str):
                dist_type = ast.literal_eval(i)
                co_morbidity_type_list.append(dist_type['name'])
            else:
                co_morbidity_type_list.append(i['name'])

        
        record_create_timestamp = ''

        rat_created_id = 0
        
        user_dist_status = Testing_Lab_Facility.objects.get(user_id= user_id)

        get_user_master_dist_code = Master_Labs.objects.get(id= user_dist_status.testing_lab_master_id)

        srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

        yr = str(asdatetime.now().year)[2:]
        mn = str(asdatetime.now().month).zfill(2)
        dd = str(asdatetime.now().day)

        srf_data = srf_dist_code+yr+mn+dd

        last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

        if last_srf_id:
            srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
        else:
            srf_data = srf_data + '1'.zfill(5)

        if rat_created_id_data:
            get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
            srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
            

        if data.get('id'):
                Contact_Tracing.objects.filter(id= data.get('id')).update(sample_collected= 1)

        patients_data = Patient.objects.create(reason_for_testing= reason_testing, reason_for_testing_description= reason, patient_type_id= patient_type_ref_data.id,
                                        added_by_id= user_id,
                                        patient_name= patient_name, 
                                        mobile_number= mobile_number, 
                                        mobile_number_belongs_to= mobile_number_belongs_to,

                                        gender= gender, 
                                        age= age,
                                        age_type= age_type,
                                        id_proof_type= idProof_type,
                                        aadhar_number= encriptrd_aadhar, 
                                        ration_card_number= ration_card_number, 
                                        vaccine_status= vaccine_status, 
                                        # vaccine_mobile_registered= vaccine_mobile_registered,
                                        specimen_type_id= specimen_type_ref_data.id, 
                                        co_morbidity= co_morbidity,
                                        co_morbidity_type= co_morbidity_type_list,
                                        patient_status = patient_status_type,
                                        # specimen_collection_date= specimen_collection_date, 
                                        #testing_kit_barcode_id= testing_type_ref_data.id,
                                        # symptoms_list= symptoms, 
                                        symptoms_list= symptoms_list, 
                                        test_type_id= test_type_ref_data.id, 
                                        srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                        # barcode= barcode,
                                        barcode= srf_data,
                                        rat_created_id= rat_created_id_data, arrival_date= arrival_date,

                                        father_name = father_name,
                                        occupation = occupation,
                                        mode_of_transport = mode_of_transport,
                                        arogya_setu_app = arogya_setu_app,
                                        vaccine_type = vaccine_type,
                                        first_dose_date = first_dose_date,
                                        hospitalized = hospitalized,
                                        driver_license= driver_license,
                                        passport= passport,
                                        lab_master_id= user_dist_status.testing_lab_master_id,

                                    )
        record_create_timestamp = str(patients_data.create_timestamp)
        # if test_type == 'RAT':
        #     Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
        rat_created_id = patients_data.id
        if resident_type == 'Other-state':
            Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                            state_name= states, 
                                            district_name= district_name, #district_type= district_type, 
                                            city_name= city_name,
                                            zone_type= zone_name, 
                                            ward_name= ward_name, 
                                            taluk_name= taluk_name, 
                                            panchayat_name= panchayat_name, 
                                            village_name= village_name, 
                                            resident_type= resident_type, 
                                            ward_type= ward_type, 
                                            flat_door_no= flat_door_no, 
                                            main_road_no= main_road_no,
                                            pincode= pincode,
                                            locality= locality,
                                            landmark= landmark
                                            )
        else:
            Patient_Address.objects.create(patient_id= patients_data.id, 
                                            state_name= states, 
                                            district_name= district_name, #district_type= district_type, 
                                            city_name= city_name,
                                            zone_type= zone_name, 
                                            ward_name= ward_name, 
                                            taluk_name= taluk_name, 
                                            panchayat_name= panchayat_name, 
                                            village_name= village_name, 
                                            resident_type= resident_type, 
                                            ward_type= ward_type, 
                                            flat_door_no= flat_door_no, 
                                            main_road_no= main_road_no,
                                            pincode= pincode,
                                            locality= locality,
                                            landmark= landmark)

        # Patient_Testing.objects.create()                                        

        # Patient_Testing.objects.create(patient_id= patients_data.id, lab_received_date= , testing_kit_id= , testing_status= , ct_value= , 
        #                                 comments= ,)                             
        res_data = [{'patient_name':patient_name, 'mobile_number':mobile_number, 'gender': gender, 'age':age, 'speciman_type':speciman_type,'patient_status_type':patient_status_type, 'test_type':test_type, 'added_date':record_create_timestamp, 'srf_id': srf_data, 'rat_created_id':rat_created_id}]
        return Response({'result': res_data,'message':"Patient Data added Sucessfully"}, status= status.HTTP_200_OK)



    


#########################          CONTACT TESTING OFF LINE          #########################
class ContectTestingOffline(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        lpdata = request.data
        print("DDDDDDDDD:")
        print(lpdata)

        cnt = 0
        for data in lpdata:

            reason_testing = data.get('reason_testing')
            reason = data.get('reason')
            patient_type = data.get('patient_type')
            patient_name = data.get('patient_name')
            mobile_number_belongs_to = data.get('mobile_number_belongs_to')
            mobile_number = data.get('mobile_number')
        
            otp_no = data.get('otp_no')
            states = data.get('states')
            district_name = data.get('district_name')
            resident_type = data.get('resident_type')
            ward_type = data.get('ward_type')
            city_name = data.get('city_name')
            taluk_name = data.get('taluk_name')
            village_name = data.get('village_name')
            panchayat_name = data.get('panchayat_name')
            zone_name = data.get('zone_name')
            ward_name = data.get('ward_name')
            flat_door_no = data.get('flat_door_no')
            main_road_no = data.get('main_road_no')
            pincode = data.get('pincode')
            gender = data.get('gender')
            age = data.get('age')
            age_type = data.get('age_type')
            idProof_type = data.get('idProof_type')
            
            speciman_collection_date = data.get('speciman_collection_date')
            swab_collection_status = data.get('swab_collection_status')
            antigen = data.get('antigen')

            aadhar_number = data.get('aadhar_number')
            ration_card_number = data.get('ration_card_number')
            speciman_type = data.get('speciman_type')
            speciman_collection_date = data.get('speciman_collection_date')
            patient_status_type = data.get('patient_status_type')
            symptoms = data.get('symptoms')
            co_morbidity = data.get('co_morbidity')
            co_morbidity_type = data.get('co_morbidity_type')
            test_type = data.get('test_type')
            old_srf_id = data.get('old_srf_id')
            
            vaccine_status = data.get('vaccine_status')
            con_mobile_number = data.get('con_mobile_number')
            existing_mobile_number = data.get('existing_mobile_number')
            user_id = data.get('user_id')

            locality = data.get('locality')
            landmark = data.get('landmark')

            arrival_date = data.get('arrival_date')

            rat_created_id_data = data.get('rat_created_id')

            generate_srf = random.randint(100000000, 999999999)

            barcode = data.get('barcode')
            
            rtpcr_sample = data.get('rtpct_sample')
            print(rtpcr_sample)
            


            print(reason_testing)
            print(reason)
            print(patient_type)
            print(patient_name)
            print(mobile_number_belongs_to)
            print(mobile_number)
            print(otp_no)
            print(states)
            print(district_name)
            print(resident_type)
            print(ward_type)
            print(city_name)
            print(taluk_name)
            print(village_name)
            print(panchayat_name)
            print(zone_name)
            print(ward_name)
            print(flat_door_no)
            print(main_road_no)
            print(pincode)
            print(gender)
            print(age)
            print(idProof_type)
            print(aadhar_number)
            print(ration_card_number)
            print(speciman_type)
            print(speciman_collection_date)
            print(patient_status_type)
            print(symptoms)
            print(co_morbidity)
            print(co_morbidity_type)
            print(test_type)
            print(old_srf_id)
            print(vaccine_status)
            print(con_mobile_number)
            print(existing_mobile_number)
            print(user_id)
            print(locality)
            print(landmark)
            print(arrival_date)
            print(rat_created_id_data)
            print(generate_srf)
            print(barcode)

            patient_type_ref_data = Patient_Type_Ref.objects.get(patient_type_name= patient_type)
            specimen_type_ref_data = Specimen_Type_Ref.objects.get(specimen_type_name= speciman_type)
            # testing_type_ref_data = Testing_Kit_Barcode.objects.get(testing_kit_barcode_name= testing_kit_barcode)
            test_type_ref_data = Test_Type_Ref.objects.get(test_type_name= test_type)
        
            symptoms_list = []
            
            print(type(symptoms))
            print(type(co_morbidity))
            
            dddd = co_morbidity
            print(dddd)
            print(type(dddd))
            cccc = str(dddd)
            print(cccc)
            print(type(cccc))
            
            check_symt = ast.literal_eval(symptoms)
            
            if symptoms:
                for i in check_symt:
                    print(i)
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        symptoms_list.append(dist_type['name'])
                    else:
                        symptoms_list.append(i['name'])
            
            co_morbidity_type_list = []
            
            check_co_mrobidity = ast.literal_eval(str(co_morbidity_type))
            if co_morbidity:
                for i in check_co_mrobidity:
                    print(i)
                    # print(i['name'])
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        co_morbidity_type_list.append(dist_type['name'])
                    else:
                        co_morbidity_type_list.append(i['name'])

            record_create_timestamp = ''

            rat_created_id = 0

            user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

            get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

            srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

            yr = str(asdatetime.now().year)[2:]
            mn = str(asdatetime.now().month).zfill(2)
            dd = str(asdatetime.now().day)

            srf_data = srf_dist_code+yr+mn+dd

            last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

            print('hhhhhhhhhh', last_srf_id)
            if last_srf_id:
                srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                print(srf_data)
            else:
                srf_data = srf_data + '1'.zfill(5)

            if rat_created_id_data:
                get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                print("RAT SRF ID")
                print(srf_data)

            if data.get('id'):
                Contact_Tracing.objects.filter(id= data.get('id')).update(sample_collected= 1)

            patients_data = Patient.objects.create(reason_for_testing= reason_testing, reason_for_testing_description= reason, patient_type_id= patient_type_ref_data.id,
                                            added_by_id= user_id,
                                            patient_name= patient_name, 
                                            mobile_number= mobile_number, 
                                            mobile_number_belongs_to= mobile_number_belongs_to,

                                            gender= gender, 
                                            age= age,
                                            age_type= age_type,
                                            id_proof_type= idProof_type,
                                            aadhar_number= aadhar_number, 
                                            ration_card_number= ration_card_number, 
                                            vaccine_status= vaccine_status, 
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            specimen_type_id= specimen_type_ref_data.id, 
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            patient_status = patient_status_type,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms,
                                            create_timestamp = speciman_collection_date,
                                            swab_collection_status = swab_collection_status,
                                            symptoms_list= symptoms_list, 
                                            test_type_id= test_type_ref_data.id, 
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            barcode= barcode,
                                            rat_created_id= rat_created_id_data, arrival_date= arrival_date
                                        )
            record_create_timestamp = str(patients_data.create_timestamp)
            if test_type == 'RAT':
                # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
            rat_created_id = patients_data.id
            # if resident_type == 'Other-state':
            #     Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
            #                                     state_name= states, 
            #                                     district_name= district_name, #district_type= district_type, 
            #                                     city_name= city_name,
            #                                     zone_type= zone_name, 
            #                                     ward_name= ward_name, 
            #                                     taluk_name= taluk_name, 
            #                                     panchayat_name= panchayat_name, 
            #                                     village_name= village_name, 
            #                                     resident_type= resident_type, 
            #                                     ward_type= ward_type, 
            #                                     flat_door_no= flat_door_no, 
            #                                     main_road_no= main_road_no,
            #                                     pincode= pincode,
            #                                     locality= locality,
            #                                     landmark= landmark
            #                                     )
            # else:
            Patient_Address.objects.create(patient_id= patients_data.id, 
                                            state_name= states, 
                                            district_name= district_name, #district_type= district_type, 
                                            city_name= city_name,
                                            zone_type= zone_name, 
                                            ward_name= ward_name, 
                                            taluk_name= taluk_name, 
                                            panchayat_name= panchayat_name, 
                                            village_name= village_name, 
                                            resident_type= resident_type, 
                                            ward_type= ward_type, 
                                            flat_door_no= flat_door_no, 
                                            main_road_no= main_road_no,
                                            pincode= pincode,
                                            locality= locality,
                                            landmark= landmark)
            
            
            # if resident_type == 'Other State':
            #     Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
            #                                     state_name= states, 
            #                                     district_name= district_name, #district_type= district_type, 
            #                                     city_name= city_name,
            #                                     zone_type= zone_name, 
            #                                     ward_name= ward_name, 
            #                                     taluk_name= taluk_name, 
            #                                     panchayat_name= panchayat_name, 
            #                                     village_name= village_name, 
            #                                     resident_type= resident_type, 
            #                                     ward_type= ward_type, 
            #                                     flat_door_no= flat_door_no, 
            #                                     main_road_no= main_road_no,
            #                                     pincode= pincode,
            #                                     locality= locality,
            #                                     landmark= landmark)

            # else:
            #     Patient_Address.objects.create(patient_id= patients_data.id, 
            #                                     state_name= states, 
            #                                     district_name= district_name, #district_type= district_type, 
            #                                     city_name= city_name,
            #                                     zone_type= zone_name, 
            #                                     ward_name= ward_name, 
            #                                     taluk_name= taluk_name, 
            #                                     panchayat_name= panchayat_name, 
            #                                     village_name= village_name, 
            #                                     resident_type= resident_type, 
            #                                     ward_type= ward_type, 
            #                                     flat_door_no= flat_door_no, 
            #                                     main_road_no= main_road_no,
            #                                     pincode= pincode,
            #                                     locality= locality,
            #                                     landmark= landmark)
            
            

            # Patient_Testing.objects.create()                                        

            # Patient_Testing.objects.create(patient_id= patients_data.id, lab_received_date= , testing_kit_id= , testing_status= , ct_value= , 
            #                                 comments= ,)                             
            #res_data = [{'patient_name':patient_name, 'mobile_number':mobile_number, 'gender': gender, 'age':age, 'speciman_type':speciman_type,'patient_status_type':patient_status_type, 'test_type':test_type, 'added_date':record_create_timestamp, 'srf_id': srf_data, 'rat_created_id':rat_created_id}]
            print(patient_status_type)
            print(test_type)
            print(rtpcr_sample)
            print(antigen)
            
            print(type(patient_status_type))
            print(type(test_type))
            print(type(rtpcr_sample))
            print(type(antigen))
            if (patient_status_type == 'Symptomatic' and test_type == 'RAT' and rtpcr_sample == 'true' and antigen == '0'):
                
                print("HELOO HELLO HELLO HELLO HELLO")
                
                last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

                if last_srf_id:
                    srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                    print(srf_data)
                else:
                    srf_data = srf_data + '1'.zfill(5)

                if rat_created_id_data:
                    get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                    srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                    print("RAT SRF ID")
                    print(srf_data)
                    
                patients_data = Patient.objects.create(
                                            reason_for_testing= reason_testing, 
                                            reason_for_testing_description= reason,
                                            arrival_date= arrival_date,
                                            patient_name= patient_name,
                                            patient_type_id= patient_type_ref_data.id,
                                            mobile_number= mobile_number,
                                            added_by_id= user_id,
                                            gender= gender,
                                            age= age,
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            id_proof_type= idProof_type,
                                            ration_card_number= ration_card_number,
                                            patient_status = patient_status_type,
                                            symptoms_list= symptoms_list,
                                            test_type_id= 2,
                                            specimen_type_id= specimen_type_ref_data.id,
                                            vaccine_status= vaccine_status,
                                            create_timestamp = speciman_collection_date,
                                            aadhar_number= aadhar_number,
                                            swab_collection_status = swab_collection_status,
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            
                                            # mobile_number_belongs_to= mobile_number_belongs_to,
                                            age_type= age_type,
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            # barcode= barcode,
                                            # rat_created_id= rat_created_id_data,
                                        )
                print(patients_data.id)
                record_create_timestamp = str(patients_data.create_timestamp)
                if test_type == 'RAT':
                    # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                    Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
                
                print(resident_type)
                if resident_type == 'Other State':
                    Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

                else:
                    Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

            
            cnt += 1

        return Response({'result': cnt,'message':"Data Uploaded Sucessfully"}, status= status.HTTP_200_OK)


    
    
"""
#########################          ADD PATIENT OFF LINE          #########################
class ContectTestingOfflineAddPatient(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        lpdata = request.data
        print("ADD PATIENT OFFLINE:")
        print(lpdata)
        

        cnt = 0
        for data in lpdata:

            reason_testing = data.get('reason_testing')
            reason = data.get('reason')
            arrival_date = data.get('arrival_date')
            patient_name = data.get('patient_name')
            patient_type = data.get('patient_type')
            mobile_number = data.get('mobile_number')
            resident_type = data.get('resident_type')
            states = data.get('states')
            district_name = data.get('district_name')
            ward_type = data.get('ward_type')
            user_id = data.get('user_id')
            city_name = data.get('city_name')
            ward_name = data.get('ward_name')
            taluk_name = data.get('taluk_name')
            panchayat_name = data.get('panchayat_name')
            village_name = data.get('village_name')
            flat_door_no = data.get('flat_door_no')
            main_road_no = data.get('main_road_no')
            pincode = data.get('pincode')
            gender = data.get('gender')
            age_data = data.get('age')
            co_morbidity = data.get('co_morbidity')
            co_morbidity_type = data.get('co_morbidity_type')
            idProof_type = data.get('idProof_type')
            ration_card_number = data.get('ration_card_number')
            patient_status_type = data.get('patient_status_type')
            symptoms = data.get('symptoms')
            test_type = data.get('test_type')
            speciman_type = data.get('speciman_type')
            vaccine_status = data.get('vaccine_status')
            speciman_collection_date = data.get('speciman_collection_date')
            aadhar_number = data.get('aadhar_number')
            ct_latitude = data.get('ct_latitude')
            ct_longitude = data.get('ct_longitude')
            swab_collection_status = data.get('swab_collection_status')
            antigen = data.get('antigen')
            
            rtpcr_sample = data.get('rtpct_sample')
            print(rtpcr_sample)
            
            rat_created_id_data = data.get('rat_created_id_data')
            print(speciman_collection_date)
            
            age = age_data.split(' ')[0]
            age_type = age_data.split(' ')[1]
            
            sero_category = data.get('sero_category')
            igg_sample = data.get('igg_sample')
            


            # mobile_number_belongs_to = data.g et('mobile_number_belongs_to')
            # otp_no = data.get('otp_no')
            # zone_name = data.get('zone_name')
            # age_type = data.get('age_type')
            # speciman_collection_date = data.get('speciman_collection_date')
            # old_srf_id = data.get('old_srf_id')
            # con_mobile_number = data.get('con_mobile_number')
            # existing_mobile_number = data.get('existing_mobile_number')
            # locality = data.get('locality')
            # landmark = data.get('landmark')
            # rat_created_id_data = data.get('rat_created_id')
            # generate_srf = random.randint(100000000, 999999999)
            # barcode = data.get('barcode')


            # print(reason_testing)
            # print(reason)
            # print(patient_type)
            # print(patient_name)
            # print(mobile_number_belongs_to)
            # print(mobile_number)
            # print(otp_no)
            # print(states)
            # print(district_name)
            # print(resident_type)
            # print(ward_type)
            # print(city_name)
            # print(taluk_name)
            # print(village_name)
            # print(panchayat_name)
            # print(zone_name)
            # print(ward_name)
            # print(flat_door_no)
            # print(main_road_no)
            # print(pincode)
            # print(gender)
            # print(age)
            # print(idProof_type)
            # print(aadhar_number)
            # print(ration_card_number)
            # print(speciman_type)
            # print(speciman_collection_date)
            # print(patient_status_type)
            # print(symptoms)
            # print(co_morbidity)
            # print(co_morbidity_type)
            # print(test_type)
            # print(old_srf_id)
            # print(vaccine_status)
            # print(con_mobile_number)
            # print(existing_mobile_number)
            # print(user_id)
            # print(locality)
            # print(landmark)
            # print(arrival_date)
            # print(rat_created_id_data)
            # print(generate_srf)
            # print(barcode)
            
            # check_sero = ''
            # if sero_category:
            #    check_ser= igg_sample
            # else:
            #    check_sero = 'No'
            

            patient_type_ref_data = Patient_Type_Ref.objects.get(patient_type_name= patient_type)
            specimen_type_ref_data = Specimen_Type_Ref.objects.get(specimen_type_name= speciman_type)
            # testing_type_ref_data = Testing_Kit_Barcode.objects.get(testing_kit_barcode_name= testing_kit_barcode)
            test_type_ref_data = Test_Type_Ref.objects.get(test_type_name= test_type)
        
            symptoms_list = []
            
            check_symt = ast.literal_eval(symptoms)
            if symptoms:
                for i in check_symt:
                    print(i)
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        symptoms_list.append(dist_type['name'])
                    else:
                        symptoms_list.append(i['name'])
            
            co_morbidity_type_list = []
            check_co_mrobidity = ast.literal_eval(str(co_morbidity_type))
            if co_morbidity:
                for i in check_co_mrobidity:
                    print(i)
                    # print(i['name'])
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        co_morbidity_type_list.append(dist_type['name'])
                    else:
                        co_morbidity_type_list.append(i['name'])

            record_create_timestamp = ''

            rat_created_id = 0

            user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

            get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

            srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

            yr = str(asdatetime.now().year)[2:]
            mn = str(asdatetime.now().month).zfill(2)
            dd = str(asdatetime.now().day)

            srf_data = srf_dist_code+yr+mn+dd

            last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

            print('hhhhhhhhhh', last_srf_id)
            if last_srf_id:
                srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                print(srf_data)
            else:
                srf_data = srf_data + '1'.zfill(5)

            if rat_created_id_data:
                get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                print("RAT SRF ID")
                print(srf_data)

            patients_data = Patient.objects.create(
                                            reason_for_testing= reason_testing, 
                                            reason_for_testing_description= reason,
                                            arrival_date= arrival_date,
                                            patient_name= patient_name,
                                            patient_type_id= patient_type_ref_data.id,
                                            mobile_number= mobile_number,
                                            added_by_id= user_id,
                                            gender= gender,
                                            age= age,
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            id_proof_type= idProof_type,
                                            ration_card_number= ration_card_number,
                                            patient_status = patient_status_type,
                                            symptoms_list= symptoms_list,
                                            test_type_id= test_type_ref_data.id,
                                            specimen_type_id= specimen_type_ref_data.id,
                                            vaccine_status= vaccine_status,
                                            # create_timestamp = asdatetime.strptime(speciman_collection_date,'%Y-%m-%d %H:%M'),
                                            create_timestamp = speciman_collection_date,
                                            aadhar_number= aadhar_number,
                                            swab_collection_status = swab_collection_status,
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            
                                            # mobile_number_belongs_to= mobile_number_belongs_to,
                                            age_type= age_type,
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            # barcode= barcode,
                                            # rat_created_id= rat_created_id_data,
                                            sero_category= sero_category,
                                            igg_sample = igg_sample,
                                        )
            print(patients_data.id)
            record_create_timestamp = str(patients_data.create_timestamp)
            if test_type == 'RAT':
                # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
            
            print(resident_type)
            if resident_type == 'Other State':
                Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                                state_name= states, 
                                                district_name= district_name, #district_type= district_type, 
                                                city_name= city_name,
                                                zone_type= '', 
                                                ward_name= ward_name, 
                                                taluk_name= taluk_name, 
                                                panchayat_name= panchayat_name, 
                                                village_name= village_name, 
                                                resident_type= resident_type, 
                                                ward_type= ward_type, 
                                                flat_door_no= flat_door_no, 
                                                main_road_no= main_road_no,
                                                pincode= pincode,
                                                locality= '',
                                                landmark= '')

            else:
                Patient_Address.objects.create(patient_id= patients_data.id, 
                                                state_name= states, 
                                                district_name= district_name, #district_type= district_type, 
                                                city_name= city_name,
                                                zone_type= '', 
                                                ward_name= ward_name, 
                                                taluk_name= taluk_name, 
                                                panchayat_name= panchayat_name, 
                                                village_name= village_name, 
                                                resident_type= resident_type, 
                                                ward_type= ward_type, 
                                                flat_door_no= flat_door_no, 
                                                main_road_no= main_road_no,
                                                pincode= pincode,
                                                locality= '',
                                                landmark= '')
                
             
            print(patient_status_type)
            print(test_type)
            print(rtpcr_sample)
            print(antigen)
            
            print(type(patient_status_type))
            print(type(test_type))
            print(type(rtpcr_sample))
            print(type(antigen))
            if (patient_status_type == 'Symptomatic' and test_type == 'RAT' and rtpcr_sample == 'true' and antigen == '0'):
                
                print("HELOO HELLO HELLO HELLO HELLO")
                
                last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

                if last_srf_id:
                    srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                    print(srf_data)
                else:
                    srf_data = srf_data + '1'.zfill(5)

                if rat_created_id_data:
                    get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                    srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                    print("RAT SRF ID")
                    print(srf_data)
                    
                patients_data = Patient.objects.create(
                                            reason_for_testing= reason_testing, 
                                            reason_for_testing_description= reason,
                                            arrival_date= arrival_date,
                                            patient_name= patient_name,
                                            patient_type_id= patient_type_ref_data.id,
                                            mobile_number= mobile_number,
                                            added_by_id= user_id,
                                            gender= gender,
                                            age= age,
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            id_proof_type= idProof_type,
                                            ration_card_number= ration_card_number,
                                            patient_status = patient_status_type,
                                            symptoms_list= symptoms_list,
                                            test_type_id= 2,
                                            specimen_type_id= specimen_type_ref_data.id,
                                            vaccine_status= vaccine_status,
                                            create_timestamp = speciman_collection_date,
                                            aadhar_number= aadhar_number,
                                            swab_collection_status = swab_collection_status,
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            
                                            # mobile_number_belongs_to= mobile_number_belongs_to,
                                            age_type= age_type,
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            # barcode= barcode,
                                            # rat_created_id= rat_created_id_data,
                                        )
                print(patients_data.id)
                record_create_timestamp = str(patients_data.create_timestamp)
                if test_type == 'RAT':
                    # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                    Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
                
                print(resident_type)
                if resident_type == 'Other State':
                    Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

                else:
                    Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

            
            
            cnt += 1

        return Response({'result': cnt,'message':"Data Uploaded Sucessfully"}, status= status.HTTP_200_OK)
"""




#########################          ADD PATIENT OFF LINE          #########################
class ContectTestingOfflineAddPatient(APIView):

    def post(self, request):

        lpdata = request.data

        cnt = 0
        for data in lpdata:

            reason_testing = data.get('reason_testing')
            reason = data.get('reason')
            arrival_date = data.get('arrival_date')
            patient_name = data.get('patient_name')
            patient_type = data.get('patient_type')
            mobile_number = data.get('mobile_number')
            resident_type = data.get('resident_type')
            states = data.get('states')
            district_name = data.get('district_name')
            ward_type = data.get('ward_type')
            user_id = data.get('user_id')
            city_name = data.get('city_name')
            ward_name = data.get('ward_name')
            taluk_name = data.get('taluk_name')
            panchayat_name = data.get('panchayat_name')
            village_name = data.get('village_name')
            flat_door_no = data.get('flat_door_no')
            main_road_no = data.get('main_road_no')
            pincode = data.get('pincode')
            gender = data.get('gender')
            age_data = data.get('age')
            co_morbidity = data.get('co_morbidity')
            co_morbidity_type = data.get('co_morbidity_type')
            idProof_type = data.get('idProof_type')
            ration_card_number = data.get('ration_card_number')
            patient_status_type = data.get('patient_status_type')
            symptoms = data.get('symptoms')
            test_type = data.get('test_type')
            speciman_type = data.get('speciman_type')
            vaccine_status = data.get('vaccine_status')
            speciman_collection_date = data.get('speciman_collection_date')
            aadhar_number = data.get('aadhar_number')
            ct_latitude = data.get('ct_latitude')
            ct_longitude = data.get('ct_longitude')
            swab_collection_status = data.get('swab_collection_status')
            antigen = data.get('antigen')
            
            rtpcr_sample = data.get('rtpct_sample')
            
            rat_created_id_data = data.get('rat_created_id_data')
            
            age = age_data.split(' ')[0]
            age_type = age_data.split(' ')[1]
            
            sero_category = data.get('sero_category')
            igg_sample = data.get('igg_sample')

            speciman_type_scan = data.get('speciman_type_scan')
            speciman_typeRFID_scan = data.get('speciman_typeRFID_scan')
            fathers_name = data.get('fathers_name')
            contact_with_lab_confirmed_patient = data.get('contact_with_lab_confirmed_patient')
            occupation = data.get('occupation')
            aarogya_setu_app_downloaded = data.get('aarogya_setu_app_downloaded')
            transport_mode_used_to_visit_testing_facility= data.get('transport_mode_used_to_visit_testing_facility')
            vaccine_type = data.get('vaccine_type')
            vaccine_dose1_date = data.get('vaccine_dose1_date')
            hospitalized = data.get('hospitalized')
            speciman_type_blood_test_scan = data.get('speciman_type_blood_test_scan')
            speciman_type_nasal_throat_scan = data.get('speciman_type_nasal_throat_scan')



            print(reason_testing)
            print(reason)
            print(arrival_date)
            print(patient_name)
            print(patient_type)
            print(mobile_number)
            print(resident_type)
            print(states)
            print(district_name)
            print(ward_type)
            print(user_id)

            print(city_name)
            print(ward_name)
            print(taluk_name)
            print(panchayat_name)
            print(village_name)
            print(flat_door_no)
            print(main_road_no)
            print(pincode)
            print(gender)
            print(age_data)

            print(co_morbidity)
            print(co_morbidity_type)
            print(idProof_type)
            print(ration_card_number)
            print(patient_status_type)
            print(symptoms)
            print(test_type)
            print(speciman_type)
            print(vaccine_status)
            print(speciman_collection_date)

            print(aadhar_number)
            print(ct_latitude)
            print(ct_longitude)
            print(swab_collection_status)
            print(antigen)
            print(rtpcr_sample)
            print(rat_created_id_data)
            print(sero_category)
            print(igg_sample)
            print(speciman_type_scan)

            print(speciman_typeRFID_scan)
            print(fathers_name)
            print(contact_with_lab_confirmed_patient)
            print(occupation)
            print(aarogya_setu_app_downloaded)
            print(transport_mode_used_to_visit_testing_facility)
            print(vaccine_type)
            print(vaccine_dose1_date)
            print(hospitalized)
            print(speciman_type_blood_test_scan)
            print(speciman_type_nasal_throat_scan)


            # Encode
            aadhar_bytes = str(aadhar_number).encode('ascii')
            base64_bytes = base64.b64encode(aadhar_bytes)
            encriptrd_aadhar = base64_bytes.decode('ascii')
            
            # Decode
            # base64_message = encriptrd_aadhar
            # base64_bytes = base64_message.encode('ascii')
            # aadhar_bytes = base64.b64decode(base64_bytes)
            # aadhar_number = aadhar_bytes.decode('ascii')


            # mobile_number_belongs_to = data.g et('mobile_number_belongs_to')
            # otp_no = data.get('otp_no')
            # zone_name = data.get('zone_name')
            # age_type = data.get('age_type')
            # speciman_collection_date = data.get('speciman_collection_date')
            # old_srf_id = data.get('old_srf_id')
            # con_mobile_number = data.get('con_mobile_number')
            # existing_mobile_number = data.get('existing_mobile_number')
            # locality = data.get('locality')
            # landmark = data.get('landmark')
            # rat_created_id_data = data.get('rat_created_id')
            # generate_srf = random.randint(100000000, 999999999)
            # barcode = data.get('barcode')

            patient_type_ref_data = Patient_Type_Ref.objects.get(patient_type_name= patient_type)
            specimen_type_ref_data = Specimen_Type_Ref.objects.get(specimen_type_name= speciman_type)
            # testing_type_ref_data = Testing_Kit_Barcode.objects.get(testing_kit_barcode_name= testing_kit_barcode)
            test_type_ref_data = Test_Type_Ref.objects.get(test_type_name= test_type)
        
            symptoms_list = []
            
            check_symt = ast.literal_eval(symptoms)
            if symptoms:
                for i in check_symt:
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        symptoms_list.append(dist_type['name'])
                    else:
                        symptoms_list.append(i['name'])
            
            co_morbidity_type_list = []
            check_co_mrobidity = ast.literal_eval(str(co_morbidity_type))
            if co_morbidity:
                for i in check_co_mrobidity:
                    if isinstance(i, str):
                        dist_type = ast.literal_eval(i)
                        co_morbidity_type_list.append(dist_type['name'])
                    else:
                        co_morbidity_type_list.append(i['name'])

            record_create_timestamp = ''

            rat_created_id = 0

            user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

            get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

            srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

            yr = str(asdatetime.now().year)[2:]
            mn = str(asdatetime.now().month).zfill(2)
            dd = str(asdatetime.now().day)

            srf_data = srf_dist_code+yr+mn+dd

            last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

            if last_srf_id:
                srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
            else:
                srf_data = srf_data + '1'.zfill(5)

            if rat_created_id_data:
                get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                

            patients_data = Patient.objects.create(
                                            reason_for_testing= reason_testing, 
                                            reason_for_testing_description= reason,
                                            arrival_date= arrival_date,
                                            patient_name= patient_name,
                                            patient_type_id= patient_type_ref_data.id,
                                            mobile_number= mobile_number,
                                            added_by_id= user_id,
                                            gender= gender,
                                            age= age,
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            id_proof_type= idProof_type,
                                            ration_card_number= ration_card_number,
                                            patient_status = patient_status_type,
                                            symptoms_list= symptoms_list,
                                            test_type_id= test_type_ref_data.id,
                                            specimen_type_id= specimen_type_ref_data.id,
                                            vaccine_status= vaccine_status,
                                            create_timestamp = speciman_collection_date,
                                            aadhar_number= encriptrd_aadhar,
                                            swab_collection_status = swab_collection_status,
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            
                                            # mobile_number_belongs_to= mobile_number_belongs_to,
                                            age_type= age_type,
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            # barcode= barcode,
                                            # rat_created_id= rat_created_id_data,
                                            sero_category= sero_category,
                                            igg_sample = igg_sample,
                                            hospitalized= hospitalized,
                                            first_dose_date= vaccine_dose1_date,
                                            vaccine_type= vaccine_type,
                                            mode_of_transport= transport_mode_used_to_visit_testing_facility,
                                            arogya_setu_app= aarogya_setu_app_downloaded,
                                            occupation= occupation,
                                            father_name= fathers_name,
                                            contact_with_lab_confirmed_patient= contact_with_lab_confirmed_patient,
                                            speciman_typeRFID_scan= speciman_typeRFID_scan,
                                            speciman_type_scan= speciman_type_scan,
                                            speciman_type_blood_test_scan= speciman_type_blood_test_scan,
                                            speciman_type_nasal_throat_scan= speciman_type_nasal_throat_scan,

                                        )
            record_create_timestamp = str(patients_data.create_timestamp)
            if test_type == 'RAT':
                # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
            
            if resident_type == 'Other State':
                Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                                state_name= states, 
                                                district_name= district_name, #district_type= district_type, 
                                                city_name= city_name,
                                                zone_type= '', 
                                                ward_name= ward_name, 
                                                taluk_name= taluk_name, 
                                                panchayat_name= panchayat_name, 
                                                village_name= village_name, 
                                                resident_type= resident_type, 
                                                ward_type= ward_type, 
                                                flat_door_no= flat_door_no, 
                                                main_road_no= main_road_no,
                                                pincode= pincode,
                                                ct_latitude= ct_latitude,
                                                ct_longitude= ct_longitude,
                                                locality= '',
                                                landmark= '')

            else:
                Patient_Address.objects.create(patient_id= patients_data.id, 
                                                state_name= states, 
                                                district_name= district_name, #district_type= district_type, 
                                                city_name= city_name,
                                                zone_type= '', 
                                                ward_name= ward_name, 
                                                taluk_name= taluk_name, 
                                                panchayat_name= panchayat_name, 
                                                village_name= village_name, 
                                                resident_type= resident_type, 
                                                ward_type= ward_type, 
                                                flat_door_no= flat_door_no, 
                                                main_road_no= main_road_no,
                                                pincode= pincode,
                                                ct_latitude= ct_latitude,
                                                ct_longitude= ct_longitude,
                                                locality= '',
                                                landmark= '')
                
             
            if (patient_status_type == 'Symptomatic' and test_type == 'RAT' and rtpcr_sample == 'true' and antigen == '0'):
                
                
                last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

                if last_srf_id:
                    srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                else:
                    srf_data = srf_data + '1'.zfill(5)

                if rat_created_id_data:
                    get_patient_rat_data = Patient.objects.get(id= rat_created_id_data)
                    srf_data = str(get_patient_rat_data.srf_id) + '-TEMP'
                    
                    
                patients_data = Patient.objects.create(
                                            reason_for_testing= reason_testing, 
                                            reason_for_testing_description= reason,
                                            arrival_date= arrival_date,
                                            patient_name= patient_name,
                                            patient_type_id= patient_type_ref_data.id,
                                            mobile_number= mobile_number,
                                            added_by_id= user_id,
                                            gender= gender,
                                            age= age,
                                            co_morbidity= co_morbidity,
                                            co_morbidity_type= co_morbidity_type_list,
                                            id_proof_type= idProof_type,
                                            ration_card_number= ration_card_number,
                                            patient_status = patient_status_type,
                                            symptoms_list= symptoms_list,
                                            test_type_id= 2,
                                            specimen_type_id= specimen_type_ref_data.id,
                                            vaccine_status= vaccine_status,
                                            create_timestamp = speciman_collection_date,
                                            aadhar_number= aadhar_number,
                                            swab_collection_status = swab_collection_status,
                                            srf_id= srf_data, # generate_srf, #swab_collection_status= swab_collection_status_ref_data.id,
                                            
                                            # mobile_number_belongs_to= mobile_number_belongs_to,
                                            age_type= age_type,
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            # barcode= barcode,
                                            # rat_created_id= rat_created_id_data,
                                        )
                record_create_timestamp = str(patients_data.create_timestamp)
                if test_type == 'RAT':
                    # Patient.objects.filter(id= patients_data.id).update(rat_created_id= patients_data.id)
                    Patient_Testing.objects.create(patient_id= patients_data.id, testing_status= antigen)
                
                if resident_type == 'Other State':
                    Outside_Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

                else:
                    Patient_Address.objects.create(patient_id= patients_data.id, 
                                                    state_name= states, 
                                                    district_name= district_name, #district_type= district_type, 
                                                    city_name= city_name,
                                                    zone_type= '', 
                                                    ward_name= ward_name, 
                                                    taluk_name= taluk_name, 
                                                    panchayat_name= panchayat_name, 
                                                    village_name= village_name, 
                                                    resident_type= resident_type, 
                                                    ward_type= ward_type, 
                                                    flat_door_no= flat_door_no, 
                                                    main_road_no= main_road_no,
                                                    pincode= pincode,
                                                    locality= '',
                                                    landmark= '')

            cnt += 1

        return Response({'result': cnt,'message':"Data Uploaded Sucessfully"}, status= status.HTTP_200_OK)



    

    
    

#########################          CONTACT TESTING DATEWISE DUMP          #########################
class ContectTestingDateWiseDump(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        from_date = data.get('from_date')
        to_date = data.get('to_date')

        acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
        token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
        acc_json_data = json.dumps(token_body)
        acc_tok_res = requests.post(acc_url, data= token_body)

        acc_token_res = acc_tok_res.json()
        body_hdr = acc_token_res['access_token']

        header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
        json_header = json.dumps(header)

        url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetContactTesting_Datewise'
        input_body = {'FromDate':from_date, 'ToDate':to_date}

        json_data = json.dumps(input_body, indent=4)

        check_contact_testing_dump_response = requests.post(url, data= json_data, headers= header)

        ct_dmp_data = check_contact_testing_dump_response.json()
        res_data = ct_dmp_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA_DATEWISE']

        print(res_data)

        created_ids= []

        for i in res_data:

            # if i['district_number'] != 0:
            #     check_dist_data = Master_District.objects.filter(district_code= i['district_number'])
            #     if check_dist_data:
            #         check_dist_data_get = Master_District.objects.get(district_code= i['district_number'])
            #         i['district_name'] = check_dist_data_get.district_name_eng
            
            # if i['taluk_number'] != 0:
            #     check_tlk_data = Master_Block.objects.filter(block_code= i['taluk_number'])
            #     if check_tlk_data:
            #         check_tlk_data_get = Master_Block.objects.get(block_code= i['taluk_number'])
            #         i['taluk_name'] = check_tlk_data_get.block_name_eng

            # if i['panchayat_number'] != 0:
            #     check_pnc_data = Master_Panchayat.objects.filter(panchayat_code= i['panchayat_number'])
            #     if check_pnc_data:
            #         check_pnc_data_get = Master_Panchayat.objects.get(panchayat_code= i['panchayat_number'])
            #         i['panchayat_name'] = check_pnc_data_get.panchayat_name_eng

            # if i['Village_number'] != 0:
            #     check_vil_data = Master_Village.objects.filter(village_code= i['Village_number'])
            #     if check_vil_data:
            #         check_vil_data_get = Master_Village.objects.get(village_code= i['Village_number'])
            #         i['village_name'] = check_vil_data_get.village_name_eng

            # if i['city_number'] != 0:
            #     check_city_data = Master_Ward.objects.filter(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #     if check_city_data:
            #         check_city_data_get = Master_Ward.objects.get(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #         i['city_name'] = check_city_data_get.town_name

            # if i['ward_number'] != 0:
            #     check_ward_data = Master_Ward.objects.filter(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #     if check_ward_data:
            #         check_ward_data_get = Master_Ward.objects.get(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #         i['ward_name'] = check_ward_data_get.ward_name

            # if i['zone_id'] != 0:
            #     check_zone_data = Master_Zone.objects.filter(Q(bbmp_zone_no_ksrsac= i['zone_id']))
            #     if check_zone_data:
            #         check_zone_data_get = Master_Zone.objects.get(Q(bbmp_zone_no_ksrsac= i['zone_id']))
            #         i['zone_name'] = check_zone_data_get.zone_name


            created_data = Contact_Tracing.objects.create(

                # covid_id = i['covid_id'],
                name = i['patient_name'],
                mobile_number = i['mobile_number'],
                age = i['age'],
                gender = i['gender'],
                # category = i['category'],
                district = i['district_number'],
                city = i['city_number'],
                block = i['taluk_number'],
                panchayat = i['panchayat_number'],
                village = i['Village_number'],
                town = i['city_number'],
                ward = i['ward_number'],
                taluk = i['taluk_number'],
                bbmp_zone = i['zone_id'],
                pincode = i['pincode'],
                street = i['main_road_no'],
                door_no = i['flat_door_no'],
                district_name_eng = i['district_name'],
                city_name_eng = i['city_name'],
                block_name_eng = i['taluk_name'],
                panchayat_name_eng = i['panchayat_name'],
                village_name_eng = i['village_name'],
                town_name_eng = i['city_name'],
                ward_name_eng = i['ward_name'],
                taluk_name_eng = i['taluk_name'],
                bbmp_zone_name_eng = i['zone_name'],
                
            )
            created_ids.append(created_data.id)

        return Response({'result':'Updated Sucessfully', 'resp':res_data, 'created_ids':created_ids}, status= status.HTTP_200_OK)

    
    
    

#########################          CONTACT TESTING DATEWISE URBAN DUMP          #########################
class ContectTestingDateWiseUrbanDump(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        from_date = data.get('from_date')
        to_date = data.get('to_date')

        acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
        token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
        acc_json_data = json.dumps(token_body)
        acc_tok_res = requests.post(acc_url, data= token_body)

        acc_token_res = acc_tok_res.json()
        body_hdr = acc_token_res['access_token']

        header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
        json_header = json.dumps(header)

        url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetContactTesting_Datewise'
        input_body = {'FromDate':from_date, 'ToDate':to_date}

        json_data = json.dumps(input_body, indent=4)

        check_contact_testing_dump_response = requests.post(url, data= json_data, headers= header)

        ct_dmp_data = check_contact_testing_dump_response.json()
        res_data = ct_dmp_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA_DATEWISE']

        print(res_data)

        created_ids= []

        for i in res_data:

            # if i['district_number'] != 0:
            #     check_dist_data = Master_District.objects.filter(district_code= i['district_number'])
            #     if check_dist_data:
            #         check_dist_data_get = Master_District.objects.get(district_code= i['district_number'])
            #         i['district_name'] = check_dist_data_get.district_name_eng
            
            # if i['taluk_number'] != 0:
            #     check_tlk_data = Master_Block.objects.filter(block_code= i['taluk_number'])
            #     if check_tlk_data:
            #         check_tlk_data_get = Master_Block.objects.get(block_code= i['taluk_number'])
            #         i['taluk_name'] = check_tlk_data_get.block_name_eng

            # if i['panchayat_number'] != 0:
            #     check_pnc_data = Master_Panchayat.objects.filter(panchayat_code= i['panchayat_number'])
            #     if check_pnc_data:
            #         check_pnc_data_get = Master_Panchayat.objects.get(panchayat_code= i['panchayat_number'])
            #         i['panchayat_name'] = check_pnc_data_get.panchayat_name_eng

            # if i['Village_number'] != 0:
            #     check_vil_data = Master_Village.objects.filter(village_code= i['Village_number'])
            #     if check_vil_data:
            #         check_vil_data_get = Master_Village.objects.get(village_code= i['Village_number'])
            #         i['village_name'] = check_vil_data_get.village_name_eng

            # if i['city_number'] != 0:
            #     check_city_data = Master_Ward.objects.filter(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #     if check_city_data:
            #         check_city_data_get = Master_Ward.objects.get(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #         i['city_name'] = check_city_data_get.town_name

            # if i['ward_number'] != 0:
            #     check_ward_data = Master_Ward.objects.filter(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #     if check_ward_data:
            #         check_ward_data_get = Master_Ward.objects.get(Q(ward_no= i['ward_number']) & Q(new_town_code= i['city_number']))
            #         i['ward_name'] = check_ward_data_get.ward_name

            # if i['zone_id'] != 0:
            #     check_zone_data = Master_Zone.objects.filter(Q(bbmp_zone_no_ksrsac= i['zone_id']))
            #     if check_zone_data:
            #         check_zone_data_get = Master_Zone.objects.get(Q(bbmp_zone_no_ksrsac= i['zone_id']))
            #         i['zone_name'] = check_zone_data_get.zone_name


            created_data = Contact_Tracing.objects.create(

                covid_id = i['covid_id'],
                name = i['patient_name'],
                mobile_number = i['mobile_number'],
                age = i['age'],
                gender = i['gender'],
                category = i['category'],
                district = i['district_number'],
                city = i['city_number'],
                block = i['taluk_number'],
                panchayat = i['panchayat_number'],
                village = i['Village_number'],
                town = i['city_number'],
                ward = i['ward_number'],
                taluk = i['taluk_number'],
                bbmp_zone = i['zone_id'],
                pincode = i['pincode'],
                street = i['main_road_no'],
                door_no = i['flat_door_no'],
                district_name_eng = i['district_name'],
                city_name_eng = i['city_name'],
                block_name_eng = i['taluk_name'],
                panchayat_name_eng = i['panchayat_name'],
                village_name_eng = i['village_name'],
                town_name_eng = i['city_name'],
                ward_name_eng = i['ward_name'],
                taluk_name_eng = i['taluk_name'],
                bbmp_zone_name_eng = i['zone_name'],
                
            )
            created_ids.append(created_data.id)

        return Response({'result':'Updated Sucessfully', 'resp':res_data, 'created_ids':created_ids}, status= status.HTTP_200_OK)



#########################          CONTACT TESTING DATEWISE RURAL DUMP          #########################
class ContectTestingDateWiseRuralDump(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        
        print("CONTACT TESTING   ",data)

        from_date = data.get('from_date')
        to_date = data.get('to_date')

        acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
        token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
        acc_json_data = json.dumps(token_body)
        acc_tok_res = requests.post(acc_url, data= token_body)

        acc_token_res = acc_tok_res.json()
        body_hdr = acc_token_res['access_token']
        print(body_hdr)

        header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
        json_header = json.dumps(header)

        url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetContactTesting_Datewise_Rural/'
        input_body = {'FromDate':from_date, 'ToDate':to_date}

        json_data = json.dumps(input_body, indent=4)

        check_contact_testing_dump_response = requests.post(url, data= json_data, headers= header)

        ct_dmp_data = check_contact_testing_dump_response.json()
        res_data = ct_dmp_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA_DATEWISE']
        print("RESPONSE DATA", ct_dmp_data['TOTAL_COUNT'])
        print("RESPONSE MESSAGE  ",ct_dmp_data['RESPONSE_MESSAGE'])
        created_ids= []
        cnt_dd = 0
        for i in res_data:
            
            print(i)
            print("TESTING LOOP", i)
            

            if i['district_number']:
                check_dist_data = Master_District.objects.get(Q(district_code= i['district_number']))
                i['district_name'] = check_dist_data.district_name_eng
            
            if i['taluk_number']:
                check_tlk_data = Master_Block.objects.get(Q(district_code= i['district_number']) & Q(block_code= i['taluk_number']))
                i['taluk_name'] = check_tlk_data.block_name_eng

            if i['panchayat_number']:
                check_pnc_data = Master_Panchayat.objects.get(Q(district_code= i['district_number']) & Q(block_code= i['taluk_number']) & Q(panchayat_code= i['panchayat_number']))
                i['panchayat_name'] = check_pnc_data.panchayat_name_eng

            if i['Village_number']:
                check_vil_data = Master_Village.objects.get(Q(district_code= i['district_number']) & Q(block_code= i['taluk_number']) & Q(panchayat_code= i['panchayat_number']) & Q(village_code= i['Village_number']))
                i['village_name'] = check_vil_data.village_name_eng

            if i['district_number'] and i['taluk_number'] and i['panchayat_number'] and i['Village_number']:

                check_master_phc_data = Master_PHC.objects.filter(Q(district_code= i['district_number']) & Q(block_code= i['taluk_number']) & Q(panchayat_code= i['panchayat_number']) & Q(village_code= i['Village_number']))
                
                if check_master_phc_data:
                    check_master_phc_data_get = Master_PHC.objects.get(Q(district_code= i['district_number']) & Q(block_code= i['taluk_number']) & Q(panchayat_code= i['panchayat_number']) & Q(village_code= i['Village_number']))
                    check_master_phc_details = Master_PHC.objects.filter(phc_code= check_master_phc_data_get.phc_code).values()[:1]

                    for cmpd in check_master_phc_details:
                        i['phc_id']= cmpd['id']
                else:
                    i['phc_id'] = 'None of the PHC matched'
            
            if i['ward_type'] == 1:
                i['ward_type_name'] = 'urban'
            if i['ward_type'] == 2:
                i['ward_type_name'] = 'rural'


            if i['gender'] == 1:
                i['gender_name'] = 'male'
            if i['gender'] == 2:
                i['gender_name'] = 'female'
            if i['gender'] == 3:
                i['gender_name'] = 'others'
                
            

            # created_ids.append(Contact_Tracing(covid_id = str(cnt_dd).zfill(5),name= i['patient_name'], age = i['age'], gender = i['gender_name'], district= i['district_number'], taluk= i['taluk_number'], 
            #                                     panchayat= i['panchayat_number'], village= i['Village_number'], district_name_eng= i['district_name'], 
            #                                     taluk_name_eng = i['taluk_name'], panchayat_name_eng = i['panchayat_name'], village_name_eng = i['village_name'],
            #                                     date_of_contact_created= i['createdDate'], assigned_phc= i['phc_id'] ))
            Contact_Tracing.objects.create(covid_id = str(cnt_dd).zfill(5), name= i['patient_name'], age = i['age'], gender = i['gender_name'], district= i['district_number'], 
                                                taluk= i['taluk_number'], mobile_number = i['mobile_number'],  ward_type= i['ward_type'],
                                                panchayat= i['panchayat_number'], village= i['Village_number'], district_name_eng= i['district_name'], 
                                                taluk_name_eng = i['taluk_name'], panchayat_name_eng = i['panchayat_name'], village_name_eng = i['village_name'],
                                                date_of_contact_created= i['createdDate'], assigned_phc= i['phc_id'], door_no = i['flat_door_no'], street= i['main_road_no'])
            
            cnt_dd += 1

        print(created_ids)
        # create_data = Contact_Tracing.objects.bulk_create(created_ids)
        # return Response({'result':'Updated Sucessfully', 'resp':res_data, 'created_ids':created_ids}, status= status.HTTP_200_OK)
        return Response({'result':'Updated Sucessfully', 'resp':ct_dmp_data,}, status= status.HTTP_200_OK)

    
    
    
    
#########################          GET 
#########################
class GetOTPData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):


        data = request.data
        print(data)
        print("GET OTP")

        mobile_number = data.get('mobile_number')
        patient_type = data.get('mobile_number_belongs_to')
        print(mobile_number)

        

        if mobile_number and patient_type:
            check_patient_data = Patient.objects.none()
            if patient_type == 'Patient':
                check_patient_data = Patient.objects.filter(Q(mobile_number= mobile_number) & Q(mobile_number_belongs_to= patient_type)).values()
            if check_patient_data:
                return Response({'result': check_patient_data, 'message':'Mobile Number Already Exist' }, status=status.HTTP_406_NOT_ACCEPTABLE)

            else:

                otp = random.randint(10000, 99999)
                print(otp)

                mob_no_array = []

                mob_no_array.append(str(mobile_number))

                body = {'mobileNumber':mob_no_array,'message':'Your OTP is '+str(otp)+', Don\'t share with anyone. From Govt of Karnataka - SNS'}
                # body = {'mobileNumber':['9741862958'],'message':'Your OTP is 12345, Don\'t share with anyone. From Govt of Karnataka - SNS'}

                json_data = json.dumps(body)

                print(json_data)

                # print(body)

                # response = requests.post('http://103.148.156.208:81/Covid/SendOTP.php', data= json_data)
                # response = requests.post('http://securesmsc.com/httpapi/send?username=Sathish@stepnstones.in&password=Sns12345&sender_id=DACWAR&route=T&phonenumber='+str(mobile_number)+'&message=Your%20'+str(otp)+'%20is%20%23field1%23%2C%20Don%27t%20share%20with%20anyone.%20From%20Govt%20of%20Karnataka%20-%20SNS', data= json_data)
                # response = requests.post('http://securesmsc.com/httpapi/send?username=Sathish@stepnstones.in&password=Sns12345&sender_id=DACWAR&route=T&phonenumber='+str(mobile_number)+'&message=Your%20'+str(otp)+'%20is%20%23field1%23%2C%20Don%27t%20share%20with%20anyone.%20From%20Govt%20of%20Karnataka%20-%20SNS')
                response = requests.post('http://securesmsc.com/httpapi/send?username=Sathish@stepnstones.in&password=Sns12345&sender_id=DACWAR&route=T&phonenumber='+str(mobile_number)+'&message=Your%20OTP%20is%20'+str(otp)+'%2C%20Don%27t%20share%20with%20anyone.%20From%20Govt%20of%20Karnataka%20-%20SNS')


                return Response({'result':otp,}, status= status.HTTP_200_OK)
        else:
            return Response({'result':'Something Went Wrong'}, status= status.HTTP_400_BAD_REQUEST)




#########################          ALREADY TESTED PATIENTS          #########################
class ChackAlreadyTestedPatients(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        srf_id = data.get('old_srf_id')
        mobile_number = data.get('existing_mobile_number')

        if srf_id and mobile_number:
            check_already_tested_patient = Patient.objects.filter(Q(mobile_number= mobile_number) & Q(srf_id= srf_id)).values()
            return Response({'result':check_already_tested_patient}, status= status.HTTP_200_OK)

        elif srf_id and mobile_number == '':
            check_already_tested_patient = Patient.objects.filter(Q(srf_id= srf_id)).values()
            return Response({'result':check_already_tested_patient}, status= status.HTTP_200_OK)

        elif srf_id == '' and mobile_number:
            check_already_tested_patient = Patient.objects.filter(Q(mobile_number= mobile_number)).values()            
            return Response({'result':check_already_tested_patient}, status= status.HTTP_200_OK)
        else:
            return Response({'result':'Did not match any records'}, status= status.HTTP_406_NOT_ACCEPTABLE)





#########################          ALREADY TESTED LINE LIST PATIENTS DATA          #########################
class ChackAlreadyTestedPatientsLineListData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        srf_id = data.get('old_srf_id')
        mobile_number = data.get('existing_mobile_number')



        if srf_id and mobile_number:

            acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
            token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
            acc_json_data = json.dumps(token_body)
            acc_tok_res = requests.post(acc_url, data= token_body)

            acc_token_res = acc_tok_res.json()
            body_hdr = acc_token_res['access_token']

            header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
            json_header = json.dumps(header)

            url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetAlreadyTestedData/'
            input_body = {'SRF_ID_OR_MOBILE_NO':mobile_number, 'ID_TYPE':2}

            json_data = json.dumps(input_body, indent=4)

            check_alredy_tested_data_response = requests.post(url, data= json_data, headers= header)

            j_data = check_alredy_tested_data_response.json()
            res_data = j_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA']

            return Response({'result':res_data, 'line_list_details': True}, status= status.HTTP_200_OK)

        elif srf_id and mobile_number == '':
            
            acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
            token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
            acc_json_data = json.dumps(token_body)
            acc_tok_res = requests.post(acc_url, data= token_body)

            acc_token_res = acc_tok_res.json()
            body_hdr = acc_token_res['access_token']

            header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
            json_header = json.dumps(header)

            url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetAlreadyTestedData/'
            input_body = {'SRF_ID_OR_MOBILE_NO':mobile_number, 'ID_TYPE':1}

            json_data = json.dumps(input_body, indent=4)

            check_alredy_tested_data_response = requests.post(url, data= json_data, headers= header)

            j_data = check_alredy_tested_data_response.json()
            res_data = j_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA']

            return Response({'result':res_data, 'line_list_details': True}, status= status.HTTP_200_OK)

        elif srf_id == '' and mobile_number:

            acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
            token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
            acc_json_data = json.dumps(token_body)
            acc_tok_res = requests.post(acc_url, data= token_body)

            acc_token_res = acc_tok_res.json()
            body_hdr = acc_token_res['access_token']

            header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
            json_header = json.dumps(header)

            url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetAlreadyTestedData/'
            input_body = {'SRF_ID_OR_MOBILE_NO':mobile_number, 'ID_TYPE':2}

            json_data = json.dumps(input_body, indent=4)

            check_alredy_tested_data_response = requests.post(url, data= json_data, headers= header)

            j_data = check_alredy_tested_data_response.json()
            res_data = j_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA']

            return Response({'result':res_data, 'line_list_details': True}, status= status.HTTP_200_OK)

        else:
            return Response({'result':'Did not match any records'}, status= status.HTTP_406_NOT_ACCEPTABLE)

        
        
        

#########################          CONTACT TRACING PATIENTS          #########################
class ChackContactTracingPatients(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        # srf_id = data.get('old_srf_id')
        mobile_number = data.get('existing_mobile_number')

        if mobile_number:
            check_contact_tracing_patient = Contact_Tracing.objects.filter(Q(mobile_number= mobile_number)).values()
            if check_contact_tracing_patient:
                for i in check_contact_tracing_patient:
                    i['patient_name'] = i['name']
                return Response({'result':check_contact_tracing_patient}, status= status.HTTP_200_OK)

            else:

                acc_url = 'https://www.covidwar.karnataka.gov.in/service19_test/token'
                token_body = {'grant_type':'password','username':'uan387r8hdo9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs678sfui8udf8u', 'password':'vnm488d76go9734eb83d03ec5ba1e3252d08d9ad102b8f0b2cs6785562sed6vv'}
                acc_json_data = json.dumps(token_body)
                acc_tok_res = requests.post(acc_url, data= token_body)

                acc_token_res = acc_tok_res.json()
                body_hdr = acc_token_res['access_token']

                print(body_hdr)

                header = {"Authorization": "Bearer "+body_hdr +"", "Content-Type":"application/json"}
                json_header = json.dumps(header)

                # url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetAlreadyTestedData/'
                # input_body = {'SRF_ID_OR_MOBILE_NO':mobile_number, 'ID_TYPE':2}

                url = 'https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_GetContactTesting/'
                input_body = {'PATIENT_MOBILE_NUMBER':mobile_number}

                json_data = json.dumps(input_body, indent=4)

                check_alredy_tested_data_response = requests.post(url, data= json_data, headers= header)

                j_data = check_alredy_tested_data_response.json()
                print(j_data)
                res_data = j_data['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA']
                return Response({'result':res_data}, status= status.HTTP_200_OK)


                # url = 'https://www.covidwar.karnataka.gov.in/service19_test'
                # input_body = {'PATIENT_MOBILE_NUMBER':mobile_no}
                # json_data = json.dumps(input_body)
                # check_contact_testing_response = requests.post(url, data= json_data)
                # res_json = check_contact_testing_response.json()
                # res_data = res_json['RESPONSE_REC_RESULT']['REC_RESPONCE_DATA']

                # return Response({'result':res_data}, status= status.HTTP_200_OK)


        # elif srf_id and mobile_number == '':
        #     check_contact_tracing_patient = Contact_Tracing.objects.filter(Q(srf_id= srf_id)).values()
        #     for i in check_contact_tracing_patient:
        #         i['patient_name'] = i['name']
        #     return Response({'result':check_contact_tracing_patient}, status= status.HTTP_200_OK)

        # elif srf_id == '' and mobile_number:
        #     check_contact_tracing_patient = Contact_Tracing.objects.filter(Q(mobile_number= mobile_number)).values()
        #     for i in check_contact_tracing_patient:
        #         i['patient_name'] = i['name']
        #     return Response({'result':check_contact_tracing_patient}, status= status.HTTP_200_OK)

        else:
            return Response({'result':'Did not match any records'}, status= status.HTTP_406_NOT_ACCEPTABLE)






#########################          GET ALREADY TESTED PATIENT DETAILS          #########################
class GetAlreadyTestedPatientsData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        patient_id = data.get('table_id')
        mobile_number = data.get('existing_mobile_number')
        srf_id = data.get('srf_id')

        check_already_tested_patient_sel = Patient.objects.filter(Q(id= patient_id) & Q(mobile_number= mobile_number) & Q(srf_id= srf_id)).values().order_by('-id')
        # check_already_tested_patient_pre = Patient.objects.filter(Q(id= patient_id) & Q(mobile_number= mobile_number) & Q(srf_id= srf_id)).prefetch_related('specimen_type__specimen_type_name', 'test_type__test_type_name',).values()
        
        patient_dist = Master_District.objects.none()
        patient_taluk = Master_Block.objects.none()
        patient_panc = Master_Panchayat.objects.none()
        patient_vill = Master_Village.objects.none()
        patient_ward = Master_Ward.objects.none()
        patient_zone = Master_Zone.objects.none()



        for i in check_already_tested_patient_sel:

            check_address_data = Patient_Address.objects.filter(patient_id= i['id'])
            check_outsider_address_data = Outside_Patient_Address.objects.filter(patient_id= i['id'])
            
            if check_address_data:
                print("ONEEEEE")
                spe_type_ref = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                tt_ref = Test_Type_Ref.objects.get(id= i['test_type_id'])
                pati_add = Patient_Address.objects.filter(patient_id= i['id'])

                i['specimen_type_name'] = spe_type_ref.specimen_type_name
                i['test_type_name'] = tt_ref.test_type_name

                i['co_morbidity_type'] = ast.literal_eval(i['co_morbidity_type'])
                i['symptoms_list'] = ast.literal_eval(i['symptoms_list'])

                patient_dist = Master_District.objects.none()
                patient_taluk = Master_Block.objects.none()
                patient_panc = Master_Panchayat.objects.none()
                patient_vill = Master_Village.objects.none()
                patient_ward = Master_Ward.objects.none()
                patient_zone = Master_Zone.objects.none()


                if pati_add:
                    print("TWOOOOOOOOOO")
                    patint_addr = Patient_Address.objects.get(patient_id= i['id'])

                    if patint_addr.resident_type == 'Local':
                        print("LOCALLLLLLLLLLL")

                        patient_dist = Master_District.objects.filter(Q(district_code= patint_addr.district_name) | Q(district_name_eng= patint_addr.district_name)).values()
                        # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                        # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                        patient_taluk = Master_Block.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                        patient_panc = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                        patient_vill = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                        patient_ward = Master_Ward.objects.none()
                        patient_zone = Master_Zone.objects.none()


                        # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                        # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                        # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                        i['state_name'] = patint_addr.state_name
                        i['district_name'] = patint_addr.district_name
                        i['city_name'] = patint_addr.city_name
                        i['ward_name'] = patint_addr.ward_name
                        i['taluk_name'] = patint_addr.taluk_name
                        i['panchayat_name'] = patint_addr.panchayat_name
                        i['village_name'] = patint_addr.village_name
                        i['resident_type'] = patint_addr.resident_type
                        i['zone_type'] = patint_addr.zone_type
                        i['ward_type'] = patint_addr.ward_type
                        i['flat_door_no'] = patint_addr.flat_door_no
                        i['main_road_no'] = patint_addr.main_road_no
                        i['pincode'] = patint_addr.pincode
                        i['locality'] = patint_addr.locality
                        i['landmark'] = patint_addr.landmark

                        i['patient_dist'] = patient_dist
                        i['patient_taluk'] = patient_taluk
                        i['patient_panc'] = patient_panc
                        i['patient_vill'] = patient_vill

                        i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                        i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
                        i['patient_ward_details'] = Master_Ward.objects.none()
                        i['patient_zone_details'] = Master_Zone.objects.none()


                    if patint_addr.resident_type == 'Outsider':
                        print("Outsiderrrrrrr")
                        if patint_addr.ward_type == 'rural':
                            print('RURALLLLLLLLLLL')
                            patient_dist = Master_District.objects.filter(Q(district_code= patint_addr.district_name) | Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                            patient_taluk = Master_Block.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                            patient_panc = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                            patient_vill = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                            patient_ward = Master_Ward.objects.none()
                            patient_zone = Master_Zone.objects.none()

                            # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                            i['state_name'] = patint_addr.state_name
                            i['district_name'] = patint_addr.district_name
                            i['city_name'] = patint_addr.city_name
                            i['ward_name'] = patint_addr.ward_name
                            i['taluk_name'] = patint_addr.taluk_name
                            i['panchayat_name'] = patint_addr.panchayat_name
                            i['village_name'] = patint_addr.village_name
                            i['resident_type'] = patint_addr.resident_type
                            i['zone_type'] = patint_addr.zone_type
                            i['ward_type'] = patint_addr.ward_type
                            i['flat_door_no'] = patint_addr.flat_door_no
                            i['main_road_no'] = patint_addr.main_road_no
                            i['pincode'] = patint_addr.pincode
                            i['locality'] = patint_addr.locality
                            i['landmark'] = patint_addr.landmark

                            i['patient_dist'] = patient_dist
                            i['patient_taluk'] = patient_taluk
                            i['patient_panc'] = patient_panc
                            i['patient_vill'] = patient_vill

                            i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                            i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
                            i['patient_ward_details'] = Master_Ward.objects.none()
                            i['patient_zone_details'] = Master_Zone.objects.none()
                            
                        if patint_addr.ward_type == 'urban':
                            print("URBANNNNNNNNNNNN")

                            patient_dist = Master_District.objects.filter(Q(district_code= patint_addr.district_name) | Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                            patient_ward = Master_Ward.objects.filter(Q(district_code= patint_addr.district_name) & Q(new_town_code= patint_addr.city_name) & Q(ward_no= patint_addr.ward_name)).values()
                            patient_zone = Master_Zone.objects.none()
                            patient_taluk = Master_Block.objects.none()
                            patient_panc = Master_Panchayat.objects.none()
                            patient_vill = Master_Village.objects.none()

                            # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                            i['state_name'] = patint_addr.state_name
                            i['district_name'] = patint_addr.district_name
                            i['city_name'] = patint_addr.city_name
                            i['ward_name'] = patint_addr.ward_name
                            i['taluk_name'] = patint_addr.taluk_name
                            i['panchayat_name'] = patint_addr.panchayat_name
                            i['village_name'] = patint_addr.village_name
                            i['resident_type'] = patint_addr.resident_type
                            i['zone_type'] = patint_addr.zone_type
                            i['ward_type'] = patint_addr.ward_type
                            i['flat_door_no'] = patint_addr.flat_door_no
                            i['main_road_no'] = patint_addr.main_road_no
                            i['pincode'] = patint_addr.pincode
                            i['locality'] = patint_addr.locality
                            i['landmark'] = patint_addr.landmark

                            i['patient_dist'] = patient_dist
                            i['patient_taluk'] = patient_taluk
                            i['patient_panc'] = patient_panc
                            i['patient_vill'] = patient_vill

                            # i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                            # i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
                            i['patient_panchayt_single_row'] = Master_Panchayat.objects.none()
                            i['patient_village_single_row'] = Master_Village.objects.none()
                            i['patient_ward_details'] = Master_Ward.objects.filter(Q(district_code= patint_addr.district_name) & Q(new_town_code= patint_addr.city_name) & Q(ward_no= patint_addr.ward_name)).values()
                            i['patient_zone_details'] = Master_Zone.objects.none()


                        if patint_addr.ward_type == 'bbmp':
                            print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
                            patient_dist = Master_District.objects.filter(Q(district_code= patint_addr.district_name) | Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                            # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                            patient_taluk = Master_Block.objects.none()
                            patient_panc = Master_Panchayat.objects.none()
                            patient_vill = Master_Village.objects.none()
                            patient_ward = Master_Ward.objects.none()
                            patient_zone = Master_Zone.objects.filter(Q(district_code= patint_addr.district_name) & Q(zone_name= patint_addr.zone_type) & Q(new_ward_no= patint_addr.ward_name)).values()

                            # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                            # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                            i['state_name'] = patint_addr.state_name
                            i['district_name'] = patint_addr.district_name
                            i['city_name'] = patint_addr.city_name
                            i['ward_name'] = patint_addr.ward_name
                            i['taluk_name'] = patint_addr.taluk_name
                            i['panchayat_name'] = patint_addr.panchayat_name
                            i['village_name'] = patint_addr.village_name
                            i['resident_type'] = patint_addr.resident_type
                            i['zone_type'] = patint_addr.zone_type
                            i['ward_type'] = patint_addr.ward_type
                            i['flat_door_no'] = patint_addr.flat_door_no
                            i['main_road_no'] = patint_addr.main_road_no
                            i['pincode'] = patint_addr.pincode
                            i['locality'] = patint_addr.locality
                            i['landmark'] = patint_addr.landmark

                            i['patient_dist'] = patient_dist
                            i['patient_taluk'] = patient_taluk
                            i['patient_panc'] = patient_panc
                            i['patient_vill'] = patient_vill


                            # i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                            # i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
                            i['patient_panchayt_single_row'] = Master_Panchayat.objects.none()
                            i['patient_village_single_row'] = Master_Village.objects.none()
                            # i['patient_ward_details'] = Master_Ward.objects.filter(Q(district_name= patint_addr.district_name) & Q(city_name= patint_addr.city_name) & Q(ward_name= patint_addr.ward_name)).values()
                            i['patient_ward_details'] = Master_Ward.objects.none()
                            i['patient_zone_details'] = Master_Zone.objects.filter(Q(district_code= patint_addr.district_name) & Q(zone_name= patint_addr.zone_type) & Q(new_ward_no= patint_addr.ward_name)).values()
                            


                else:
                    print("ELSEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    i['state_name'] = ''
                    i['district_name'] = ''
                    i['city_name'] = ''
                    i['ward_name'] = ''
                    i['taluk_name'] = ''
                    i['panchayat_name'] = ''
                    i['village_name'] = ''
                    i['resident_type'] = ''
                    i['zone_type'] = ''
                    i['ward_type'] = ''
                    i['flat_door_no'] = ''
                    i['main_road_no'] = ''
                    i['pincode'] = ''
                    i['locality'] = ''
                    i['landmark'] = ''
                    i['patient_dist'] = patient_dist
                    i['patient_taluk'] = patient_taluk
                    i['patient_panc'] = patient_panc
                    i['patient_vill'] = patient_vill

                # print(check_already_tested_patient_sel)
                # print(patient_dist)
                # print(patient_taluk)
                # print(patient_panc)
                # print(patient_vill)
                # return Response({'result':check_already_tested_patient_sel, 'patient_dist':patient_dist, 'patient_taluk':patient_taluk, 'patient_panc':patient_panc, 'patient_vill':patient_vill}, status=status.HTTP_200_OK)

            if check_outsider_address_data:
                print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                spe_type_ref = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                tt_ref = Test_Type_Ref.objects.get(id= i['test_type_id'])
                pati_add = Outside_Patient_Address.objects.filter(patient_id= i['id'])

                i['specimen_type_name'] = spe_type_ref.specimen_type_name
                i['test_type_name'] = tt_ref.test_type_name

                i['co_morbidity_type'] = ast.literal_eval(i['co_morbidity_type'])
                i['symptoms_list'] = ast.literal_eval(i['symptoms_list'])

                patient_dist = Master_District.objects.none()
                patient_taluk = Master_Block.objects.none()
                patient_panc = Master_Panchayat.objects.none()
                patient_vill = Master_Village.objects.none()
                patient_ward = Master_Ward.objects.none()
                patient_zone = Master_Zone.objects.none()


                if pati_add:
                    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm")
                    patint_addr = Outside_Patient_Address.objects.get(patient_id= i['id'])

                    patient_dist = Master_District.objects.none()
                    # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                    # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                    patient_taluk = Master_Block.objects.none()
                    patient_panc = Master_Panchayat.objects.none()
                    patient_vill = Master_Village.objects.none()

                    patient_ward = Master_Ward.objects.none()
                    patient_zone = Master_Zone.objects.none()

                    # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                    # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                    # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                    i['state_name'] = patint_addr.state_name
                    i['district_name'] = patint_addr.district_name
                    i['city_name'] = patint_addr.city_name
                    i['ward_name'] = patint_addr.ward_name
                    i['taluk_name'] = patint_addr.taluk_name
                    i['panchayat_name'] = patint_addr.panchayat_name
                    i['village_name'] = patint_addr.village_name
                    i['resident_type'] = patint_addr.resident_type
                    i['zone_type'] = patint_addr.zone_type
                    i['ward_type'] = patint_addr.ward_type
                    i['flat_door_no'] = patint_addr.flat_door_no
                    i['main_road_no'] = patint_addr.main_road_no
                    i['pincode'] = patint_addr.pincode
                    i['locality'] = patint_addr.locality
                    i['landmark'] = patint_addr.landmark

                    i['patient_dist'] = patient_dist
                    i['patient_taluk'] = patient_taluk
                    i['patient_panc'] = patient_panc
                    i['patient_vill'] = patient_vill

                    # i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                    # i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
                    i['patient_panchayt_single_row'] = Master_Panchayat.objects.none()
                    i['patient_village_single_row'] = Master_Village.objects.none()
                    i['patient_ward_details'] = Master_Ward.objects.none()
                    i['patient_zone_details'] = Master_Zone.objects.none()
                    
                else:
                    i['state_name'] = ''
                    i['district_name'] = ''
                    i['city_name'] = ''
                    i['ward_name'] = ''
                    i['taluk_name'] = ''
                    i['panchayat_name'] = ''
                    i['village_name'] = ''
                    i['resident_type'] = ''
                    i['zone_type'] = ''
                    i['ward_type'] = ''
                    i['flat_door_no'] = ''
                    i['main_road_no'] = ''
                    i['pincode'] = ''
                    i['locality'] = ''
                    i['landmark'] = ''
                    i['patient_dist'] = patient_dist
                    i['patient_taluk'] = patient_taluk
                    i['patient_panc'] = patient_panc
                    i['patient_vill'] = patient_vill

                
                # print(check_already_tested_patient_sel)
                # print(patient_dist)
                # print(patient_taluk)
                # print(patient_panc)
                # print(patient_vill)
                # return Response({'result':check_already_tested_patient_sel, 'patient_dist':patient_dist, 'patient_taluk':patient_taluk, 'patient_panc':patient_panc, 'patient_vill':patient_vill}, status=status.HTTP_200_OK)


        # print(check_already_tested_patient_sel)
        # print(patient_dist)
        # print(patient_taluk)
        # print(patient_panc)
        # print(patient_vill)
        # return Response({'result':check_already_tested_patient_sel, 'patient_dist':patient_dist, 'patient_taluk':patient_taluk, 'patient_panc':patient_panc, 'patient_vill':patient_vill}, status=status.HTTP_200_OK)

        print(check_already_tested_patient_sel)
        print(patient_dist)
        print(patient_taluk)
        print(patient_panc)
        print(patient_vill)
        return Response({'result':check_already_tested_patient_sel, 'patient_dist':patient_dist, 'patient_taluk':patient_taluk, 'patient_panc':patient_panc, 'patient_vill':patient_vill}, status=status.HTTP_200_OK)


#########################          GET CONTACT TRACING PATIENT DETAILS          #########################
class GetContactTracingPatientsData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        patient_id = data.get('table_id')
        mobile_number = data.get('existing_mobile_number')
        srf_id = data.get('srf_id')

        check_already_tested_patient_sel = Contact_Tracing.objects.filter(Q(id= patient_id) & Q(mobile_number= mobile_number) | Q(srf_id= srf_id)).values().order_by('-id')
        # check_already_tested_patient_pre = New_Entry_Contact_Tracing.objects.filter(Q(id= patient_id) & Q(mobile_number= mobile_number) & Q(srf_id= srf_id)).prefetch_related('specimen_type__specimen_type_name', 'test_type__test_type_name',).values()

        for i in check_already_tested_patient_sel:
            spe_type_ref = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
            tt_ref = Test_Type_Ref.objects.get(id= i['test_type_id'])
            pati_add = New_Entry_Contact_Tracing_Address.objects.filter(patient_id= i['id'])

            i['specimen_type_name'] = spe_type_ref.specimen_type_name
            i['test_type_name'] = tt_ref.test_type_name

            i['co_morbidity_type'] = ast.literal_eval(i['co_morbidity_type'])
            i['symptoms_list'] = ast.literal_eval(i['symptoms_list'])

            patient_dist = Master_District.objects.none()
            patient_taluk = Master_Block.objects.none()
            patient_panc = Master_Panchayat.objects.none()
            patient_vill = Master_Village.objects.none()
            if pati_add:
                patint_addr = New_Entry_Contact_Tracing_Address.objects.get(patient_id= i['id'])

                patient_dist = Master_District.objects.filter(Q(district_code= patint_addr.district_name) | Q(district_name_eng= patint_addr.district_name)).values()
                # patient_dist = Master_District.objects.filter(Q(district_name_eng= patint_addr.district_name)).values()
                # patient_dist_get = Master_District.objects.get(Q(district_name_eng= patint_addr.district_name))

                patient_taluk = Master_Block.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                patient_panc = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()
                patient_vill = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name)).values()

                # patient_taluk = Master_Block.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                # patient_panc = Master_Panchayat.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()
                # patient_vill = Master_Village.objects.filter(Q(district_code= patient_dist_get.district_code) & Q(block_code= patint_addr.taluk_name)).values()

                i['state_name'] = patint_addr.state_name
                i['district_name'] = patint_addr.district_name
                i['city_name'] = patint_addr.city_name
                i['ward_name'] = patint_addr.ward_name
                i['taluk_name'] = patint_addr.taluk_name
                i['panchayat_name'] = patint_addr.panchayat_name
                i['village_name'] = patint_addr.village_name
                i['resident_type'] = patint_addr.resident_type
                i['zone_type'] = patint_addr.zone_type
                i['ward_type'] = patint_addr.ward_type
                i['flat_door_no'] = patint_addr.flat_door_no
                i['main_road_no'] = patint_addr.main_road_no
                i['pincode'] = patint_addr.pincode

                i['patient_dist'] = patient_dist
                i['patient_taluk'] = patient_taluk
                i['patient_panc'] = patient_panc
                i['patient_vill'] = patient_vill

                i['patient_panchayt_single_row'] = Master_Panchayat.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name)).values()
                i['patient_village_single_row'] = Master_Village.objects.filter(Q(district_code= patint_addr.district_name) & Q(block_code= patint_addr.taluk_name) & Q(panchayat_code= patint_addr.panchayat_name) & Q(village_code= patint_addr.village_name)).values()
            else:
                i['state_name'] = ''
                i['district_name'] = ''
                i['city_name'] = ''
                i['ward_name'] = ''
                i['taluk_name'] = ''
                i['panchayat_name'] = ''
                i['village_name'] = ''
                i['resident_type'] = ''
                i['zone_type'] = ''
                i['ward_type'] = ''
                i['flat_door_no'] = ''
                i['main_road_no'] = ''
                i['pincode'] = ''
                i['patient_dist'] = patient_dist
                i['patient_taluk'] = patient_taluk
                i['patient_panc'] = patient_panc
                i['patient_vill'] = patient_vill

        return Response({'result':check_already_tested_patient_sel, 'patient_dist':patient_dist, 'patient_taluk':patient_taluk, 'patient_panc':patient_panc, 'patient_vill':patient_vill}, status=status.HTTP_200_OK)



#########################          MASTER TABLE FILTER          #########################
class MasterTableFilterData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        district = data.get('district_name')
        type = data.get('ward_type')
        resident_type = data.get('resident_type')
        user_id= data.get('user_id')


        if resident_type == 'Local':

            taluk = data.get('taluk')
            panchayat = data.get('panchayat')
            village = data.get('village')


            check_swab_collector_details = Swab_Collection_Centre.objects.get(user_id= user_id)

            master_data = Master_PHC.objects.get(id= check_swab_collector_details.phc_master_id)

            if taluk == '' and panchayat == '' and village == '':
                print("3 EMPTY")
                taluk_data = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district)).values('block_name_eng', 'block_code').distinct()

                # check_block_id = []

                # phc_block_details = []

                # print(taluk_data)

                # for i in taluk_data:
                #     if i['block_code'] not in check_block_id:
                #         check_block_id.append(i['block_code'])

                # print(check_block_id)
                # for i in check_block_id:
                #     get_phc_block_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district) & Q(block_code= i)).values()
                #     if get_phc_block_details:
                #         for j in get_phc_block_details:
                #             phc_block_details.append(j)
                # print("LLLLLLLLLLLLLLLLLLLLLLLLLL", phc_block_details)
                return Response(taluk_data)

            if taluk and panchayat == '' and village == '':

                check_pan_id = []

                phc_pan_details = []

                panchayat_data = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district) & Q(block_code= taluk)).values('panchayat_name_eng', 'panchayat_code').distinct()

                # for i in panchayat_data:
                    
                #     if i['panchayat_code'] not in check_pan_id:
                #         check_pan_id.append(i['panchayat_code'])


                # for i in check_pan_id:
                #     get_phc_pan_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district) & Q(block_code= i)).values()
                    
                #     if get_phc_pan_details:
                #         for j in get_phc_pan_details:
                #             phc_pan_details.append(j)

                # print("FFFFFFFFFFFFFFFFFFFFFFFFFF", phc_pan_details)
                return Response(panchayat_data)
                

            if taluk and panchayat and village == '':
                print("1 EMPTY")

                check_vill_id = []

                phc_vill_details = []

                village_data = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district) & Q(block_code= taluk) & Q(panchayat_code= panchayat)).values('village_name_eng', 'village_code').distinct()

                # for i in panchayat_data:
                #     if i['village_code'] not in check_vill_id:
                #         check_vill_id.append(i['village_code'])

                
                # for i in check_vill_id:
                #     get_phc_vill_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= district) & Q(block_code= taluk) & Q(panchayat_code= i)).values()
                    
                #     if get_phc_vill_details:
                #         for j in get_phc_vill_details:
                #             phc_vill_details.append(j)

                # print("DDDDDDDDDDDDDDDDDDDDDD", phc_vill_details)
                return Response(village_data)
            else:
                empty_arry = []
                return Response(empty_arry)
            
            
            # check_swab_collector_details = Swab_Collection_Centre.objects.get(user_id= user_id)

            # master_data = Master_PHC.objects.get(id= check_swab_collector_details.phc_master_id)

            # check_village_details = Master_PHC.objects.filter(phc_code= master_data.phc_code).values()

            # check_dist_id = []
            # check_block_id = []
            # check_pan_id = []
            # check_vill_id = []

            # dist_details = Master_PHC.objects.filter(phc_code= master_data.phc_code).values('district_code').distinct()
            # locat_phc_dist_details = []


            # for i in check_village_details:

            #     if i['district_code'] not in check_dist_id:
            #         check_dist_id.append(i['district_code'])
                
            #     if i['block_code'] not in check_block_id:
            #         check_block_id.append(i['block_code'])
                
            #     if i['panchayat_code'] not in check_pan_id:
            #         check_pan_id.append(i['panchayat_code'])

            #     if i['village_code'] not in check_vill_id:
            #         check_vill_id.append(i['village_code'])

            # phc_dist_details = []
            # phc_block_details = []
            # phc_pan_details = []
            # phc_vill_details = []

            # print(master_data.phc_code)

            # for i in check_dist_id:
            #     print(i)
            #     get_phc_dist_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= i)).values('district_code', 'district_name_eng').distinct()
            #     print(get_phc_dist_details)
            #     print(len(get_phc_dist_details))
            #     if get_phc_dist_details:
            #         for j in get_phc_dist_details:
            #             phc_dist_details.append(j)

            # for i in check_block_id:
            #     print(i)
            #     get_phc_block_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(block_code= i)).values('block_name_eng', 'block_code').distinct()
            #     print(get_phc_block_details)
            #     print(len(get_phc_block_details))
            #     if get_phc_block_details:
            #         for j in get_phc_block_details:
            #             phc_block_details.append(j)

            # for i in check_pan_id:
            #     print(i)
            #     get_phc_pan_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(panchayat_code= i)).values('panchayat_name_eng', 'panchayat_code').distinct()
            #     print(get_phc_pan_details)
            #     print(len(get_phc_pan_details))
            #     if get_phc_pan_details:
            #         for j in get_phc_pan_details:
            #             phc_pan_details.append(j)

            # for i in check_vill_id:
            #     print(i)
            #     get_phc_vill_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(village_code= i)).values('village_name', 'village_code').distinct()
            #     print(get_phc_vill_details)
            #     print(len(get_phc_vill_details))
            #     if get_phc_vill_details:
            #         for j in get_phc_vill_details:
            #             phc_vill_details.append(j)


            # print(phc_dist_details)
            # print(phc_block_details)
            # print(phc_pan_details)
            # print(phc_vill_details)

            # return Response({'phc_district_details':phc_dist_details, 'phc_block_details': phc_block_details, 'phc_pan_details':phc_pan_details, 'phc_vill_details':phc_vill_details}, status=status.HTTP_200_OK)
        else:

            if type == 'urban':
                print("URBAN")
                city = data.get('city')
                ward = data.get('ward')
                print(city)
                print(ward)

                if city == '' and ward == '':
                    city_data = Master_Ward.objects.filter(district_code= district).values('town_name', 'new_town_code').distinct()
                    print("YYYYYYYYYYYYYYYYYYYY")
                    print(city_data)
                    return Response(city_data)
                if city and ward == '':
                    ward_data = Master_Ward.objects.filter(Q(district_code= district) & Q(new_town_code= city)).values()
                    return Response(ward_data)
                else:
                    empty_arry = []
                    return Response(empty_arry)


            if type == 'rural':
                print("RURAl")
                taluk = data.get('taluk')
                panchayat = data.get('panchayat')
                village = data.get('village')

                

                print(taluk)
                print(panchayat)
                print(village)

                if taluk == '' and panchayat == '' and village == '':
                    print("3 EMPTY")
                    taluk_data = Master_Block.objects.filter(district_code= district).values()
                    return Response(taluk_data)

                if taluk and panchayat == '' and village == '':
                    panchayat_data = Master_Panchayat.objects.filter(Q(district_code= district) & Q(block_code= taluk)).values()
                    return Response(panchayat_data)

                if taluk and panchayat and village == '':
                    print("1 EMPTY")
                    village_data = Master_Village.objects.filter(Q(district_code= district) & Q(block_code= taluk) & Q(panchayat_code= panchayat)).values()
                    return Response(village_data)
                else:
                    empty_arry = []
                    return Response(empty_arry)

            if type == 'bbmp':
                print("BBMP")
                zone = data.get('zone')
                ward = data.get('ward')
                print(zone)
                print(ward)


                
                if zone == '' and ward == '':
                    zone_data = Master_Zone.objects.filter(district_code= district).values('zone_name', 'bbmp_zone_no_ksrsac').distinct()
                    print("YYYYYYYYYYYYYYYYYYYY")
                    print(zone_data)
                    return Response(zone_data)
                if zone and ward == '':
                    ward_data = Master_Zone.objects.filter(Q(district_code= district) & Q(zone_name= zone)).values()
                    return Response(ward_data)
                else:
                    empty_arry = []
                    return Response(empty_arry)




#########################          PHC DATE FILTER          #########################
class PHCUserDAteFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id      = data.get('user_id')
        start_date = data.get('startdate')
        end_date = data.get('endDate')

        start_data_split = start_date.split('-')
        end_date_split = end_date.split('-')


        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()
        check_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':
                all_phcm_data = []
                check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                for i in check_all_slab_collector:
                    # patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                    patient_details = Patient.objects.filter(Q(added_by=i['user_id'])  & Q(package_sampling_id__isnull = True) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
                    for pd in patient_details:
                        print(pd)
                        patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                        patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                        patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                        pd['patient_type_name'] = patient_type_data.patient_type_name
                        pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                        pd['test_type_name']= patient_test_type_data.test_type_name

                        check_test_status = Patient_Testing.objects.filter(patient_id= pd['id'])
                        if check_test_status:
                            check_test_status_get = Patient_Testing.objects.get(patient_id= pd['id'])
                            i['test_result'] = check_test_status_get.testing_status
                        else:
                            i['test_result'] = 2

                        all_phcm_data.append(pd)
                return Response({'patient_details':all_phcm_data,'result': 'successfull'}, status= status.HTTP_200_OK)

            if check_user_roles.role_name == 'PHCS':
                # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()

                patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= 31) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
                    if check_test_status:
                        check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
                        i['test_result'] = check_test_status_get.testing_status
                    else:
                        i['test_result'] = 2

                return Response({'patient_details':patient_details,'result': 'successfull'}, status= status.HTTP_200_OK)
        
        elif check_lab_user:

            patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= 31) & Q(create_timestamp__date__gte= asdatetime.strptime(start_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(end_date,'%Y-%m-%d'))).values().order_by('-id')
            
            for i in patient_details:
                patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                i['patient_type_name'] = patient_type_data.patient_type_name
                i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                i['test_type_name']= patient_test_type_data.test_type_name

                check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
                if check_test_status:
                    check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
                    i['test_result'] = check_test_status_get.testing_status
                else:
                    i['test_result'] = 2
            return Response({'patient_details':patient_details,'result': 'successfull'}, status= status.HTTP_200_OK)

        else:
            return Response({'result': 'Something Went Wrong'}, status= status.HTTP_400_BAD_REQUEST)






#########################          PHC CONTACT TRACING DATE FILTER          #########################
class PHCContactTracingDAteFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)
        print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        # user_id      = data.get('user_id')
        start_date = data.get('startdate')
        end_date = data.get('endDate')

        start_data_split = start_date.split('-')
        end_date_split = end_date.split('-')

        # contact_tracing = Contact_Tracing.objects.filter(Q(assigned_msc_user__isnull= True) & Q(date_of_contact_created__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(date_of_contact_created__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
        contact_tracing = Contact_Tracing.objects.filter(Q(date_of_contact_created__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(date_of_contact_created__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
        # for pd in patient_details:
        #     print(pd)
        #     patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
        #     patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
        #     patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
        #     pd['patient_type_name'] = patient_type_data.patient_type_name
        #     pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
        #     pd['test_type_name']= patient_test_type_data.test_type_name

        #     check_test_status = Patient_Testing.objects.filter(patient_id= pd['id'])
        #     if check_test_status:
        #         check_test_status_get = Patient_Testing.objects.get(patient_id= pd['id'])
        #         i['test_result'] = check_test_status_get.testing_status
        #     else:
        #         i['test_result'] = 2

        #     all_phcm_data.append(pd)
        for i in contact_tracing:
            print(i['assigned_msc_user_id'])
            print(i)
            if i['assigned_msc_user_id'] == None:
                i['status'] = 0
                i['msc_name'] = 'N/A'
            else:
                i['status'] = 1
                check_user_name = User.objects.get(id= i['assigned_msc_user_id'])
                i['msc_name'] = check_user_name.first_name

        return Response({'contact_tracing_filter_data':contact_tracing,'result': 'successfull'}, status= status.HTTP_200_OK)

        

        # # check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        # if check_user:
        #     check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
        #     check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
        #     if check_user_roles.role_name == 'PHCMO':
        #         all_phcm_data = []
        #         check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
        #         for i in check_all_slab_collector:
        #             # patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
        #             patient_details = Patient.objects.filter(Q(added_by=i['user_id'])  & Q(package_sampling_id__isnull = True) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
        #             for pd in patient_details:
        #                 print(pd)
        #                 patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
        #                 patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
        #                 patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
        #                 pd['patient_type_name'] = patient_type_data.patient_type_name
        #                 pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
        #                 pd['test_type_name']= patient_test_type_data.test_type_name

        #                 check_test_status = Patient_Testing.objects.filter(patient_id= pd['id'])
        #                 if check_test_status:
        #                     check_test_status_get = Patient_Testing.objects.get(patient_id= pd['id'])
        #                     i['test_result'] = check_test_status_get.testing_status
        #                 else:
        #                     i['test_result'] = 2

        #                 all_phcm_data.append(pd)
        #         return Response({'patient_details':all_phcm_data,'result': 'successfull'}, status= status.HTTP_200_OK)

        #     if check_user_roles.role_name == 'PHCS':
        #         # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
        #         # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()

        #         patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values().order_by('-id')
        #         for i in patient_details:
        #             patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
        #             patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
        #             patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
        #             i['patient_type_name'] = patient_type_data.patient_type_name
        #             i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
        #             i['test_type_name']= patient_test_type_data.test_type_name

        #             check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
        #             if check_test_status:
        #                 check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
        #                 i['test_result'] = check_test_status_get.testing_status
        #             else:
        #                 i['test_result'] = 2

        #         return Response({'patient_details':patient_details,'result': 'successfull'}, status= status.HTTP_200_OK)
        # else:
        #     return Response({'result': 'Something Went Wrong'}, status= status.HTTP_400_BAD_REQUEST)



#########################          PHC STATUS FILTER          #########################
class PHCUseStatusFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id      = data.get('user_id')
        status_filter = data.get('swab_collection_status')


        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()
        check_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':
                all_phcm_data = []
                check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                for i in check_all_slab_collector:
                    # patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                    
                    patient_details = Patient.objects.filter(Q(added_by=i['user_id'])  & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= status_filter)).values().order_by('-id')
                    for pd in patient_details:
                        patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                        patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                        patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                        pd['patient_type_name'] = patient_type_data.patient_type_name
                        pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                        pd['test_type_name']= patient_test_type_data.test_type_name

                        check_tkb = Testing_Kit_Barcode.objects.filter(id= pd['testing_kit_barcode_id'])
                        if check_tkb:
                            check_tkb_get = Testing_Kit_Barcode.objects.get(id= pd['testing_kit_barcode_id'])
                            pd['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                        else:
                            pd['test_kit_name'] = 21

                        check_test_status = Patient_Testing.objects.filter(patient_id= pd['id'])
                        if check_test_status:
                            check_test_status_get = Patient_Testing.objects.get(patient_id= pd['id'])
                            pd['test_result'] = check_test_status_get.testing_status
                        else:
                            pd['test_result'] = 2

                        all_phcm_data.append(pd)
                return Response({'patient_details':all_phcm_data,'result': 'successfull'})

            if check_user_roles.role_name == 'PHCS':
                # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= status_filter)).values().order_by('-id')
                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id'])
                    if check_tkb:
                        check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
                        i['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                    else:
                        i['test_kit_name'] = 21

                    check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
                    if check_test_status:
                        check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
                        i['test_result'] = check_test_status_get.testing_status
                    else:
                        i['test_result'] = 2
                return Response({'patient_details':patient_details,'result': 'successfull'})
        elif check_lab_user:

            patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= status_filter)).values().order_by('-id')
            for i in patient_details:
                patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                i['patient_type_name'] = patient_type_data.patient_type_name
                i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                i['test_type_name']= patient_test_type_data.test_type_name

                check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
                if check_test_status:
                    check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
                    i['test_result'] = check_test_status_get.testing_status
                else:
                    i['test_result'] = 2
            return Response({'patient_details':patient_details,'result': 'successfull'})

        else:
            return Response({'result': 'Something Went Wrong'})




#########################          PHC TEST TYPE FILTER          #########################
class PHCUseTestTypeFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id      = data.get('user_id')
        test_type = data.get('test_type')


        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':

                test_type_id = Test_Type_Ref.objects.get(test_type_name= test_type)

                all_phcm_data = []
                check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                for i in check_all_slab_collector:
                    # patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                    patient_details = Patient.objects.filter(Q(added_by=i['user_id'])  & Q(package_sampling_id__isnull = True) & Q(test_type_id= test_type_id.id)).values().order_by('-id')
                    for pd in patient_details:
                        patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                        patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                        patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                        pd['patient_type_name'] = patient_type_data.patient_type_name
                        pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                        pd['test_type_name']= patient_test_type_data.test_type_name

                        check_tkb = Testing_Kit_Barcode.objects.filter(id= pd['testing_kit_barcode_id'])
                        if check_tkb:
                            check_tkb_get = Testing_Kit_Barcode.objects.get(id= pd['testing_kit_barcode_id'])
                            pd['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                        else:
                            pd['test_kit_name'] = 21

                        

                        check_test_status = Patient_Testing.objects.filter(patient_id= pd['id'])
                        if check_test_status:
                            check_test_status_get = Patient_Testing.objects.get(patient_id= pd['id'])
                            pd['test_result'] = check_test_status_get.testing_status
                        else:
                            pd['test_result'] = 2

                        all_phcm_data.append(pd)
                return Response({'patient_details':all_phcm_data,'result': 'successfull'})

            if check_user_roles.role_name == 'PHCS':
                # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                test_type_id = Test_Type_Ref.objects.get(test_type_name= test_type)

                patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status= 31) & Q(test_type_id= test_type_id.id)).values().order_by('-id')
                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id'])
                    if check_tkb:
                        check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
                        i['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                    else:
                        i['test_kit_name'] = 21

                    check_test_status = Patient_Testing.objects.filter(patient_id= i['id'])
                    if check_test_status:
                        check_test_status_get = Patient_Testing.objects.get(patient_id= i['id'])
                        i['test_result'] = check_test_status_get.testing_status
                    else:
                        i['test_result'] = 2

                return Response({'patient_details':patient_details,'result': 'successfull'})
        else:
            return Response({'result': 'Something Went Wrong'})


#########################          Upadate Patient Testing Status  RAT RTPCR          #########################
class UpdatePatientTestingResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        test_type = data.get('test_type')
        test_result = data.get('test_result')
        rat_Lab_testkit_id = data.get('rat_Lab_testkit_id')
        patient_id = data.get('patient_id')
        srf_id = data.get('srf_id')
        id = data.get('id')
        user_id = data.get('user_id')


        test  = Test_Type_Ref.objects.none()

        patient_data = Patient.objects.get(Q(id= id))
        patient_data_fil = Patient.objects.filter(Q(id= id)).update(testing_kit_barcode_id= rat_Lab_testkit_id)

        check_patient_data = Patient_Testing.objects.filter(patient_id= id)
        if check_patient_data:
            lab_test_result_update = Patient_Testing.objects.filter(patient_id= id).update(testing_status= test_result)
            if test_result == '0':
                # generate_srf = random.randint(100000000, 999999999)

                user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

                get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

                srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

                yr = str(asdatetime.now().year)[2:]
                mn = str(asdatetime.now().month).zfill(2)
                dd = str(asdatetime.now().day)

                srf_data = srf_dist_code+yr+mn+dd

                last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

                if last_srf_id:
                    srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                else:
                    srf_data = srf_data + '1'.zfill(5)

                check_rtpcr_data = Patient.objects.filter(rat_created_id= id).update(srf_id= srf_data)
                # print("Antigen Negative", check_rtpcr_data)

            if test_result == '1':
                check_rtpcr_data = Patient.objects.filter(rat_created_id= id).delete()
                # print("Antigen Positive", check_rtpcr_data)
        else:
            lab_test_result_update = Patient_Testing.objects.create(patient_id= id, testing_status= test_result)

            if test_result == '0':
                # generate_srf = random.randint(100000000, 999999999)
                
                user_dist_status = Swab_Collection_Centre.objects.get(user_id= user_id)

                get_user_master_dist_code = Master_PHC.objects.get(id= user_dist_status.phc_master_id)

                srf_dist_code= str(get_user_master_dist_code.district_code)[1:]

                yr = str(asdatetime.now().year)[2:]
                mn = str(asdatetime.now().month).zfill(2)
                dd = str(asdatetime.now().day)

                srf_data = srf_dist_code+yr+mn+dd

                last_srf_id = Patient.objects.filter(Q(srf_id__icontains= srf_data) & Q(create_timestamp__date= asdatetime.now().date())).values_list('srf_id', flat=True).order_by('-id')[:1]

                if last_srf_id:
                    srf_data = str(int((last_srf_id[0]).split('-')[0]) + 1)
                else:
                    srf_data = srf_data + '1'.zfill(5)

                check_rtpcr_data = Patient.objects.filter(rat_created_id= id).update(srf_id= srf_data)
                # print("Antigen Negative DATA", check_rtpcr_data)

            if test_result == '1':
                check_rtpcr_data = Patient.objects.filter(rat_created_id= id).delete()
                # print("Antigen Positive DATA", check_rtpcr_data)

        if test_type == 'RAT':
            get_swab_detail = Swab_Collection_Centre.objects.get(user_id= user_id)
            test_kit_details = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id= get_swab_detail.phc_master_id) & Q(active= 1))
            if test_kit_details:
                test_kit_detail_data = Phc_Id_Test_Kit_Id.objects.get(Q(phc_id= get_swab_detail.phc_master_id) & Q(active= 1))
                if int(test_kit_detail_data.capacity)-1 == 0:
                    test_kit_details_update = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id= get_swab_detail.phc_master_id) & Q(active= 1) & Q(test_kit_id= rat_Lab_testkit_id)).delete()
                else:
                    test_kit_details_update = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id= get_swab_detail.phc_master_id) & Q(active= 1) & Q(test_kit_id= rat_Lab_testkit_id)).update(capacity= int(test_kit_detail_data.capacity)-1)

        header = getToken()

        get_patient_details = list(Patient.objects.filter(id= id).values('patient_name', 'age', 'age_type', 'gender', 
        'srf_id', 'mobile_number', 'test_type__test_type_name', 'lab_master__lab_id', 
        'id_proof_type', 'aadhar_number', 'ration_card_number', 'mobile_number_belongs_to', ))

        get_patient_add_details = list(Patient_Address.objects.filter(patient_id= id).values('state_name', 'district_name', 'city_name', 'ward_name', 'taluk_name', 'panchayat_name', 'village_name', 'resident_type', 'zone_type', 'ward_type', 'flat_door_no', 'main_road_no', 'locality', 'landmark', 'pincode'))

        get_patient_outside_add_details = list(Outside_Patient_Address.objects.filter(patient_id= id).values('state_name', 
        'district_name', 'city_name', 'ward_name', 'taluk_name', 'panchayat_name', 'village_name', 'resident_type', 'zone_type', 'ward_type', 
        'flat_door_no', 'main_road_no', 'locality', 'landmark', 'pincode'))

        address_details = None

        district_name_eng = ''
        taluk_name_eng = ''
        panchayat_name_eng = ''
        village_name_eng = ''
        ward_name_eng = ''
        zone_name_eng = ''
        city_name_eng = ''
            
            

        if get_patient_add_details:
            address_details = get_patient_add_details
            if address_details[0]['district_name']:
                district_name = (Master_District.objects.filter(district_code= address_details[0]['district_name']).values_list('district_name_eng', flat=True))[0]
            if address_details[0]['taluk_name']:
                taluk_name = (Master_Block.objects.filter(block_code= address_details[0]['taluk_name']).values_list('block_name_eng', flat=True))[0]
            if address_details[0]['panchayat_name']:                
                panchayat_name = (Master_Panchayat.objects.filter(panchayat_code= address_details[0]['panchayat_name']).values_list('panchayat_name_eng', flat=True))[0]
            if address_details[0]['village_name']:                
                village_name = (Master_Village.objects.filter(village_code= address_details[0]['village_name']).values_list('village_name_eng', flat=True))[0]
            if address_details[0]['ward_name']:                
                ward_name = (Master_Ward.objects.filter(ward_no= address_details[0]['ward_name']).values_list('ward_name', flat=True))[0]
            if address_details[0]['zone_type']:                
                zone_name = (Master_Zone.objects.filter(bbmp_zone_no_ksrsac= address_details[0]['zone_type']).values_list('zone_name', flat=True))[0]
            if address_details[0]['city_name']:                
                city_name = (Master_Ward.objects.filter(district_code= address_details[0]['city_name']).values_list('town_name', flat=True))[0]
        
        if get_patient_outside_add_details:
            address_details = get_patient_outside_add_details

        res_str_name = ''
        if test_result == '0':
            res_str_name = 'Negative'
        if test_result == '1':
            res_str_name = 'Positive'


        test_positive_url = "https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_InsertTestResultForSMS"
        pos_input_data = {
                            "Name": str(get_patient_details[0]['patient_name']),
                            "Age": str(get_patient_details[0]['age']),
                            "AgeIn": str(get_patient_details[0]['age_type']),
                            "Gender": str(get_patient_details[0]['gender']),
                            "SRFID": str(get_patient_details[0]['srf_id']),
                            "MobileNumber": str(get_patient_details[0]['mobile_number']),
                            "TestType": str(get_patient_details[0]['test_type__test_type_name']),
                            "TestResult": res_str_name,
                            "TestLab": str(get_patient_details[0]['lab_master__lab_id'])
                        }
        post_sms_input_json_data = json.dumps(pos_input_data, indent=4)
        check_sms_data_response = requests.post(test_positive_url, data= post_sms_input_json_data, headers= header)
        sms_j_data = check_sms_data_response.json()
        print(sms_j_data)

        if test_result == '1':

            test_positive_url = "https://www.covidwar.karnataka.gov.in/service19_test/api/Values/FnSwab_InsertPositiveTestResult"
            
            pos_lin_input_data = {
                                "patient_name": str(get_patient_details[0]['patient_name']),
                                "srf_id": str(get_patient_details[0]['srf_id']),
                                "age": int(get_patient_details[0]['age']),
                                "age_in": str(get_patient_details[0]['age_type']),
                                "gender": str(get_patient_details[0]['gender']), 
                                "id_proof_type": str(get_patient_details[0]['id_proof_type']),
                                "aadhar_number": str(get_patient_details[0]['aadhar_number']),
                                "ration_card_number": str(get_patient_details[0]['ration_card_number']),
                                "mobile_number": int(get_patient_details[0]['mobile_number']),
                                "mobile_number_belongs_to": str(get_patient_details[0]['mobile_number_belongs_to']),
                                "resident_type": 11,
                                "flat_door_no": str(address_details[0]['flat_door_no']),
                                "main_road_no": str(address_details[0]['main_road_no']),
                                "locality": str(address_details[0]['locality']),
                                "landmark": str(address_details[0]['landmark']),
                                "pincode": str(address_details[0]['pincode']),
                                "state_name": str(address_details[0]['state_name']),
                                "ward_type": str(address_details[0]['ward_type']),
                                "district_id": str(address_details[0]['district_name']),
                                "district_name": district_name_eng,
                                "taluk_id": str(address_details[0]['taluk_name']),
                                "taluk_name": taluk_name_eng,
                                "town_id": str(address_details[0]['city_name']),
                                "town_name": city_name_eng,
                                "ward_id": str(address_details[0]['ward_name']),
                                "ward_name": ward_name_eng,
                                "zone_id": str(address_details[0]['zone_type']),
                                "zone_name": zone_name_eng,
                                "panchayat_id": str(address_details[0]['panchayat_name']),
                                "panchayat_name": panchayat_name_eng,
                                "village_id": str(address_details[0]['village_name']),
                                "village_name": village_name_eng,
                                "symp_asymp": True,
                                "symp_fever": False,
                                "symp_cough": False,
                                "symp_breathness": False,
                                "symp_ILI": False,
                                "symp_SARI": False,
                                "sysp_cold_nasaldischarge": False,
                                "symp_sore_throat": False,
                                "symp_diarahea": False,
                                "symp_nausea_vomating": False,
                                "symp_bodyache": False,
                                "symp_loss_of_smell": False,
                                "symp_loss_of_taste": False,
                                "symp_chestpain": False,
                                "symp_other": False,
                                "symp_other_desc": "sample string 48",
                                "combdties_diabties": False,
                                "combdties_heartproblem": False,
                                "combdties_hiv": False,
                                "combdties_hypertension": False,
                                "combdties_malignancy": False,
                                "combdties_tb": False,
                                "combdties_kidneydesies": False,
                                "combdties_copd": False,
                                "combdties_liverdesiese": False,
                                "combdties_pregnancy": False,
                                "combdties_lactating": False,
                                "combdties_cancer": False,
                                "combdties_other": False,
                                "combdties_otherdesc": "",
                                "testingLabName": "LBID",
                                "test_method": "RAT",
                                "result_date": "2021-08-13T17:55:58.3095284+05:30",
                                "isVaccinated": True,
                                "TypeOFVaccine": "",
                                "DateOfVaccination": ""
                                }
            post_sms_input_json_data = json.dumps(pos_lin_input_data, indent=4)

            check_ln_data_response = requests.post(test_positive_url, data= post_sms_input_json_data, headers= header)

            ln_j_data = check_ln_data_response.json()
            print(ln_j_data)

        return Response({'result':"Updated Sucessfully"}, status= status.HTTP_200_OK)







#########################          UPDATE PATIENT STATUS          #########################
class UpdatePatientCollectionStatus(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print("DDDDDDDDDDDD",data)

        user_id = data.get('user_id')
        srf_id = data.get('srf_id')
        id = data.get('id')
        status = data.get('swab_collection_status')

        Patient.objects.filter(Q(id= id) & Q(added_by_id= user_id) & Q(srf_id= srf_id)).update(swab_collection_status= status,)

        return Response("Updated Sucessfully")




#########################          CREATE PACKAGE          #########################
class CreatePackage(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        print("PACKAGE",data)

        user_id = data.get('user_id')
        patient_lists = data.get('packageData')
        package_barcode = data.get('barcode')
        print(patient_lists)
        print(len(patient_lists))
        patient_status = ''

        patient_ids = []
        count = 0
        for i in patient_lists:
            count += 1
            patient_status = i['patient_status']
            patient_ids.append({'id':i['id'], 'srf_id': i['srf_id']})
        
        print(patient_status)

        print("COUNT", count)

        tho_deatils_check = Swab_Collection_Centre.objects.filter(user_id= user_id)
        tlab_user_details_check = Testing_Lab_Facility.objects.filter(user_id= user_id)

        if tho_deatils_check:
            tho_deatils = Swab_Collection_Centre.objects.get(user_id= user_id)
            last_package_name = Package_Sampling.objects.filter(Q(master_phc= tho_deatils.phc_master_id) & Q(create_timestamp__date= asdatetime.now())).values().order_by('-id')[:1]
            print(last_package_name)

            master_phc_data = Master_PHC.objects.get(id= tho_deatils.phc_master_id)
            
            last_package_name_data = ''
            if last_package_name:
                # last_package_name = Package_Sampling.objects.filter(master_phc= tho_deatils.phc_master_id).values().order_by('-id')[0]
                for i in last_package_name:
                    current_datetime = asdatetime.now().strftime('%Y-%m-%d')
                    # last_package_name_data = 'PHCID_'+str(current_datetime)+'_'+str(int((last_package_name['package_sampling_name']).split('_')[2]) + 1)
                    last_package_name_data = str(master_phc_data.phc_name)+'_'+str(current_datetime)+'_'+str(int((i['package_sampling_name']).split('_')[2]) + 1)
                # current_datetime = asdatetime.now().strftime('%Y-%m-%d')
                # # last_package_name_data = 'PHCID_'+str(current_datetime)+'_'+str(int((last_package_name['package_sampling_name']).split('_')[2]) + 1)
                # last_package_name_data = str(master_phc_data.phc_name)+'_'+str(current_datetime)+'_'+str(int((last_package_name['package_sampling_name']).split('_')[2]) + 1)
            else:
                current_datetime = asdatetime.now().strftime('%Y-%m-%d')
                # last_package_name_data = 'PHCID_'+str(current_datetime)+'_1'
                last_package_name_data = str(master_phc_data.phc_name)+'_'+str(current_datetime)+'_1'

            created_package_list = Package_Sampling.objects.create(user_id= user_id, swab_cc_id= tho_deatils.id, master_phc_id= tho_deatils.phc_master_id, package_sampling_name= last_package_name_data, package_sampling_barcode= random.randint(1000000000,9999999999), samples_count= count, dispatch_status= 0, sympto_indication= patient_status, package_type_status= 6, package_type_action=16)

            for pid in patient_ids:
                print(pid)
                print(pid['id'])
                check_patients_details = Patient.objects.filter(Q(id= pid['id']) & Q(srf_id= pid['srf_id'])).update(package_sampling_id= created_package_list.id, swab_collection_result= 1)


            last_package_data = Package_Sampling.objects.filter(id= created_package_list.id).values()

            # check_user_phc = Swab_Collection_Centre.objects.get(user_id= user_id)
            # test_lab_data = Testing_Lab_Facility.objects.get(id= check_user_phc.test_lab)
            
            
            # check_taluk = Master_Block.objects.get(id= check_user_phc.city_id)
            for i in last_package_data:
                i['phc_name'] = master_phc_data.phc_name
                i['taluk'] = master_phc_data.block_name_eng
                i['package_type_status'] = i['sympto_indication']

            # for i in last_package_data:
            #     i['phc_name'] = check_user_phc.swab_collection_centre_name
            #     i['taluk'] = check_taluk.block_name_eng


            
            # return Response({'created_package_data':last_package_data,'result':"Package Created Sucessfully"})

            return Response({'created_package_data':last_package_data,'result':"Package Created Sucessfully"})
        
        elif tlab_user_details_check:
            tlab_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

            # last_package_name = Package_Sampling.objects.filter(Q(master_phc= tho_deatils.phc_master_id) & Q(create_timestamp__date= asdatetime.now())).values().order_by('-id')[:1]
            last_package_name = Package_Sampling.objects.filter(Q(user_id= user_id) & Q(create_timestamp__date= asdatetime.now())).values().order_by('-id')[:1]
            
            master_lab_data = Master_Labs.objects.get(id= tlab_user_details.testing_lab_master_id)
            
            last_package_name_data = ''
            if last_package_name:

                for i in last_package_name:

                    current_datetime = asdatetime.now().strftime('%Y-%m-%d')
                    last_package_name_data = str(master_lab_data.lab_id)+'_'+str(current_datetime)+'_'+str(int((i['package_sampling_name']).split('_')[2]) + 1)

            else:
                
                current_datetime = asdatetime.now().strftime('%Y-%m-%d')
                last_package_name_data = str(master_lab_data.lab_id)+'_'+str(current_datetime)+'_1'

            # created_package_list = Package_Sampling.objects.create(user_id= user_id, swab_cc_id= tho_deatils.id, master_phc_id= tho_deatils.phc_master_id, package_sampling_name= last_package_name_data, package_sampling_barcode= random.randint(1000000000,9999999999), samples_count= count, dispatch_status= 0, sympto_indication= patient_status, package_type_status= 6, package_type_action=16)
            created_package_list = Package_Sampling.objects.create(user_id= user_id, test_lab_id= tlab_user_details.id, lab_master_id= tlab_user_details.testing_lab_master_id ,package_sampling_name= last_package_name_data, package_sampling_barcode= random.randint(1000000000,9999999999), samples_count= count, dispatch_status= 0, sympto_indication= patient_status, package_type_status= 5, package_type_action=15, lab_received_datetime= asdatetime.now())

            for pid in patient_ids:
                print(pid)
                print(pid['id'])
                check_patients_details = Patient.objects.filter(Q(id= pid['id']) & Q(srf_id= pid['srf_id'])).update(package_sampling_id= created_package_list.id, swab_collection_result= 1)


            last_package_data = Package_Sampling.objects.filter(id= created_package_list.id).values()

            # check_user_phc = Swab_Collection_Centre.objects.get(user_id= user_id)
            # test_lab_data = Testing_Lab_Facility.objects.get(id= check_user_phc.test_lab)
            
            
            # check_taluk = Master_Block.objects.get(id= check_user_phc.city_id)
            for i in last_package_data:
                i['phc_name'] = master_lab_data.lab_id
                i['taluk'] = master_lab_data.karnataka_blocks_id
                i['package_type_status'] = i['sympto_indication']

            # for i in last_package_data:
            #     i['phc_name'] = check_user_phc.swab_collection_centre_name
            #     i['taluk'] = check_taluk.block_name_eng

            # return Response({'created_package_data':last_package_data,'result':"Package Created Sucessfully"})

            return Response({'created_package_data':last_package_data,'result':"Package Created Sucessfully"})
        else:
            return Response({'result': 'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)







#########################          GET PACKAGE SAMPLES          #########################
class GetPackageSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        package_id = data.get('package_id')

        package_barcode_id = data.get('package_barcode')
        package_res_type_status = data.get('received_id')

        # package_details = Package_Sampling.objects.get(Q(id= package_id) & Q(package_sampling_barcode= package_barcode_id))
        package_details = Package_Sampling.objects.get(Q(package_sampling_barcode= package_barcode_id))
        package_details_update = Package_Sampling.objects.filter(Q(package_sampling_barcode= package_barcode_id)).update(lab_accept_reject_status= 1)

        # package_res_update_details = Package_Sampling.objects.filter(Q(package_sampling_barcode= package_barcode_id)).update(package_received_status= package_res_type_status)

        get_package_patients_details = Patient.objects.filter(package_sampling_id= package_details.id).values()


        for i in get_package_patients_details:
            Patient.objects.filter(id= i['id']).update(sample_status= 'Accepted', lab_accepted_datetime= asdatetime.now())
            specimen_type_details = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
            test_type_details = Test_Type_Ref.objects.get(id= i['test_type_id'])
            package_details = Package_Sampling.objects.get(id= i['package_sampling_id'])
            
            i['specimen_type_name'] = specimen_type_details.specimen_type_name
            i['test_type_name'] = test_type_details.test_type_name
            i['package_barcode'] = package_details.package_sampling_barcode

            i['disable'] = True
            i['drop_down'] = False

            # Patient.objects.filter(id= i['id']).update(sample_status= 'Accepted', lab_accepted_datetime= asdatetime.now())

        return Response(get_package_patients_details)









class CollectionDetailsAndStatus(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        sco_id = data.get('sco_id')

        current_sco_patient_details = Patient.objects.filter(created_user= sco_id).values()

        return Response(current_sco_patient_details)



#########################          GET PHC ADDED PATIENTS          #########################
class GetPHCUseraddedPatients(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()
        check_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id).values()

        if check_user:

            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)

            if check_user_roles.role_name == 'PHCMO':

                check_all_slab_collector = Swab_Collection_Centre.objects.filter(phc_master_id= check_user_data.phc_master_id).values_list('user_id', flat=True)
            
                patient_data = Patient.objects.filter(Q(added_by_id__in= check_all_slab_collector)  & Q(package_sampling_id__isnull = True) & Q(create_timestamp__date= asdatetime.now().date())).values().order_by('-id')
                patient_details_count = Patient.objects.filter(Q(added_by_id__in= check_all_slab_collector)  & Q(package_sampling_id__isnull = True) & Q(create_timestamp__date= asdatetime.now().date())).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)
                
                for pd in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= pd['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_tkb:
                        pd['test_kit_name'] = check_tkb[0]
                    else:
                        pd['test_kit_name'] = 21

                    pd['patient_type_name'] = patient_type_data.patient_type_name
                    pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    pd['test_type_name']= patient_test_type_data.test_type_name

                    if patient_test_type_data.test_type_name == 'RAT':

                        lab_test_data = Patient_Testing.objects.filter(patient_id= pd['id']).values_list('testing_status', flat=True)
                        if lab_test_data:
                            pd['test_result'] = lab_test_data[0]
                        else:
                            pd['test_result'] = 2

                return Response({'patient_details':LIST(patient_details), 'total_pg_count': patient_details_count,'result': 'successfull'})

            if check_user_roles.role_name == 'PHCS':
                # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 'Complete') & Q(package_sampling_id__isnull = True)).values()
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 1) & Q(package_sampling_id__isnull = True)).values()
                # patient_details = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status=31) & Q(create_timestamp__date= asdatetime.now().date())).values().order_by('-id',)
                
                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status=31)  & Q(create_timestamp__date= asdatetime.now().date())).values().order_by('-id',)
                patient_details_count = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status=31)  & Q(create_timestamp__date= asdatetime.now().date())).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_tkb:
                        i['test_kit_name'] = check_tkb[0]
                    else:
                        i['test_kit_name'] = 21

                    if patient_test_type_data.test_type_name == 'RAT':
                        lab_test_data = Patient_Testing.objects.filter(patient_id= i['id']).values_list('testing_status', flat=True)
                        if lab_test_data:
                            i['test_result'] = lab_test_data[0]
                        else:
                            i['test_result'] = 2

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_details_count,'result': 'successfull'})

            else:
                return Response({'result':'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)
        
        elif check_lab_user:
            # check_lab_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_lab_user_roles  = Roles.objects.get(id= User_Role_Ref.objects.filter(user_id= user_id).values_list('role_id', flat=True)[0])

            if check_lab_user_roles.role_name == 'TLAB':


                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status=31)  & Q(create_timestamp__date= asdatetime.now().date())).values().order_by('-id',)
                patient_details_count = Patient.objects.filter(Q(added_by=user_id) & Q(package_sampling_id__isnull = True) & Q(swab_collection_status=31)  & Q(create_timestamp__date= asdatetime.now().date())).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    # check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    # if check_tkb:
                    #     i['test_kit_name'] = check_tkb[0]
                    # else:
                    #     i['test_kit_name'] = 21

                    # if patient_test_type_data.test_type_name == 'RAT':
                    #     lab_test_data = Patient_Testing.objects.filter(patient_id= i['id']).values_list('testing_status', flat=True)
                    #     if lab_test_data:
                    #         i['test_result'] = lab_test_data[0]
                    #     else:
                    #         i['test_result'] = 2

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_details_count,'result': 'successfull'})
            else:
                return Response({'result': 'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response({'result': 'Something Went Wrong'})









#########################          GET PHC USER PACKAGE CREATED LIST          #########################
class GetPHCUserPackageList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()
        check_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id)

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':

                check_all_slab_collector = Swab_Collection_Centre.objects.filter(phc_master_id= check_user_data.phc_master_id).values_list('user_id', flat=True)

                patient_data = Patient.objects.filter(Q(added_by_id__in=check_all_slab_collector) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).values()
                patient_data_count = Patient.objects.filter(Q(added_by_id__in=check_all_slab_collector) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)
                
                for pd in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                    pd['patient_type_name'] = patient_type_data.patient_type_name
                    pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    pd['test_type_name']= patient_test_type_data.test_type_name

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})

            if check_user_roles.role_name == 'PHCS':
                 # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).values()
                patient_data_count = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})
            
            if check_user_roles.role_name == 'PHCM':
                 # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id__in = [2, 3]) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).values()
                patient_data_count = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id__in = [2, 3]) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})
        
        elif check_lab_user:

            
            check_lab_user_roles = User_Role_Ref.objects.filter(user_id= user_id).values_list('role_id', flat=True)[0]
            # check_lab_user_roles = User_Role_Ref.objects.filter(user_id= user_id).values('role_role_name')
            # print(check_lab_user_roles)
            # check_lab_user_roles = list(User_Role_Ref.objects.filter(user_id= user_id).values('role_role_name'))[0]['role_name']
            # print(check_lab_user_roles)

            check_lab_user_roles  = Roles.objects.get(id= check_lab_user_roles)

            if check_lab_user_roles.role_name == 'TLAB':

                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).values()
                patient_data_count = Patient.objects.filter(Q(added_by=user_id) & Q(test_type_id = 2) & Q(swab_collection_status= 32) & Q(package_sampling_id__isnull = True)).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})

            else:
                return Response({'result': 'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response({'result': 'successfull'})




#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
class GetTHOPackageData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        tho_data = THO.objects.get(user_id= user_id)

        check_tho_lab_data = Package_Sampling.objects.filter(tho_id=tho_data.id).values()
        check_tho_lab_data_count = Package_Sampling.objects.filter(tho_id=tho_data.id).count()

        check_tho_lab_details = paginatorCreation(check_tho_lab_data, selected_page_no)

        for i in check_tho_lab_details:
            check_lab = Testing_Lab_Facility.objects.filter(id=  i['test_lab_id'])
            if check_lab:
                check_lab = Testing_Lab_Facility.objects.get(id=  i['test_lab_id'])
                lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                i['lab_name'] = lab_master_data.lab_name
            else:
                i['lab_name'] = '-'
                
        return Response({'details':list(check_tho_lab_details), 'total_pg_count': check_tho_lab_data_count,'result': 'successfull'})




class GetDSOPackageData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        
        # sc = Package_Sampling.objects.filter(dso_id=user_id).values()
        dso_data = DSO.objects.get(user_id= user_id)
        sc_data = Package_Sampling.objects.filter(Q(dso_id=dso_data.id) & ~Q(package_type_status = 2)).values()
        sc_count = Package_Sampling.objects.filter(Q(dso_id=dso_data.id) & ~Q(package_type_status = 2)).count()

        sc_details = paginatorCreation(sc_data, selected_page_no)

        for i in sc_details:
            check_lab = Testing_Lab_Facility.objects.filter(id=  i['test_lab_id'])
            if check_lab:
                check_lab = Testing_Lab_Facility.objects.get(id=  i['test_lab_id'])
                lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                i['lab_name'] = lab_master_data.lab_name
            else:
                i['lab_name'] = '-'
        
        return Response({'details':list(sc_details), 'total_pg_count': sc_count, 'result': 'successfull '})
  




class GetSSUPackageData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        print(data)
        user_id = data.get('user_id')
        
        # sc = Package_Sampling.objects.filter(ssu_id=user_id).values()
        ssu_data = SSU.objects.get(user_id= user_id)
        sc = Package_Sampling.objects.filter(ssu_id=ssu_data.id).values()

        for i in sc:
            check_lab = Testing_Lab_Facility.objects.filter(id=  i['test_lab_id'])
            if check_lab:
                check_lab = Testing_Lab_Facility.objects.get(id=  i['test_lab_id'])
                lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                i['lab_name'] = lab_master_data.lab_name
            else:
                i['lab_name'] = '-'
        
        return Response({'details':sc,'result': 'successfull '})



#########################          GET TESTING LAB PACKAGE DETAILS          #########################
class GetTLCPackageData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        
        # sc = Package_Sampling.objects.filter(test_lab_id=user_id).values()
        test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
        
        sc_data = Package_Sampling.objects.filter(test_lab_id=test_lab_data.id, lab_master_id= test_lab_data.testing_lab_master_id, lab_accept_reject_status= 0).values().order_by('-id')
        sc_count = Package_Sampling.objects.filter(test_lab_id=test_lab_data.id, lab_master_id= test_lab_data.testing_lab_master_id, lab_accept_reject_status= 0).count()
        

        print(test_lab_data.id)
        print(test_lab_data.testing_lab_master_id)
        
        sc_details = paginatorCreation(sc_data, selected_page_no)

        for i in sc_details:
            i['testing_lab_name'] = test_lab_data.testing_lab_facility_name
            check_swb_col = Swab_Collection_Centre.objects.filter(id= i['swab_cc_id'])
            if check_swb_col:
                check_swb_col = Swab_Collection_Centre.objects.get(id= i['swab_cc_id'])
                phc_data = Master_PHC.objects.get(id= check_swb_col.phc_master_id)
                i['phc_name'] = phc_data.phc_name
            else:
                i['phc_name'] = Master_Labs.objects.filter(id= test_lab_data.testing_lab_master_id).values_list('lab_id', flat=True)[0]
        
        return Response({'details':list(sc_details), 'total_pg_count': sc_count,'result':'successfull '})



#########################          GET TESTING LAB PACKAGE DETAILS          #########################
class GetTLOPSPackageData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        print(data)

        user_id = data.get('user_id')
        print(user_id)
        
        # sc = Package_Sampling.objects.filter(test_lab_id=user_id).values()
        test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        print(test_lab_data.id)

        sc = Package_Sampling.objects.filter(Q(lab_master_id=test_lab_data.testing_lab_master_id) & Q(package_type_status= 5) & Q(package_type_action= 15) & Q(created_group_pool_data= 0)).values()

        for i in sc:
            i['testing_lab_name'] = test_lab_data.testing_lab_facility_name
            check_swb_col = Swab_Collection_Centre.objects.get(id= i['swab_cc_id'])
            phc_data = Master_PHC.objects.get(id= check_swb_col.phc_master_id)
            i['phc_name'] = phc_data.phc_name
        

        print(sc)
        print(sc)

        return Response({'details':sc,'result': 'successfull '})





#########################          GET TESTING LAB CATEGORIZED COUNTS          #########################
class GetTLOPSCategorizedCounts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        get_all_users= Testing_Lab_Facility.objects.filter(testing_lab_master_id= test_lab_data.testing_lab_master_id).values_list('user_id', flat=True)

        sc = Package_Sampling.objects.filter(Q(lab_master_id=test_lab_data.testing_lab_master_id) & Q(package_type_status= 5) & Q(package_type_action= 15) & Q(created_group_pool_data= 0)).values_list('id', flat=True)

        all_samples_data = []

        total_samples_collected = 0
        direct_lab = 0
        priority = 0
        de_pool = 0
        retest = 0
        

        direct_lab += Patient.objects.filter(Q(test_lab_id__isnull = True) & Q(added_by_id__in= get_all_users) & Q(swab_collection_status= 32) & Q(lab_master_id=test_lab_data.testing_lab_master_id)).count()
        for i in sc:

            total_samples_collected += Patient.objects.filter(Q(package_sampling_id = i) & Q(test_lab_id__isnull = True) & Q(de_pool= 0) & Q(priority= 0)).count()
            # direct_lab += Patient.objects.filter(Q(test_lab_id__isnull = True) & Q(added_by_id__in= get_all_users) & Q(swab_collection_status= 32) & Q(lab_master_id=test_lab_data.testing_lab_master_id)).count()
            priority += Patient.objects.filter(Q(package_sampling_id = i) & Q(test_lab_id__isnull = True) & Q(priority= 1)).count()
            # de_pool += Patient.objects.filter(Q(package_sampling_id = i) & Q(test_lab_id__isnull = False) & Q(de_pool= 1) & Q(group_samples= 1) & Q(pool_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples_result = 1) & Q(submit_for_individual_testing= 1) & Q(group_samples_result= 0)).count()
            de_pool += Patient.objects.filter(Q(package_sampling_id = i) & Q(test_lab_id__isnull = False) & Q(de_pool= 1)).count()

            # get_patient_data = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 1) & Q(pool_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples_result = 1) & Q(submit_for_individual_testing= 1) & Q(group_samples_result= 0)).values()
        return Response({'total_samples_collected': total_samples_collected, 'direct_lab':direct_lab, 'priority':priority, 'de_pool':de_pool, 'retest':retest, 'total':retest + de_pool + priority + direct_lab + total_samples_collected}, status= status.HTTP_200_OK)




class GenerateLabIdsForCategorizedSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        row_value = data.get('row_value')
        column_value = data.get('column_value')
        total_individual_sample_count = data.get('total_individual_sample_count')
        total_pool_sample_count = data.get('total_pool_sample_count')
        multiple_of_five_value = data.get('multiple_of_five_value')
        entered_ind_samples = data.get('entered_ind_samples')
        entered_pool_samples = data.get('entered_pool_samples')

        print(data)

        # {"total_phc_samples": this.indTotalSamplePhc, "lab_direct": this.indladDirect, "priority": this.indpriority, "retest": this.indretest, "de_Pool": this.inddepool}
        # {"total_phc_samples": this.poolTotalSamplePhc, "lab_direct": this.poolladDirect, "priority": this.poolpriority, "retest": this.poolretest, "de_Pool": this.pooldepool}

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        all_patient_details = []
        patient_ids = []
        

        if int(entered_ind_samples.get('total_phc_samples')) > 0:

            phc_samples_patient_details = Patient.objects.filter(Q(test_lab_id__isnull = True) & Q(lab_master_id= check_user_details.testing_lab_master_id)).values()[:int(entered_ind_samples.get('total_phc_samples'))]
            

            for i in phc_samples_patient_details:
                print(i)
                    
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_individual_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:

                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                
                else:
                    
                    update_lab_id_data = int(split_gen_lab_id) + 1

                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])

                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_ind_samples.get('lab_direct')) > 0:

            lab_direct_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(added_by_id__in= Testing_Lab_Facility.objects.filter(testing_lab_master_id= check_user_details.testing_lab_master_id).values_list('user_id', flat=True))).values()[:int(entered_ind_samples.get('lab_direct'))]
            

            for i in lab_direct_samples_patient_details:
                    
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_individual_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:

                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                
                else:
                    
                    update_lab_id_data = int(split_gen_lab_id) + 1

                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_ind_samples.get('priority')) > 0:

            priority_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(priority= 1)).values()[:int(entered_ind_samples.get('priority'))]

            for i in priority_samples_patient_details:
                    
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_individual_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:

                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                
                else:
                    
                    update_lab_id_data = int(split_gen_lab_id) + 1

                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_ind_samples.get('retest')) > 0:
            pass
            # priority_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(priority= 1)).values()[:int(entered_ind_samples.get('retest'))]

            # for i in priority_samples_patient_details:
                    
            #     master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

            #     lab_max_cap= int(master_lab_data.max_capacity) - 1

            #     split_gen_lab_id = ''
            #     if master_lab_data.last_genearte_individual_lab_id:
            #         # print("CHECK LAB ID PRESENT")
            #         split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
            #     else:
            #         # print("CHECK LAB ID NOT")
            #         len_of_cap = str(master_lab_data.max_capacity)
            #         split_gen_lab_id = '0000'


            #     if int(split_gen_lab_id) == lab_max_cap:

            #         patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
            #         Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

            #         # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                
            #     else:
                    
            #         update_lab_id_data = int(split_gen_lab_id) + 1

            #         last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

            #         # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
            #         patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
            #         Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
            #         test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

            #         # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])

        elif int(entered_ind_samples.get('de_Pool')) > 0:
        
            # de_pool_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = False) & Q(group_samples= 1) & Q(pool_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples_result = 1) & Q(submit_for_individual_testing= 1) & Q(group_samples_result= 0)).values()[:int(entered_ind_samples.get('de_Pool'))]
            de_pool_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = False) & Q(de_pool= 1)).values()[:int(entered_ind_samples.get('de_Pool'))]

            print(de_pool_samples_patient_details, "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk")
            
            for i in de_pool_samples_patient_details:
                    
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_individual_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:

                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1, de_pool= 2)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                    patient_data_update_data = Patient.objects.filter(id= i['id']).values()
                    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ",patient_data_update_data)
                else:
                    
                    update_lab_id_data = int(split_gen_lab_id) + 1

                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1, de_pool= 2)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                    patient_data_update_data = Patient.objects.filter(id= i['id']).values()
                    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ",patient_data_update_data)
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])
        
        if int(entered_pool_samples.get('total_phc_samples')):

            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            phc_samples_patient_details = Patient.objects.filter(Q(test_lab_id__isnull = True) & Q(lab_master_id= check_user_details.testing_lab_master_id)).values()[:int(entered_pool_samples.get('total_phc_samples'))]

            for i in phc_samples_patient_details:
                
                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0

                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_pool_samples.get('lab_direct')):

            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            phc_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(added_by_id__in= Testing_Lab_Facility.objects.filter(testing_lab_master_id= check_user_details.testing_lab_master_id).values_list('user_id', flat=True))).values()[:int(entered_ind_samples.get('lab_direct'))]

            for i in phc_samples_patient_details:

                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_pool_samples.get('priority')):

            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            phc_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(added_by_id= user_id) & Q(priority= 1)).values()[:int(entered_ind_samples.get('priority'))]

            for i in phc_samples_patient_details:

                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0
                
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_pool_samples.get('retest')):

            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            phc_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(added_by_id= user_id)).values()[:int(entered_ind_samples.get('retest'))]

            for i in phc_samples_patient_details:

                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0

                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        elif int(entered_pool_samples.get('de_Pool')):

            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            # phc_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = True) & Q(added_by_id= user_id)).values()[:int(entered_ind_samples.get('de_Pool'))]
            phc_samples_patient_details = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(test_lab_id__isnull = False) & Q(de_pool= 1)).values()[:int(entered_ind_samples.get('de_Pool'))]

            for i in phc_samples_patient_details:

                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1, de_pool= 2)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1, de_pool= 2)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0
                
                all_patient_details.append(list(Patient.objects.filter(id= i['id']).values('id', 'srf_id', 'patient_name', 'test_lab_id', 'lab_master__lab_id', 'lab_accepted_datetime', 'lab_ops_received_datetime'))[0])
                patient_ids.append(i['id'])

        print(all_patient_details)
        print(patient_ids)
        return Response({'result': all_patient_details, 'patient_ids': patient_ids}, status= status.HTTP_200_OK)




#########################          GET TESTING LAB PACKAGE SAMPLES DETAILS          #########################
class GetTLOPSPackageSamplesData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        
        # sc = Package_Sampling.objects.filter(test_lab_id=user_id).values()
        test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        sc = Package_Sampling.objects.filter(Q(lab_master_id=test_lab_data.testing_lab_master_id) & Q(package_type_status= 5) & Q(package_type_action= 15) & Q(created_group_pool_data= 0)).values_list('id', flat=True)

        all_samples_data = []
        for i in sc:
            patient_details = Patient.objects.filter(Q(package_sampling_id = i) & Q(test_lab_id__isnull = True)).values('id', 'srf_id', 'lab_accepted_datetime', 'lab_ops_received_datetime', 'lab_master__lab_id')
            
            [all_samples_data.append(j) for j in patient_details]


        paginator = Paginator(all_samples_data, 20)
        try:
            package_details_data = paginator.page(selected_page_no)
        except PageNotAnInteger:
            package_details_data = paginator.page(1)
        except EmptyPage:
            package_details_data = paginator.page(paginator.num_pages)

        return Response({'details':list(package_details_data),'total_pg_count': len(all_samples_data),'result': 'successfull '})





#########################          TESTING LAB GENERATE PACKAGE SAMPLES LAB IDS          #########################
class GetTLOPSGeneratePoolIndLabIds(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        user_id = data.get('user_id')
        selected_samples_id = data.get('selected_id')
        selected_type = int(data.get('selected_type'))

        print("FFFFFFFFFFF", data)

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)


        if selected_type == 0:

            for i in selected_samples_id:
                

                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_individual_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_individual_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:

                    patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= 'A0001')

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                
                else:
                    
                    update_lab_id_data = int(split_gen_lab_id) + 1

                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_individual_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_individual_lab_id= last_lab_id)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_individual_lab_id= last_lab_id)

                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])


            return Response({'result': 'Updated Sucessfully'}, status= status.HTTP_200_OK)
        elif selected_type == 1:
            
            iter_count =0
            laste_lab_id = ''
            split_gen_lab_id = ''
            lab_max_cap = 0

            for i in selected_samples_id:
                if iter_count == 0:
                    master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                    lab_max_cap= int(master_lab_data.max_capacity) - 1

                    if master_lab_data.last_genearte_pool_lab_id:
                        split_gen_lab_id = master_lab_data.last_genearte_pool_lab_id[1:]
                    else:
                        len_of_cap = str(master_lab_data.max_capacity)
                        split_gen_lab_id = '0000'

                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                    
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= last_lab_id)

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_pool_lab_id= 'P0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                
                else:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)
                    
                    patient_data_update = Patient.objects.filter(id= i).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_pool_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_pool_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_pool_lab_id,)
                iter_count += 1
                if iter_count == 5:
                    iter_count = 0
            return Response({'result': 'Updated Sucessfully'}, status= status.HTTP_200_OK)
            
        else:
            return Response({'result': 'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)


        # return Response({'details':list(package_details_data),'total_pg_count': len(all_samples_data),'result': 'successfull '})




#########################          SUBMIT FOR TESTING          #########################
class SubmitForMergedPlateTesting(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        patient_ids = data.get('patient_ids')
        user_id = data.get('user_id')

        print(data)

        # last_plate_no_details = MergedPlateDetails.objects.filter(Q(test_lab_id= test_lab_data_get.id) & Q(master_lab_id= test_lab_data_get.testing_lab_master_id)).order_by('-id')[:1]

        # last_plate_no = '0'
        # if last_plate_no_details:
        #     for i in last_plate_no_details:
        #         last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        # else:
        #     last_plate_no = str(1).zfill(3)

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        last_plate_no_details = MergedPlateDetails.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id)).order_by('-id')[:1]

        print(last_plate_no_details)

        last_plate_no = '0'
        if last_plate_no_details:
            for i in last_plate_no_details:
                last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        else:
            last_plate_no = str(1).zfill(3)

        create_plate = MergedPlateDetails.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_no= last_plate_no)


        # patient_details = Patient.objects.filter(id__in= patient_ids).update(submit_for_pool_testing= 1)

        for i in patient_ids:
            patient_details = MergedPlateSamples.objects.create(merge_plate_id= create_plate.id, submit_for_testing= 0, test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, patient_id= i, ind_pool_id= Patient.objects.get(id= i).test_lab_id)

        # patient_details = MergedPlateSamples.objects.filter(merge_plate_id__in= pool_ids).update(submit_for_testing= 1)

        all_plate_details = MergedPlateDetails.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(testing_status= 0)).values('id', 'plate_no', 'testing_status', 'create_datetime', 'master_lab__lab_id')

        return Response({'result':'Plate Submitted For Testing', 'all_plate_details': all_plate_details}, status= status.HTTP_200_OK)




class UpdateMergedPlateStatus(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        plate_id = data.get('plate_id')
        plate_no = data.get('plate_no')

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        create_plate = MergedPlateDetails.objects.filter(Q(id= plate_id) & Q(plate_no= plate_no) & Q(master_lab_id= check_user_details.testing_lab_master_id)).update(testing_status= 1)
        MergedPlateSamples.objects.filter(merge_plate_id= plate_id).update(submit_for_testing= 1)

        return Response({'result': 'Status Updated Sucessfully'}, status= status.HTTP_200_OK)




#########################      GET LAB PLATE DATA      #########################
class GetTlabOPSIndiMergedPlateData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)


        # get_plate_details = Patient.objects.filter(Q(test_lab_id= get_tlf_data.id)).values().order_by('-id')
        # print(get_plate_details)
        
        get_plate_details = Patient.objects.filter(Q(lab_master_id= get_tlf_data.testing_lab_master_id) & Q(group_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples= 0) | Q(de_pool= 2)).values().order_by('-id')
        print(get_plate_details)
        get_plate_details_count = Patient.objects.filter(Q(lab_master_id= get_tlf_data.testing_lab_master_id) & Q(group_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples= 0) | Q(de_pool= 2)).count()

        get_plate_data = paginatorCreation(get_plate_details, selected_page_no)

        for i in get_plate_data:
            master_lab_data = Master_Labs.objects.get(id= i['lab_master_id'])
            i['lab_name'] = master_lab_data.lab_name
            i['lab_id'] = master_lab_data.lab_id
            plate_data = list(MergedPlateSamples.objects.filter(patient_id= i['id']).values('id', 'merge_plate__plate_no').order_by('-id'))
            if plate_data:
                i['plate_no'] = plate_data[0]['merge_plate__plate_no']
            else:
                i['plate_no'] = '-'
        return Response({'result':list(get_plate_data), 'total_pg_count': get_plate_details_count})



#########################      GET LAB PLATE DATA      #########################
class GetTlabOPSPoolMergedPlateData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)


        merge_palte_data = MergedPlateSamples.objects.filter(Q(submit_for_testing= 1)).values('ind_pool_id', 'merge_plate_id').distinct()
        print(merge_palte_data)
        merge_palte_data = MergedPlateSamples.objects.filter(Q(submit_for_testing= 1) & Q(test_lab_id= get_tlf_data.id)).values('ind_pool_id', 'merge_plate_id').distinct()
        print(merge_palte_data)
        merge_palte_data = MergedPlateSamples.objects.filter(Q(submit_for_testing= 1) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values('ind_pool_id', 'merge_plate_id').distinct()
        print(merge_palte_data)
        merge_palte_data = MergedPlateSamples.objects.filter(Q(submit_for_testing= 1) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id) & Q(test_result__isnull= True)).values('ind_pool_id', 'merge_plate_id').distinct()
        print(merge_palte_data)
        merge_palte_data = MergedPlateSamples.objects.filter(Q(submit_for_testing= 1) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id) & Q(test_result__isnull= True) & Q(ind_pool_id__startswith= 'P')).values('ind_pool_id', 'merge_plate_id').distinct()
        print(merge_palte_data)
        # merge_palte_details_count = MergedPlateSamples.objects.filter(Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id) & Q(test_result__isnull= True) & Q(ind_pool_id__startswith= 'P')).values('ind_pool_id', 'merge_plate_id').count()

        # get_plate_data = paginatorCreation(merge_palte_details, selected_page_no)
        
        print(merge_palte_data)

        resp_details = []

        for gpd in merge_palte_data:
            
            merge_palte_details = MergedPlateSamples.objects.filter(Q(ind_pool_id= gpd['ind_pool_id']) & Q(merge_plate_id= gpd['merge_plate_id'])).values()[:1]

            for i in merge_palte_details:
                
                master_lab_data = Master_Labs.objects.get(id= i['master_lab_id'])
                i['lab_name'] = master_lab_data.lab_name
                i['lab_id'] = master_lab_data.lab_id

                plate_data = list(MergedPlateDetails.objects.filter(id= i['merge_plate_id']).values('id', 'plate_no').order_by('-id'))
                
                print(plate_data)

                if plate_data:
                    i['plate_no'] = plate_data[0]['plate_no']
                else:
                    i['plate_no'] = '-'

                resp_details.append(i)

        # return Response({'result':resp_details, 'total_pg_count': merge_palte_details_count})
        return Response({'result':resp_details,})




#########################      UPDATE GROUP SAMPLES TEST RESULT       #########################
class UpdateIndMergePlateSamplesTestResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        patient_id = data.get('patient_id')
        result_status= data.get('result_status')
        print(user_id)
        print(patient_id)
        print(result_status)

        # check_data = Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= patient_id))

        
        if int(result_status) != 6:
            Patient.objects.filter(id= patient_id).update(group_samples_result= 1)
            Patient_Testing.objects.create(patient_id= patient_id, testing_status= result_status, rtpcr_test= 1)
            # Patient_Testing.objects.filter(patient_id= patient_id).update(test_result= int(result_status))

        else:
            Patient.objects.filter(id= patient_id).update(retest = 1, test_lab_id__isnull = True, group_samples= 0, pool_samples= 0, group_samples_result= 0, pool_samples_result= 0)
            

        # if check_data:
        #     Patient.objects.filter(id= patient_id).update(group_samples_result= 1)
        #     Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= patient_id)).update(testing_status= result_status, last_update_timestamp= asdatetime.now())
            
        # else:
        #     Patient.objects.filter(id= patient_id).update(group_samples_result= 1)
        #     Patient_Testing.objects.create(Q(id= test_result_id) & Q(patient_id= patient_id)).update(testing_status= result_status)
                       
        # if user_id:

        #     check_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
        #     Master_Labs.objects.filter(id = check_lab_data.testing_lab_master_id).update(closing_balance = F('closing_balance') + 1)

        return Response({'result': 'Result Updated'})


#########################      UPDATE GROUP SAMPLES TEST RESULT       #########################
class UpdatePoolMergePlateSamplesTestResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):


        data = request.data

        user_id = data.get('user_id')
        pool_id = data.get('pool_id')
        plate_id = data.get('plate_id')
        result_status= data.get('result_status')

        print(data, "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")


        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)


        master_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

        testing_result_pool = MergedPlateSamples.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(merge_plate_id= plate_id) & Q(ind_pool_id= pool_id)).values()

        for i in testing_result_pool:

            if int(result_status) == 2:


                # check_data = Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id']))

                # if check_data:
                #     Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id'])).update(testing_status= result_status, last_update_timestamp= asdatetime.now())
                #     Patient.objects.filter(id= i['patient_id']).update(pool_samples_result= 1)
                # else:

                Patient_Testing.objects.create(patient_id= i['patient_id'], testing_status= result_status, rtpcr_test= 1)
                Patient.objects.filter(id= i['patient_id']).update(pool_samples_result= 1)
                MergedPlateSamples.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(merge_plate_id= plate_id) & Q(ind_pool_id= pool_id) & Q()).update(test_result= int(result_status))

                ppp = MergedPlateSamples.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(merge_plate_id= plate_id) & Q(ind_pool_id= pool_id) & Q()).values()
                print(ppp)
            
            if int(result_status) == 3:

                print(int(result_status))
                print("HHHHHHHHHHHHHHHHHHHHHHHHH")

                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                # print(master_lab_data.max_capacity)
                # print(master_lab_data.last_genearte_lab_id)

                # lab_max_cap= int(master_lab_data.max_capacity) - 1

                # split_gen_lab_id = ''
                # if master_lab_data.last_genearte_lab_id:
                #     # print("CHECK LAB ID PRESENT")
                #     split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
                # else:
                #     # print("CHECK LAB ID NOT")
                #     len_of_cap = str(master_lab_data.max_capacity)
                #     split_gen_lab_id = '0000'


                # if int(split_gen_lab_id) == lab_max_cap:
                #     print("IF MAX LAB REACHED")
                #     patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, test_lab_id= master_lab_data.last_genearte_lab_id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0)
                #     Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'A0001')
                
                # else:
                #     print("HELLO HELLO HELLO")
                #     update_lab_id_data = int(split_gen_lab_id) + 1
                #     last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                #     patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, test_lab_id= last_lab_id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0)
                #     Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)

                patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0, submit_for_individual_testing=1, de_pool= 1)
                # Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)
                MergedPlateSamples.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(merge_plate_id= plate_id) & Q(ind_pool_id= pool_id) & Q()).update(test_result= int(result_status))
            
            if int(result_status) == 6:

                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0, submit_for_individual_testing=1, de_pool= 1)
                # Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)
                MergedPlateSamples.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(merge_plate_id= plate_id) & Q(ind_pool_id= pool_id) & Q()).update(test_result= int(result_status))

        return Response({'result': 'Updated'})



class AllPlateDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        print(data)

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        all_plate_details = MergedPlateDetails.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(testing_status= 0)).values('id', 'plate_no', 'testing_status', 'create_datetime', 'master_lab__lab_id')
        all_plate_details_count = MergedPlateDetails.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id) & Q(testing_status= 0)).count()
        
        get_plate_data = paginatorCreation(all_plate_details, selected_page_no)
        
        return Response({'result': list(get_plate_data),'total_pg_count':all_plate_details_count}, status= status.HTTP_200_OK)




class UpdatePrioritySampleData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        srf_id = self.request.query_params.get('srf_id')
        mobile_number = self.request.query_params.get('mobile_number')
        user_id = self.request.query_params.get('user_id')

        check_swab_collector = Swab_Collection_Centre.objects.filter(user_id= user_id).get(user_id= user_id)

        if check_swab_collector:
            query_data = {'test_type__test_type_name': 'RTPCR'}
            
            if mobile_number:
                query_data['mobile_number'] = mobile_number
            elif srf_id:
                query_data['srf_id'] = srf_id
            
            query_data['added_by_id__in']= Swab_Collection_Centre.objects.filter(phc_master_id=  check_swab_collector.phc_master_id).values_list('user_id', flat= True)

            check_patient_data = Patient.objects.filter(**query_data).values('id', 'srf_id', 'mobile_number', 'patient_name', 'age', 'gender', 'patient_status', 'test_type__test_type_name', 'priority')

            if check_patient_data:
                return Response({'result': check_patient_data,}, status= status.HTTP_200_OK)
            else:
                return Response({'result':'Search Data is not comes under this PHC'}, status= status.HTTP_406_NOT_ACCEPTABLE)
        
            return Response(check_swab_collector.user_id)
        else:
            return Response({'result':'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)



    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        patient_id = data.get('patient_id')

        print(data)

        Patient.objects.filter(id= patient_id).update(priority= 1)
        
        return Response({'result': 'Updated Sucessfully'}, status= status.HTTP_200_OK)
















#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


#########################          GET ALL PACKAGES          #########################
class GetAllPackageDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data
        user_id = data.get('user_id')

        check_scc_user = Swab_Collection_Centre.objects.filter(user_id= user_id)

        tho_present  = THO.objects.filter(user_id= user_id)
        dso_present  = DSO.objects.filter(user_id= user_id)
        ssu_present  = SSU.objects.filter(user_id= user_id)

        if check_scc_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':
                all_phcm_data = []
                # check_all_slab_collector = Swab_Collection_Centre.objects.filter(phc_master_id= check_user_data.phc_master_id).values_list('user_id',flat=True)
                # for i in check_all_slab_collector:
                #     package_details = Package_Sampling.objects.filter(Q(user_id=i['user_id']) & (Q(package_type_status= 6) & Q(package_type_action=16)) | (Q(package_type_status=7) & Q(package_type_action=17))).values()
                #     for pd in package_details:
                #         # patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                #         # patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                #         # patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                #         # pd['patient_type_name'] = patient_type_data.patient_type_name
                #         # pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                #         # pd['test_type_name']= patient_test_type_data.test_type_name
                #         check_lab = Testing_Lab_Facility.objects.filter(id=  pd['test_lab_id'])
                #         if check_lab:
                #             check_lab = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                #             lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                #             pd['lab_name'] = lab_master_data.lab_name
                #         else:
                #             pd['lab_name'] = '-'


                #         all_phcm_data.append(pd)
                # return Response({'package_details':all_phcm_data,'result': 'Sucess'})

                check_all_slab_collector = Swab_Collection_Centre.objects.filter(phc_master_id= check_user_data.phc_master_id).values_list('user_id',flat=True)
                print(check_all_slab_collector)
                print(list(check_all_slab_collector))
                print("LISTTTTTTTTT")
                print("DATA           ", check_all_slab_collector)
                # for i in check_all_slab_collector:
                package_details = Package_Sampling.objects.filter(Q(user_id__in=list(check_all_slab_collector))).filter((Q(package_type_status= 6) & Q(package_type_action=16)) | (Q(package_type_status=7) & Q(package_type_action=17))).values()
                print("AAAAAA     ", package_details)
                # package_details = Package_Sampling.objects.filter(Q(user_id__in=list(check_all_slab_collector)) & ((Q(package_type_status= 6) & Q(package_type_action=16)) | (Q(package_type_status=7) & Q(package_type_action=17)))).values()
                # print("AAAAAA     ", package_details)
                
                # for pd in package_details:
                #     check_lab = Testing_Lab_Facility.objects.filter(id=  pd['test_lab_id'])
                #     if check_lab:
                #         check_lab = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                #         lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                #         pd['lab_name'] = lab_master_data.lab_name
                #     else:
                #         pd['lab_name'] = '-'


                #     all_phcm_data.append(pd)


                return Response({'package_details':package_details,'result': 'Sucess'})

            if check_user_roles.role_name == 'PHCS':
                 # sc = Swab_Collection_Centre.objects.filter(added_by=user_id)
                package_details = Package_Sampling.objects.filter(user_id=user_id).values().order_by('-id')

                return Response({'package_details':package_details,'result': 'Sucess'})

        
        # tho_user  = THO.objects.filter(user_id= user_id)

        # if tho_user:
        #     tho_data = THO.objects.get(user_id= user_id)
        #     tho_package_datas = Package_Sampling.objects.filter(tho_id= tho_data.id).values()

        #     return Response({'package_details':tho_package_datas,'result':'Sucess'})

       

        if tho_present:
            tho_data            = THO.objects.get(user_id= user_id)
            tho_package_datas   = Package_Sampling.objects.filter(Q(tho_id= tho_data.id) & Q(package_type_action=13)).values()
            for pd in tho_package_datas:
                check_lab = Testing_Lab_Facility.objects.filter(id= pd['test_lab_id'])
                if check_lab:
                    check_lab = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                    lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                    pd['lab_name'] = lab_master_data.lab_name
                else:
                    pd['lab_name'] = '-'

            return Response({'package_details':tho_package_datas,'result':'Sucess'})


        elif dso_present:
            dso_data            = DSO.objects.get(user_id= user_id)
            dso_package_datas   = Package_Sampling.objects.filter(dso_id= dso_data.id).values()
            for pd in dso_package_datas:
                check_lab = Testing_Lab_Facility.objects.filter(id=  pd['test_lab_id'])
                if check_lab:
                    check_lab = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                    lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                    pd['lab_name'] = lab_master_data.lab_name
                else:
                    pd['lab_name'] = '-'

            return Response({'package_details':dso_package_datas,'result':'Sucess'})
        
        elif ssu_present:
            ssu_data            = SSU.objects.get(user_id= user_id)
            ssu_package_datas   = Package_Sampling.objects.filter(ssu_id= ssu_data.id).values()
            for pd in ssu_package_datas:
                check_lab = Testing_Lab_Facility.objects.filter(id=  pd['test_lab_id'])
                if check_lab:
                    check_lab = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                    lab_master_data = Master_Labs.objects.get(id= check_lab.testing_lab_master_id)
                    pd['lab_name'] = lab_master_data.lab_name
                else:
                    pd['lab_name'] = '-'

            return Response({'package_details':ssu_package_datas,'result':'Sucess'})
        
        else:
            return Response({'result': 'INVALID '})




class UpdatePatientSwabTestingResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)
        patient_id      = data.get('patient_id')
        user_id         = data.get('user_id')
        result          = data.get('result')
        
        patient_res_data = Patient.object.filter(id=patient_id).update(patient_testing_id=result )

        return Response({'details':patient_res_data,'result': 'successfull '})

#########################################################################################



#########################          UPDATE PACKAGE SAMPLES          #########################
class UpadtePackagetoLabOrHigherOfc(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        package_id      = data.get('package_id')
        user_id         = data.get('user_id')
        click_str          = data.get('action')
        lab_id =data.get('lab_id')
        
        if click_str == 'notify_tho':

            check_user_tho = Swab_Collection_Centre.objects.get(user_id=user_id)
            tho_data = Package_Sampling.objects.filter(id=package_id).update(tho_id=check_user_tho.id, )

            return Response({'details':tho_data,'result': 'successfull '})

        elif click_str == 'dso':

            # check_user_dso = DSO.objects.get(user_id=user_id)
            check_user_dso = Swab_Collection_Centre.objects.get(user_id=user_id)
            check_tho_data = THO.objects.get(id= check_user_dso.tho_id)
            dso_data=Package_Sampling.objects.filter(id=package_id).update(dso_id = check_tho_data.dso_id, tho_id= check_user_dso.tho_id, package_type_action= 13, package_type_status= 3)

            dso_data=Package_Sampling.objects.filter(id=package_id).values()


            return Response({'details':dso_data,'result': 'successfull '})

        elif click_str == 'ssu':

            check_user_ssu = SSU.objects.get(user_id=user_id)
            ssu_data=Package_Sampling.objects.filter(id=package_id).update(ssu_id=check_user_ssu.id, dispatch_status= 0,  dso_disptch_status= 0, ssu_disptch_status= 0)

            ssu_data=Package_Sampling.objects.filter(id=package_id).values()

            return Response({'details':ssu_data,'result': 'successfull '})

        elif click_str == 'lab':
            print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKk")

            check_tlab_user = Testing_Lab_Facility.objects.get(id= lab_id)
            lab_data=Package_Sampling.objects.filter(id=package_id).update(test_lab_id= check_tlab_user.id, lab_master_id= check_tlab_user.testing_lab_master_id, last_update_timestamp= asdatetime.now(), dispatch_status= 0,  dso_disptch_status= 0, ssu_disptch_status= 0, test_lab_disptch_status= 0, package_type_status=5, package_type_action=15, reference_tlab= None)

            lab_data=Package_Sampling.objects.filter(id=package_id).values()

            lab_data_get = Package_Sampling.objects.get(id=package_id)

            # check_tlab_user = Testing_Lab_Facility.objects.filter(id= lab_id).update(availability_limit = int(check_tlab_user.availability_limit) - int(lab_data_get.samples_count) )
            get_master_table = Master_Labs.objects.get(id= check_tlab_user.testing_lab_master_id)
            update_master_table = Master_Labs.objects.filter(id= check_tlab_user.testing_lab_master_id).update(closing_balance= int(get_master_table.closing_balance) - int(lab_data_get.samples_count))
            print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
            return Response({'details':lab_data,'result': 'successfull '})

        else:
            return Response({'result': 'INVALID '})




#########################          GET PACKAGES SAMPLES          #########################
class GetPackageSamplesDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        package_id = data.get('id')

        get_package_samples_details = Patient.objects.filter(package_sampling_id= package_id).values()
        

        for i in get_package_samples_details:
            test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
            spcm_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])

            i['test_type_name'] = test_type_data.test_type_name
            i['specimen_type_name'] = spcm_type_data.specimen_type_name

        return Response({'result':get_package_samples_details}, status= status.HTTP_200_OK)




#########################          PHC USER LOCATION DETAILS          #########################
class GetPHCUserLocationDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data 

        resident_type = data.get('resident_type')
        user_id= data.get('user_id')


       

        swab_coll_data_user_data = Swab_Collection_Centre.objects.filter(user_id = user_id).values()
        # print(swab_coll_data_user_data)
        # swab_coll_data = Swab_Collection_Centre.objects.get(user_id = user_id)

        # zone_data = ''
        # district_data = ''
        # block_data = ''
        # ward_data = ''
        # panchayat_data = ''
        # village_data = ''

        # phc_master_district = Master_District.objects.none()
        # all_block_details = Master_Block.objects.none()
        # all_panchayat_details = Master_Panchayat.objects.none()
        # all_village_details = Master_Village.objects.none()



        # for i in swab_coll_data:
        #     phc_master_data = Master_PHC.objects.get(id= swab_coll_data.phc_master_id)
        #     print(phc_master_data.sys_id)
        #     print(phc_master_data.district_name_eng)
        #     print(phc_master_data.block_name_eng)
        #     print(phc_master_data.village_name)
        #     print(phc_master_data.block_code)
        #     print(phc_master_data.panchayat_code)
        #     print(phc_master_data.village_code)
        #     print(phc_master_data.phc_name)
        #     print(phc_master_data.phc_code)

        # all_block_details = Master_Block.objects.filter(block_code= phc_master_data.block_code).values()
        # print("BLOCK DETAILS", all_block_details)

        # check_block_dist_code = Master_Block.objects.get(block_code= phc_master_data.block_code)
        # print(check_block_dist_code.district_code)
        # print(check_block_dist_code.block_code)
        # print(check_block_dist_code.block_name_eng)
        
        # phc_master_district = Master_District.objects.filter(district_code= check_block_dist_code.district_code).values()
        # print(phc_master_district)

        # all_panchayat_details = Master_Panchayat.objects.filter(Q(block_code= phc_master_data.block_code)).values()# & Q(panchayat_code= phc_master_data.panchayat_code)).values()
        # print(all_panchayat_details)

        # all_village_details = Master_Village.objects.filter(Q(district_code= check_block_dist_code.district_code) & Q(block_code= phc_master_data.block_code.strip()) & Q(panchayat_code= phc_master_data.panchayat_code.strip())).values()
        # print(all_village_details)




        # for i in swab_coll_data:
        #     phc_master_data = Master_PHC.objects.get(id= i['phc_master_id'])

        #     print(phc_master_data.block_code)

        #     all_block_details = Master_Block.objects.filter(block_code= phc_master_data.block_code).values()

        #     check_block_dist_code = Master_Block.objects.get(block_code= phc_master_data.block_code)

        #     print(check_block_dist_code.district_code)
        #     print(phc_master_data.panchayat_code)
            

        #     phc_master_district = Master_District.objects.filter(district_code= check_block_dist_code.district_code).values()

            
        #     all_panchayat_details = Master_Panchayat.objects.filter(Q(block_code= phc_master_data.block_code)).values()# & Q(panchayat_code= phc_master_data.panchayat_code)).values()

        #     all_village_details = Master_Village.objects.filter(Q(district_code= check_block_dist_code.district_code) & Q(block_code= phc_master_data.block_code.strip()) & Q(panchayat_code= phc_master_data.panchayat_code.strip())).values()

        #     print(all_village_details)

        #     if i['zone_id']:
        #         zone_name = Master_Zone.objects.get(id= i['zone_id'])
        #         i['zone_name_eng']= zone_name.zone_name
        #         zone_data = zone_name.bbmp_zone_no_ksrsac

        #     if i['district_id']:
        #         district_name = Master_District.objects.get(id= i['district_id'])
        #         i['district_name_eng']= district_name.district_name_eng
        #         district_data = district_name.district_code

        #     if i['city_id']:
        #         block_name = Master_Block.objects.get(id= i['city_id'])
        #         i['block_name_eng']= block_name.block_name_eng
        #         block_data = block_name.block_code

        #     if i['ward_id']:
        #         ward_name = Master_Ward.objects.get(id= i['ward_id'])
        #         i['ward_name']= ward_name.ward_name
        #         ward_data = ward_name.ward_no
            
        #     if i['panchayat_id']:
        #         panchayat_name = Master_Panchayat.objects.get(id= i['panchayat_id'])
        #         i['panchayat_name_eng']= panchayat_name.panchayat_name_eng
        #         panchayat_data = panchayat_name.panchayat_code

        #     if i['village_id']:
        #         village_name = Master_Village.objects.get(id= i['village_id'])  
        #         i['village_name_eng']= village_name.village_name_eng
        #         village_data = village_name.village_code
        
        # zone_details = Master_Zone.objects.all().values()
        # ward_details = Master_Ward.objects.all().values()
        # village_details = Master_Village.objects.filter(Q(district_code= district_data) & Q(block_code= block_data) & Q(panchayat_code= panchayat_data) & Q(village_code= village_data)).values()
        # panchayat_details = Master_Panchayat.objects.filter(Q(district_code= district_data) & Q(block_code= block_data) & Q(panchayat_code= panchayat_data)).values()
        # block_details = Master_Block.objects.filter(Q(district_code= district_data) & Q(block_code= block_data)).values()
        # district_details = Master_District.objects.all().values()
        
        # return Response({'phc_user_details':swab_coll_data_user_data, 'zone_details':[], 'ward_details':[], 'village_details':[], 'panchayat_details':[], 'block_details':[], 'city_details':[], 'phc_master_district':phc_master_district, 'all_block_details':all_block_details, 'all_panchayat_details':all_panchayat_details, 'all_village_details':all_village_details, 'rural':True, 'urban':False, 'bbmp': False}, status= status.HTTP_200_OK)
        if resident_type == 'Local':

            check_swab_collector_details = Swab_Collection_Centre.objects.get(user_id= user_id)

            master_data = Master_PHC.objects.get(id= check_swab_collector_details.phc_master_id)

            check_village_details = Master_PHC.objects.filter(phc_code= master_data.phc_code).values()

            check_dist_id = []
            check_block_id = []
            check_pan_id = []
            check_vill_id = []
            check_zone_id = []
            check_ward_id = []

            rural_flag = True
            urban_flag = False
            bbmp_flag = False

            if master_data.phc_type == 'R':
                rural_flag = True
            if master_data.phc_type == 'U':
                urban_flag = True
            if master_data.phc_type == 'B':
                bbmp_flag = True


            dist_details = Master_PHC.objects.filter(phc_code= master_data.phc_code).values('district_code').distinct()
            locat_phc_dist_details = []


            for i in check_village_details:

                if i['district_code'] not in check_dist_id:
                    check_dist_id.append(i['district_code'])
                
                if i['block_code'] not in check_block_id:
                    check_block_id.append(i['block_code'])
                
                if i['panchayat_code'] not in check_pan_id:
                    check_pan_id.append(i['panchayat_code'])

                if i['village_code'] not in check_vill_id:
                    check_vill_id.append(i['village_code'])

                if i['zone_code'] not in check_zone_id:
                    check_zone_id.append(i['zone_code'])

                if i['ward_code'] not in check_ward_id:
                    check_ward_id.append(i['ward_code'])

            phc_dist_details = []
            phc_block_details = []
            phc_pan_details = []
            phc_vill_details = []
            phc_zone_details = []
            phc_ward_details = []

            print(master_data.phc_code)

            for i in check_dist_id:
                print(i)
                get_phc_dist_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(district_code= i)).values('district_code', 'district_name_eng').distinct()
                print(get_phc_dist_details)
                print(len(get_phc_dist_details))
                # if get_phc_dist_details:
                for j in get_phc_dist_details:
                    phc_dist_details.append(j)

            for i in check_block_id:
                print(i)
                get_phc_block_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(block_code= i)).values('block_name_eng', 'block_code').distinct()
                print(get_phc_block_details)
                print(len(get_phc_block_details))
                # if get_phc_block_details:
                for j in get_phc_block_details:
                    phc_block_details.append(j)

            for i in check_pan_id:
                print(i)
                get_phc_pan_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(panchayat_code= i)).values('panchayat_name_eng', 'panchayat_code').distinct()
                print(get_phc_pan_details)
                print(len(get_phc_pan_details))
                # if get_phc_pan_details:
                for j in get_phc_pan_details:
                    phc_pan_details.append(j)

            for i in check_vill_id:
                print(i)
                get_phc_vill_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(village_code= i)).values('village_name_eng', 'village_code').distinct()
                print(get_phc_vill_details)
                print(len(get_phc_vill_details))
                # if get_phc_vill_details:
                for j in get_phc_vill_details:
                    phc_vill_details.append(j)

            for i in check_zone_id:
                print(i)
                get_phc_zone_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(zone_code= i)).values('zone_name_eng', 'zone_code').distinct()
                print(get_phc_zone_details)
                print(len(get_phc_zone_details))
                # if get_phc_zone_details:
                for j in get_phc_zone_details:
                    phc_zone_details.append(j)

            for i in check_ward_id:
                print(i)
                get_phc_ward_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(ward_code= i)).values('ward_name_eng', 'ward_code').distinct()
                print(get_phc_ward_details)
                print(len(get_phc_ward_details))
                # if get_phc_ward_details:
                for j in get_phc_ward_details:
                    phc_ward_details.append(j)


            print(phc_dist_details)
            print(phc_block_details)
            print(phc_pan_details)
            print(phc_vill_details)
            print(phc_zone_details)
            print(phc_ward_details)
            
            swab_coll_data_user_data = Swab_Collection_Centre.objects.filter(user_id = user_id).values()

            for i in swab_coll_data_user_data:
                phc_master_data = Master_PHC.objects.get(id= i['phc_master_id'])
                i['district_name_eng']  = (phc_master_data.district_name_eng).strip()
                i['block_name_eng'] = (phc_master_data.block_name_eng).strip()
                i['panchayat_name_eng'] = (phc_master_data.panchayat_name_eng).strip()
                i['village_name_eng'] = (phc_master_data.village_name_eng).strip()
                i['district_code'] = phc_master_data.district_code
                i['block_code'] = phc_master_data.block_code
                i['panchayat_code'] = phc_master_data.panchayat_code
                i['village_code'] = phc_master_data.village_code
                i['phc_name'] = (phc_master_data.phc_name).strip()
                i['phc_code'] = phc_master_data.phc_code

            return Response({'swab_coll_data_user_data':swab_coll_data_user_data,'rural':rural_flag, 'urban':urban_flag, 'bbmp':bbmp_flag, 'phc_district_details':phc_dist_details, 'phc_block_details': phc_block_details, 'phc_pan_details':phc_pan_details, 'phc_vill_details':phc_vill_details, 'phc_zone_details': phc_zone_details, 'phc_ward_details': phc_ward_details}, status=status.HTTP_200_OK)




#########################          PHC USER LOCATION VILLAGE FILTER          #########################
class GetPHCUserVillageDataFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        print(data)

        resident_type = data.get('resident_type')
        user_id= data.get('user_id')
        village_code = data.get('village_name')

        swab_coll_data_user_data = Swab_Collection_Centre.objects.filter(user_id = user_id).values()

        if resident_type == 'Local':
            
            check_swab_collector_details = Swab_Collection_Centre.objects.get(user_id= user_id)

            # print(check_swab_collector_details.phc_master_id)

            master_data = Master_PHC.objects.get(id= check_swab_collector_details.phc_master_id)
            # print(master_data.phc_code)

            # check_village_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(village_code = village_code)).values()
            check_village_details = Master_PHC.objects.filter(Q(village_code = village_code)).values()
            # print(check_village_details)


            return Response({'check_village_details':check_village_details}, status=status.HTTP_200_OK)
        
        else:
            return Response({'check_village_details': []})


        

#########################          PHC USER LOCATION WARD FILTER          #########################
class GetPHCUserWardDataFilter(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        print(data)

        resident_type = data.get('resident_type')
        user_id= data.get('user_id')
        ward_code = data.get('ward_name')

        swab_coll_data_user_data = Swab_Collection_Centre.objects.filter(user_id = user_id).values()

        if resident_type == 'Local':
            
            check_swab_collector_details = Swab_Collection_Centre.objects.get(user_id= user_id)

            # print(check_swab_collector_details.phc_master_id)

            master_data = Master_PHC.objects.get(id= check_swab_collector_details.phc_master_id)
            # print(master_data.phc_code)

            # check_ward_details = Master_PHC.objects.filter(Q(phc_code= master_data.phc_code) & Q(ward_code = ward_code)).values()
            check_ward_details = Master_PHC.objects.filter(Q(ward_code = ward_code)).values()
            # print(check_ward_details)


            return Response({'check_ward_details':check_ward_details}, status=status.HTTP_200_OK)
        
        else:
            return Response({'check_ward_details': []})

        
        

#########################          GET PHC MOBILE USERS          #########################
class GetPHCMobileUsers(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':
                check_mobile_slab_collector = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= check_user_data.swab_collection_centre_name) & Q(role_id= 8)).values()
                for i in check_mobile_slab_collector:
                    check_user_info = User.objects.get(id= i['user_id'])
                    i['user_name'] = check_user_info.username
                    i['name'] = check_user_info.first_name
                return Response({'mobile_swab_collectors':check_mobile_slab_collector,'result': 'successfull'}, status= status.HTTP_200_OK)

        else:
            return Response({'result': 'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)

##############################################                 GET PHC 



#########################          GET ALL MO CONTRACING TACING DATA          #########################
class AllContactTracingData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        call_page = data.get('type')
        action = data.get('action')

        if call_page == 'Update':

            if action == 'CT':

                all_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_msc_user__isnull= True)).values()
                # all_contact_tracing = Contact_Tracing.objects.all().values()

                return Response({'result':all_contact_tracing}, status= status.HTTP_200_OK)

            if action == 'ILI':

                all_ili = ILI.objects.filter(Q(assigned_msc_user__isnull= True)).values()
                # all_contact_tracing = Contact_Tracing.objects.all().values()

                return Response({'result':all_ili}, status= status.HTTP_200_OK)
        
        if call_page == 'Status':
            all_contact_tracing = Contact_Tracing.objects.filter(date_of_contact_created__date= asdatetime.now().date()).values()

            for i in all_contact_tracing:

                print(i['assigned_msc_user_id'])

                if i['assigned_msc_user_id'] == None:
                    i['status'] = 0
                    i['msc_name'] = 'N/A'
                else:
                    i['status'] = 1
                    check_user_name = User.objects.get(id= i['assigned_msc_user_id'])
                    i['msc_name'] = check_user_name.first_name

            return Response({'result':all_contact_tracing}, status= status.HTTP_200_OK)
            
        else:
            return Response({'result':'Something went wrong'})




#########################          ASSIGN CONTACT TRACING          #########################
class AssignContactTracing(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data
        print(data)

        assigned_user   = data.get('user_id')
        tracing_ids     = data.get('assign_contact_tracing_data')
        action_type     = data.get('action_type')

        if action_type=='CT':
            for i in tracing_ids:
                check_phc_data = Swab_Collection_Centre.objects.get(user_id= assigned_user)
                Contact_Tracing.objects.filter(id= i).update(assigned_date= asdatetime.now(), assigned_msc_user_id= assigned_user, assigned_phc= check_phc_data.phc_master_id)

        if action_type=='ILI':
            for i in tracing_ids:
                check_phc_data = Swab_Collection_Centre.objects.get(user_id= assigned_user)
                ILI.objects.filter(id= i).update(assigned_date= asdatetime.now(), assigned_msc_user_id= assigned_user, assigned_phc= check_phc_data.phc_master_id)
        
        return Response({'result': 'Assigned Sucessfully'}, status= status.HTTP_200_OK)





#########################          ACCEPT PACKAGE SAMPLES          #########################
class LabReceivePackage(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)

        user_id = data.get('user_id')
        package_id = data.get('package_id')

        Package_Sampling.objects.filter(id= package_id).update(package_type_status= 5, package_type_action= 15, lab_received_datetime= asdatetime.now())

        return Response({'result': 'Updated Sucessfully'})




#########################          ACCEPT PACKAGE SAMPLES          #########################
class AcceptPackagePatientSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        srf_id = data.get('srf_id')
        result_status = data.get('received_status')
        result_status_comment = data.get('reject_reason')
        user_id = data.get('user_id')
        package_id = data.get('package_id')

        if result_status:

            if result_status == 'Reject':
                test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
                master_lab_data = Master_Labs.objects.get(id= test_lab_data.testing_lab_master_id)
                get_patient_details = Patient.objects.filter(srf_id= srf_id).update(sample_status= result_status, lab_accepted_datetime= asdatetime.now(), samples_rejected= 1, package_sampling_id= None) # test_lab_id= master_lab_data.lab_id)

                get_package_details = Package_Sampling.objects.get(id= package_id)
                print(get_package_details.samples_count)
                # Package_Sampling.objects.filter(id= package_id).update(samples_count= int(get_package_details.samples_count) - 1)


                get_pa_data = Package_Sampling.objects.filter(id= package_id).values()

            elif result_status == 'Inconclusive':

                test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
                master_lab_data = Master_Labs.objects.get(id= test_lab_data.testing_lab_master_id)
                get_patient_details = Patient.objects.filter(srf_id= srf_id).update(sample_status= result_status, lab_accepted_datetime= asdatetime.now(), samples_inconclusive= 1, package_sampling_id= None) # test_lab_id= master_lab_data.lab_id)

                get_package_details = Package_Sampling.objects.get(id= package_id)
                print(get_package_details.samples_count)

            else:
                test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
                master_lab_data = Master_Labs.objects.get(id= test_lab_data.testing_lab_master_id)
                get_patient_details = Patient.objects.filter(srf_id= srf_id).update(sample_status= result_status, lab_accepted_datetime= asdatetime.now()) # test_lab_id= master_lab_data.lab_id)

        if result_status_comment:

            get_patient_details = Patient.objects.filter(srf_id= srf_id).update(sample_rejected_reason= result_status_comment, lab_accepted_datetime= asdatetime.now())

            get_package_details = Package_Sampling.objects.get(id= package_id)
            Package_Sampling.objects.filter(id= package_id).update(samples_count= int(get_package_details.samples_count) - 1)
            

            check_data = Package_Sampling.objects.filter(Q(id= package_id) & Q(samples_count = 0)).delete()
            

            get_pa_data = Package_Sampling.objects.filter(id= package_id).values()

        # get_added_user_details = Patient.objects.get(srf_id= srf_id)

        # get_roles = Roles.objects.get(role_name= 'PHCMO')

        # get_phcs_user_details = Swab_Collection_Centre.objects.get(Q(user_id= get_added_user_details.added_by))

        # get_phcm_user_details = Swab_Collection_Centre.objects.get(Q(swab_collection_centre_name= get_phcs_user_details.swab_collection_centre_name) & Q(role= get_roles.id))

        return Response('Updated Sucessfully')




#########################          GET REJECTED SAMPLES DETAILS          #########################
class GetRejectedSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        print(data)

        user_details = Swab_Collection_Centre.objects.get(user_id= user_id)

        phc_users_list = Swab_Collection_Centre.objects.filter(phc_master_id= user_details.phc_master_id).values()

        phc_user_id = []

        for i in phc_users_list:
            phc_user_id.append(i['user_id'])

        
        get_rejected_samples = Patient.objects.filter(Q(added_by_id__in= phc_user_id) & Q(samples_rejected= 1)).values()

        for j in get_rejected_samples:

            get_sp_type = Specimen_Type_Ref.objects.get(id= j['specimen_type_id'])
            j['specimen_type_name'] = get_sp_type.specimen_type_name
            added_user_data = User.objects.get(id= j['added_by_id'])
            j['added_user_name'] = added_user_data.first_name

        return Response({'result': get_rejected_samples}, status= status.HTTP_200_OK)





#########################          GENERATE LAB ID          #########################
class GenerateLabId(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        user_id = data.get('user_id')

        test_lab_data = Testing_Lab_Facility.objects.filter(user_id= user_id)

        if test_lab_data:
            test_lab_data_get = Testing_Lab_Facility.objects.get(user_id= user_id)

            master_lab_data = Master_Labs.objects.get(id= test_lab_data_get.testing_lab_master_id)

            # get_patient = Patient.objects.filter(test_lab_id= master_lab_data.lab_id).values('id','test_lab_id', 'patient_name', 'gender', 'age', 'mobile_number', 'patient_status', 'srf_id')
            get_patient = Patient.objects.filter(lab_master_id= master_lab_data.id).values('id','test_lab_id', 'lab_master_id', 'patient_name', 'gender', 'age', 'mobile_number', 'patient_status', 'srf_id', 'lab_ops_received_datetime').order_by('lab_ops_received_datetime')

            for i in get_patient:
                check_add = Patient_Address.objects.filter(patient_id= i['id'])
                chcek_out_add = Outside_Patient_Address.objects.filter(patient_id = i['id'])

                i['lab_ops_received_datetime'] = str(i['lab_ops_received_datetime'])

                if check_add:
                    i['address'] = ''
                if chcek_out_add:
                    i['address'] = ''

            return Response({'result': get_patient})
        else:
            return Response({'result':[]})




#########################          AVALIABLE LAS FOR ASSIGN PACKAGES          #########################
class GetTestingLabs(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print('FFFFFFFFFFFFFFF')
        print(data)

        user_id = data.get('user_id')


        check_swab_collection_user = Swab_Collection_Centre.objects.filter(user_id= user_id)
        check_dso_user = DSO.objects.filter(user_id= user_id)
        check_ssu_user = SSU.objects.filter(user_id= user_id)



        if check_swab_collection_user:
            print("LLLLLLLLLLLLLLLLLLLLLLl")
            swab_collection_user_details = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_testing_lab_details = Testing_Lab_Facility.objects.get(id= swab_collection_user_details.test_lab_id)

            max_limit = check_testing_lab_details.current_count
            availlable_limit = check_testing_lab_details.availability_limit

            lab_master_details = Master_Labs.objects.get(id= check_testing_lab_details.testing_lab_master_id)

            print(swab_collection_user_details.test_lab_id)

            # if (int(max_limit) <= int(availlable_limit)):
            # if (int(availlable_limit) >= 5):
            if (int(lab_master_details.closing_balance) >= 100):
                test_lab_details = Testing_Lab_Facility.objects.filter(id= swab_collection_user_details.test_lab_id).values()
                print(test_lab_details)
                for i in test_lab_details:
                    lab_master = Master_Labs.objects.get(id= i['testing_lab_master_id'])
                    i['lab_type'] = lab_master.lab_type

                print(test_lab_details)
                return Response(test_lab_details)
            else:
                return Response([])


        if check_dso_user:
            check_dso_user = DSO.objects.get(user_id= user_id)
            check_testing_lab_details = Testing_Lab_Facility.objects.filter(district_id= check_dso_user.district).values()

            final_data = []

            for i in check_testing_lab_details:
                max_limit = i['current_count']
                availlable_limit = i['availability_limit']
                lab_master = Master_Labs.objects.get(id= i['testing_lab_master_id'])
                i['lab_type'] = lab_master.lab_type

                # if (int(max_limit) <= int(availlable_limit)):
                if (int(availlable_limit) >= 5):
                    final_data.append(i)

            return Response(final_data)


        if check_ssu_user:
            swab_collection_user_details = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_testing_lab_details = Testing_Lab_Facility.objects.get(id= swab_collection_user_details.test_lab_id)

            max_limit = check_testing_lab_details.current_count
            availlable_limit = check_testing_lab_details.availability_limit

            # if (int(max_limit) <= int(availlable_limit)):
            if (int(availlable_limit) >= 5):
                test_lab_details = Testing_Lab_Facility.objects.filter(id= swab_collection_user_details.test_lab_id).values()
                for i in test_lab_details:
                    lab_master = Master_Labs.objects.get(id= i['testing_lab_master_id'])
                    i['lab_type'] = lab_master.lab_type
                return Response(test_lab_details)
            else:
                return Response([])
        
        else:
            return Response([])




#########################          PHC LABS CHECK          #########################
class CheckPHCLabAvailable(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        user_id = data.get('user_id')
        package_id = data.get('package_id')

        swab_collection_user_details = Swab_Collection_Centre.objects.get(user_id= user_id)
        check_testing_lab_details = Testing_Lab_Facility.objects.get(id= swab_collection_user_details.test_lab_id)

        lab_master_details = Master_Labs.objects.get(id= check_testing_lab_details.testing_lab_master_id)

        package_details = Package_Sampling.objects.get(id= package_id)

        if lab_master_details.closing_balance > package_details.samples_count:

            lab_data=Package_Sampling.objects.filter(id=package_id).update(test_lab_id= check_testing_lab_details.id, lab_master_id= check_testing_lab_details.testing_lab_master_id, last_update_timestamp= asdatetime.now(), dispatch_status= 0,  dso_disptch_status= 0, ssu_disptch_status= 0, test_lab_disptch_status= 0, package_type_status= 8, package_type_action=18, reference_tlab= None)

            update_master_table = Master_Labs.objects.filter(id= check_testing_lab_details.testing_lab_master_id).update(closing_balance= int(lab_master_details.closing_balance) - int(package_details.samples_count))

            lab_master_details = Master_Labs.objects.filter(id= check_testing_lab_details.testing_lab_master_id).values()
            return Response({'result': lab_master_details}, status= status.HTTP_200_OK)
        
        else:
            
            return Response({'result': []})





#########################          DSO GET LABS          #########################
class DSOReferenceTlabData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print("GGGGGGGGGGGGGGGGGGGGG")
        print(data)

        user_id = data.get('user_id')
        package_id = data.get('package_id')
        test_lab_id = data.get('lab_id')

        update_package_data = Package_Sampling.objects.filter(id= package_id)
        print(update_package_data)

        # update_package_data = Package_Sampling.objects.filter(id= package_id).update(reference_tlab= test_lab_id, test_lab_id= test_lab_id, package_type_status= 2, package_type_action= 12)
        update_package_data = Package_Sampling.objects.filter(id= package_id).update(reference_tlab= test_lab_id, package_type_status= 2, package_type_action= 12)

        return Response("Sucessfully")



#########################          CHECK PACKAGE REFERENCE TEST LABS          #########################
class CheckPackageReferenceCheck(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)
        print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        package_id = data.get('package_id')

        check_package_details = Package_Sampling.objects.filter(id= package_id).values()
        print(check_package_details)

        if check_package_details:
            chack_data = Package_Sampling.objects.get(id= package_id)

            reference_test_lab = Testing_Lab_Facility.objects.filter(testing_lab_master_id= chack_data.reference_tlab).values()
            # reference_test_lab = Master_Labs.objects.filter(id= chack_data.reference_tlab).values()
            print(reference_test_lab)
            return Response(reference_test_lab)
        else:
            return Response("Error")



#########################          GENERATE USERNAME FOR MO LOGINS (PHCS AND PHCMC)          #########################
class GenerateUsername(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        user_role = data.get('user_role')

        phc_mo_details = Swab_Collection_Centre.objects.filter(user_id= user_id)
        if phc_mo_details:
            phc_mo_details = Swab_Collection_Centre.objects.get(user_id= user_id)
            role_data = Roles.objects.get(role_name= user_role)
            if user_role == 'PHCS':
                check_phc_users_data_check = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).values()
                if check_phc_users_data_check:
                    check_phc_users_data = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).values().order_by('-id')[:1]
                    last_phc_user_name = ''
                    for i in check_phc_users_data:
                        last_user_name = User.objects.get(id= i['user_id'])
                        user_name_split_data = (last_user_name.username).split('-')
                        last_phc_user_name = str((user_name_split_data[0]).split('_')[0])+'_'+str((user_name_split_data[0]).split('_')[1])+'_SC'+'-'+str(int(user_name_split_data[1])+ 1)

                    return Response({'last_user_name':last_phc_user_name}, status=status.HTTP_200_OK)
                else:
                    # check_phc_users_data = Swab_Collection_Centre.objects.get(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).order_by('-id')[:1]
                    # print("PHCS",phc_mo_details.swab_collection_centre_name)
                    # return Response({'last_user_name': str(phc_mo_details.swab_collection_centre_name)+'_SC-1'})

                    print("PHCS",phc_mo_details.swab_collection_centre_name)
                    get_mo_user_data = User.objects.get(id= phc_mo_details.user_id)

                    lst_user_name = get_mo_user_data.username.split('-')

                    last_dd_data = str((lst_user_name[0]).split('_')[0])+'_'+str((lst_user_name[0]).split('_')[1])+'_SC-1'

                    # return Response({'last_user_name': str(phc_mo_details.swab_collection_centre_name)+'_SC-1'})
                    return Response({'last_user_name': last_dd_data})

            if user_role == 'PHCM':
                role_data = Roles.objects.get(role_name= user_role)
                check_phc_users_data_check = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).values()
                if check_phc_users_data_check:
                   
                    check_phc_users_data = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).values().order_by('-id')[:1]
                    
                    last_phc_user_name = ''
                    for i in check_phc_users_data:
                        last_user_name = User.objects.get(id= i['user_id'])
                        user_name_split_data = (last_user_name.username).split('-')
                        last_phc_user_name = str((user_name_split_data[0]).split('_')[0])+'_'+str((user_name_split_data[0]).split('_')[1])+'_MSC'+'-'+str(int(user_name_split_data[1]) + 1)

                    return Response({'last_user_name':last_phc_user_name}, status=status.HTTP_200_OK)
                else:
                    # check_phc_users_data = Swab_Collection_Centre.objects.get(Q(swab_collection_centre_name= phc_mo_details.swab_collection_centre_name) & Q(role_id= role_data.id)).values().order_by('-id')[:1]
                    # print("PHCS",phc_mo_details.swab_collection_centre_name)
                    # return Response({'last_user_name': str(phc_mo_details.swab_collection_centre_name)+'_MSC-1'})

                    print("PHCS",phc_mo_details.swab_collection_centre_name)
                    get_mo_user_data = User.objects.get(id= phc_mo_details.user_id)

                    lst_user_name = get_mo_user_data.username.split('-')

                    last_dd_data = str((lst_user_name[0]).split('_')[0])+'_'+str((lst_user_name[0]).split('_')[1])+'_MSC-1'

                    # return Response({'last_user_name': str(phc_mo_details.swab_collection_centre_name)+'_MSC-1'})
                    return Response({'last_user_name': last_dd_data})
        
        else:
            return Response({'result':'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)



#########################          CREATE NEW USERS          #########################
class CreateUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)

        user_name = data.get('username')
        password = data.get('password')
        user_id = data.get('user_id')
        mobile_no = data.get('mobile_number')
        role = data.get('userrole')
        first_name = data.get('name')

        get_role_data = Roles.objects.get(role_name= role)

        phc_mo_details = Swab_Collection_Centre.objects.get(user_id= user_id)


        create_user = User.objects.create_user(username= user_name, password= password, first_name= first_name)

        create_user_role_ref = User_Role_Ref.objects.create(user_id= create_user.id, role_id= get_role_data.id, user_role_name= get_role_data.role_name, user_role_desc= get_role_data.role_name, mobile_number= mobile_no, )

        swab_collection_create = Swab_Collection_Centre.objects.create(user_id= create_user.id, test_lab_id= phc_mo_details.test_lab_id, phc_master_id=phc_mo_details.phc_master_id, tho_id= phc_mo_details.tho_id, role_id= get_role_data.id,
                                                                        swab_collection_centre_name= phc_mo_details.swab_collection_centre_name, swab_collection_centre_desc= phc_mo_details.swab_collection_centre_name,
                                                                        zone_id= phc_mo_details.zone_id, district_id= phc_mo_details.district_id, city_id= phc_mo_details.city_id,
                                                                        ward_id= phc_mo_details.ward_id, taluk_name= phc_mo_details.taluk_name, panchayat_id= phc_mo_details.panchayat_id,
                                                                        village_id= phc_mo_details.village_id, pincode= phc_mo_details.pincode)

        return Response("User Created Sucessfully")



#########################          USER SUSPEND          #########################
class UserSuspend(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        
        suspend_user_id = data.get('suspend_user_id')

        check_user = User_Role_Ref.objects.filter(user_id = suspend_user_id)

        if check_user:
            user_suspend_data = User_Role_Ref.objects.get(user_id = suspend_user_id)
            if user_suspend_data.suspend == True:
                check_user = User_Role_Ref.objects.filter(user_id = suspend_user_id).update(suspend= False)
            if user_suspend_data.suspend == False:
                check_user = User_Role_Ref.objects.filter(user_id = suspend_user_id).update(suspend= True)
            return Response({'result':'Updated Sucessfully'}, status= status.HTTP_200_OK)
        else:
            return Response({'result':'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)



#########################          GET USER DETAILS AND UPDATE USER DETAILS          #########################
class GetUserAndUpdateUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        if len(data) == 1:
            user_id  = data.get('user_id')

            user_data = User.objects.filter(id= user_id).values()
            if user_data:
                user_role_ref_data = User_Role_Ref.objects.get(user_id= user_id)
                role_data = Roles.objects.get(id= user_role_ref_data.role_id)
                for i in user_data:
                    i['role_name'] = role_data.role_name
                    i['mobile_number'] = user_role_ref_data.mobile_number
                    i['suspend'] = user_role_ref_data.suspend
                    i['name']= i['first_name']
                return Response({'result':user_data}, status= status.HTTP_200_OK)
            else:
                return Response({'result':'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)
        if len(data) > 1:

            user_id = data.get('user_id')
            first_name = data.get('name')
            password = data.get('new_password')
            mobile_number = data.get('mobile_number')
            
            print(data)
            print(password)

            user_data = User.objects.filter(id= user_id).values()
            if user_data:
                user_data = User.objects.filter(id= user_id).update(first_name= first_name)

                if password != '':
                    user_password_update = User.objects.get(id= user_id)
                    user_password_update.set_password(password)
                    user_password_update.save()
                

                user_role_ref_data = User_Role_Ref.objects.filter(user_id= user_id).update(mobile_number= mobile_number)


                return Response({'result':'User Updated Sucessfully'}, status= status.HTTP_200_OK)
            else:
                return Response({'result':'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'result': 'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)



#########################          GET ALL PHC USERS LIST MO LOGIN          #########################
class GetMOALLUserDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        get_phcm_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)

        get_phc_user_details = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= get_phcm_user_data.swab_collection_centre_name).values()

        user_details = []

        for i in get_phc_user_details:
            if i['role_id'] != 6:
                user_name = User.objects.get(id= i['user_id'])
                check_role = Roles.objects.get(id= i['role_id'])
                mob_no = User_Role_Ref.objects.get(user_id= i['user_id'])

                res_data = {'id': user_name.id,'username': user_name.username, 'password': user_name.password, 'name': user_name.first_name, 'userrole': check_role.role_name, 'mobile_number': mob_no.mobile_number, 'suspend':mob_no.suspend}
                user_details.append(res_data)


        return Response(user_details)






#########################          GET PHC LOGIN DASHBOARD DETAILS          #########################
class GetPHCDashboardDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id      = data.get('user_id')
        start_date = data.get('from_date')
        end_date = data.get('to_date')

        print(data)

        
        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
            check_user_roles  = Roles.objects.get(id= check_user_data.role_id)
            if check_user_roles.role_name == 'PHCMO':

                # all_phcm_data = []
                # check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                # for i in check_all_slab_collector:
                #     patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(test_type_id = 2) & Q(swab_collection_status= 0) & Q(package_sampling_id__isnull = True)).values()
                #     for pd in patient_details:
                #         patient_type_data =  Patient_Type_Ref.objects.get(id= pd['patient_type_id'])
                #         patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= pd['specimen_type_id'])
                #         patient_test_type_data = Test_Type_Ref.objects.get(id= pd['test_type_id'])
                #         pd['patient_type_name'] = patient_type_data.patient_type_name
                #         pd['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                #         pd['test_type_name']= patient_test_type_data.test_type_name
                #     all_phcm_data.append(patient_details)

                # check_roles  = Roles.objects.get(role_name= 'PHCM')


                if start_date and end_date:

                    start_data_split = start_date.split('-')
                    end_date_split = end_date.split('-')
                    
                    total_samples_collected = 0
                    total_rat_result_published = 0
                    check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                    for i in check_all_slab_collector:
                        
                        patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2])))).values()
                        for pd in patient_details:
                            total_samples_collected += 1
                            if int(pd['test_type_id']) == 1:
                                total_rat_result_published += 1                


                    check_phc_target_data = PHCTargetAssignment.objects.filter(Q(phc_id= check_user_data.phc_master_id) & Q(created_datetime__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(created_datetime__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))))
                    total_target_today = 0
                    if check_phc_target_data:
                        check_phc_target_details = PHCTargetAssignment.objects.filter(Q(phc_id= check_user_data.phc_master_id) & Q(created_datetime__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(created_datetime__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))).values()
                        check_all_count = 0
                        for i in check_phc_target_details:
                            check_all_count += int(i['phc_target'])
                        # total_target_today = check_phc_target_details.phc_target
                        total_target_today = check_all_count

                    today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(assigned_msc_user__isnull= False))
                    today_contact_tracing_ass = 0
                    if today_contact_tracing:
                        today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(assigned_msc_user__isnull= False)).values()
                        cnt_data = 0
                        for i in today_contact_tracing_details:
                            cnt_data += 1
                        # today_contact_tracing_ass = today_contact_tracing_details
                        today_contact_tracing_ass = cnt_data


                    today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(sample_collected= 1))
                    today_total_sam_collected_cnt = 0
                    if today_total_sam_collected:
                        today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(sample_collected= 1)).values()
                        cnt_smp_coll = 0
                        for i in today_sam_collected_details:
                            cnt_smp_coll+= 1
                        # today_total_sam_collected_cnt = today_sam_collected_details
                        today_total_sam_collected_cnt = cnt_smp_coll


                    short_fall = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(assigned_msc_user__isnull= True))
                    short_fall_cnt = 0
                    if short_fall:
                        short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(assigned_date__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(assigned_msc_user__isnull= True)).values()
                        # short_fall_cnt = short_fall_cnt_details

                        cnt_shrt_fall = 0
                        for i in short_fall_cnt_details:
                            cnt_shrt_fall += 1

                        short_fall_cnt = cnt_shrt_fall

                    no_of_mobile_team = check_all_slab_collector = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= check_user_data.swab_collection_centre_name) & Q(role_id= 8)).count()
                    no_of_swab_collector = check_all_slab_collector = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= check_user_data.swab_collection_centre_name) & Q(role_id= 7)).count()

                # total_samples_collected = Patient.objects.filter(swab_collection_id= check_user_data.id).count()
                # total_rat_result_published = Patient.objects.filter(Q(swab_collection_id= check_user_data.id) & Q(test_type_id= 1)).count()

                # return Response({'total_patient_added':patient_count,'patient_symptomatic_count': patient_symptomatic_count,'patient_asymptomatic_count':patient_asymptomatic_count, 'total_samples_collected':patient_count})
                    # return Response({'no_of_mobile_team': no_of_mobile_team,'no_of_swab_collector': no_of_swab_collector,'total_samples_collected':total_samples_collected, 'total_rat_result_published':total_rat_result_published,}, status= status.HTTP_200_OK)
                    
                    print("DDDDDDDDDDDDDDDDDDDDDDDDDDD")
                    print({'no_of_mobile_team': no_of_mobile_team,
                                        'no_of_swab_collector': no_of_swab_collector,
                                        'total_samples_collected':total_samples_collected, 
                                        'total_rat_result_published':total_rat_result_published,
                                        'total_target_tersting_today':total_target_today, 'total_testing_assigned_today': today_contact_tracing_ass,
                                        'total_testing_collected':today_total_sam_collected_cnt, 'short_fall':short_fall_cnt})
                    
                    return Response({'no_of_mobile_team': no_of_mobile_team,
                                        'no_of_swab_collector': no_of_swab_collector,
                                        'total_samples_collected':total_samples_collected, 
                                        'total_rat_result_published':total_rat_result_published,
                                        'total_target_tersting_today':total_target_today, 'total_testing_assigned_today': today_contact_tracing_ass,
                                        'total_testing_collected':today_total_sam_collected_cnt, 'short_fall':short_fall_cnt}, status= status.HTTP_200_OK)

                else:

                    
                    total_samples_collected = 0
                    total_rat_result_published = 0
                    check_all_slab_collector = Swab_Collection_Centre.objects.filter(swab_collection_centre_name= check_user_data.swab_collection_centre_name).values()
                    for i in check_all_slab_collector:
                        
                        patient_details = Patient.objects.filter(Q(added_by=i['user_id']) & Q(create_timestamp__date= asdatetime.now().date())).values()
                        for pd in patient_details:
                            total_samples_collected += 1
                            if int(pd['test_type_id']) == 1:
                                total_rat_result_published += 1



                    check_phc_target_data = PHCTargetAssignment.objects.filter(Q(phc_id= check_user_data.phc_master_id) & Q(created_datetime__date= asdatetime.now().date()))
                    total_target_today = 0
                    if check_phc_target_data:
                        check_phc_target_details = PHCTargetAssignment.objects.get(Q(phc_id= check_user_data.phc_master_id) & Q(created_datetime__date= asdatetime.now().date()))
                        total_target_today = check_phc_target_details.phc_target

                    today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False))
                    today_contact_tracing_ass = 0
                    if today_contact_tracing:
                        today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False)).count()
                        today_contact_tracing_ass = today_contact_tracing_details


                    today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1))
                    today_total_sam_collected_cnt = 0
                    if today_total_sam_collected:
                        today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).count()
                        today_total_sam_collected_cnt = today_sam_collected_details


                    short_fall = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True))
                    short_fall_cnt = 0
                    if short_fall:
                        short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True)).count()
                        short_fall_cnt = short_fall_cnt_details


                    no_of_mobile_team = check_all_slab_collector = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= check_user_data.swab_collection_centre_name) & Q(role_id= 8)).count()
                    no_of_swab_collector = check_all_slab_collector = Swab_Collection_Centre.objects.filter(Q(swab_collection_centre_name= check_user_data.swab_collection_centre_name) & Q(role_id= 7)).count()

                    return Response({'no_of_mobile_team': no_of_mobile_team,
                                        'no_of_swab_collector': no_of_swab_collector,
                                        'total_samples_collected':total_samples_collected, 
                                        'total_rat_result_published':total_rat_result_published,
                                        'total_target_tersting_today':total_target_today, 'total_testing_assigned_today': today_contact_tracing_ass,
                                        'total_testing_collected':today_total_sam_collected_cnt, 'short_fall':short_fall_cnt}, status= status.HTTP_200_OK)

            if check_user_roles.role_name == 'PHCS':

                print("FFFFFFFFFFFFFFFFFFFFFFFFFFFF")
                print(data)

                check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)
                if start_date  and end_date :
                    start_data_split = start_date.split('-')
                    end_date_split = end_date.split('-')
                    patient_count = Patient.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(added_by=user_id)).count()
                    patient_symptomatic_count = Patient.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(added_by=user_id) & Q(patient_status= 'Symptomatic')).count()
                    patient_asymptomatic_count = Patient.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(added_by=user_id) & Q(patient_status= 'Asymptomatic')).count()

                    package_count = Package_Sampling.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(user_id= user_id)).count()

                    return Response({'total_patient_added':patient_count,'patient_symptomatic_count': patient_symptomatic_count,'patient_asymptomatic_count':patient_asymptomatic_count, 'total_samples_collected':patient_count, 'package_count': package_count}, status= status.HTTP_200_OK)

                else:
                    patient_count = Patient.objects.filter(Q(added_by=user_id) & Q(create_timestamp__date= asdatetime.now().date())).count()
                    patient_symptomatic_count = Patient.objects.filter(Q(added_by=user_id) & Q(patient_status= 'Symptomatic') & Q(create_timestamp__date= asdatetime.now().date())).count()
                    patient_asymptomatic_count = Patient.objects.filter(Q(added_by=user_id) & Q(patient_status= 'Asymptomatic') & Q(create_timestamp__date= asdatetime.now().date())).count()

                    package_count = Package_Sampling.objects.filter(Q(user_id= user_id) & Q(create_timestamp__date= asdatetime.now().date())).count()
                # for i in patient_details:
                #     patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                #     patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                #     patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                #     i['patient_type_name'] = patient_type_data.patient_type_name
                #     i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                #     i['test_type_name']= patient_test_type_data.test_type_name

                    return Response({'total_patient_added':patient_count,'patient_symptomatic_count': patient_symptomatic_count,'patient_asymptomatic_count':patient_asymptomatic_count, 'total_samples_collected':patient_count, 'package_count': package_count}, status= status.HTTP_200_OK)

            if check_user_roles.role_name == 'PHCM':

                check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)

                # patient_count = Patient.objects.filter(Q(added_by=user_id)).count()
                # patient_symptomatic_count = Patient.objects.filter(Q(added_by=user_id) & Q(patient_status= 'Symptomatic')).count()
                # patient_asymptomatic_count = Patient.objects.filter(Q(added_by=user_id) & Q(patient_status= 'Asymptomatic')).count()

                # package_count = Package_Sampling.objects.filter(user_id= user_id).count()
                if start_date and end_date :  
                    start_data_split = start_date.split('-')
                    end_date_split = end_date.split('-')
                    contact_testing_pending = Contact_Tracing.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(assigned_msc_user_id= user_id) & Q(sample_collected= 0)).count()
                    ili_count_pending = ILI.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(assigned_msc_user_id= user_id) & Q(sample_collected= 0)).count()
                    target_assigned = TargetAssignToUser.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(user_id= user_id) ).count()
                    total_swab_collected = New_Entry_Contact_Tracing.objects.filter(Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) &Q(user_id= user_id) ).count()

                    return Response({'contact_testing_pending':contact_testing_pending,'ili_count_pending': ili_count_pending,'target_assigned':target_assigned, 'total_swab_collected':total_swab_collected}, status= status.HTTP_200_OK) 

                else:
                    contact_testing_pending = Contact_Tracing.objects.filter(Q(assigned_msc_user_id= user_id) & Q(sample_collected= 0) & Q()).count()
                    ili_count_pending = ILI.objects.filter(Q(assigned_msc_user_id= user_id) & Q(sample_collected= 0)).count()
                    target_assigned = TargetAssignToUser.objects.filter(Q(user_id= user_id) & Q(created_datetime__date= asdatetime.now().date())).count()
                    total_swab_collected = New_Entry_Contact_Tracing.objects.filter(create_timestamp__date = asdatetime.now().date()).count()

                # for i in patient_details:
                #     patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                #     patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                #     patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                #     i['patient_type_name'] = patient_type_data.patient_type_name
                #     i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                #     i['test_type_name']= patient_test_type_data.test_type_name

                    return Response({'contact_testing_pending':contact_testing_pending,'ili_count_pending': ili_count_pending,'target_assigned':target_assigned, 'total_swab_collected':total_swab_collected}, status= status.HTTP_200_OK) 
        
        else:
            return Response({'result': 'successfull'})




#########################          GET THO DSO SSU DASHBOARD DETAILS          #########################
class GetThoDsoSsuDashboardDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        print(data)

        tho_data = THO.objects.filter(user_id= user_id)
        dso_data = DSO.objects.filter(user_id= user_id)
        ssu_data = SSU.objects.filter(user_id= user_id)


        if tho_data:
            from_date = data.get('from_date')
            to_date = data.get('to_date')

            if from_date and to_date:
                tho_data_get = THO.objects.get(user_id= user_id)

                no_of_swab_collector = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(role_id= 6)).count()
                phc_user_ids = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(role_id= 6)).values_list('user_id', flat=True)

                no_of_packages = 0
                no_of_samples = 0
                no_of_lab_allocation_req = 0
                no_of_package_for_dispatch = 0
                no_of_package_dispatch_to_lab = 0

                today_contact_tracing_assigned = 0
                today_total_sam_collected_cnt = 0
                short_fall_cnt = 0
                """

                for i in phc_user_ids:
                    phc_mo_user_data = Swab_Collection_Centre.objects.get(Q(user_id= i) & Q(role_id= 6))
                    phc_all_user_ids = list(Swab_Collection_Centre.objects.filter(Q(phc_master_id= phc_mo_user_data.phc_master_id)).values_list('user_id'))
                    no_of_packages += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                    no_of_samples += Patient.objects.filter(Q(added_by_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                    no_of_lab_allocation_req += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(package_type_status= 9) | Q(package_type_status= 10)).count()
                    no_of_package_for_dispatch += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(package_type_status= 1)).count()
                    no_of_package_dispatch_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(package_type_status= 2) & (Q(package_type_action= 12) | Q(package_type_status= 5)) & Q(package_type_action= 15)).count()

                    today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False))
                    if today_contact_tracing:
                        today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False)).values()
                        cnt_data = 0
                        for i in today_contact_tracing_details:
                            cnt_data += 1
                        today_contact_tracing_assigned += cnt_data


                    today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(sample_collected= 1))
                    if today_total_sam_collected:
                        today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(sample_collected= 1)).values()
                        cnt_smp_coll = 0
                        for i in today_sam_collected_details:
                            cnt_smp_coll+= 1
                        # today_total_sam_collected_cnt = today_sam_collected_details
                        today_total_sam_collected_cnt += cnt_smp_coll


                    short_fall = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= True))
                    if short_fall:
                        short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= True)).values()
                        # short_fall_cnt = short_fall_cnt_details

                        cnt_shrt_fall = 0
                        for i in short_fall_cnt_details:
                            cnt_shrt_fall += 1

                        short_fall_cnt += cnt_shrt_fall
                
                """



                # for i in phc_user_ids:
                phc_mo_user_data = Swab_Collection_Centre.objects.filter(Q(user_id__in= phc_user_ids) & Q(role_id= 6)).values_list('phc_master_id', flat=True)
                phc_all_user_ids = Swab_Collection_Centre.objects.filter(Q(phc_master_id__in= phc_mo_user_data)).values_list('user_id', flat=True)
                
                no_of_packages += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                no_of_samples += Patient.objects.filter(Q(added_by_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                no_of_lab_allocation_req += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(package_type_status= 9) | Q(package_type_status= 10)).count()
                no_of_package_for_dispatch += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(package_type_status= 1)).count()
                
                # no_of_package_dispatch_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & (Q(package_type_status= 2) & Q(package_type_action= 12)) | (Q(package_type_status= 5) & Q(package_type_action= 15))).count()
                no_of_package_dispatch_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).filter((Q(package_type_status= 2) & Q(package_type_action= 12)) | (Q(package_type_status= 5) & Q(package_type_action= 15))).filter(lab_master__isnull= False).count()

                # today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False))
                # if today_contact_tracing:
                #     today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False)).values()
                #     cnt_data = 0
                #     for i in today_contact_tracing_details:
                #         cnt_data += 1
                #     today_contact_tracing_assigned += cnt_data
                

                today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False))
                today_contact_tracing_assigned += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False)).count()
                # if today_contact_tracing:
                #     today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= False)).values()
                #     cnt_data = 0
                #     for i in today_contact_tracing_details:
                #         cnt_data += 1
                #     today_contact_tracing_assigned += cnt_data


                today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(sample_collected= 1))
                today_total_sam_collected_cnt += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(sample_collected= 1)).count()
                # if today_total_sam_collected:
                #     today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(sample_collected= 1)).values()
                #     cnt_smp_coll = 0
                #     for i in today_sam_collected_details:
                #         cnt_smp_coll+= 1
                #     # today_total_sam_collected_cnt = today_sam_collected_details
                #     today_total_sam_collected_cnt += cnt_smp_coll


                short_fall = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= True))
                short_fall_cnt += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= True)).count()
                # if short_fall:
                #     short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(assigned_date__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d')) & Q(assigned_msc_user__isnull= True)).values()
                #     # short_fall_cnt = short_fall_cnt_details

                #     cnt_shrt_fall = 0
                #     for i in short_fall_cnt_details:
                #         cnt_shrt_fall += 1

                #     short_fall_cnt += cnt_shrt_fall




                # swab_collectios_details = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(role_id= 6)).values()
                # if swab_collectios_details:
                #     for i in swab_collectios_details:
                #         print(i)
                #         # phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id'))
                #         # print("FFFFFFFFFFFFF",phc_swab_collection_team)
                #         # for j in phc_swab_collection_team:
                #         #     ss= Patient.objects.filter(Q(added_by_id= j['user_id']) & Q(create_timestamp__date= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                #         #     print(ss)
                #         #     no_of_samples += Patient.objects.filter(Q(added_by_id= j['user_id']) & Q(create_timestamp__date= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                #         phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id'))
                      
                #         ss= Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                #         print(ss)
                #         no_of_samples += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                return Response({'no_of_swab_collector':no_of_swab_collector, 'no_of_packages':no_of_packages, 'no_of_samples':no_of_samples, 'no_of_lab_allocation_request':no_of_lab_allocation_req, 'no_of_packages_for_dispatch':no_of_package_for_dispatch, 'no_of_packages_dispatched_to_lab':no_of_package_dispatch_to_lab, 'today_contact_tracing_assigned':today_contact_tracing_assigned, 'today_total_sam_collected_cnt':today_total_sam_collected_cnt, 'short_fall_cnt':short_fall_cnt},status= status.HTTP_200_OK)

            else:

                tho_data_get = THO.objects.get(user_id= user_id)

                no_of_swab_collector = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(role_id= 6)).count()
                
                phc_user_ids = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data_get.id) & Q(role_id= 6)).values_list('user_id', flat=True)

                no_of_packages = 0
                no_of_samples = 0
                no_of_lab_allocation_req = 0
                no_of_package_for_dispatch = 0
                no_of_package_dispatch_to_lab = 0

                today_contact_tracing_assigned = 0
                today_total_sam_collected_cnt = 0 
                short_fall_cnt = 0

                # for i in phc_user_ids:
                #     phc_mo_user_data = Swab_Collection_Centre.objects.get(Q(user_id= i) & Q(role_id= 6))
                #     phc_all_user_ids = list(Swab_Collection_Centre.objects.filter(Q(phc_master_id= phc_mo_user_data.phc_master_id)).values_list('user_id'))
                #     no_of_packages += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date())).count()

                #     no_of_samples += Patient.objects.filter(Q(added_by_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date())).count()

                #     no_of_lab_allocation_req += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date()) & Q(package_type_status= 9) | Q(package_type_status= 10)).count()
                #     no_of_package_for_dispatch += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date()) & Q(package_type_status= 1)).count()
                #     no_of_package_dispatch_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date()) & Q(package_type_status= 2) & Q(package_type_action= 12) | Q(package_type_status= 5) & Q(package_type_action= 15)).count()
                
                
                #     today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False))
                #     if today_contact_tracing:
                #         today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False)).values()
                #         cnt_data = 0
                #         for i in today_contact_tracing_details:
                #             cnt_data += 1
                #         today_contact_tracing_assigned += cnt_data


                #     today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1))
                #     if today_total_sam_collected:
                #         today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).values()
                #         cnt_smp_coll = 0
                #         for i in today_sam_collected_details:
                #             cnt_smp_coll+= 1
                #         today_total_sam_collected_cnt += cnt_smp_coll


                #     short_fall = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True))
                #     if short_fall:
                #         short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True)).values()
                #         cnt_shrt_fall = 0
                #         for i in short_fall_cnt_details:
                #             cnt_shrt_fall += 1
                #         short_fall_cnt += cnt_shrt_fall


                phc_mo_user_data = Swab_Collection_Centre.objects.filter(Q(user_id__in= phc_user_ids) & Q(role_id= 6)).values_list('phc_master_id', flat=True)
                phc_all_user_ids = list(Swab_Collection_Centre.objects.filter(Q(phc_master_id__in= phc_mo_user_data)).values_list('user_id'))
                no_of_packages += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date())).count()

                no_of_samples += Patient.objects.filter(Q(added_by_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date())).count()

                no_of_lab_allocation_req += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date()) & Q(package_type_status= 9) | Q(package_type_status= 10)).count()
                no_of_package_for_dispatch += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date()) & Q(package_type_status= 1)).count()
                no_of_package_dispatch_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_all_user_ids) & Q(create_timestamp__date= asdatetime.now().date())).filter((Q(package_type_status= 2) & Q(package_type_action= 12)) | (Q(package_type_status= 5) & Q(package_type_action= 15))).filter(lab_master__isnull= False).count()
            
            
                today_contact_tracing = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False))
                today_contact_tracing_assigned += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False)).count()
                # if today_contact_tracing:
                #     today_contact_tracing_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= False)).values()
                #     cnt_data = 0
                #     for i in today_contact_tracing_details:
                #         cnt_data += 1
                #     today_contact_tracing_assigned += cnt_data


                today_total_sam_collected = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1))
                today_total_sam_collected_cnt += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).count()
                # if today_total_sam_collected:
                #     today_sam_collected_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).values()
                #     cnt_smp_coll = 0
                #     for i in today_sam_collected_details:
                #         cnt_smp_coll+= 1
                #     today_total_sam_collected_cnt += cnt_smp_coll


                short_fall = Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True))
                short_fall_cnt += Contact_Tracing.objects.filter(Q(assigned_phc__in= phc_mo_user_data) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True)).count()
                # if short_fall:
                #     short_fall_cnt_details = Contact_Tracing.objects.filter(Q(assigned_phc= phc_mo_user_data.phc_master_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(assigned_msc_user__isnull= True)).values()
                #     cnt_shrt_fall = 0
                #     for i in short_fall_cnt_details:
                #         cnt_shrt_fall += 1
                #     short_fall_cnt += cnt_shrt_fall
            
                return Response({'no_of_swab_collector':no_of_swab_collector, 'no_of_packages':no_of_packages, 'no_of_samples':no_of_samples, 'no_of_lab_allocation_request':no_of_lab_allocation_req, 'no_of_packages_for_dispatch':no_of_package_for_dispatch, 'no_of_packages_dispatched_to_lab':no_of_package_dispatch_to_lab, 'today_contact_tracing_assigned':today_contact_tracing_assigned, 'today_total_sam_collected_cnt':today_total_sam_collected_cnt, 'short_fall_cnt':short_fall_cnt},status= status.HTTP_200_OK)


        if dso_data:

            from_date = data.get('from_date')
            to_date = data.get('to_date')

            if from_date and to_date:
                
                dso_data_get = DSO.objects.get(user_id= user_id)

                tho_data_get = THO.objects.filter(dso_id= dso_data_get.id).values_list('id', flat= True)

                no_of_swab_collector_team = 0
                total_samples_collected = 0
                rat_result_published = 0
                packeges_dispatched_to_lab = 0
                request_for_lab_allocation = 0

                """
                for th in tho_data_get:
                    no_of_swab_collector_team += Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).count()

                    swab_collectios_details = Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).values()
                    if swab_collectios_details:
                        for i in swab_collectios_details:
                            phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True))
                            # for j in phc_swab_collection_team:
                            #     total_samples_collected += Patient.objects.filter(added_by_id__in= j['user_id']).count()
                            #     rat_result_published += Patient.objects.filter(Q(added_by_id__in= j['user_id']) & Q(test_type_id= 1)).count()

                            #     packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= j['user_id']) & Q(test_lab__isnull= False)).count()

                            #     request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= user_id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0)).count()
                           
                            total_samples_collected += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                            rat_result_published += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(test_type_id= 1) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                            packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_swab_collection_team) & Q(test_lab__isnull= False) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                            
                            request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= dso_data_get.id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                """
                
                no_of_swab_collector_team += Swab_Collection_Centre.objects.filter(Q(tho_id__in= tho_data_get) & Q(role_id= 6)).count()


                # phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id__in= tho_data_get) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True))

                phc_swab_collection_team = Swab_Collection_Centre.objects.filter(Q(tho_id__in= tho_data_get)).values_list('user_id', flat=True)
               
                total_samples_collected += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                rat_result_published += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(test_type_id= 1) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_swab_collection_team) & Q(test_lab__isnull= False) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                
                request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= dso_data_get.id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()


                # for th in tho_data_get:
                #     no_of_swab_collector_team += Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).count()

                #     swab_collectios_details = Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).values()
                #     if swab_collectios_details:
                #         for i in swab_collectios_details:
                #             phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True))
                #             # for j in phc_swab_collection_team:
                #             #     total_samples_collected += Patient.objects.filter(added_by_id__in= j['user_id']).count()
                #             #     rat_result_published += Patient.objects.filter(Q(added_by_id__in= j['user_id']) & Q(test_type_id= 1)).count()

                #             #     packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= j['user_id']) & Q(test_lab__isnull= False)).count()

                #             #     request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= user_id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0)).count()
                           
                #             total_samples_collected += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                #             rat_result_published += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(test_type_id= 1) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                #             packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_swab_collection_team) & Q(test_lab__isnull= False) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                            
                #             request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= dso_data_get.id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()


            else:

                dso_data_get = DSO.objects.get(user_id= user_id)

                tho_data_get = THO.objects.filter(dso_id= dso_data_get.id).values_list('id', flat=True)

                no_of_swab_collector_team = 0
                total_samples_collected = 0
                rat_result_published = 0
                packeges_dispatched_to_lab = 0
                request_for_lab_allocation = 0

                """
                for th in tho_data_get:
                    no_of_swab_collector_team += Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).count()

                    swab_collectios_details = Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(role_id= 6)).values()
                    if swab_collectios_details:
                        for i in swab_collectios_details:
                            # phc_swab_collection_team = Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(phc_master_id= i['phc_master_id'])).values()
                            # for j in phc_swab_collection_team:

                            #     total_samples_collected += Patient.objects.filter(added_by_id= j['user_id']).count()
                            #     rat_result_published += Patient.objects.filter(Q(added_by_id= j['user_id']) & Q(test_type_id= 1)).count()

                            #     packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id= j['user_id']) & Q(test_lab__isnull= False)).count()

                            #     request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= user_id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0)).count()

                            phc_swab_collection_team = list(Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True))

                            total_samples_collected += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date= asdatetime.now().date())).count()
                            rat_result_published += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(test_type_id= 1) & Q(create_timestamp__date=asdatetime.now().date())).count()
                            packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_swab_collection_team) & Q(test_lab__isnull= False) & Q(create_timestamp__date=asdatetime.now().date())).count()
                            request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= dso_data_get.id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0) & Q(create_timestamp__date=asdatetime.now().date())).count()
                """

                no_of_swab_collector_team += Swab_Collection_Centre.objects.filter(Q(tho_id__in= tho_data_get) & Q(role_id= 6)).count()

                # phc_swab_collection_team = Swab_Collection_Centre.objects.filter(Q(tho_id= th['id']) & Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True))
                phc_swab_collection_team = Swab_Collection_Centre.objects.filter(Q(tho_id__in= tho_data_get)).values_list('user_id', flat=True)

                total_samples_collected += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(create_timestamp__date= asdatetime.now().date())).count()
                rat_result_published += Patient.objects.filter(Q(added_by_id__in= phc_swab_collection_team) & Q(test_type_id= 1) & Q(create_timestamp__date=asdatetime.now().date())).count()
                packeges_dispatched_to_lab += Package_Sampling.objects.filter(Q(user_id__in= phc_swab_collection_team) & Q(test_lab__isnull= False) & Q(create_timestamp__date=asdatetime.now().date())).count()
                request_for_lab_allocation += Package_Sampling.objects.filter(Q(dso_id= dso_data_get.id) & Q(test_lab__isnull= True) & ~Q(reference_tlab = 0) & Q(create_timestamp__date=asdatetime.now().date())).count()

            return Response({'no_of_swab_collector_team':no_of_swab_collector_team, 'total_samples_collected':total_samples_collected, 'rat_result_published':rat_result_published, 'packeges_dispatched_to_lab':packeges_dispatched_to_lab, 'request_for_lab_allocation':request_for_lab_allocation},status= status.HTTP_200_OK)


        if ssu_data:
            ssu_data_get = SSU.objects.get(user_id= user_id)

            no_of_lab_requests = 0

            from_date = data.get('from_date')
            to_date = data.get('to_date')

            print(from_date)
            print(to_date)

            if from_date and to_date:

                no_of_samples_collected = Patient.objects.filter(Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                print(no_of_samples_collected)
                no_of_packages_at_lab = Package_Sampling.objects.filter(Q(package_type_status= 5) & Q(package_type_action= 15)).count()

                return Response({'no_of_lab_requests':no_of_lab_requests, 'no_of_samples_collected':no_of_samples_collected, 'no_of_packages_at_lab':no_of_packages_at_lab},status= status.HTTP_200_OK)

            else:

                no_of_samples_collected = Patient.objects.filter(create_timestamp__date= asdatetime.now().date()).count()

                no_of_packages_at_lab = Package_Sampling.objects.filter(Q(package_type_status= 5) & Q(package_type_action= 15)).count()

                return Response({'no_of_lab_requests':no_of_lab_requests, 'no_of_samples_collected':no_of_samples_collected, 'no_of_packages_at_lab':no_of_packages_at_lab},status= status.HTTP_200_OK)
            

        else:
            return Response({'message':'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)




#########################          GET TLAB TLAB OPS DASHBOARD DETAILS          #########################
class GetTlabTlapOPSDashboardDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data

        print(data)

        user_id = data.get('user_id')

        check_user = User_Role_Ref.objects.filter(user_id= user_id)

        if check_user:
            check_user_get = User_Role_Ref.objects.get(user_id= user_id)
            get_user_lab = Testing_Lab_Facility.objects.get(user_id= user_id)

            if check_user_get.role.role_name == 'TLAB':
                # get_user_lab = Testing_Lab_Facility.objects.get(user_id= user_id)

                from_date = data.get('from_date')
                to_date = data.get('to_date')

                if from_date and to_date:
                    resp_data = {}
                    resp_data['no_of_packages_arrived'] = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & (Q(package_type_status= 8) | Q(package_type_action= 18)) & Q(lab_received_datetime__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(lab_received_datetime__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                    resp_data['no_of_packages_received'] = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & (Q(package_type_status= 5) | Q(package_type_action= 15)) & Q(lab_received_datetime__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(lab_received_datetime__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()

                    return Response({'result': resp_data, 'message':'Sucess'}, status= status.HTTP_200_OK)

                else:
                    resp_data = {}
                    resp_data['no_of_packages_arrived'] = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & (Q(package_type_status= 8) | Q(package_type_action= 18)) & Q(lab_received_datetime__date= asdatetime.now().date())).count()
                    resp_data['no_of_packages_received'] = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & (Q(package_type_status= 5) | Q(package_type_action= 15)) & Q(lab_received_datetime__date= asdatetime.now().date())).count()
                
                    return Response({'result': resp_data, 'message':'Sucess'}, status= status.HTTP_200_OK)

            if check_user_get.role.role_name == 'LABOP':
                from_date = data.get('from_date')
                to_date = data.get('to_date')

                if from_date and to_date:

                    samples_received_total_count = Package_Sampling.objects.filter(Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(lab_received_datetime__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(lab_received_datetime__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).aggregate(total_samples= Sum('samples_count'))
                    print(samples_received_total_count)
                    if samples_received_total_count['total_samples']:
                        pass
                    else:
                        samples_received_total_count['total_samples'] = 0

                    individual_testing = Package_Sampling.objects.filter(Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(lab_received_datetime__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(lab_received_datetime__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).values_list('id', flat=True)
                    
                    check_patients = Patient.objects.filter(Q(package_sampling_id__in= individual_testing) & Q(lab_accepted_datetime__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(lab_accepted_datetime__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).values()
                    
                    individual_testing_under_testing = 0
                    pool_testing_under_testing = 0
                    result_not_declared = 0
                    result_declared = 0
                    total_c_positive = 0
                    total_inconclusive = 0
                    total_rejected_samples = 0 
                    for i in check_patients:

                        result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                        if i['group_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            individual_testing_under_testing += 1

                        # if i['group_samples'] == '1' and i['group_samples_result'] == '1':
                        #     result_declared += 1
                        # else:
                        #     result_not_declared += 1


                        if i['pool_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            pool_testing_under_testing += 1


                        # if i['pool_samples'] == '1' and i['pool_samples_result'] == '1':
                        #     result_declared += 1
                        # else:
                        #     result_not_declared += 1

                        # result_declared += Patient_Testing.objects.filter(patient_id= i['id']).count()
                        total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                        total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                        total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(samples_rejected= 1)).count()
                    
                    return Response({'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})

                else:
                    samples_received_total_count = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(lab_received_datetime__date= asdatetime.now().date())).aggregate(total_samples= Sum('samples_count'))
                    
                    if samples_received_total_count['total_samples']:
                        pass
                    else:
                        samples_received_total_count['total_samples'] = 0

                    individual_testing = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(lab_received_datetime__date= asdatetime.now().date())).values_list('id', flat=True)
                    check_patients = Patient.objects.filter(package_sampling_id__in= individual_testing).values()
                    individual_testing_under_testing = 0
                    pool_testing_under_testing = 0
                    result_not_declared = 0
                    result_declared = 0
                    total_c_positive = 0
                    total_inconclusive = 0
                    total_rejected_samples = 0
                    for i in check_patients:
                        # if i['group_samples'] == 1 and i['group_samples_result'] == 0:
                        #     individual_testing_under_testing += 1

                        # if i['group_samples'] == 1 and i['group_samples_result'] == 1:
                        #     result_declared += 1
                        # else:
                        #     result_not_declared += 1


                        # if i['pool_samples'] == 1 and i['pool_samples_result'] == 0:
                        #     pool_testing_under_testing += 1

                        # if i['pool_samples'] == 1 and i['pool_samples_result'] == 1:
                        #     result_declared += 1
                        # else:
                        #     result_not_declared += 1

                        result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                        if i['group_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            individual_testing_under_testing += 1

                        if i['pool_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            pool_testing_under_testing += 1
                        
                        total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                        total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                        total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(samples_rejected= 1)).count()

                        
                        
                    
                    # return Response({'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':result_not_declared, 'result_declared':result_declared})
                    return Response({'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})
            else:
                return Response({'result':[], 'message':'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)
        else:   
            return Response({'result':[], 'message':'Something Went Wong'}, status= status.HTTP_400_BAD_REQUEST)



#########################          GET TLAB TLAB OPS DASHBOARD MO THO DSO DETAILS          #########################
class LabOpsDashboardGetThoDsoPhcData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        # selected_type = data.get('type')
        check_testing_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id).values_list('testing_lab_master_id', flat=True)
        if check_testing_lab_user:
            check_packegs = list(set(Package_Sampling.objects.filter(lab_master_id= check_testing_lab_user[0]).values_list('user_id', flat=True)))
            
            dso_details = [] 
            tho_details = []
            tho_data_alrdy_present = []
            mo_details = []

            for i in check_packegs:
                check_swb_col_user = Swab_Collection_Centre.objects.filter(user_id= i).values_list('phc_master_id', flat=True)
                check_lab_user = Testing_Lab_Facility.objects.filter(user_id= i)


                
                if check_swb_col_user:
                    check_master_phc = Master_PHC.objects.get(id= check_swb_col_user[0])

                    # check_dso_data_present = [True for elem in dso_details if check_master_phc.district_code not in elem.values()]
                    check_dso_data_present = any(check_master_phc.district_code in ele.values() for ele in dso_details)

                    if not check_dso_data_present:
                        check_master_dist_data = list(Master_District.objects.filter(district_code= check_master_phc.district_code).values('district_code', 'district_name_eng'))
                        dso_details.append({'code':check_master_dist_data[0]['district_code'], 'name':check_master_dist_data[0]['district_name_eng']})
                    

                    # check_tho_data_present = [True for elem in tho_details if check_master_phc.block_code in elem.values()]
                    # check_tho_data_present = any(str(check_master_phc.block_code) in ele.values() for ele in tho_details)
                    # if not check_tho_data_present:

                    if check_master_phc.block_code not in [str(block_id['code']) for block_id in tho_details]:
                        check_master_block_data = list(Master_Block.objects.filter(block_code= check_master_phc.block_code).values('block_code', 'block_name_eng'))
                        tho_details.append({'code':check_master_block_data[0]['block_code'], 'name':check_master_block_data[0]['block_name_eng']})
                    

                    # check_mo_data_present = [True for elem in mo_details if check_master_phc.phc_code in elem.values()]
                    check_mo_data_present = any(check_master_phc.phc_code in ele.values() for ele in mo_details)
                    if not check_mo_data_present:
                        mo_details.append({'code':check_master_phc.phc_code, 'name':check_master_phc.phc_name})

                    
                elif check_lab_user:
                    pass


            return Response({'dso_details': dso_details, 'tho_details': tho_details, 'mo_details': mo_details}, status= status.HTTP_200_OK)

        else:
            return Response({'result':'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)



#########################          GET TLAB TLAB OPS DASHBOARD MO THO DSO DETAILS          #########################
class LabOpsDashboardGetSelectedTypeDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        selected_code = data.get('selected_code')
        selected_type = data.get('selected_type')

        check_testing_lab_user = Testing_Lab_Facility.objects.filter(user_id= user_id).values_list('testing_lab_master_id', flat=True)

        if check_testing_lab_user:

            master_phc_data = Master_PHC.objects.none()


            if selected_type == 'DSO':
                master_phc_data = Master_PHC.objects.filter(district_code= selected_code).values_list('id', flat=True)
            elif selected_type == 'THO':
                master_phc_data = Master_PHC.objects.filter(block_code= selected_code).values_list('id', flat=True)
            elif selected_type == 'MO':
                master_phc_data = Master_PHC.objects.filter(phc_code= selected_code).values_list('id', flat=True)

            phc_users = Swab_Collection_Centre.objects.filter(phc_master_id__in= master_phc_data).values_list('user_id', flat=True)

            check_packegs = Package_Sampling.objects.filter(Q(lab_master_id= check_testing_lab_user[0]) & Q(user_id__in= phc_users)).values_list('id', flat=True)
            

            # individual_testing = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id)).values_list('id', flat=True)
            
            check_patients = Patient.objects.filter(package_sampling_id__in= check_packegs).values()

            # samples_received_total_count = Package_Sampling.objects.filter(Q(test_lab_id=get_user_lab.id) & Q(lab_master_id= get_user_lab.testing_lab_master_id) & Q(lab_received_datetime__date= asdatetime.now().date())).aggregate(total_samples= Sum('samples_count'))
            samples_received_total_count = Package_Sampling.objects.filter(Q(lab_master_id= check_testing_lab_user[0]) & Q(user_id__in= phc_users)).aggregate(total_samples= Sum('samples_count'))
                    
            if samples_received_total_count['total_samples']:
                pass
            else:
                samples_received_total_count['total_samples'] = 0

            individual_testing_under_testing = 0
            pool_testing_under_testing = 0
            result_not_declared = 0
            result_declared = 0
            total_c_positive = 0
            total_inconclusive = 0
            total_rejected_samples = 0
            for i in check_patients:
                result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                if i['group_samples'] == 1 and result_declared_check:
                    result_declared += 1
                else:
                    individual_testing_under_testing += 1

                if i['pool_samples'] == 1 and result_declared_check:
                    result_declared += 1
                else:
                    pool_testing_under_testing += 1
                
                total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= check_testing_lab_user[0]) & Q(samples_rejected= 1)).count()

            return Response({'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})

        else:
            return Response({'result':'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)




#########################          GET ACTIVATED PHC TEST KITS DETAILS          #########################
class GetAvailableMOTestKits(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        user_id  = data.get('user_id')

        get_swab_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        swab_collected = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id=get_swab_detail.phc_master_id) & Q(active= 1))

        if swab_collected:
            swab_collected_data = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id=get_swab_detail.phc_master_id) & Q(active= 1)).values()
            for i in swab_collected_data:
                test_kit_data = Testing_Kit_Barcode.objects.get(id= i['test_kit_id'])
                i['test_kit_name']= test_kit_data.testing_kit_barcode_name

            return Response({'result':swab_collected_data, 'kit_available':True,'message':'Sucessfull'},status= status.HTTP_200_OK) 
        else:
            
            test_kit_barcode = Testing_Kit_Barcode.objects.filter(active=1).values()
            return Response({'result':test_kit_barcode, 'kit_available':False,'message':'Sucessfull'},status= status.HTTP_200_OK) 


        # test_kit_ids = []
        # for i in swab_collected:
        #     if i.capacity > 0:
        #         test_kit_ids.append(i.test_kit_id)
        #     elif(i.capacity == 0):
        #         swab_collected_delete = Phc_Id_Test_Kit_Id.objects.filter(Q(id__in= test_kit_ids) & Q(phc_id=get_swab_detail.phc_master_id) & Q(active= 1)).delete()

        # get_test_kit_details = Testing_Kit_Barcode.objects.filter(Q(id__in= test_kit_ids) & Q(active=1)).values()



        # class TestingKitBarcode(APIView):
        #     def get(self, request):
        #         test_kit_barcode = Testing_Kit_Barcode.objects.filter(active=1).values()
        #         return Response({'result': test_kit_barcode,'message':'Sucessfull'})

        # get_test_kit_details = Testing_Kit_Barcode.objects.filter(Q(id__in= test_kit_ids)).values()
        # return Response({'result': get_test_kit_details, 'message':'Sucessfully'})



#########################          GET ASSIGNED PHC MSC USER TEST KITS DETAILS          #########################
class GetAvailableMSCTestKits(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data

        user_id  = data.get('user_id')

        get_swab_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        mobile_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= get_swab_detail.phc_master_id) & Q(role__role_name= 'PHCM')).values()

        response_list = []
        for i in mobile_swab_collector:
            res={}
            res['user_name'] = User.objects.get(id= i['user_id']).first_name
            res['msc_user_id'] = i['user_id']
            total_test_kit_assigned = Phc_MSC_Id_Test_Kit_Id.objects.filter(user_id= i['user_id']).aggregate(total_capacity= Sum('capacity'))
            if total_test_kit_assigned['total_capacity']:
                res['capacity'] = total_test_kit_assigned['total_capacity']
            else:
                res['capacity'] =  0

            response_list.append(res)

        return Response({'result':response_list,}, status= status.HTTP_200_OK)



#########################          GET ASSIGNED PHC MSC USER TEST KITS DETAILS          #########################
class AssignMSCUserTestKits(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        
        user_id  = data.get('user_id')
        msc_user_id = data.get('selected_user')
        test_kit_id  = data.get('test_kit_id')
        capacity  = data.get('capacity')

        get_swab_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        Phc_MSC_Id_Test_Kit_Id.objects.create(user_id= msc_user_id, phc_id= get_swab_detail.phc_master_id, test_kit_id= test_kit_id, capacity= capacity)
       
        return Response({'result': 'Test kit Assigned Sucessfully',}, status= status.HTTP_200_OK)



#########################          GET TESTING KIT DETAILS          #########################
class GetTestingKitDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        user_id  = data.get('user_id')

        get_swab_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        swab_collected = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id=get_swab_detail.phc_master_id) & Q(active= 1))

        test_kit_ids = []
        for i in swab_collected:
            if i.capacity > 0:
                test_kit_ids.append(i.test_kit_id)
            elif(i.capacity == 0):
                swab_collected_delete = Phc_Id_Test_Kit_Id.objects.filter(Q(id__in= test_kit_ids) & Q(phc_id=get_swab_detail.phc_master_id) & Q(active= 1)).delete()

        get_test_kit_details = Testing_Kit_Barcode.objects.filter(Q(id__in= test_kit_ids) & Q(active=1)).values()

        # get_test_kit_details = Testing_Kit_Barcode.objects.filter(Q(id__in= test_kit_ids)).values()
        return Response({'result': get_test_kit_details, 'message':'Sucessfully'})




#########################          GET ASSIGNED CONTACT TRACING DETAILS          #########################
class MSCAssignedData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)

        user_id = data.get('user_id')

        contact_tracing = Contact_Tracing.objects.filter(Q(assigned_msc_user_id= user_id) & Q(sample_collected= 0)).values()

        return Response(contact_tracing)




#########################          GET ASSIGNED COMPLETED PENDING MSC COUNT          #########################
class GetAssignedCompletedPendingMscCounts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user_id = data.get('user_id')

        print(data)

        total_assigned = Contact_Tracing.objects.filter(Q(assigned_msc_user_id= user_id) & Q(assigned_date__date= asdatetime.now().date())).count()
        completed = Contact_Tracing.objects.filter(Q(assigned_msc_user_id= user_id) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).count()

        pending = total_assigned - completed

        print({'total_assigned': total_assigned, 'completed': completed, 'pending': pending})

        return Response({'total_assigned': total_assigned, 'completed': completed, 'pending': pending}, status= status.HTTP_200_OK)



#########################          SAVE CONTACT TRACING          #########################
class SaveContactTracing(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass



#########################          Accept Package          #########################
class AcceptPackage(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        package_id      = data.get('package_id')
        user_id         = data.get('user_id')

        last_package_data = Package_Sampling.objects.filter(id= package_id).update(package_type_status= 7, package_type_action=17)
        return Response({'result': 'Updated Sucessfully'}, status= status.HTTP_200_OK)




#########################          GET CONTACTEE PATIENT DETAILS          #########################
class GetContacteePatientDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        id = data.get('id')

        contactee_details = Contact_Tracing.objects.filter(id= id).values()

        for i in contactee_details:
            dist_data = Master_District.objects.filter(district_code= i['district'])
            if dist_data:
                dist_data_get = Master_District.objects.filter(district_code= i['district']).values()
                i['district_details'] = dist_data_get
                # i['district_details'] = dist_data
            else:
                i['district_details'] = []


            ward_data = Master_Ward.objects.filter(Q(district_code= i['district']) & Q(new_town_code= i['town']) & Q(ward_no= i['ward']))
            if ward_data:
                ward_data_get = Master_Ward.objects.filter(Q(district_code= i['district']) & Q(new_town_code= i['town']) & Q(ward_no= i['ward'])).values()
                i['ward_details'] = ward_data_get
            else:
                i['ward_details'] = []
                #i['ward_details'] = ward_data


            village_data = Master_Village.objects.filter(Q(district_code= i['district']) & Q(block_code= i['taluk']) & Q(panchayat_code= i['panchayat']) & Q(village_code= i['village'])).values()
            if village_data:
                for j in village_data:
                    block_data_get = Master_Block.objects.get(block_code=j['block_code'])
                    i['block_name_eng'] = block_data_get.block_name_eng
                    panchayat_data_get = Master_Panchayat.objects.get(panchayat_code=j['panchayat_code'])
                    i['panchayat_name_eng'] = panchayat_data_get.panchayat_name_eng
                    district_data_get = Master_District.objects.get(district_code=j['district_code'])
                    i['district_name_eng'] = district_data_get.district_name_eng

                i['location_detail'] =  village_data
            else:
                i['location_detail'] = []
                

            
        print(contactee_details)
        return Response(contactee_details)



#########################          CREATE DYNAMIC PHC USERNAME          #########################
class CreatePHCUserNames(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        dist_code = data.get('dist_code')

        dist_filter = Master_PHC.objects.filter(district_code= dist_code).values('district_code', 'district_name_eng').distinct()

        data = []
    
        for i in dist_filter:
            data = {}
            print("New DSO Login")
            print("DSO USERNAME : ", str((i['district_name_eng'].lower()).strip()).replace(' ', '.')+'_dso')
            print("DSO Password : ", str((i['district_name_eng'].lower()).strip()).replace(' ', '')+'@123')

            data['dso_username'] = str((i['district_name_eng'].lower()).strip()).replace(' ', '.')+'_dso'
            data['dso_password'] = str((i['district_name_eng'].lower()).strip()).replace(' ', '')+'@123'
            data['tho_logins'] = []
            data['phc_logins'] = []

            check_master_dist = Master_District.objects.get(district_code= i['district_code'])

            create_dso_user = User.objects.create_user(username= str((i['district_name_eng'].lower()).strip()).replace(' ', '.')+'_dso', password= str((i['district_name_eng'].lower()).strip()).replace(' ', '')+'@123')
            create_dso_user_ref = User_Role_Ref.objects.create(user_id= create_dso_user.id, role_id= 2, user_role_name= 'DSO', user_role_desc='DSO')
            create_dso_details = DSO.objects.create(user_id= create_dso_user.id, role_id= 2, dso_name= str((i['district_name_eng'].lower()).strip()).replace(' ', '.')+' dso', district_id= check_master_dist.id)

            if i['district_code']:

                taluk_data = Master_PHC.objects.filter(district_code= dist_code).values('block_name_eng', 'block_code').distinct()

                for j in taluk_data:
                    print("New THO Login")
                    print("THO USERNAME : ", str((j['block_name_eng'].lower()).strip()).replace(' ', '.')+'_tho')
                    print("THO Password : ", str((j['block_name_eng'].lower()).strip()).replace(' ', '')+'@123')

                    data['tho_logins'].append({'tho_username': str((j['block_name_eng'].lower()).strip()).replace(' ', '.')+'_tho', 'tho_password': str((j['block_name_eng'].lower()).strip()).replace(' ', '')+'@123'})
                    
                    check_master_taluk = Master_Block.objects.get(Q(district_code= i['district_code']) & Q(block_code= j['block_code']))

                    create_tho_user = User.objects.create_user(username= str((j['block_name_eng'].lower()).strip()).replace(' ', '.')+'_tho', password= str((j['block_name_eng'].lower()).strip()).replace(' ', '')+'@123')
                    create_tho_user_ref = User_Role_Ref.objects.create(user_id= create_tho_user.id, role_id= 3, user_role_name= 'THO', user_role_desc='THO')
                    create_tho_details = THO.objects.create(user_id= create_tho_user.id, role_id= 3, tho_name= str((j['block_name_eng'].lower()).strip()).replace(' ', '.')+' tho', district_id= check_master_dist.id, city_id= check_master_taluk.id)


                    phc_data = Master_PHC.objects.filter(district_code= dist_code).values('phc_name', 'phc_code').distinct()

                    lab_ids = [6,7,8,9,10]
                    cnd_lab = 0
                    
                    for k in phc_data:
                        print(k['phc_code'])
                        print("New PHC Loging RE Enter")
                        print("PHC MO USERNAME : "+ str((k['phc_name']).lower().strip()).replace(' ', '.')+'_'+str((k['phc_code']).strip())+'_MO-1')
                        print("PHC MO USERNAME : "+ str((k['phc_name']).lower().strip()).replace(' ', '')+'@123')

                        data['phc_logins'].append({'phc_username': str((k['phc_name']).lower().strip()).replace(' ', '.')+'_'+str((k['phc_code']).strip())+'_MO-1', 'phc_password': str((k['phc_name']).lower().strip()).replace(' ', '')+'@123'})

                        create_phc_user = User.objects.create_user(username= str((k['phc_name']).lower().strip()).replace(' ', '.')+'_'+str((k['phc_code']).strip())+'_MO-1', password= str((k['phc_name']).lower().strip()).replace(' ', '')+'@123')
                        create_phc_user_ref = User_Role_Ref.objects.create(user_id= create_phc_user.id, role_id= 6, user_role_name= 'PHCMO', user_role_desc='PHCMO')
                        create_phc_details = Swab_Collection_Centre.objects.create(user_id= create_phc_user.id, role_id= 6, swab_collection_centre_name= str((k['phc_name']).lower().strip()).replace(' ', '.'), district_id= check_master_dist.id, city_id= check_master_taluk.id)
                        if cnd_lab == 4:
                            cnd_lab = 0
                        else: 
                            cnd_lab += 1
        return Response(data)




def haversine(lat1, lon1, lat2, lon2):

    #   R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km
    
    R = 6372.8 # this is in miles.  For Earth radius in kilometers use 6372.8 km
    # print(lat1)
    # print(lat2)
    # print(lon1)
    # print(lon2)

    # print(type(lat1))
    # print(type(lat2))
    # print(type(lon1))
    # print(type(lon2))

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

# # Usage
# lon1 = 13.3368016
# lat1 = 77.1017528
# lon2 = 13.014204
# lat2 = 77.555803

# print(haversine(lat1, lon1, lat2, lon2))




#########################          FILTER TESTING LABS          #########################
class FilterDSOLabsBasedLocation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        user_id = data.get('user_id')

        dso_data = DSO.objects.filter(user_id= user_id)

        dist_inside_hundr = []
        dist_inside_twohund = []
        dist_inside_threehund = []

        if dso_data:
            dso_data_get = DSO.objects.get(user_id= user_id)

            dist_data = Master_District.objects.filter(id= dso_data_get.district_id)
            dist_lat = 0.0
            dist_lon = 0.0
            if dist_data:
                dist_data = Master_District.objects.get(id= dso_data_get.district_id)
                dist_lat = dist_data.district_lat
                dist_lon = dist_data.district_lon

            lab_data = Master_Labs.objects.all().values()

            # print(dist_lat)
            # print(dist_lon)

            for i in lab_data:
                if i['gps_lat'] and i['gps_lon']:
                    if dist_lat and dist_lon != 0:
                        dist_cal = haversine(float(dist_lat), float(dist_lon), float(i['gps_lat']), float(i['gps_lon']))
                        # print(dist_cal)

                        if dist_cal < 100:
                            # if int(i['closing_balance']) >=10:
                            if (int(i['closing_balance'])*100/int(i['max_capacity'])) < 80:
                                # if int(i['closing_balance']) == 10 and int(i['closing_balance']) > 0:
                                dist_inside_hundr.append(i)
                        if dist_cal > 100 and dist_cal < 200:
                            # if int(i['closing_balance']) >= 10:
                            if (int(i['closing_balance'])*100/int(i['max_capacity'])) < 80:
                                # if int(i['closing_balance']) <= 20 and int(i['closing_balance']) > 0:
                                dist_inside_twohund.append(i)
                        if dist_cal > 200 and dist_cal < 300:
                            # if int(i['closing_balance']) >= 10:
                            if (int(i['closing_balance'])*100/int(i['max_capacity'])) < 80:
                                # if int(i['closing_balance']) <= 20 and int(i['closing_balance']) > 0:
                                dist_inside_threehund.append(i)

        # print(dist_inside_hundr)
        # print(dist_inside_twohund)
        # print(dist_inside_threehund)

        if dist_inside_hundr:
            return Response({'result': dist_inside_hundr, 'message':'Labs within 100km range'})
        if dist_inside_twohund:
            return Response({'result': dist_inside_twohund, 'message':'Labs within 200km range'})
        if dist_inside_threehund:
            return Response({'result': dist_inside_threehund, 'message':'Labs within 300km range'})
        else:
            return Response({'result': [], 'message':'No labs Avalilable'})



#########################          GET CONTACT TRACING DATA          #########################
class GetContactTracingDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        mobile_number = data.get('mobile_number')

        if mobile_number:
            contact_tracing_data = Contact_Tracing.objects.filter(Q(mobile_number= mobile_number)).values()

            for i in contact_tracing_data:

                dist_data = Master_District.objects.filter(district_code= i['district'])
                if dist_data:
                    # dist_data_get = Master_District.objects.get(district_code= i['district'])
                    # i['district_details'] = dist_data_get.district_name_eng
                    i['district_details'] = dist_data

                ward_data = Master_Ward.objects.filter(Q(district_code= i['district']) & Q(new_town_code= i['town']) & Q(ward_no= i['ward']))
                if ward_data:
                    # ward_data_get = Master_Ward.objects.get(Q(district_code= i['district']) & Q(new_town_code= i['town']) & Q(ward_no= i['ward']))
                    # i['ward_details'] = ward_data_get.ward_data_get
                    i['ward_details'] = ward_data

            return Response({'result':contact_tracing_data}, status= status.HTTP_200_OK)

        # elif srf_id and mobile_number == '':
        #     check_already_tested_patient = Patient.objects.filter(Q(srf_id= srf_id)).values()
        #     return Response({'result':check_already_tested_patient}, status= status.HTTP_200_OK)

        # elif srf_id == '' and mobile_number:
        #     check_already_tested_patient = Patient.objects.filter(Q(mobile_number= mobile_number)).values()
        #     return Response({'result':check_already_tested_patient}, status= status.HTTP_200_OK)

        else:
            return Response({'result':'Did not match any records'}, status= status.HTTP_406_NOT_ACCEPTABLE)










#########################          MASTER         LAB          #########################
#!-------------------------------------------------------------------------------------------------------------------------------------          
#!-------------------------------------------------------------------------------------------------------------------------------------          

class Posttaluk(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):  
        data = request.data
        print(data)

        district_code              = data.get('district_code')
        user_id                    = data.get('user_id')

        get_taluk = Master_Block.objects.filter(Q(district_code=district_code)).values()

        return Response({
                'taluks':   get_taluk,
                'result':   'get Taluk Sucessfully'}) 

#!-------------------------------------------------------------------------------------------------------------------------------------          
#!-------------------------------------------------------------------------------------------------------------------------------------          



#########################          CREATE LABS          #########################
class Postlabs(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        lab_name                = data.get('lab_name')
        district_name           = data.get('district_name')
        district_code = data.get('district_code')
        lab_type                = data.get('lab_type')
        lab_id = data.get('lab_id')
        karnataka_districts_id = data.get('karnataka_districts_id')
        karnataka_blocks_id = data.get('karnataka_blocks_id')
        lab_type_id = data.get('lab_type_id')
        address                 = data.get('address')
        pincode                 = data.get('pincode')
        latitude                = data.get('latitude')
        longitude               = data.get('longitude')
        max_capacity            = data.get('max_capacity')
        phone                   = data.get('phone')
        test_type = data.get('test_type')
        closing_balance = data.get('closing_balance')

        lab_create = Master_Labs.objects.create(
            lab_name =lab_name,
            district_code = district_code, 
            district_name = district_name,
            lab_type = lab_type,
            lab_id = lab_id,
            karnataka_districts_id = karnataka_districts_id,
            karnataka_blocks_id = karnataka_blocks_id,
            lab_type_id = lab_type_id,
            address = address,
            pincode = pincode,
            gps_lat = latitude,
            gps_lon = longitude,
            max_capacity = max_capacity,
            phone = phone,
            test_type = test_type,
            lab_classification_id = lab_classification_id,
            closing_balance = closing_balance,)


        return Response({'result': 'Labs added Sucessfully'})




#########################          EDIT LABS          #########################
class GetEditLabs(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_dso = DSO.objects.filter(user_id= user_id)
        check_ssu = SSU.objects.filter(user_id= user_id)

        if check_dso:
            
            check_master_labs_details = Master_Labs.objects.none()
            lab_counts = Master_Labs.objects.none().count()
            for i in check_dso:
                check_master_labs_details = Master_Labs.objects.filter(Q(active= 1) & Q(district_code= i.district.district_code) | Q(karnataka_districts_id= i.district.district_code)).values()
                lab_counts = Master_Labs.objects.filter(Q(active= 1) & Q(district_code= i.district.district_code) | Q(karnataka_districts_id= i.district.district_code)).count()

                check_master_labs = paginatorCreation(check_master_labs_details, selected_page_no)

                # paginator = Paginator(check_master_labs_details, 10)
                # try:
                #     check_master_labs = paginator.page(selected_page_no)
                # except PageNotAnInteger:
                #     check_master_labs = paginator.page(1)
                # except EmptyPage:
                #     check_master_labs = paginator.page(paginator.num_pages)

            for i in check_master_labs:
                check_dist = Master_District.objects.filter(district_code= i['karnataka_districts_id']).values_list('district_name_eng', flat= True)
                check_block = Master_Block.objects.filter(block_code= i['karnataka_blocks_id']).values_list('block_name_eng', flat= True)

                if check_dist:
                    i['district_name'] = check_dist[0]
                else:
                    i['district_name'] = '-'

                if check_block:
                    i['taluk_name'] = check_block[0]
                else:
                    i['taluk_name'] = '-'
            
            return Response({'result': list(check_master_labs), 'total_lab_count': lab_counts}, status= status.HTTP_200_OK)

        elif check_ssu:
            
            all_labs_details = Master_Labs.objects.filter(active= 1).values()
            lab_counts = Master_Labs.objects.filter(active= 1).count()

            all_labs_data = paginatorCreation(all_labs_details, selected_page_no)

            # paginator = Paginator(all_labs_details, 10)
            # try:
            #     all_labs_data = paginator.page(selected_page_no)
            # except PageNotAnInteger:
            #     all_labs_data = paginator.page(1)
            # except EmptyPage:
            #     all_labs_data = paginator.page(paginator.num_pages)

            for i in all_labs_data:
                check_dist = Master_District.objects.filter(district_code= i['karnataka_districts_id']).values_list('district_name_eng', flat= True)
                check_block = Master_Block.objects.filter(block_code= i['karnataka_blocks_id']).values_list('block_name_eng', flat= True)

                if check_dist:
                    i['district_name'] = check_dist[0]
                else:
                    i['district_name'] = '-'

                if check_block:
                    i['taluk_name'] = check_block[0]
                else:
                    i['taluk_name'] = '-'

            return Response({'result': list(all_labs_data), 'total_lab_count': lab_counts}, status= status.HTTP_200_OK)

        else:
            return Response({'result':[]}, status= status.HTTP_400_BAD_REQUEST)



#########################          EDIT UPDATE LABS          #########################
class EditUpdateLabs(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        id = data.get('id')
        max_capacity= data.get('max_capacity')

        check_master_labs = Master_Labs.objects.filter(id= id).update(max_capacity= max_capacity)
            
        return Response({'result':'Updated Sucessfully'}, status= status.HTTP_200_OK)

    


class get_all_labs(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        master_lab =   Master_Labs.objects.filter(active= 1).values()
        
        for i in master_lab:
            
            taluk_name              =   Master_Block.objects.filter(Q(block_code = i['karnataka_blocks_id'])).values()


            if taluk_name:
                taluk_name              =   Master_Block.objects.get(Q(block_code = i['karnataka_blocks_id']))
                i['taluk_name']    = taluk_name.block_name_eng
            else:
                i['taluk_name'] = 'NA'

            # taluk_name              =   Master_Block.objects.get(Q(district_code = i['karnataka_districts_id']) & Q(block_code = i['karnataka_blocks_id']))
            
            district_name           =   Master_District.objects.filter(district_code = i['karnataka_districts_id'])
            if district_name:

                district_name           =   Master_District.objects.get(district_code = i['karnataka_districts_id'])
            
                i['district_name']          = district_name.district_name_eng
            else:
                i['district_name'] = 'NA'
            

        return Response({
                'Lab_data'  :   master_lab,
                'result'    :   'Sucessfully'})  

    
    


class Postdelete(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        id  = data.get('id')

        group_data = Master_Labs.objects.filter(id = id).update(active=0)

        return Response({'result':'Deleted Sucessfully'})



class Posttestkit(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        test_kit_name  = data.get('test_kit_name')

        group_data = Testing_Kit_Barcode.objects.create(testing_kit_barcode_name = test_kit_name)

        return Response({'result':'Testing Kit Added Sucessfully'})



class All_testkit(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
       
        master_testkit =   Testing_Kit_Barcode.objects.filter().values()

        return Response({
                'testkit_data'  :   master_testkit,
                'result'    :   'Sucessfully'})  



class get_all_patients(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):

        all_patient = Patient.objects.all().values()
        for i in all_patient:
            specimen_name = Specimen_Type_Ref.objects.filter(Q(id = i['specimen_type_id']))

            if specimen_name:
                specimen_name = Specimen_Type_Ref.objects.get(Q(id = i['specimen_type_id']))
                i['specimen_name'] = specimen_name.specimen_type_name
            else:
                i['specimen_name'] = 'NA'
            
            test_name = Test_Type_Ref.objects.filter(id = i['test_type_id'])
            if test_name:
                test_type = Test_Type_Ref.objects.get(id = i['test_type_id'])
                i['test_type'] = test_type.test_type_name
            else:
                i['test_type'] = 'NA'

            i['create_timestamp'] = str(i['create_timestamp'])
            i['last_update_timestamp'] = str(i['last_update_timestamp'])
            i['specimen_collection_date'] = str(i['specimen_collection_date'])


        return Response({'Lab_data':all_patient, 'result':'Sucessfully'})



class get_all_contact_testing(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):

        page_no = self.request.query_params.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        all_contact_tracing = Contact_Tracing.objects.all().values()
        all_contact_tracing_count = Contact_Tracing.objects.all().count()

        all_contact_tracing_details = paginatorCreation(all_contact_tracing, selected_page_no)

        for i in all_contact_tracing_details:

            if i['assigned_msc_user_id'] == None:
                i['status'] = 0
                i['msc_name'] = 'N/A'
            else:
                i['status'] = 1
                check_user_name = User.objects.get(id= i['assigned_msc_user_id'])
                i['msc_name'] = check_user_name.first_name

        return Response({'result':list(all_contact_tracing_details), 'total_pg_count':all_contact_tracing_count}, status= status.HTTP_200_OK)



#!! (D) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#?-----------------       ALL USERS               -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
class get_all_user(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get(self,request):

        all_users = User_Role_Ref.objects.filter(role_id= 1).values('user_id').distinct()
        for i in all_users:
            tho_user = THO.objects.filter(dso_id=i[user_id]).values('user_id').distinct()
            for j in tho_user:
                swab_coll_team = Swab_Collection_Centre.objects.filter(tho_id= tho_loop_tho_id).count()

        
        return Response({'result':all_users}, status= status.HTTP_200_OK)



#!! (E) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#?-----------------       GENERATE PACKAGE LIST               -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 


class get_all_generated_package(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        package_details = Package_Sampling.objects.all().values()
        for pd in package_details:
    
            check_lab = Testing_Lab_Facility.objects.filter(id=  pd['test_lab_id'])

            if check_lab:
                check_lab_data = Testing_Lab_Facility.objects.get(id=  pd['test_lab_id'])
                lab_master_data = Master_Labs.objects.get(id= check_lab_data.testing_lab_master_id)
                pd['lab_name'] = lab_master_data.lab_name
            else:
                pd['lab_name'] = '-'

            pd['create_timestamp']           = str(pd['create_timestamp'])
            pd['last_update_timestamp']      = str(pd['last_update_timestamp'])

        return Response({
                    'Lab_data'  :   package_details,
                    'result'    :   'Sucessfully'})



#!! (F) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#?-----------------       LAB ALLOCATION               -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 

class get_all_lab_allocation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):

        page_no = self.request.query_params.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        
        all_lab_allocation_details = Package_Sampling.objects.all().values()
        all_lab_allocation_count = Package_Sampling.objects.all().count()

        all_lab_allocation = paginatorCreation(all_lab_allocation_details, selected_page_no)

        # paginator = Paginator(all_lab_allocation_details, 10)
        # try:
        #     all_lab_allocation = paginator.page(selected_page_no)
        # except PageNotAnInteger:
        #     all_lab_allocation = paginator.page(1)
        # except EmptyPage:
        #     all_lab_allocation = paginator.page(paginator.num_pages)

        for i in all_lab_allocation:
            
            lab_name               =   Testing_Lab_Facility.objects.filter(Q(id = i['test_lab_id'])).values()
            if lab_name:
                lab_name_data           =   Testing_Lab_Facility.objects.get(Q(id = i['test_lab_id']))
                i['lab_name']      =   lab_name_data.testing_lab_facility_name
            else:
                i['lab_name'] = '-'
            
            i['create_timestamp']           = str(i['create_timestamp'])
            i['last_update_timestamp']      = str(i['last_update_timestamp'])

        return Response({'Lab_data':list(all_lab_allocation), 'all_lab_allocation_count':all_lab_allocation_count,'result':'Sucessfully'}) 






#########################          ASSIGN TEST KIT TO PHC           #########################
class AssignTestKitToPhc(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        user_id     = data.get('user_id')
        testkit_id  = data.get('phc_test_kit_name')
        capacity  = data.get('capacity')
        get_phc_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        add_test_phc = Phc_Id_Test_Kit_Id.objects.create(phc_id = get_phc_detail.phc_master_id,test_kit_id=testkit_id, capacity= capacity)

        return Response({'result':'Added Sucessfully'})



#########################          DELETE PHC TEST KIT         #########################
class DeletePHCTestKit(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        print(data)
        user_id  = data.get('user_id')
        testkit_id  = data.get('testkit_id')

        get_phc_detail = Swab_Collection_Centre.objects.get(user_id=user_id)
        active_test_phc = Phc_Id_Test_Kit_Id.objects.filter(Q(phc_id = get_phc_detail.phc_master_id) & Q(test_kit_id=testkit_id)).update(active=0)

        return Response({
            'result'  :   active_test_phc,
            'message':   'Deleted Sucessfully'})



#########################      TESTING KIT BARCODE               #########################
class TestingKitBarcode(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        test_kit_barcode = Testing_Kit_Barcode.objects.filter(active=1).values()
        return Response({'result': test_kit_barcode,'message':'Sucessfull'})




#########################      USER TARGET ASSIGNED COUNTS               #########################
class UserTargetAssignedCounts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def post(self, request):

        data = request.data
        print(data)

        assigned_user   = data.get('user_id')

        target_assigned    =   TargetAssignToUser.objects.filter(Q(user_id=user_id) & Q(created_datetime__date=asdatetime.now().date()))

        return Response({
            'result' : target_assigned,
            'message' :'Sucessfull'
        })







####################################################################            REPORT             #####################################################################


#########################          PHC ADDED PATIENTS REPORT          #########################
class GetPHCUseraddedPatientsReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data
        user_id      = data.get('user_id')
        from_date      = data.get('startdate')
        to_date      = data.get('endDate')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        if check_user:
            check_user_data = Swab_Collection_Centre.objects.get(user_id= user_id)

            if from_date and to_date:

                patient_data = Patient.objects.filter(Q(added_by=user_id) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).values().order_by('-id',)
                patient_data_count = Patient.objects.filter(Q(added_by=user_id) & Q(create_timestamp__date__gte= asdatetime.strptime(from_date,'%Y-%m-%d')) & Q(create_timestamp__date__lte= asdatetime.strptime(to_date,'%Y-%m-%d'))).count()
                
                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_tkb:
                        # check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
                        # i['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                        i['test_kit_name'] = check_tkb[0]
                    else:
                        i['test_kit_name'] = 21

                    if patient_test_type_data.test_type_name == 'RAT':
                        lab_test_data = Patient_Testing.objects.filter(patient_id= i['id']).values_list('testing_status', flat=True)
                        if lab_test_data:
                            # lab_test_data_get = Patient_Testing.objects.get(patient_id= i['id'])
                            # i['test_result'] = lab_test_data_get.testing_status
                            i['test_result'] = lab_test_data[0]
                        else:
                            i['test_result'] = 2

                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})
            
            else:

                patient_data = Patient.objects.filter(Q(added_by=user_id)).values().order_by('-id',)
                patient_data_count = Patient.objects.filter(Q(added_by=user_id)).count()

                patient_details = paginatorCreation(patient_data, selected_page_no)

                for i in patient_details:
                    
                    patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
                    patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
                    patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                    i['patient_type_name'] = patient_type_data.patient_type_name
                    i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
                    i['test_type_name']= patient_test_type_data.test_type_name

                    check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_tkb:
                        # check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
                        # i['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
                        i['test_kit_name'] = check_tkb[0]
                    else:
                        i['test_kit_name'] = 21

                    if patient_test_type_data.test_type_name == 'RAT':
                        lab_test_data = Patient_Testing.objects.filter(patient_id= i['id']).values_list('testing_status', flat=True)
                        if lab_test_data:
                            # lab_test_data_get = Patient_Testing.objects.get(patient_id= i['id'])
                            # i['test_result'] = lab_test_data_get.testing_status
                            i['test_result'] = lab_test_data[0]
                        else:
                            i['test_result'] = 2
                return Response({'patient_details':list(patient_details), 'total_pg_count': patient_data_count,'result': 'successfull'})

        else:
            return Response({'result': 'Something Went Wrong'})







#########################      PHC DATE WISE COLLECTION STATUS AND RESULT TOTAL COUNT               #########################
class PHCDateWiseCollectionStatusAndResultTotalCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        # check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values()

        check_all_swab_collector_data = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id', flat=True)
        # check_all_swab_collector_data_count = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id', flat=True).count()

        # phc_user_ids = []

        # for i in check_all_swab_collector:
        #     if i['user_id'] not in phc_user_ids:
        #         phc_user_ids.append(i['user_id'])


        patient_data = Patient.objects.filter(added_by_id__in= check_all_swab_collector_data).values('create_timestamp__date').distinct()
        patient_data_count = Patient.objects.filter(added_by_id__in= check_all_swab_collector_data).values('create_timestamp__date').distinct().count()

        # patient_details = paginatorCreation(patient_data, selected_page_no)
        swab_col_rep_data = []



        for i in patient_data:
            # for j in phc_user_ids:
            for j in check_all_swab_collector_data:
                user_data = User.objects.get(id= j)
                samp_collected_cnt = Patient.objects.filter(Q(added_by_id= j) & Q(create_timestamp__date= i['create_timestamp__date'])).count()
                check_cnt = samp_collected_cnt
                if samp_collected_cnt > 0:
                    swab_col_rep_data.append({'user_id':j, 'name':user_data.first_name, 'username':user_data.username,'date': i['create_timestamp__date'], 'total_collection_count':samp_collected_cnt})
                    
        return Response({'result': swab_col_rep_data, 'total_pg_count': patient_data_count, 'message': 'Sucess'})







#########################      PHC DATE WISE CONTACT TRACING STATUS REPORT               #########################
class PHCDateWiseContectTestingStatusReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id     =   data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        Arr=[]

        check_user  =   Swab_Collection_Centre.objects.get(Q(user_id= user_id) & Q(role_id=6))

        get_scc_users = Swab_Collection_Centre.objects.filter(phc_master_id= check_user.phc_master_id).values_list('user_id', flat= True)
        
        phc_target_assigned =   PHCTargetAssignment.objects.filter(Q(phc_id= check_user.phc_master_id)).values('phc_created_datetime__date').distinct()
        phc_target_assigned_count =   PHCTargetAssignment.objects.filter(Q(phc_id= check_user.phc_master_id)).values('phc_created_datetime__date').distinct().count()

        phc_target_assigned_data = paginatorCreation(phc_target_assigned, selected_page_no)

        for i in phc_target_assigned_data:
            
            phc_created_datetime    =   PHCTargetAssignment.objects.get(phc_created_datetime__date=i['phc_created_datetime__date'])
            contact_testing         =   Contact_Tracing.objects.filter(Q(assigned_phc=check_user.phc_master_id) & Q(assigned_date__date=i['phc_created_datetime__date'])).count()
            ili                     =   ILI.objects.filter(Q(assigned_phc=check_user.phc_master_id) & Q(assigned_date__date=i['phc_created_datetime__date'])).count()

            col_cnt_testing_cnt = Contact_Tracing.objects.filter(Q(assigned_phc=check_user.phc_master_id) & Q(sample_collected= 1) & Q(assigned_date__date=i['phc_created_datetime__date'])).count()
            col_ili_cnt = ILI.objects.filter(Q(assigned_phc=check_user.phc_master_id) & Q(sample_collected= 1) & Q(assigned_date__date=i['phc_created_datetime__date'])).count()
            col_rnd_samp_cnt = Patient.objects.filter(Q(added_by_id__in= get_scc_users) & Q(create_timestamp__date= i['phc_created_datetime__date'])).count()

            phc_target_count = phc_created_datetime.phc_target

            if phc_target_count:
                phc_target_count = phc_target_count
            else:
                phc_target_count = 0

            random = phc_target_count - contact_testing - ili

            Arr.append({'date':i['phc_created_datetime__date'],
                        'Total_target':phc_target_count,
                        'actieved_target':col_cnt_testing_cnt + col_ili_cnt + col_rnd_samp_cnt,
                        'contact_testing':contact_testing,
                        'ili':ili,
                        'random':random})

        return Response({'result':Arr, 'total_pg_count': phc_target_assigned_count, 'message':'Sucessfully'},status=status.HTTP_200_OK)







#########################      PHC DATE WISE CONTACT TRACING STATUS INDIVIDUAL USER COUNT               #########################
class PHCDateWiseContectTestingStatusIndividualUserReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id     =   data.get('user_id')
        date     =   data.get('date')
        Arr=[]

        check_user  =   Swab_Collection_Centre.objects.get(Q(user_id= user_id) & Q(role_id=6))

        get_scc_users = list(Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id) & Q(role_id=8)).values_list('user_id'))
        
        get_target_user     =   TargetAssignToUser.objects.filter(Q(user_id__in=get_scc_users) & Q(created_datetime__date=date)).values()
        for i in get_target_user:
            msc_user_data = User.objects.get(id= i['user_id'])
            i['msc_name']= msc_user_data.first_name
            i['total_target'] = str(int(i['contact_tracing_target']) + int(i['ili_target']) + int(i['random_other_target']))
            i['date']= date

        return Response({
            'get_target_user':get_target_user,
            'message':'Sucessfully'
        },status=status.HTTP_200_OK)




#########################      PHC DATE WISE CONTACT TRACING STATUS INDIVIDUAL USER COUNT               #########################
class PHCDateWiseContectTestingStatusIndividualUserDetailReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data            =   request.data
        user_id         =   data.get('user_id')
        date            =   data.get('date')

        contract_user   =   Contact_Tracing.objects.filter(Q(assigned_date__date=date) & Q(assigned_msc_user_id=user_id)).values()

        return Response({
            'contract_user':contract_user,
            'message':'Sucessfully'
        },status=status.HTTP_200_OK)




#########################      PHC DATE WISE COLLECTION STATUS AND RESULT TOTAL COUNT INDIVIDUAL               #########################
class PHCDateWiseCollectionStatusAndResultTotalCountndividual(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data
        print("JJJJJJJJJJJJJ", data)
        user_id = data.get('user_id')
        date = data.get('date')

        date_split = date.split('-')

        check_user = Swab_Collection_Centre.objects.filter(user_id= user_id).values()

        patient_details = Patient.objects.filter(Q(added_by_id=user_id) & Q(create_timestamp__date= datetime.datetime(int(date_split[0]), int(date_split[1]), int(date_split[2])))).values()

        for i in patient_details:
            print(i)
            
            patient_type_data =  Patient_Type_Ref.objects.get(id= i['patient_type_id'])
            patient_specimen_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])
            patient_test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
            # i.patient_type_name = i.patient_type.patient_type_name
            i['patient_type_name'] = patient_type_data.patient_type_name
            i['specimen_type_name']= patient_specimen_type_data.specimen_type_name
            i['test_type_name']= patient_test_type_data.test_type_name

            check_tkb = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id'])
            if check_tkb:
                check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
                i['test_kit_name'] = check_tkb_get.testing_kit_barcode_name
            else:
                i['test_kit_name'] = 21

            if patient_test_type_data.test_type_name == 'RAT':
                lab_test_data = Patient_Testing.objects.filter(patient_id= i['id'])
                if lab_test_data:
                    lab_test_data_get = Patient_Testing.objects.get(patient_id= i['id'])
                    i['test_result'] = lab_test_data_get.testing_status
                else:
                    i['test_result'] = 2

        #     i.patient_type_name = i.patient_type.patient_type_name
        #     i.patient_type_name = i.patient_type.patient_type_name
        #     i.specimen_type_name= i.specimen_type.specimen_type_name
        #     i.test_type_name= i.test_type.test_type_name

        #     check_tkb = Testing_Kit_Barcode.objects.filter(id= i.testing_kit_barcode_id)
        #     if check_tkb:
        #         # check_tkb_get = Testing_Kit_Barcode.objects.get(id= i['testing_kit_barcode_id'])
        #         i.test_kit_name = i.testing_kit_barcode.testing_kit_barcode_name
        #     else:
        #         i.test_kit_name = 21

        #     if i.test_type.test_type_name == 'RAT':
        #         lab_test_data = Patient_Testing.objects.filter(patient_id= i.id)
        #         if lab_test_data:
        #             # lab_test_data_get = Patient_Testing.objects.get(patient_id= i['id'])
        #             # i.test_result = i.id.testing_status
        #             lab_test_data_get = Patient_Testing.objects.get(patient_id= i.id)
        #             i.test_result = lab_test_data_get.testing_status
        #         else:
        #             i.test_result = 2

        # # json_data = json.dumps(list(patient_details))
        # rrr = serializer.serializer('json', patient_details)
        return Response({'patient_details':patient_details,'result': 'successfull'})




#########################      PHC DATE WISE SAMPLES REJECTED COUNT REPORT               #########################
class PHCDateWiseSampleRejectedCountReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        

        Arr=[]

        check_user  =   Swab_Collection_Centre.objects.get(Q(user_id= user_id) & Q(role_id=6))
        
        phc_user    =   Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id', flat=True)

        patient_data = Patient.objects.filter(Q(added_by_id__in=phc_user) & Q(samples_rejected=1)).values('create_timestamp__date').distinct()
        patient_data_count = Patient.objects.filter(Q(added_by_id__in=phc_user) & Q(samples_rejected=1)).values('create_timestamp__date').distinct().count()

        patient_details = paginatorCreation(patient_data, selected_page_no)

        for i in patient_details:
            patient_rej = Patient.objects.filter(Q(create_timestamp__date=i['create_timestamp__date']) & Q(added_by_id__in=list(phc_user)) & Q(samples_rejected=1)).count()
            
            Arr.append({'date':i['create_timestamp__date'], 'rejected_count':patient_rej})

        return Response({'result':Arr, 'total_pg_count': patient_data_count ,'message':'Sucessfully'},status=status.HTTP_200_OK)






#########################      PHC DATE WISE SAMPLES REJECTED COUNT REPORT INDETAIL               #########################
class PHCDateWiseSampleRejectedIndetailReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id     =   data.get('user_id')
        date        =   data.get('date')
        Arr=[]

        check_user  =   Swab_Collection_Centre.objects.get(Q(user_id= user_id) & Q(role_id=6))
        
        phc_user    =   Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id')

        rejected_patient_samp_details = Patient.objects.filter(Q(added_by_id__in=list(phc_user)) & Q(samples_rejected=1) &Q(create_timestamp__date=date)).values()

        for j in rejected_patient_samp_details:

            get_sp_type = Specimen_Type_Ref.objects.get(id= j['specimen_type_id'])
            j['specimen_type_name'] = get_sp_type.specimen_type_name
            added_user_data = User.objects.get(id= j['added_by_id'])
            j['added_user_name'] = added_user_data.first_name

        
        return Response({
            'result':rejected_patient_samp_details,
            'message':'Sucessfully'
        },status=status.HTTP_200_OK)







#########################      PHC TARGET VS ACTUAL SWAB COLLECTION               #########################
class PHCTargetvsActualSwabCollection(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        all_targets  = PHCTargetAssignment.objects.filter(phc_id= check_user.phc_master_id).values('phc_created_datetime__date').distinct()
        all_targets_count  = PHCTargetAssignment.objects.filter(phc_id= check_user.phc_master_id).values('phc_created_datetime__date').distinct().count()
        
        all_targets_details = paginatorCreation(all_targets, selected_page_no)

        rep_data = []

        for i in all_targets_details:

            rep_details = {}
            all_targets  = PHCTargetAssignment.objects.get(Q(phc_id= check_user.phc_master_id) & Q(phc_created_datetime__date= i['phc_created_datetime__date']))
            rep_details['date']= i['phc_created_datetime__date']
            rep_details['daily_target'] = all_targets.phc_target

            no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_phc= check_user.phc_master_id) & Q(assigned_date__date= i['phc_created_datetime__date'])).count()
            no_of_swab_collected = Contact_Tracing.objects.filter(Q(assigned_phc= check_user.phc_master_id) & Q(assigned_date__date= i['phc_created_datetime__date']) & Q(sample_collected= 1)).count()
            rep_details['no_of_patient_alloted'] = no_of_patient_alloted
            rep_details['no_of_swab_collected'] = no_of_swab_collected
            rep_details['balance'] = no_of_patient_alloted - no_of_swab_collected

            rep_data.append(rep_details)
        
        return Response({'result': rep_data, 'total_pg_count': all_targets_count, 'message': 'Sucess'})






#########################      PHC TARGET VS ACTUAL SWAB COLLECTION DATE VIEW               #########################
class PHCTargetvsActualSwabCollectionDateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        data = request.data

        user_id = data.get('user_id')
        date = data.get('date')

        print(data)
        print("GGGGGG")

        split_date = date.split('-')
        print(split_date)

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        print(check_user.phc_master_id)

        # all_targets  = PHCTargetAssignment.objects.filter(Q(phc_id= check_user.phc_master_id) & Q(phc_created_datetime__date= datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])))).values('phc_created_datetime__date').distinct()

        ct_details = Contact_Tracing.objects.filter(Q(assigned_phc= check_user.phc_master_id) & Q(assigned_date__date= datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])))).values()

        print(ct_details)
        # rep_data = []

        # for i in all_targets:
        #     rep_details = {}
        #     all_targets  = PHCTargetAssignment.objects.get(Q(phc_id= check_user.phc_master_id) & Q(created_datetime__date= i['created_datetime__date']))
        #     rep_details['date']= i['created_datetime__date']
        #     rep_details['daily_target'] = all_targets.phc_target

        #     no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_phc= check_user.phc_master_id) & Q(assigned_date__date= i['created_datetime__date'])).count()
        #     no_of_swab_collected = Contact_Tracing.objects.filter(Q(assigned_phc= check_user.phc_master_id) & Q(assigned_date__date= i['created_datetime__date']) & Q(sample_collected= 1)).count()
        #     rep_details['no_of_patient_alloted'] = no_of_patient_alloted
        #     rep_details['no_of_swab_collected'] = no_of_swab_collected
        #     rep_details['balance'] = no_of_patient_alloted - no_of_swab_collected

        #     rep_data.append(rep_details)

        for i in ct_details:
            user_data = User.objects.filter(id= i['assigned_msc_user_id'])
            if user_data:
                user_data_get = User.objects.get(id= i['assigned_msc_user_id'])
                i['assigned_user_name'] = user_data_get.first_name
            else:
                i['assigned_user_name'] = 'N/A'


        
        return Response({'result': ct_details, 'message': 'Sucess'}, status= status.HTTP_200_OK)





#########################      SWAB COLLECTION BY SWAB COLLECTOR               #########################
class SwabCollectionBySwabCollector(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)


        check_all_swab_collector_data = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id) & Q(role_id= 8)).values()
        check_all_swab_collector_data_count = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id) & Q(role_id= 8)).count()

        check_all_swab_collector_details = paginatorCreation(check_all_swab_collector_data, selected_page_no)

        swab_col_rep_data = []

        total_swab_coll = 0
        total_swab_alloted = 0
        total_swab_collected = 0
        total_balance = 0
        
        for i in check_all_swab_collector_details:

            swab_col_rep_details = {}

            check_user = User.objects.get(id= i['user_id'])
            no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_msc_user= i['user_id']) & Q(assigned_date__date= asdatetime.now().date())).count()
            no_of_swab_collected = Contact_Tracing.objects.filter(Q(assigned_msc_user= i['user_id']) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).count()

            swab_col_rep_details['name_of_swab_collector'] = check_user.first_name
            swab_col_rep_details['swab_collector_user_id'] = check_user.id
            swab_col_rep_details['no_of_patient_allotted'] = no_of_patient_alloted
            swab_col_rep_details['no_of_swab_collected'] = no_of_swab_collected
            swab_col_rep_details['balance'] = no_of_patient_alloted - no_of_swab_collected
            
            
            # if (no_of_patient_alloted != 0 and no_of_swab_collected != 0):
            if (no_of_patient_alloted != 0):
                swab_col_rep_data.append(swab_col_rep_details)
                total_swab_coll += 1
                total_swab_alloted += no_of_patient_alloted
                total_swab_collected += no_of_swab_collected
                total_balance += no_of_patient_alloted - no_of_swab_collected

        # swab_col_rep_data.append({'total_swab_coll':total_swab_coll, 'total_swab_alloted':total_swab_alloted, 'total_swab_collected':total_swab_collected, 'total_balance':total_balance})

        return Response({'result': swab_col_rep_data, 'total_pg_count': check_all_swab_collector_data_count, 'total_swab_coll':total_swab_coll, 'total_swab_alloted':total_swab_alloted, 'total_swab_collected':total_swab_collected, 'total_balance':total_balance, 'total_pg_count': check_all_swab_collector_data_count, 'message': 'Sucess'})








#########################      SWAB COLLECTION BY SWAB COLLECTOR SWABCOLLECTOR VIEW               #########################
class SwabCollectionBySwabCollectorSwabcollectorView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        swab_collector_id = data.get('swab_collector_id')
        from_date = data.get('from_date')
        to_date = data.get('to_date')

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id) & Q(role_id= 8)).values()

        if from_date and to_date:
            
            from_date = data.get('from_date')
            to_date = data.get('to_date')

            start_date = from_date.split('-')
            end_date = from_date.split('-')

            no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_msc_user= swab_collector_id) & Q(assigned_date__date__gte= datetime.datetime(start_date[0], start_date[1], start_date[2])) & Q(assigned_date__date__lte= datetime.datetime(end_date[0], end_date[1], end_date[2]))).values()

            return Response({'result': no_of_patient_alloted, 'message': 'Sucess'})

        else:
            no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_msc_user= swab_collector_id) & Q(assigned_date__date= asdatetime.now().date())).values()

            return Response({'result': no_of_patient_alloted, 'message': 'Sucess'})
        
        # for i in check_all_swab_collector:

        #     swab_col_rep_details = {}

        #     check_user = User.objects.get(id= i['user_id'])
        #     no_of_patient_alloted = Contact_Tracing.objects.filter(Q(assigned_msc_user= i['user_id']) & Q(assigned_date__date= asdatetime.now().date())).count()
        #     no_of_swab_collected = Contact_Tracing.objects.filter(Q(assigned_msc_user= i['user_id']) & Q(assigned_date__date= asdatetime.now().date()) & Q(sample_collected= 1)).count()

        #     swab_col_rep_details['name_of_swab_collector'] = check_user.first_name
        #     swab_col_rep_details['no_of_patient_allotted'] = no_of_patient_alloted
        #     swab_col_rep_details['no_of_swab_collected'] = no_of_swab_collected
        #     swab_col_rep_details['balance'] = no_of_patient_alloted - no_of_swab_collected
            
        #     total_swab_coll += 1
        #     total_swab_alloted += no_of_patient_alloted
        #     total_swab_collected += no_of_swab_collected
        #     total_balance += no_of_patient_alloted - no_of_swab_collected

        #     swab_col_rep_data.append(swab_col_rep_details)

        # swab_col_rep_data.append({'total_swab_coll':total_swab_coll, 'total_swab_alloted':total_swab_alloted, 'total_swab_collected':total_swab_collected, 'total_balance':total_balance})

        # return Response({'result': swab_col_rep_data, 'total_swab_coll':total_swab_coll, 'total_swab_alloted':total_swab_alloted, 'total_swab_collected':total_swab_collected, 'total_balance':total_balance, 'message': 'Sucess'})



#########################      SWAB PACKAGE DISPATCH DETAILS               #########################
class SwabPackageDespatchDetailsCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)


        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        # check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values()
        check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id', flat=True)

        # swab_col_users = []

        # for i in check_all_swab_collector:
        #     if i['user_id'] not in swab_col_users:
        #         swab_col_users.append(i['user_id'])

        get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector)).values('create_timestamp__date').distinct()
        get_all_pack_count = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector)).values('create_timestamp__date').distinct().count()

        package_sts_details = []

        total_package_created = 0
        total_package_acc_mo = 0
        total_package_dispatched_lab = 0
        total_package_dispatched_to_tho = 0

        get_all_pack_details = paginatorCreation(get_all_pack, selected_page_no)

        for i in get_all_pack_details:
            
            package_details = {}

            check_package_created = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date'])).count()
            check_package_received_mo = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_status= 7)).count()
            check_package_dispatched_lab = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_action= 15)).count()
            check_package_dispatched_tho = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_action= 13)).count()

            package_details['date'] = i['create_timestamp__date']
            package_details['no_of_package_created'] = check_package_created

            if check_package_received_mo != 0:
                package_details['no_of_package_accepted_mo'] = check_package_received_mo
            else:
                package_details['no_of_package_accepted_mo'] = '-'

            if check_package_dispatched_lab != 0:
                package_details['no_of_package_dispatched_lab'] = check_package_dispatched_lab
            else:
                package_details['no_of_package_dispatched_lab'] = '-'

            if check_package_dispatched_tho != 0:
                package_details['no_of_package_dispatched_tho'] = check_package_dispatched_tho
            else:
                package_details['no_of_package_dispatched_tho'] = '-'
            
            

            total_package_created += check_package_created
            total_package_acc_mo += check_package_received_mo
            total_package_dispatched_lab += check_package_dispatched_lab
            total_package_dispatched_to_tho += check_package_dispatched_tho

            package_sts_details.append(package_details)

        # package_sts_details.append({'total_package_created':total_package_created, 'total_package_acc_mo':total_package_acc_mo, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho})


        return Response({'result': package_sts_details, 'total_pg_count': get_all_pack_count, 'total_package_created':total_package_created, 'total_package_acc_mo':total_package_acc_mo, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho,'message': 'Sucess'})






#########################      SWAB PACKAGE DISPATCH DETAILS               #########################
class SwabPackageDespatchDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id     =   data.get('user_id')
        date     =   data.get('date')

        check_user  =   Swab_Collection_Centre.objects.get(Q(user_id= user_id) & Q(role_id=6))
        user_created_package_details = Package_Sampling.objects.filter(Q(master_phc_id= check_user.phc_master_id) & Q(create_timestamp__date=date)).values()
        
        return Response({
            'get_scc_users':user_created_package_details,
            'message':'Sucessfully'
        },status=status.HTTP_200_OK)




#########################      PHC PACKAGE LAB WISE REPORT               #########################
class PHCPackageLabWiseReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user = Swab_Collection_Centre.objects.get(user_id= user_id)

        check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= check_user.phc_master_id)).values_list('user_id', flat=True)

        get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(test_lab__isnull= False)).values('create_timestamp__date').distinct().order_by('-create_timestamp__date')
        get_all_pack_count = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(test_lab__isnull= False)).values('create_timestamp__date').distinct().count()


        get_all_pack_details = paginatorCreation(get_all_pack, selected_page_no)

        package_lab_details = []

        total_lab_created = 0
        total_samples = 0

        for i in get_all_pack_details:
            
            lab_package_details = {}

            lab_package_details['date'] = i['create_timestamp__date']

            # check_package_dis_lab = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_action= 5)).values()
            # print(check_package_dis_lab)

            check_package_dis_lab = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(test_lab__isnull= False)).values('test_lab_id').distinct()

            if check_package_dis_lab:
                for j in check_package_dis_lab:

                    
                    check_test_lab = Testing_Lab_Facility.objects.get(id= j['test_lab_id'])
                    lab_name_data = Master_Labs.objects.get(id= check_test_lab.testing_lab_master_id)

                    lab_package_details['lab_name'] = lab_name_data.lab_name
                    
                    total_lab_created += 1

                    check_package_sam_count = Package_Sampling.objects.filter(Q(user_id__in= check_all_swab_collector) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(test_lab_id= j['test_lab_id'])).values()

                    if check_package_sam_count:
                        sample_count = 0
                        for k in check_package_sam_count:
                            sample_count += int(k['samples_count'])
                            total_samples += int(k['samples_count'])
                        lab_package_details['sample_count'] = sample_count
                    else:
                        lab_package_details['sample_count'] = 0
            else:
                lab_package_details['lab_name'] = '-'
                lab_package_details['sample_count'] = 0

            package_lab_details.append(lab_package_details)
        
        # package_lab_details.append({'total_lab_created':total_lab_created, 'total_samples':total_samples})


        return Response({'result': package_lab_details, 'total_lab_created':total_lab_created, 'total_samples':total_samples, 'total_pg_count': get_all_pack_count,'message': 'Sucess'})





#########################      THO TARGET VS ACTUAL SWAB COLLECTION               #########################
class THOTargetvsActualSwabCollection(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')

        rep_data = []

        total_target = 0
        total_no_of_patient = 0
        total_no_of_swab_coll = 0
        total_balance = 0

        check_tho = THO.objects.get(user_id= user_id)

        check_all_phc_details = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()

        for i in check_all_phc_details:
            
            tho_rep_data = {}

            master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

            tho_rep_data['phc_name'] = master_phc_details.phc_name

            phc_target = PHCTargetAssignment.objects.filter(Q(tho_id= user_id) & Q(phc_id= i['phc_master_id']) & Q(created_datetime__date= asdatetime.now().date())).values()
            if phc_target:
                phc_target_cnt = PHCTargetAssignment.objects.filter(Q(tho_id= user_id) & Q(phc_id= i['phc_master_id']) & Q(created_datetime__date= asdatetime.now().date())).count()
                tho_rep_data['daily_target'] = phc_target_cnt
                total_target += phc_target_cnt
            else:
                tho_rep_data['daily_target'] = 0

            check_phc_target_cnt = Contact_Tracing.objects.filter(Q(assigned_phc = i['phc_master_id']) & Q(assigned_date= asdatetime.now().date())).count()
            tho_rep_data['no_of_patient_allotted'] = check_phc_target_cnt
            total_no_of_patient += check_phc_target_cnt

            check_phc_swab_coll = Contact_Tracing.objects.filter(Q(assigned_phc = i['phc_master_id']) & Q(assigned_date= asdatetime.now().date()) & Q(sample_collected= 1)).count()
            tho_rep_data['no_of_patient_swab_collected'] = check_phc_swab_coll
            total_no_of_swab_coll += check_phc_swab_coll

            tho_rep_data['balance']= check_phc_target_cnt - check_phc_swab_coll
            total_balance += check_phc_target_cnt - check_phc_swab_coll

            if len(phc_target) > 0:
                rep_data.append(tho_rep_data)

        # rep_data.append({'total_target':total_target, 'total_no_of_patient':total_no_of_patient, 'total_no_of_swab_coll':total_no_of_swab_coll, 'total_balance':total_balance})
        
        return Response({'result': rep_data, 'total_target':total_target, 'total_no_of_patient':total_no_of_patient, 'total_no_of_swab_coll':total_no_of_swab_coll, 'total_balance':total_balance, 'message': 'Sucess'})


    
    

    
#########################      THO TARGET VS ACTUAL SWAB COLLECTION VIEW               #########################
class THOTargetvsActualSwabCollectionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data 

        user_id = data.get('user_id')
        phc_id = data.get('phc_id')

        ct_data = Contact_Tracing.objects.filter(Q(assigned_phc= phc_id)).values()

        return Response({'result': ct_data, 'message':'Sucessfully'}, status= status.HTTP_200_OK)



#########################      THO SWAB DISPATCH DETAILS               #########################
class THOSwabDispatchDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        rep_data = []

        total_package_created = 0
        total_package_dispatched_lab = 0
        total_package_dispatched_to_tho = 0

        check_tho = THO.objects.get(user_id= user_id)

        check_all_phc_details = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()


        date_data = Package_Sampling.objects.all().values('create_timestamp__date').distinct()
        date_data_count = Package_Sampling.objects.all().values('create_timestamp__date').distinct().count()

        date_details = paginatorCreation(date_data, selected_page_no)

        for dd in date_details:

            for i in check_all_phc_details:
                
                tho_rep_data = {}

                master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

                tho_rep_data['date'] = dd['create_timestamp__date']
                tho_rep_data['phc_name'] = master_phc_details.phc_name

                # check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= i['phc_master_id'])).values()

                # swab_col_users = []

                # for j in check_all_swab_collector:
                #     if j['user_id'] not in swab_col_users:
                #         swab_col_users.append(j['user_id'])
                
                swab_col_users = Swab_Collection_Centre.objects.filter(Q(phc_master_id= i['phc_master_id'])).values_list('user_id', flat=True)


                # get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users)).values('create_timestamp__date').distinct()

                check_package_created = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(create_timestamp__date= dd['create_timestamp__date'])).count()
                # check_package_received_mo = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_status= 7)).count()
                check_package_dispatched_lab = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(package_type_status= 5)  & Q(create_timestamp__date= dd['create_timestamp__date'])).count()
                check_package_accepted_tho = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 13)  & Q(create_timestamp__date= dd['create_timestamp__date'])).count()

                # package_sts_details = []

                tho_rep_data['no_of_package_created'] = check_package_created
                tho_rep_data['no_of_package_dis_lab'] = check_package_dispatched_lab
                tho_rep_data['no_of_package_acc_tho'] = check_package_accepted_tho


                total_package_created += check_package_created
                # total_package_acc_mo += check_package_received_mo
                total_package_dispatched_lab += check_package_dispatched_lab
                total_package_dispatched_to_tho += check_package_accepted_tho

                if check_package_created != 0:
                    rep_data.append(tho_rep_data)

        # rep_data.append({'total_package_created':total_package_created, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho,})
        
        return Response({'result': rep_data, 'total_pg_count': date_data_count,'total_package_created':total_package_created, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho, 'message': 'Sucess'})










#########################      THO PACKAGE LAB WISE REPORT               #########################
class THOPackageLabWiseReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)


        check_tho = THO.objects.get(user_id= user_id)

        check_all_phc_data = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()
        check_all_phc_data_count = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).count()

        # phc_id = check_all_phc_details.phc_master_id

        # all_swab_collector = []

        # for i in

        check_all_phc_details = paginatorCreation(check_all_phc_data, selected_page_no)

        no_of_labs = 0
        total_samples = 0

        rep_data = []
        this_final_data = []

        for i in check_all_phc_details:
            
            master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

            check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= i['phc_master_id'])).values()

            swab_col_users = []

            for i in check_all_swab_collector:
                if i['user_id'] not in swab_col_users:
                    swab_col_users.append(i['user_id'])

            get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users)).values('test_lab_id').distinct()
            

            for i in get_all_pack:

                if i['test_lab_id']:
                    tho_rep_data = {}
                    tho_rep_data['phc_name'] = master_phc_details.phc_name

                    no_of_labs += 1
                    lab_name = '-'
                    sample_count = 0

                    check_package_dis_lab = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(test_lab_id= i['test_lab_id'])).values()

                    if check_package_dis_lab:
                        
                        for j in check_package_dis_lab:

                            check_test_lab = Testing_Lab_Facility.objects.get(id= j['test_lab_id'])
                            lab_name_data = Master_Labs.objects.get(id= check_test_lab.testing_lab_master_id)

                            lab_name = lab_name_data.lab_name

                            check_package_sam_count = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(test_lab_id= j['test_lab_id'])).values()

                            if check_package_sam_count:
                                for k in check_package_sam_count:
                                    sample_count += int(k['samples_count'])
                                    total_samples += int(k['samples_count'])
                    
                    tho_rep_data['lab_name'] = lab_name
                    tho_rep_data['sample_count'] = sample_count
                    
                    this_final_data.append(tho_rep_data)
        
        # this_final_data.append({'no_of_labs':no_of_labs, 'total_samples':total_samples})

        return Response({'result': this_final_data, 'no_of_labs':no_of_labs, 'total_samples':total_samples, 'message': 'Sucess'})


 


#########################      THO DATE WISE COLLECTED SAMPLES               #########################
class THODateWiseSamplesCollectionReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user_id= data.get('user_id')

        page_no = data.get('page_no')
        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        tho_data = THO.objects.filter(user_id= user_id)
        if tho_data:
            
            tho_data_get = THO.objects.get(user_id= user_id)

            uniq_date = Patient.objects.filter(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id= tho_data_get.id).values_list('user_id', flat=True)).values_list('id', flat=True)).values('create_timestamp__date').order_by('-create_timestamp__date').distinct()
            uniq_date_count = Patient.objects.filter(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id= tho_data_get.id).values_list('user_id', flat=True)).values_list('id', flat=True)).values('create_timestamp__date').distinct().count()
            
            uniq_deatils = paginatorCreation(uniq_date, selected_page_no)

            for i in uniq_deatils:
                
                i['phc_count'] = Swab_Collection_Centre.objects.filter(Q(role_id= 6) & Q(tho_id= tho_data_get.id)).count()
                i['samples_count'] = Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id= tho_data_get.id).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= i['create_timestamp__date'])).count()

            return Response({'result':list(uniq_deatils), 'total_pg_count':uniq_date_count}, status= status.HTTP_200_OK)
        else:
            return Response({'result': []}, status=status.HTTP_400_BAD_REQUEST)






#########################      THO DATE WISE COLLECTED SAMPLES PHC VIEW1               #########################
class THODateWisePHCWiseSamplesCollectionReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user_id= data.get('user_id')
        date = data.get('date')

        tho_data = THO.objects.filter(user_id= user_id)
        if tho_data:
            
            tho_data_get = THO.objects.get(user_id= user_id)

            scc_data = Swab_Collection_Centre.objects.filter(Q(role_id= 6) & Q(tho_id= tho_data_get.id)).values()

            for i in scc_data:
                get_phc_data = Master_PHC.objects.get(id= i['phc_master_id'])
                i['phc_name'] = get_phc_data.phc_name
                i['samples_count'] = Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(phc_master_id= i['phc_master_id']).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()
                i['date'] = date
            return Response({'result':scc_data}, status= status.HTTP_200_OK)
        else:
            return Response({'result': []}, status=status.HTTP_400_BAD_REQUEST)

     
    
  


#########################      DSO TARGET VS ACTUAL SWAB COLLECTION               #########################
class DSOTargetvsActualSwabCollection(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        rep_data = []

        total_target = 0
        total_no_of_patient = 0
        total_no_of_swab_coll = 0
        total_balance = 0

        dso_data = DSO.objects.get(user_id= user_id)

        check_dso_tho = THO.objects.filter(dso_id= dso_data.id).values()
        total_pg_count = THO.objects.filter(dso_id= dso_data.id).count()

        for cdt in check_dso_tho:

            check_tho = THO.objects.get(user_id= cdt['user_id'])

            check_all_phc_data = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()

            check_all_phc_details = paginatorCreation(check_all_phc_data, selected_page_no)

            for i in check_all_phc_details:
                
                tho_rep_data = {}

                master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

                tho_rep_data['phc_name'] = master_phc_details.phc_name
                tho_rep_data['phc_id'] = i['phc_master_id']

                phc_target = PHCTargetAssignment.objects.filter(Q(tho_id= cdt['user_id']) & Q(phc_id= i['phc_master_id']) & Q(created_datetime__date= asdatetime.now().date())).values()
                if phc_target:
                    phc_target_cnt = PHCTargetAssignment.objects.filter(Q(tho_id= cdt['user_id']) & Q(phc_id= i['phc_master_id']) & Q(created_datetime__date= asdatetime.now().date())).count()
                    tho_rep_data['daily_target'] = phc_target_cnt
                    total_target += phc_target_cnt
                else:
                    tho_rep_data['daily_target'] = 0

                check_phc_target_cnt = Contact_Tracing.objects.filter(Q(assigned_phc = i['phc_master_id']) & Q(assigned_date= asdatetime.now().date())).count()
                tho_rep_data['no_of_patient_allotted'] = check_phc_target_cnt
                total_no_of_patient += check_phc_target_cnt

                check_phc_swab_coll = Contact_Tracing.objects.filter(Q(assigned_phc = i['phc_master_id']) & Q(assigned_date= asdatetime.now().date()) & Q(sample_collected= 1)).count()
                tho_rep_data['no_of_patient_swab_collected'] = check_phc_swab_coll
                total_no_of_swab_coll += check_phc_swab_coll

                tho_rep_data['balance']= check_phc_target_cnt - check_phc_swab_coll
                total_balance += check_phc_target_cnt - check_phc_swab_coll

                if tho_rep_data['daily_target'] and tho_rep_data['no_of_patient_allotted']:

                    rep_data.append(tho_rep_data)

        # rep_data.append({'total_target':total_target, 'total_no_of_patient':total_no_of_patient, 'total_no_of_swab_coll':total_no_of_swab_coll, 'total_balance':total_balance})
            
        return Response({'result': rep_data, 'total_pg_count': total_pg_count, 'total_target':total_target, 'total_no_of_patient':total_no_of_patient, 'total_no_of_swab_coll':total_no_of_swab_coll, 'total_balance':total_balance, 'message': 'Sucess'})







#########################      DSO SWAB DISPATCH DETAILS               #########################
class DSOTargetvsActualSwabCollectionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data 

        user_id = data.get('user_id')
        phc_id = data.get('phc_id')

        ct_data = Contact_Tracing.objects.filter(Q(assigned_phc= phc_id)).values()

        return Response({'result': ct_data, 'message':'Sucessfully'}, status= status.HTTP_200_OK)




#########################      DSO SWAB DISPATCH DETAILS               #########################
class DSOSwabDispatchDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        rep_data = []

        total_package_created = 0
        total_package_dispatched_lab = 0
        total_package_dispatched_to_tho = 0

        dso_data = DSO.objects.get(user_id= user_id)

        check_dso_tho = THO.objects.filter(dso_id= dso_data.id).values()
        check_dso_tho_count = THO.objects.filter(dso_id= dso_data.id).count()

        check_dso_tho_details = paginatorCreation(check_dso_tho, selected_page_no)

        for cdt in check_dso_tho_details:

            check_tho = THO.objects.get(user_id= cdt['user_id'])

            check_all_phc_details = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()

            for i in check_all_phc_details:
                
                tho_rep_data = {}

                master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

                tho_rep_data['phc_name'] = master_phc_details.phc_name


                check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= i['phc_master_id'])).values()

                swab_col_users = []

                for i in check_all_swab_collector:
                    if i['user_id'] not in swab_col_users:
                        swab_col_users.append(i['user_id'])

                # get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users)).values('create_timestamp__date').distinct()


                check_package_created = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users)).count()
                # check_package_received_mo = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(create_timestamp__date= i['create_timestamp__date']) & Q(package_type_status= 7)).count()
                check_package_dispatched_lab = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(package_type_status= 5)).count()
                check_package_accepted_tho = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 19) & Q(package_type_status= 9)).count()

                # package_sts_details = []

                tho_rep_data['no_of_package_created'] = check_package_created
                tho_rep_data['no_of_package_dis_lab'] = check_package_dispatched_lab
                tho_rep_data['no_of_package_acc_tho'] = check_package_accepted_tho


                total_package_created += check_package_created
                # total_package_acc_mo += check_package_received_mo
                total_package_dispatched_lab += check_package_dispatched_lab
                total_package_dispatched_to_tho += check_package_accepted_tho

                rep_data.append(tho_rep_data)

        # rep_data.append({'total_package_created':total_package_created, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho,})
        
        return Response({'result': rep_data, 'total_pg_count': check_dso_tho_count, 'total_package_created':total_package_created, 'total_package_dispatched_lab':total_package_dispatched_lab, 'total_package_dispatched_to_tho':total_package_dispatched_to_tho, 'message': 'Sucess'})





#########################      DSO PACKAGE LAB WISE REPORT               #########################
class DSOPackageLabWiseReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        dso_data = DSO.objects.get(user_id= user_id)

        check_dso_tho = THO.objects.filter(dso_id= dso_data.id).values()
        check_dso_tho_count = THO.objects.filter(dso_id= dso_data.id).count()

        check_dso_tho_details = paginatorCreation(check_dso_tho, selected_page_no)

        no_of_labs = 0
        total_samples = 0

        rep_data = []
        this_final_data = []

        for cdt in check_dso_tho_details:

            check_tho = THO.objects.get(user_id= cdt['user_id'])

            check_all_phc_details = Swab_Collection_Centre.objects.filter(Q(tho_id = check_tho.id) & Q(role_id= 6)).values()


            for i in check_all_phc_details:
                
                master_phc_details = Master_PHC.objects.get(id= i['phc_master_id'])

                check_all_swab_collector = Swab_Collection_Centre.objects.filter(Q(phc_master_id= i['phc_master_id'])).values()

                swab_col_users = []

                for j in check_all_swab_collector:
                    if j['user_id'] not in swab_col_users:
                        swab_col_users.append(j['user_id'])

                get_all_pack = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users)).values('test_lab_id').distinct()

                
                for k in get_all_pack:

                    if k['test_lab_id']:
                        tho_rep_data = {}
                        tho_rep_data['phc_name'] = master_phc_details.phc_name

                        no_of_labs += 1
                        lab_name = '-'
                        sample_count = 0

                        check_package_dis_lab = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(test_lab_id= k['test_lab_id'])).values()

                        if check_package_dis_lab:
                            
                            for l in check_package_dis_lab:

                                check_test_lab = Testing_Lab_Facility.objects.get(id= l['test_lab_id'])
                                lab_name_data = Master_Labs.objects.get(id= check_test_lab.testing_lab_master_id)

                                lab_name = lab_name_data.lab_name

                                check_package_sam_count = Package_Sampling.objects.filter(Q(user_id__in= swab_col_users) & Q(package_type_action= 15) & Q(test_lab_id= l['test_lab_id'])).values()

                                if check_package_sam_count:
                                    for m in check_package_sam_count:
                                        sample_count += int(m['samples_count'])
                                        total_samples += int(m['samples_count'])
                        
                        tho_rep_data['lab_name'] = lab_name
                        tho_rep_data['sample_count'] = sample_count
                        
                        this_final_data.append(tho_rep_data)
            
        # this_final_data.append({'no_of_labs':no_of_labs, 'total_samples':total_samples})

        return Response({'result': this_final_data, 'total_pg_count': check_dso_tho_count, 'no_of_labs':no_of_labs, 'total_samples':total_samples, 'message': 'Sucess'})





#########################      DSO DATE WISE COLLECTED SAMPLES               #########################
class DSODateWiseSamplesCollectionReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user_id= data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)


        dso_data = DSO.objects.filter(user_id= user_id)
        if dso_data:
            
            dso_data_get = DSO.objects.get(user_id= user_id)

            uniq_date_data = Patient.objects.filter( 
                added_by_id__in= User.objects.filter(
                    id__in= Swab_Collection_Centre.objects.filter(tho_id__in= THO.objects.filter(dso_id= dso_data_get.id).values_list('id', flat=True)).values_list('user_id', flat=True)
                        ).values_list('id', flat=True)
                        ).values('create_timestamp__date').order_by('-create_timestamp__date').distinct()
            
            uniq_date_data_count = Patient.objects.filter( 
                added_by_id__in= User.objects.filter(
                    id__in= Swab_Collection_Centre.objects.filter(tho_id__in= THO.objects.filter(dso_id= dso_data_get.id).values_list('id', flat=True)).values_list('user_id', flat=True)
                        ).values_list('id', flat=True)
                        ).values('create_timestamp__date').order_by('-create_timestamp__date').distinct().count()
            
            uniq_date_details = paginatorCreation(uniq_date_data, selected_page_no)

            for i in uniq_date_details:
                
                i['taluk_count'] = THO.objects.filter(dso_id= dso_data_get.id).count()
                i['samples_count'] = Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id__in= THO.objects.filter(dso_id= dso_data_get.id).values_list('id', flat=True)).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= i['create_timestamp__date'])).count()

            return Response({'result':list(uniq_date_details), 'total_pg_count': uniq_date_data_count}, status= status.HTTP_200_OK)
        else:
            return Response({'result': [], 'total_pg_count':0}, status=status.HTTP_400_BAD_REQUEST)






#########################      DSO DATE WISE COLLECTED SAMPLES TALUK VIEW1               #########################
class DSODateWiseTalukDatewiseSamplesCollectionReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user_id= data.get('user_id')
        date = data.get('date')

        dso_data = DSO.objects.filter(user_id= user_id)
        if dso_data:
            
            dso_data_get = DSO.objects.get(user_id= user_id)
            tho_data = THO.objects.filter(dso_id= dso_data_get.id).values()

            for i in tho_data:
                master_block = Master_Block.objects.get(id= i['city_id'])
                i['taluk_name'] = master_block.block_name_eng
                i['phc_count'] = Swab_Collection_Centre.objects.filter(Q(role_id= 6) & Q(tho_id= i['id'])).count()
                i['samples_count'] = Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id= i['id']).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()
                i['date'] = date

            return Response({'result':tho_data}, status= status.HTTP_200_OK)
        else:
            return Response({'result': []}, status=status.HTTP_400_BAD_REQUEST)


    
    
    



#########################      SSU DATE WISE TOTAL TARGET COUNT               #########################
class SSUDateWiseTotalTargetCountReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        data        = request.data
        id   = data.get('user_id')
        Arr=[]

        if id:
            if User.objects.filter(id=id).exists():
                all_contact_tracing = Contact_Tracing.objects.all().values('district','assigned_date__date').distinct()

                for i in all_contact_tracing:

                    date= i['assigned_date__date']
                    contact_tracing_assigned_cnt = Contact_Tracing.objects.filter(Q(district = i['district']) & Q(assigned_date__date= i['assigned_date__date'])).count()
                    contact_tracing_samp_coll = Contact_Tracing.objects.filter(Q(district = i['district']) & Q(assigned_date__date= i['assigned_date__date']) & Q(sample_collected= 1)).count()
                    contact_tracing_samp_pend = Contact_Tracing.objects.filter(Q(district = i['district']) & Q(assigned_date__date= i['assigned_date__date']) & Q(sample_collected= 0)).count()
                    # if i['assigned_msc_user_id'] == None:
                    #     i['status'] = 0
                    #     i['msc_name'] = 'N/A'
                    # else:
                    #     i['status'] = 1
                    #     check_user_name = User.objects.get(id= i['assigned_msc_user_id'])
                    #     i['msc_name'] = check_user_name.first_name

                    Arr.append({
                    # 'district_name':
                    'district_code':i['district'],
                    'date':date,

                    'assigned_count':contact_tracing_assigned_cnt,
                    'sample_collected_count':contact_tracing_samp_coll,
                    'pending_count':contact_tracing_samp_pend

                    })

                return Response({'Data':Arr})



#########################      SSU DATE WISE TOTAL TARGET COUNT DETAILS               #########################
class SSUViewTotalTargetCountDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data        = request.data
        date= data.get('date')
        disctric_code   = data.get('disctric_code')

        if date:
            date1= asdatetime.strptime(date,'%Y-%m-%d')
            if disctric_code:
                all_contact_tracing = Contact_Tracing.objects.filter(Q(district=disctric_code)&Q(assigned_date__date=date1)).values()

                return Response({'Data':all_contact_tracing})
            else:
                return Response('District Code Required')
        else:
            return Response('Date Required')



#########################      SSU SWAB COLLECTION TEAM               #########################
class SSUSwabCollectorsTeam(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        master_dist_data = Master_District.objects.all().values()
        master_dist_data_count = Master_District.objects.all().count()

        master_dist_details = paginatorCreation(master_dist_data, selected_page_no)

        for i in master_dist_details:
            
            filter_dso = DSO.objects.filter(district_id= i['id'])
            if filter_dso:
                get_dso_details = DSO.objects.get(district_id= i['id'])
                filter_tho = THO.objects.filter(dso_id= get_dso_details.id).values()
                i['no_of_tho'] = THO.objects.filter(dso_id= get_dso_details.id).count()

                if filter_tho:
                    for j in filter_tho:
                        filter_no_phc = Swab_Collection_Centre.objects.filter(Q(tho_id= j['id']) & Q(role_id= 6))
                        if filter_no_phc:
                            i['no_of_phc'] = Swab_Collection_Centre.objects.filter(Q(tho_id= j['id']) & Q(role_id= 6)).count()
                            i['phc_team_count'] = Swab_Collection_Centre.objects.filter(Q(tho_id= j['id'])).count()
                        else:
                            i['no_of_phc'] = 0
                            i['phc_team_count'] = 0
                else:
                    i['no_of_phc'] = 0
                    i['phc_team_count'] = 0
            
            else:
                i['no_of_tho'] = 0
                i['no_of_phc'] = 0
                i['phc_team_count'] = 0

        return Response({'result':list(master_dist_details), 'total_pg_count':master_dist_data_count}, status=status.HTTP_200_OK)




#########################      SSU TOTAL SAMPLE COLLECTED               #########################
class SSUTotalSampleCollected(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        start_date = data.get('from_date')
        end_date = data.get('to_date')

        print(data)

        master_dist_data = Master_District.objects.all().values()

        for i in master_dist_data:

            if start_date and end_date:

                start_data_split = start_date.split('-')
                end_date_split = end_date.split('-')

                print(start_data_split)
                print(end_date_split)
                        
            
                filter_dso = DSO.objects.filter(district_id= i['id'])
                if filter_dso:
                    get_dso_details = DSO.objects.get(district_id= i['id'])
                    filter_tho = THO.objects.filter(dso_id= get_dso_details.id).values()
                    i['no_of_tho'] = THO.objects.filter(dso_id= get_dso_details.id).count()


                    all_tho_users = []
                    if filter_tho:
                        for j in filter_tho:

                            get_all_swb_collector = Swab_Collection_Centre.objects.filter(Q(tho_id= j['id'])).values()

                            for gasc in get_all_swb_collector:
                                if gasc['user_id'] not in all_tho_users:
                                    all_tho_users.append(gasc['user_id'])



                            aa = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32)).count()
                            bb = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(test_type_id= 1)).count()
                            cc = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(test_type_id= 2)).count()
                            dd = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(patient_status= 'Symptomatic')).count()
                            ee = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(patient_status= 'Asymptomatic')).count()
                            print("aa", aa)
                            print("bb", bb)
                            print("cc", cc)
                            print("dd", dd)
                            print("ee", ee)




                            # i['total_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32)).count()
                            # i['total_rat_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(test_type_id= 1)).count()
                            # i['total_rtpcr_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(test_type_id= 2)).count()
                            # i['total_symptomatic_samples'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(patient_status= 'Symptomatic')).count()
                            # i['total_asymptomatic_samples'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date__gte= dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2]))) & Q(create_timestamp__date__lte= dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))) & Q(swab_collection_status= 32) & Q(patient_status= 'Asymptomatic')).count()
                            # i['date_from'] = str(dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2])))
                            # i['date_to'] = str(dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))

                            i['total_samples_collected'] = aa
                            i['total_rat_samples_collected'] = bb
                            i['total_rtpcr_samples_collected'] = cc
                            i['total_symptomatic_samples'] = dd
                            i['total_asymptomatic_samples'] = ee
                            i['date_from'] = str(dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2])))
                            i['date_to'] = str(dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))


                    else:
                        i['total_samples_collected'] = 0
                        i['total_rat_samples_collected'] = 0
                        i['total_rtpcr_samples_collected'] = 0
                        i['total_symptomatic_samples'] = 0
                        i['total_asymptomatic_samples'] = 0
                        i['date_from'] = str(dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2])))
                        i['date_to'] = str(dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))

                
                else:
                    i['no_of_tho'] = 0
                    i['total_samples_collected'] = 0
                    i['total_rat_samples_collected'] = 0
                    i['total_rtpcr_samples_collected'] = 0
                    i['total_symptomatic_samples'] = 0
                    i['total_asymptomatic_samples'] = 0
                    i['date_from'] = str(dt(int(start_data_split[0]), int(start_data_split[1]), int(start_data_split[2])))
                    i['date_to'] = str(dt(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2])))


            else:

                filter_dso = DSO.objects.filter(district_id= i['id'])
                if filter_dso:
                    get_dso_details = DSO.objects.get(district_id= i['id'])
                    filter_tho = THO.objects.filter(dso_id= get_dso_details.id).values()
                    i['no_of_tho'] = THO.objects.filter(dso_id= get_dso_details.id).count()

                    if filter_tho:
                        all_tho_users = []
                        for j in filter_tho:

                            get_all_swb_collector = Swab_Collection_Centre.objects.filter(Q(tho_id= j['id'])).values()

                            for gasc in get_all_swb_collector:
                                if gasc['user_id'] not in all_tho_users:
                                    all_tho_users.append(gasc['user_id'])


                        i['total_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date= asdatetime.now().date()) & Q(swab_collection_status= 32)).count()
                        i['total_rat_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date= asdatetime.now().date()) & Q(swab_collection_status= 32) & Q(test_type_id= 1)).count()
                        i['total_rtpcr_samples_collected'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date= asdatetime.now().date()) & Q(swab_collection_status= 32) & Q(test_type_id= 2)).count()
                        i['total_symptomatic_samples'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date= asdatetime.now().date()) & Q(swab_collection_status= 32) & Q(patient_status= 'Symptomatic')).count()
                        i['total_asymptomatic_samples'] = Patient.objects.filter(Q(added_by_id__in= all_tho_users) & Q(create_timestamp__date= asdatetime.now().date()) & Q(swab_collection_status= 32) & Q(patient_status= 'Asymptomatic')).count()
                        i['date_from'] = str(asdatetime.now())
                        i['date_to'] = str(asdatetime.now())
                    else:
                        i['total_samples_collected'] = 0
                        i['total_rat_samples_collected'] = 0
                        i['total_rtpcr_samples_collected'] = 0
                        i['total_symptomatic_samples'] = 0
                        i['total_asymptomatic_samples'] = 0
                        i['date_from'] = str(asdatetime.now())
                        i['date_to'] = str(asdatetime.now())

                
                else:
                    i['no_of_tho'] = 0
                    i['total_samples_collected'] = 0
                    i['total_rat_samples_collected'] = 0
                    i['total_rtpcr_samples_collected'] = 0
                    i['total_symptomatic_samples'] = 0
                    i['total_asymptomatic_samples'] = 0
                    i['date_from'] = str(asdatetime.now())
                    i['date_to'] = str(asdatetime.now())


        return Response({'result':master_dist_data}, status=status.HTTP_200_OK)




#########################      SSU DATE WISE GENERATED PACKAGE REPORT               #########################
class SSUDateWiseGeneratedPackageReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        id = data.get('user_id')
        Arr=[]

        if id:
            if User.objects.filter(id=id).exists():
                all_Package_Sampling = Package_Sampling.objects.all().values('master_phc_id','create_timestamp__date').distinct()
                for i in all_Package_Sampling:
                    
                    date= i['create_timestamp__date']
                    package_details = Package_Sampling.objects.filter(Q(master_phc_id = i['master_phc_id']) & Q(create_timestamp__date= i['create_timestamp__date']))
                    phc_name = ''
                    for j in package_details:
                        phc_name = j.master_phc.phc_name
                    package_count = Package_Sampling.objects.filter(Q(master_phc_id = i['master_phc_id']) & Q(create_timestamp__date= i['create_timestamp__date'])).count()
                    
                    Arr.append({'date':date, 'master_phc_id':i['master_phc_id'],'phc_name':phc_name,'total_packege_count':package_count})

        return Response({'result':Arr})



#########################      SSU DATE WISE GENERATED PACKAGE REPORT DETAILS               #########################
class SSUDateWiseGeneratedPackageDetailsReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data        = request.data
        date= data.get('date')
        id   = data.get('user_id')
        master_phc_id = data.get('master_phc_id')

        if date:
            date1= asdatetime.strptime(date,'%Y-%m-%d')
            if id:
                all_Package_Sampling = Package_Sampling.objects.filter(Q(master_phc_id= master_phc_id) & Q(create_timestamp__date=date)).values()

                for i in all_Package_Sampling:
                    lab_master = Master_Labs.objects.filter(id= i['lab_master_id'])
                    if lab_master:
                        lab_master = Master_Labs.objects.get(id= i['lab_master_id'])
                        i['lab_name'] = lab_master.lab_name
                    else:
                        i['lab_name'] = '-'

                return Response({'result':all_Package_Sampling})
            else:
                return Response('Invalid User')
        else:
            return Response('Date Required')





#########################      SSU DATE WISE COLLECTED SAMPLES               #########################
class SSUDateWiseSamplesCollectionReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        page_no = self.request.query_params.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        uniq_date = Patient.objects.all().values('create_timestamp__date').order_by('-create_timestamp__date').distinct()
        all_data_count = Patient.objects.all().values('create_timestamp__date').order_by('-create_timestamp__date').distinct().count()
        
        uniq_details = paginatorCreation(uniq_date, selected_page_no)

        # paginator = Paginator(uniq_date, 10)
        # try:
        #     uniq_details = paginator.page(selected_page_no)
        # except PageNotAnInteger:
        #     uniq_details = paginator.page(1)
        # except EmptyPage:
        #     uniq_details = paginator.page(paginator.num_pages)

        for i in uniq_details:
            i['district_count'] = DSO.objects.all().count()
            dso_details = DSO.objects.all().values()

            dist_samp_cnt = 0
            for j in dso_details:
                get_tho_data = THO.objects.filter(dso_id= j['id']).values_list('id', flat=True)
                print(get_tho_data)
                
                dist_samp_cnt += Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id__in= get_tho_data).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= i['create_timestamp__date'])).count()

            i['samples_collected'] = dist_samp_cnt

        return Response({'result':list(uniq_details), 'total_pg_count':all_data_count}, status= status.HTTP_200_OK)






#########################      SSU DATE WISE COLLECTED SAMPLES VIEW1               #########################
class SSUDateWiseDistrictWiseSamplesCollectionCountReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        date = data.get('date')

        dso_smp_details = DSO.objects.all().values()

        for i in dso_smp_details:
            get_dist_data = Master_District.objects.get(id= i['district_id'])
            i['district_name'] = get_dist_data.district_name_eng
            i['taluk_count'] = THO.objects.filter(dso_id= i['id']).count()
            dist_samp_cnt = 0
            # get_tho_data = THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)
            
            dist_samp_cnt += Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id__in= THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()

            i['samples_collected'] = dist_samp_cnt
            i['date'] = date

        return Response({'result':dso_smp_details}, status= status.HTTP_200_OK)
        # else:

        #     dso_smp_details = DSO.objects.all().values()

        #     for i in dso_smp_details:
        #         get_dist_data = Master_District.objects.get(id= i['district_id'])
        #         i['district_name'] = get_dist_data.district_name_eng
        #         i['taluk_count'] = THO.objects.filter(dso_id= i['id']).count()
        #         dist_samp_cnt = 0
        #         # get_tho_data = THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)
                
        #         dist_samp_cnt += Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id__in= THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()

        #         i['samples_collected'] = dist_samp_cnt
        #         i['date'] = date

        #     return Response({'result':dso_smp_details}, status= status.HTTP_200_OK)



#########################      SSU DATE WISE COLLECTED SAMPLES VIEW2               #########################
class SSUDateWiseDistrictWiseTalukWiseSamplesCollectionCountReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        date = data.get('date')
        dso_id = data.get('dso_id')

        tho_smp_details = THO.objects.filter(dso_id= dso_id).values()

        for i in tho_smp_details:
            get_block_data = Master_Block.objects.get(id= i['city_id'])
            i['block_name'] = get_block_data.block_name_eng
            i['phc_count'] = Swab_Collection_Centre.objects.filter(Q(tho_id= i['id']) & Q(role_id= 6)).count()
            dist_samp_cnt = 0
            # get_tho_data = THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)
            
            dist_samp_cnt += Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(tho_id= i['id']).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()

            i['samples_collected'] = dist_samp_cnt
            i['date'] = date

        return Response({'result':tho_smp_details}, status= status.HTTP_200_OK)




#########################      SSU DSO DATE WISE COLLECTED SAMPLES VIEW3               #########################
class SSUDSODateWiseDistrictWiseTalukWisePHCwiseSamplesCollectionCountReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        date = data.get('date')
        tho_id = data.get('tho_id')

        scc_smp_details = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_id) & Q(role_id= 6)).values()

        for i in scc_smp_details:
            get_phc_data = Master_PHC.objects.get(id= i['phc_master_id'])
            i['phc_name'] = get_phc_data.phc_name
            # i['phc_count'] = Swab_Collection_Centre.objects.filter(Q(tho_id= i['id']) & Q(role_id= 6)).count()
            dist_samp_cnt = 0
            # get_tho_data = THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)
            
            dist_samp_cnt += Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(phc_master_id= i['phc_master_id']).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).count()

            i['samples_collected'] = dist_samp_cnt
            i['date'] = date

        return Response({'result':scc_smp_details}, status= status.HTTP_200_OK)



#########################      SSU DATE WISE COLLECTED SAMPLES VIEW4               #########################
class SSUDSOTHODateWiseDistrictWiseTalukWisePHCwiseSamplesCollectionDetailsReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        date = data.get('date')
        scc_id = data.get('ssc_id')

        scc_smp_details = Swab_Collection_Centre.objects.filter(Q(id= scc_id) & Q(role_id= 6)).values()

        if scc_smp_details:

            scc_smp_details = Swab_Collection_Centre.objects.get(Q(id= scc_id) & Q(role_id= 6))

            get_phc_data = Master_PHC.objects.get(id= scc_smp_details.phc_master_id)

            patient_details = Patient.objects.none()
            # i['phc_count'] = Swab_Collection_Centre.objects.filter(Q(tho_id= i['id']) & Q(role_id= 6)).count()
            # dist_samp_cnt = 0
            # get_tho_data = THO.objects.filter(dso_id= i['id']).values_list('id', flat=True)
            
            patient_details = Patient.objects.filter(Q(added_by_id__in= User.objects.filter(id__in= Swab_Collection_Centre.objects.filter(phc_master_id= scc_smp_details.phc_master_id).values_list('user_id', flat=True)).values_list('id', flat=True)) & Q(create_timestamp__date= date)).values()

            for i in patient_details:
                test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                spcm_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])

                i['test_type_name'] = test_type_data.test_type_name
                i['specimen_type_name'] = spcm_type_data.specimen_type_name

                # i['samples_collected'] = dist_samp_cnt
                i['date'] = date

            return Response({'result':patient_details}, status= status.HTTP_200_OK)
        else:
            return Response({'result': 'Something Went Wrong'}, status= status.HTTP_400_BAD_REQUEST)


        
        
        
        


#########################      SSU DATE WISE GENERATED PACKAGE REPORT DETAILS               #########################





#########################      LAB WISE DELAY REPORT               #########################
class SSUGetLabwiseDelayReportTest(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """def get (self,request):
        Arr=[]
        timeStamp=0
        new_time=0
        master_lab =   Master_Labs.objects.all()
        print(master_lab)
        for i in master_lab:
    
            Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
            print(Total_test_entered,'ttt')
            lab_name=i.lab_name
            lab_type=i.lab_type
            Total_test_entered=Total_test_entered
    
    
            D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
            patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
            for i in patient_testing_Obj:
                timeStamp=i.create_timestamp
            new_time=timeStamp
            hour=0
            seconds=0
            minutes=0
            ste_var = set()
            max_Delay=0
            min_Delay=0
            avg_Delay=0
            count1=0
            t_count1=0
            count2=0
            t_count2=0
            count3=0
            t_count3=0
            avg_day=0
            avg_day1=0
            avg1=0
            avg=0
            delay_pect=0
            delay_pect1=0
            for i in D1:
                t_count=count1
                t_count2=count2
                t_count3=count3
                D1_calculation=[]
                new=[]
                D1_cal= i.create_timestamp - new_time
                days = D1_cal.days
                seconds = D1_cal.seconds
                hours = seconds//3600
                minutes = (seconds//60)%60
                seconds %= 60
    
                D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
    
                for i in D1_data:
                    D1_calculation.append(i)
                    new.append(D1_calculation)
    
                if new[1][2]>=0:
                    count1=count1+new[1][2]
    
                avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                # ="{:.1%}".format(h_48)
                avg1=("%.2f" %avg)
    
                if new[1][0]>=0:
                    count2=count2+new[1][0]
                avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                avg_day1=("%.2f" %avg_day)
    
                if new[1][6]>0:
                    count3=count3+1
                delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                delay_pect1="{:.1%}".format(delay_pect)
    
            Arr.append({
                        'Lab_name':lab_name,
                        'Lab_type':lab_type,
                        'Total_test_entered':Total_test_entered,
                        'max_days_of_delay_by_the_lab':max_Delay,
                        'avg_time_taken_for_all_the_test_hours':avg1,
                        'no_of_delay_report':count3,
                        'per_of_delay_report':delay_pect1,
                        'avg_delay_day':avg_day1,
                      })
        return Response({'data':Arr,'result':' Sucessfully'})"""

    def post (self,request):
        data        = request.data
        id   = data.get('user_id')
        datef   = data.get('from_date')
        datet   = data.get('to_date')
        if data.get('id') is '':
            return Response("user id required ")

        elif User.objects.filter(id=id).exists():

            if datet and datef:
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet=date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    
                    D1=  Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name))
                    
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60

                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']

                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)

                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        
                        avg1=("%.2f" %avg)

                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)

                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        
                    Arr.append({
                                'Lab_name':lab_name,
                                'Lab_type':lab_type,
                                'Total_test_entered':Total_test_entered,
                                'max_days_of_delay_by_the_lab':max_Delay,
                                'avg_time_taken_for_all_the_test_hours':avg1,
                                'no_of_delay_report':count3,
                                'per_of_delay_report':delay_pect1,
                                'avg_delay_day':avg_day1,
                                })
                return Response({'data':Arr,'result':' Sucessfully'})

            else:
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    
                    D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
                    
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60
                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)
                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)
                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)
                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    Arr.append({
                                'Lab_name':lab_name, 'Lab_type':lab_type, 'Total_test_entered':Total_test_entered,
                                'max_days_of_delay_by_the_lab':max_Delay, 'avg_time_taken_for_all_the_test_hours':avg1,
                                'no_of_delay_report':count3, 'per_of_delay_report':delay_pect1, 'avg_delay_day':avg_day1,
                                })
                return Response({'data':Arr,'result':' Sucessfully'})                
        else:
            return Response("user not found")





            """if data.get('from_date') is None:
                print('111111')
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                print(master_lab)
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    print(Total_test_entered,'ttt')
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    # #!-------------------------------------------------------------------------------------------------------------------------------------
                    D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
                    print(i.lab_name)
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    print(new_time,'gfgf')
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60
                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)
                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)
                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)
                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    Arr.append({
                    'Lab_name':lab_name,
                    'Lab_type':lab_type,
                    'Total_test_entered':Total_test_entered,
                    'max_days_of_delay_by_the_lab':max_Delay,
                    'avg_time_taken_for_all_the_test_hours':avg1,
                    'no_of_delay_report':count3,
                    'per_of_delay_report':delay_pect1,
                    'avg_delay_day':avg_day1,
                            })
                return Response({
                'data':Arr,
                'result':' Sucessfully'
                })
            else:
                print('else')
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet=date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                print(master_lab)
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    print(Total_test_entered,'ttt')
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    # #!-------------------------------------------------------------------------------------------------------------------------------------
                    D1=  Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name))
                    print(i.lab_name)
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    print(new_time,'gfgf')
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60

                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']

                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)

                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)

                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)

                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    Arr.append({
                    'Lab_name':lab_name,
                    'Lab_type':lab_type,
                    'Total_test_entered':Total_test_entered,
                    'max_days_of_delay_by_the_lab':max_Delay,
                    'avg_time_taken_for_all_the_test_hours':avg1,
                    'no_of_delay_report':count3,
                    'per_of_delay_report':delay_pect1,
                    'avg_delay_day':avg_day1,
                            })
                return Response({
                'data':Arr,
                'result':' Sucessfully'
                })
        else:
            return Response("user not found")"""

            


#########################      LAB WISE DELAY REPORT               #########################
class SSUGetLabwiseDelayReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """def get (self,request):
        Arr=[]
        timeStamp=0
        new_time=0
        master_lab =   Master_Labs.objects.all()
        print(master_lab)
        for i in master_lab:
    
            Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
            print(Total_test_entered,'ttt')
            lab_name=i.lab_name
            lab_type=i.lab_type
            Total_test_entered=Total_test_entered
    
    
            D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
            patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
            for i in patient_testing_Obj:
                timeStamp=i.create_timestamp
            new_time=timeStamp
            hour=0
            seconds=0
            minutes=0
            ste_var = set()
            max_Delay=0
            min_Delay=0
            avg_Delay=0
            count1=0
            t_count1=0
            count2=0
            t_count2=0
            count3=0
            t_count3=0
            avg_day=0
            avg_day1=0
            avg1=0
            avg=0
            delay_pect=0
            delay_pect1=0
            for i in D1:
                t_count=count1
                t_count2=count2
                t_count3=count3
                D1_calculation=[]
                new=[]
                D1_cal= i.create_timestamp - new_time
                days = D1_cal.days
                seconds = D1_cal.seconds
                hours = seconds//3600
                minutes = (seconds//60)%60
                seconds %= 60
    
                D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
    
                for i in D1_data:
                    D1_calculation.append(i)
                    new.append(D1_calculation)
    
                if new[1][2]>=0:
                    count1=count1+new[1][2]
    
                avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                # ="{:.1%}".format(h_48)
                avg1=("%.2f" %avg)
    
                if new[1][0]>=0:
                    count2=count2+new[1][0]
                avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                avg_day1=("%.2f" %avg_day)
    
                if new[1][6]>0:
                    count3=count3+1
                delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                delay_pect1="{:.1%}".format(delay_pect)
    
            Arr.append({
                        'Lab_name':lab_name,
                        'Lab_type':lab_type,
                        'Total_test_entered':Total_test_entered,
                        'max_days_of_delay_by_the_lab':max_Delay,
                        'avg_time_taken_for_all_the_test_hours':avg1,
                        'no_of_delay_report':count3,
                        'per_of_delay_report':delay_pect1,
                        'avg_delay_day':avg_day1,
                      })
        return Response({'data':Arr,'result':' Sucessfully'})"""

    def post (self,request):

        data        = request.data
        id   = data.get('user_id')
        datef   = data.get('from_date')
        datet   = data.get('to_date')
        if data.get('id') is '':
            return Response("user id required ")

        elif User.objects.filter(id=id).exists():

            if datet and datef:
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet=date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                timeStamp=0
                new_time=0

                master_lab =   Master_Labs.objects.all()
                
                for i in master_lab:

                    Total_test_entered = Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    
                    D1=  Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name))
                    
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60

                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']

                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)

                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        
                        avg1=("%.2f" %avg)

                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)

                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                    
                    if Total_test_entered != 0:       
                        Arr.append({
                                    'Lab_name':lab_name,
                                    'Lab_type':lab_type,
                                    'Total_test_entered':Total_test_entered,
                                    'max_days_of_delay_by_the_lab':max_Delay,
                                    'avg_time_taken_for_all_the_test_hours':avg1,
                                    'no_of_delay_report':count3,
                                    'per_of_delay_report':delay_pect1,
                                    'avg_delay_day':avg_day1,
                                    })
                return Response({'data':Arr,'result':' Sucessfully'})

            else:
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    
                    D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
                    
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60
                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)
                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)
                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)
                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    if Total_test_entered != 0:
                        Arr.append({
                                    'Lab_name':lab_name, 'Lab_type':lab_type, 'Total_test_entered':Total_test_entered,
                                    'max_days_of_delay_by_the_lab':max_Delay, 'avg_time_taken_for_all_the_test_hours':avg1,
                                    'no_of_delay_report':count3, 'per_of_delay_report':delay_pect1, 'avg_delay_day':avg_day1,
                                    })
                return Response({'data':Arr,'result':' Sucessfully'})                
        else:
            return Response("user not found")





            """if data.get('from_date') is None:
                print('111111')
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                print(master_lab)
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    print(Total_test_entered,'ttt')
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    # #!-------------------------------------------------------------------------------------------------------------------------------------
                    D1=  Patient.objects.filter(Q(lab_master__lab_name__icontains=i.lab_name))
                    print(i.lab_name)
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    print(new_time,'gfgf')
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60
                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)
                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)
                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)
                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    Arr.append({
                    'Lab_name':lab_name,
                    'Lab_type':lab_type,
                    'Total_test_entered':Total_test_entered,
                    'max_days_of_delay_by_the_lab':max_Delay,
                    'avg_time_taken_for_all_the_test_hours':avg1,
                    'no_of_delay_report':count3,
                    'per_of_delay_report':delay_pect1,
                    'avg_delay_day':avg_day1,
                            })
                return Response({
                'data':Arr,
                'result':' Sucessfully'
                })
            else:
                print('else')
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet=date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                timeStamp=0
                new_time=0
                master_lab =   Master_Labs.objects.all()
                print(master_lab)
                for i in master_lab:

                    Total_test_entered          =   Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name)).count()
                    print(Total_test_entered,'ttt')
                    lab_name=i.lab_name
                    lab_type=i.lab_type
                    Total_test_entered=Total_test_entered
                    # #!-------------------------------------------------------------------------------------------------------------------------------------
                    D1=  Patient.objects.filter(Q(create_timestamp__gte=datef,create_timestamp__lt=datet)& Q(lab_master__lab_name__icontains=i.lab_name))
                    print(i.lab_name)
                    patient_testing_Obj=Patient_Testing.objects.filter(Q(patient__lab_master=i.pk))
                    for i in patient_testing_Obj:
                        timeStamp=i.create_timestamp
                    new_time=timeStamp
                    print(new_time,'gfgf')
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = set()
                    max_Delay=0
                    min_Delay=0
                    avg_Delay=0
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    avg_day=0
                    avg_day1=0
                    avg1=0
                    avg=0
                    delay_pect=0
                    delay_pect1=0
                    for i in D1:
                        t_count=count1
                        t_count2=count2
                        t_count3=count3
                        D1_calculation=[]
                        new=[]
                        D1_cal= i.create_timestamp - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60

                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']

                        for i in D1_data:
                            D1_calculation.append(i)
                            new.append(D1_calculation)

                        if new[1][2]>=0:
                            count1=count1+new[1][2]

                        avg=(count1/Total_test_entered)if Total_test_entered != 0 else 0
                        # ="{:.1%}".format(h_48)
                        avg1=("%.2f" %avg)

                        if new[1][0]>=0:
                            count2=count2+new[1][0]
                        avg_day=(count2/Total_test_entered)if Total_test_entered != 0 else 0
                        avg_day1=("%.2f" %avg_day)

                        if new[1][6]>0:
                            count3=count3+1
                        delay_pect=(count3/Total_test_entered)if Total_test_entered != 0 else 0
                        delay_pect1="{:.1%}".format(delay_pect)
                        # delay_pect1=("%.2f" %delay_pect)
                    Arr.append({
                    'Lab_name':lab_name,
                    'Lab_type':lab_type,
                    'Total_test_entered':Total_test_entered,
                    'max_days_of_delay_by_the_lab':max_Delay,
                    'avg_time_taken_for_all_the_test_hours':avg1,
                    'no_of_delay_report':count3,
                    'per_of_delay_report':delay_pect1,
                    'avg_delay_day':avg_day1,
                            })
                return Response({
                'data':Arr,
                'result':' Sucessfully'
                })
        else:
            return Response("user not found")"""

            
            
 


#########################      OVERALL LAB WISE DELAY REPORT               #########################
class SSUGetOverallLabDelayD4(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post (self,request):
        data        = request.data


        id   = data.get('user_id')
        datef   = data.get('from_date')
        datet   = data.get('to_date')

        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        if data.get('user_id') is '':

            return Response("user id required ")

        elif User.objects.filter(id=id).exists():
            if datef and datet:
                print('1111')
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet= date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                new_time=0
                timeStamp=0
                timeStamps=0
                new_times_temp=0
                new_times_temps=0

                master_dist =   Master_District.objects.all()
                master_dist_count = Master_District.objects.all().count()

                master_dist_details = paginatorCreation(master_dist, selected_page_no)
                
                for i in master_dist_details:
                    total_test  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()

                    District_name=i.district_code
                    total_Test_District=total_test

                    D1=  Patient_Address.objects.filter(Q(district_name=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet))
                    print(D1,"D")
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = list()
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    count4=0
                    t_count4=0
                    h_24=0
                    h1_24=0
                    h_24_48=0
                    h1_24_48=0
                    h_48=0
                    h1_48=0
                    pk_value=0
                    for i in D1:
                        # print("UUUUUUUUUUUUUUUUUUUU", i.patient.pk)
                        patient_sample_created_date=Patient.objects.filter( Q(id= i.patient.pk))
                        print(patient_sample_created_date,'obj')
                        for j in patient_sample_created_date:
                            new_times_temp=j.create_timestamp
                        new_time=new_times_temp
                        print(new_time,'fd')

                        patient_testing_created_date = Patient_Testing.objects.filter(Q(patient__pk= i.patient.pk))
                        for k in patient_testing_created_date:
                            new_times_temps=k.create_timestamp
                        new_times= new_times_temps
                        print(new_times,'fd')
                        # if patient_testing_created_date:
                        t_count1=count1
                        t_count2=count2
                        t_count3=count3
                        t_count4=count4
                        D1_calculation=[]
                        new=[]
                        D1_cal=new_times - new_time
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60
                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for l in D1_data:
                            D1_calculation.append(l)
                            new.append(D1_calculation)
                        if new[1][0]==0:
                            count1=count1+1
                        h_24=(count1/total_test)if total_test != 0 else 0
                        h1_24="{:.1%}".format(h_24)
                        if new[1][0]==1:
                            count2=count2+1
                        h_24_48=(count2/total_test)if total_test != 0 else 0
                        h1_24_48="{:.1%}".format(h_24_48)
                        if new[1][0]>=2:
                            count3=count3+1
                        h_48=(count3/total_test)if total_test != 0 else 0
                        h1_48="{:.1%}".format(h_48)
                        if new[1][0]>=0:
                            count4=count4+new[1][0]

                    Arr.append({
                    'district_name':District_name,
                    'total_Test_District':total_Test_District,
                    'result_given_with_in_24hours':count1,
                    'per_of_result_given_within_24hours':h1_24,
                    'result_given_in_24_to_48hours':count2,
                    'per_of_result_given_in_24_to_48hours':h1_24_48,
                    'result_given_after_48hours':count3,
                    'per_of_result_given_after_48hours':h1_48,
                    'overall_time_taken_and_providing_report_in_Days':count4
                            })

                return Response({'data':Arr,'total_pg_count':master_dist_count,'result':' Sucessfully'})

            else:
                print('else')
                Arr=[]
                new_time=0
                timeStamp=0
                timeStamps=0
                new_times_temp=0
                new_times_temps=0

                master_dist =   Master_District.objects.all()
                master_dist_count = Master_District.objects.all().count()

                master_dist_details = paginatorCreation(master_dist, selected_page_no)

                for i in master_dist_details:
                    total_test  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)).count()
                    District_name=i.district_code
                    total_Test_District=total_test
                    D1=  Patient_Address.objects.filter(Q(district_name=i.district_code))
                    print(D1,"D")
                    hour=0
                    seconds=0
                    minutes=0
                    ste_var = list()
                    count1=0
                    t_count1=0
                    count2=0
                    t_count2=0
                    count3=0
                    t_count3=0
                    count4=0
                    t_count4=0
                    h_24=0
                    h1_24=0
                    h_24_48=0
                    h1_24_48=0
                    h_48=0
                    h1_48=0
                    pk_value=0
                    for i in D1:
                        # print("UUUUUUUUUUUUUUUUUUUU", i.patient.pk)
                        patient_sample_created_date= Patient.objects.filter(Q(id= i.patient.pk))
                        # new_time_temp = datetime.now()
                        for j in patient_sample_created_date:
                            new_times_temp=j.create_timestamp
                        new_time=new_times_temp

                        # print("UUUUUUUUUUUUUUUUUUUU", new_time)


                        patient_testing_created_date = Patient_Testing.objects.filter(Q(patient__pk= i.patient.pk))
                        # print(patient_testing_created_date,'/')
                        # new_times_temps = datetime.now()
                        for k in patient_testing_created_date:
                            new_times_temps=k.create_timestamp
                        new_times= new_times_temps
                        print("UUUUUUUUUUUUUUUUUUUU", new_times)


                        # if patient_testing_created_date:
                        t_count1=count1
                        t_count2=count2
                        t_count3=count3
                        t_count4=count4
                        D1_calculation=[]
                        new=[]
                        D1_cal=new_time - new_times
                        days = D1_cal.days
                        seconds = D1_cal.seconds
                        hours = seconds//3600
                        minutes = (seconds//60)%60
                        seconds %= 60

                        D1_data=[days,'days',hours,'hours',minutes,'mint',seconds,'sec']
                        for l in D1_data:
                            D1_calculation.append(l)
                            new.append(D1_calculation)
                        if new[1][0]==0:
                            count1=count1+1
                        h_24=(count1/total_test)if total_test != 0 else 0
                        h1_24="{:.1%}".format(h_24)
                        if new[1][0]==1:
                            count2=count2+1
                        h_24_48=(count2/total_test)if total_test != 0 else 0
                        h1_24_48="{:.1%}".format(h_24_48)
                        if new[1][0]>=2:
                            count3=count3+1
                        h_48=(count3/total_test)if total_test != 0 else 0
                        h1_48="{:.1%}".format(h_48)
                        if new[1][0]>=0:
                            count4=count4+new[1][0]

                    Arr.append({
                    'district_name':District_name,
                    'total_Test_District':total_Test_District,
                    'result_given_with_in_24hours':count1,
                    'per_of_result_given_within_24hours':h1_24,
                    'result_given_in_24_to_48hours':count2,
                    'per_of_result_given_in_24_to_48hours':h1_24_48,
                    'result_given_after_48hours':count3,
                    'per_of_result_given_after_48hours':h1_48,
                    'overall_time_taken_and_providing_report_in_Days':count4
                            })


                return Response({'data':Arr,'total_pg_count':master_dist_count,'result':' Sucessfully'})

        else:
            return Response("user not found")






#########################      SYMPTOMATIC  ASYMPTOMATIC POSITIVITY RATE REPORT              #########################
class SSUGetMasterSysAsym(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):

        page_no = self.request.query_params.get('page_no')

        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        Arr=[]
        id=0
        new_id=0
        master_dist =   Master_District.objects.all()
        master_dist_count = Master_District.objects.all().count()

        master_dist_details = paginatorCreation(master_dist, selected_page_no)

        for i in master_dist_details:
            total_test  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)).count()
            patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code))
            for j in patientObj:
                id=j.patient.pk
            new_id=id
            # print(new_id)
            District_name=i.district_code
            total_Test_District=total_test
            #!--------------------------------  Symptomatic  -----------------------------------------------------------------------------------------------------

            #!-------------------------------------------------------------------------------------------------------------------------------------
            tested_symptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Symptomatic')).count()
            try:
                tested_sym          =   tested_symptomatic/total_test
            except ZeroDivisionError:
                tested_sym  =  0
            tested_sym_per      =   "{:.0%}".format(tested_sym)

            #!-------------------------------------------------------------------------------------------------------------------------------------
            sym_pos             =   Patient_Testing.objects.filter(Q(patient__patient_status='Symptomatic')&Q(testing_status__in=['1','3'])&Q(patient__pk=new_id)).count()
            print(sym_pos,'sysPo')
            # sym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Symptomatic')).count()

            # print(sym_pos,'sys')
            try:
                sym_positivity      =   sym_pos/total_test
            except ZeroDivisionError:
                sym_positivity  =  0
            sym_positivity_per  =   "{:.0%}".format(sym_positivity)

            # #!--------------------------------- ASymptomatic ----------------------------------------------------------------------------------------------------


            tested_Asymptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Asymptomatic')).count()
            try:
                tested_asym          =   tested_Asymptomatic/total_test
            except ZeroDivisionError:
                tested_asym  =  0
            tested_asym_per      =   "{:.0%}".format(tested_asym)

            asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=[1,3]) & Q(patient__patient_status='Asymptomatic')&Q(patient__pk=new_id)).count()
            # asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Asymptomatic')).count()
            try:
                asym_positivity      =   asym_pos/total_test
            except ZeroDivisionError:
                asym_positivity  =  0
            asym_positivity_per  =   "{:.0%}".format(asym_positivity)
            try:
                total_positivity        =   (sym_positivity+asym_positivity)/total_test
                print(total_positivity,'pos')
            except ZeroDivisionError:
                total_positivity  =  0

            total_positivity_per    =   "{:.0%}".format(total_positivity)

            Arr.append({
            'District_name':i.district_name_eng,
            # 'District_repeated_count':dist_cnt,
            'Total_Test_District':total_test,

            'Symptomatic_tested':tested_symptomatic,
            'Symptomatic_tested_per':tested_sym_per,
            'Symptomatic_positives':sym_pos,
            'Symptomatic_positives_per':sym_positivity_per,

            'Asymptomatic_tested':tested_Asymptomatic,
            'Asymptomatic_tested_per':tested_asym_per,
            'Asymptomatic_positives':asym_pos,
            'Asymptomatic_positives_per':asym_positivity_per,

            # 'Positives_without_Sym_Asym':pos,
            'Total_Positivity_per':total_positivity_per
            })
        return Response({'data':Arr, 'total_pg_count':master_dist_count,'result':' Sucessfully'})

    def post (self,request):
        data        = request.data
        id   = data.get('user_id')
        datef   = data.get('from_date')
        datet   = data.get('to_date')

        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)


        if data.get('user_id') is '':
            return Response("user id required ")

        elif User.objects.filter(id=id).exists():

            if datef and datet:
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet= date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                id=0
                new_id=0

                master_dist =   Master_District.objects.all()
                master_dist_count = Master_District.objects.all().count()

                master_dist_details = paginatorCreation(master_dist, selected_page_no)

                for i in master_dist_details:
                    total_test  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet))
                    for j in patientObj:
                        id=j.patient.pk
                    new_id=id
                    print(new_id,'iii')
                    District_name=i.district_code
                    total_Test_District=total_test
                    #!--------------------------------  Symptomatic  -----------------------------------------------------------------------------------------------------

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    tested_symptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Symptomatic')&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    try:
                        tested_sym          =   tested_symptomatic/total_test
                    except ZeroDivisionError:
                        tested_sym  =  0
                    tested_sym_per      =   "{:.0%}".format(tested_sym)

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    sym_pos             =   Patient_Testing.objects.filter(Q(patient__patient_status='Symptomatic')&Q(testing_status__in=['1','3'])&Q(patient__pk=new_id)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    print(sym_pos,'sysPo')
                    # sym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Symptomatic')).count()

                    # print(sym_pos,'sys')
                    try:
                        sym_positivity      =   sym_pos/total_test
                    except ZeroDivisionError:
                        sym_positivity  =  0
                    sym_positivity_per  =   "{:.0%}".format(sym_positivity)

                    # #!--------------------------------- ASymptomatic ----------------------------------------------------------------------------------------------------


                    tested_Asymptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Asymptomatic')&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    try:
                        tested_asym          =   tested_Asymptomatic/total_test
                    except ZeroDivisionError:
                        tested_asym  =  0
                    tested_asym_per      =   "{:.0%}".format(tested_asym)

                    asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=[1,3]) & Q(patient__patient_status='Asymptomatic')&Q(patient__pk=new_id)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    # asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Asymptomatic')).count()
                    # print(asym_pos,'asys')
                    try:
                        asym_positivity      =   asym_pos/total_test
                    except ZeroDivisionError:
                        asym_positivity  =  0
                    asym_positivity_per  =   "{:.0%}".format(asym_positivity)

                    try:
                        # total_positivity        =   (pos+tested_symptomatic+tested_Asymptomatic)/total_test
                        total_positivity        =   (sym_positivity+asym_positivity)/total_test
                        print(total_positivity,'pos')
                    except ZeroDivisionError:
                        total_positivity  =  0

                    total_positivity_per    =   "{:.0%}".format(total_positivity)

                    Arr.append({
                    'District_name':i.district_name_eng,
                    # 'District_repeated_count':dist_cnt,
                    'Total_Test_District':total_test,

                    'Symptomatic_tested':tested_symptomatic,
                    'Symptomatic_tested_per':tested_sym_per,
                    'Symptomatic_positives':sym_pos,
                    'Symptomatic_positives_per':sym_positivity_per,

                    'Asymptomatic_tested':tested_Asymptomatic,
                    'Asymptomatic_tested_per':tested_asym_per,
                    'Asymptomatic_positives':asym_pos,
                    'Asymptomatic_positives_per':asym_positivity_per,

                    # 'Positives_without_Sym_Asym':pos,
                    'Total_Positivity_per':total_positivity_per
                    })
                
                return Response({
                        'data':Arr,
                        'total_pg_count':master_dist_count,
                        'result':' Sucessfully'})

            else:
                Arr=[]
                id=0
                new_id=0

                master_dist =   Master_District.objects.all()
                master_dist_count = Master_District.objects.all().count()

                master_dist_details = paginatorCreation(master_dist, selected_page_no)

                for i in master_dist_details:
                    total_test  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)).count()
                    patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code))
                    for j in patientObj:
                        id=j.patient.pk
                    new_id=id
                    District_name=i.district_code
                    total_Test_District=total_test
                    #!--------------------------------  Symptomatic  -----------------------------------------------------------------------------------------------------

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    tested_symptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Symptomatic')).count()
                    try:
                        tested_sym          =   tested_symptomatic/total_test
                    except ZeroDivisionError:
                        tested_sym  =  0
                    tested_sym_per      =   "{:.0%}".format(tested_sym)

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    sym_pos             =   Patient_Testing.objects.filter(Q(patient__patient_status='Symptomatic')&Q(testing_status__in=['1','3'])&Q(patient__pk=new_id)).count()
                    print(sym_pos,'sysPo')
                    # sym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Symptomatic')).count()

                    # print(sym_pos,'sys')
                    try:
                        sym_positivity      =   sym_pos/total_test
                    except ZeroDivisionError:
                        sym_positivity  =  0
                    sym_positivity_per  =   "{:.0%}".format(sym_positivity)

                    # #!--------------------------------- ASymptomatic ----------------------------------------------------------------------------------------------------


                    tested_Asymptomatic  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code) & Q(patient__patient_status='Asymptomatic')).count()
                    try:
                        tested_asym          =   tested_Asymptomatic/total_test
                    except ZeroDivisionError:
                        tested_asym  =  0
                    tested_asym_per      =   "{:.0%}".format(tested_asym)

                    asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=[1,3]) & Q(patient__patient_status='Asymptomatic')&Q(patient__pk=new_id)).count()
                    # asym_pos             =   Patient_Testing.objects.filter(Q(testing_status__in=['1','3']) & Q(patient__patient_status='Asymptomatic')).count()
                    # print(asym_pos,'asys')
                    try:
                        asym_positivity      =   asym_pos/total_test
                    except ZeroDivisionError:
                        asym_positivity  =  0
                    asym_positivity_per  =   "{:.0%}".format(asym_positivity)

                    try:
                        # total_positivity        =   (pos+tested_symptomatic+tested_Asymptomatic)/total_test
                        total_positivity        =   (sym_positivity+asym_positivity)/total_test
                        print(total_positivity,'pos')
                    except ZeroDivisionError:
                        total_positivity  =  0

                    total_positivity_per    =   "{:.0%}".format(total_positivity)

                    Arr.append({
                                    'District_name':i.district_name_eng,
                                    # 'District_repeated_count':dist_cnt,
                                    'Total_Test_District':total_test,

                                    'Symptomatic_tested':tested_symptomatic,
                                    'Symptomatic_tested_per':tested_sym_per,
                                    'Symptomatic_positives':sym_pos,
                                    'Symptomatic_positives_per':sym_positivity_per,

                                    'Asymptomatic_tested':tested_Asymptomatic,
                                    'Asymptomatic_tested_per':tested_asym_per,
                                    'Asymptomatic_positives':asym_pos,
                                    'Asymptomatic_positives_per':asym_positivity_per,

                                    # 'Positives_without_Sym_Asym':pos,
                                    'Total_Positivity_per':total_positivity_per
                                })
                return Response({
                        'data':Arr,
                        'total_pg_count':master_dist_count,
                        'result':' Sucessfully'})

        else:
            return Response("user not found")




    
    
    

#########################      RAT RTPCR POSITIVITY RATE REPORT              #########################
class SSUGetMasterRatRtpcrPositivityReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        Arr=[]
        id=0
        new_id=0
        master_dist =   Master_District.objects.all()
        for i in master_dist:
            dist_cnt  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)).count()
            patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code))
            for j in patientObj:
                id=j.patient.pk
            new_id=id
            # print(new_id)
            antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()
            print(antigen,'antigen')
            RTPCR_other  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()
            print(RTPCR_other,'RTPCR_other')

            #!-------------------------------------------------------------------------------------------------------------------------------------
            Total_test          =  antigen+RTPCR_other
            Test_done_antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()


            try:
                RAT_vs_T          =   Test_done_antigen/Total_test
            except ZeroDivisionError:
                RAT_vs_T  =  0
            RAT_vs_T_per      =   "{:.0%}".format(RAT_vs_T)


            Antigen_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)& Q(testing_status__in=[1,3])).count()
            try:
                Total_Antigen_positivity      =   Antigen_positivity/Total_test
            except ZeroDivisionError:
                Total_Antigen_positivity  =  0
            Total_Antigen_positivity_per  =   "{:.0%}".format(Total_Antigen_positivity)

            # #!-------------------------------------------------------------------------------------------------------------------------------------

            Test_done_RTPCR_other   =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()

            try:
                RTPCR_other_vs_T          =   Test_done_RTPCR_other/Total_test
            except ZeroDivisionError:
                RTPCR_other_vs_T  =  0
            RTPCR_other_vs_T_per      =   "{:.0%}".format(RTPCR_other_vs_T)


            RTPCR_other_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))& Q(testing_status__in=[1,3])).count()
            try:
                Total_RTPCR_other_positivity      =   RTPCR_other_positivity/Total_test
            except ZeroDivisionError:
                Total_RTPCR_other_positivity  =  0
            Total_RTPCR_other_positivity_per  =   "{:.0%}".format(Total_RTPCR_other_positivity)

            # #!-------------------------------------------------------------------------------------------------------------------------------------

            Positives_total                  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & Q(testing_status__in=[1,3])).count()

            try:
                Total_positivity        =   Positives_total/Total_test
            except ZeroDivisionError:
                Total_positivity  =  0

            Total_positivity_per    =   "{:.0%}".format(Total_positivity)






            Arr.append({
            'District_name':i.district_name_eng,
            'District_repeated_count':dist_cnt,
            'Total_Test':Total_test,
            'Test_done_antigen':Test_done_antigen,
            'RAT_vs_T_per':RAT_vs_T_per,
            'Antigen_positivity':Antigen_positivity,
            'Total_Antigen_positivity_per':Total_Antigen_positivity_per,

            'Test_done_RTPCR_other':Test_done_RTPCR_other,
            'RTPCR_other_vs_T_per':RTPCR_other_vs_T_per,
            'RTPCR_other_positivity':RTPCR_other_positivity,
            'Total_RTPCR_other_positivity_per':Total_RTPCR_other_positivity_per,

            'Total_Positives':Positives_total,
            'Total_positivity_per':Total_positivity_per

            })
        return Response({

            'data':Arr,
            'result':' Sucessfully'})


    def post (self,request):

        data = request.data
        id = data.get('user_id')
        datef = data.get('from_date')
        datet = data.get('to_date')

        page_no = data.get('page_no')
        print(page_no)

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        if data.get('user_id') is '':
            return Response("user id required ")

        elif User.objects.filter(id=id).exists():
            if datef and datet:
                date_to= datetime.strptime(datet,'%Y-%m-%d')
                datet= date_to+timedelta(days=1)
                datef= datetime.strptime(datef,'%Y-%m-%d')
                Arr=[]
                id=0
                new_id=0

                master_dist =   Master_District.objects.all()
                master_dist_count =   Master_District.objects.all().count()

                print(selected_page_no)
                master_dist_details = paginatorCreation(master_dist_count, selected_page_no)

                for i in master_dist_details:
                    dist_cnt  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet)).count()
                    patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)&Q(patient__create_timestamp__gte=datef,patient__create_timestamp__lt=datet))
                    for j in patientObj:
                        id=j.patient.pk

                    new_id=id
                    # print(new_id)
                    antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()
                    print(antigen,'antigen')
                    RTPCR_other  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()
                    print(RTPCR_other,'RTPCR_other')

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    Total_test          =  antigen+RTPCR_other
                    Test_done_antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()


                    try:
                        RAT_vs_T          =   Test_done_antigen/Total_test
                    except ZeroDivisionError:
                        RAT_vs_T  =  0
                    RAT_vs_T_per      =   "{:.0%}".format(RAT_vs_T)


                    Antigen_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)& Q(testing_status__in=[1,3])).count()
                    try:
                        Total_Antigen_positivity      =   Antigen_positivity/Total_test
                    except ZeroDivisionError:
                        Total_Antigen_positivity  =  0
                    Total_Antigen_positivity_per  =   "{:.0%}".format(Total_Antigen_positivity)

                    # #!-------------------------------------------------------------------------------------------------------------------------------------

                    Test_done_RTPCR_other   =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()

                    try:
                        RTPCR_other_vs_T          =   Test_done_RTPCR_other/Total_test
                    except ZeroDivisionError:
                        RTPCR_other_vs_T  =  0
                    RTPCR_other_vs_T_per      =   "{:.0%}".format(RTPCR_other_vs_T)


                    RTPCR_other_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))& Q(testing_status__in=[1,3])).count()
                    try:
                        Total_RTPCR_other_positivity      =   RTPCR_other_positivity/Total_test
                    except ZeroDivisionError:
                        Total_RTPCR_other_positivity  =  0
                    Total_RTPCR_other_positivity_per  =   "{:.0%}".format(Total_RTPCR_other_positivity)

                    # #!-------------------------------------------------------------------------------------------------------------------------------------

                    Positives_total                  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & Q(testing_status__in=[1,3])).count()

                    try:
                        Total_positivity        =   Positives_total/Total_test
                    except ZeroDivisionError:
                        Total_positivity  =  0

                    Total_positivity_per    =   "{:.0%}".format(Total_positivity)






                    Arr.append({
                    'District_name':i.district_name_eng,
                    'District_repeated_count':dist_cnt,
                    'Total_Test':Total_test,
                    'Test_done_antigen':Test_done_antigen,
                    'RAT_vs_T_per':RAT_vs_T_per,
                    'Antigen_positivity':Antigen_positivity,
                    'Total_Antigen_positivity_per':Total_Antigen_positivity_per,

                    'Test_done_RTPCR_other':Test_done_RTPCR_other,
                    'RTPCR_other_vs_T_per':RTPCR_other_vs_T_per,
                    'RTPCR_other_positivity':RTPCR_other_positivity,
                    'Total_RTPCR_other_positivity_per':Total_RTPCR_other_positivity_per,

                    'Total_Positives':Positives_total,
                    'Total_positivity_per':Total_positivity_per

                    })
                return Response({
                    'data':Arr,
                    'total_pg_count': master_dist_count,
                    'result':' Sucessfully'})

            else:
                Arr=[]
                id=0
                new_id=0
                
                master_dist =   Master_District.objects.all()
                master_dist_count =   Master_District.objects.all().count()

                master_dist_details = paginatorCreation(master_dist, selected_page_no)

                for i in master_dist_details:
                    dist_cnt  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code)).count()
                    patientObj  =   Patient_Address.objects.filter(Q(district_name__icontains=i.district_code))
                    # print(patientObj,'obj')
                    for j in patientObj:
                        id=j.patient.pk

                    new_id=id
                    # print(new_id)
                    antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()
                    print(antigen,'antigen')
                    RTPCR_other  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()
                    print(RTPCR_other,'RTPCR_other')

                    #!-------------------------------------------------------------------------------------------------------------------------------------
                    Total_test          =  antigen+RTPCR_other
                    Test_done_antigen  =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)).count()


                    try:
                        RAT_vs_T          =   Test_done_antigen/Total_test
                    except ZeroDivisionError:
                        RAT_vs_T  =  0
                    RAT_vs_T_per      =   "{:.0%}".format(RAT_vs_T)


                    Antigen_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id)& Q(rtpcr_test= 0)& Q(testing_status__in=[1,3])).count()
                    try:
                        Total_Antigen_positivity      =   Antigen_positivity/Total_test
                    except ZeroDivisionError:
                        Total_Antigen_positivity  =  0
                    Total_Antigen_positivity_per  =   "{:.0%}".format(Total_Antigen_positivity)

                    # #!-------------------------------------------------------------------------------------------------------------------------------------

                    Test_done_RTPCR_other   =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))).count()

                    try:
                        RTPCR_other_vs_T          =   Test_done_RTPCR_other/Total_test
                    except ZeroDivisionError:
                        RTPCR_other_vs_T  =  0
                    RTPCR_other_vs_T_per      =   "{:.0%}".format(RTPCR_other_vs_T)


                    RTPCR_other_positivity             =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & (~Q(rtpcr_test= 0))& Q(testing_status__in=[1,3])).count()
                    try:
                        Total_RTPCR_other_positivity      =   RTPCR_other_positivity/Total_test
                    except ZeroDivisionError:
                        Total_RTPCR_other_positivity  =  0
                    Total_RTPCR_other_positivity_per  =   "{:.0%}".format(Total_RTPCR_other_positivity)

                    # #!-------------------------------------------------------------------------------------------------------------------------------------

                    Positives_total                  =   Patient_Testing.objects.filter(Q(patient__pk=new_id) & Q(testing_status__in=[1,3])).count()

                    try:
                        Total_positivity        =   Positives_total/Total_test
                    except ZeroDivisionError:
                        Total_positivity  =  0

                    Total_positivity_per    =   "{:.0%}".format(Total_positivity)


                    Arr.append({
                    'District_name':i.district_name_eng,
                    'District_repeated_count':dist_cnt,
                    'Total_Test':Total_test,
                    'Test_done_antigen':Test_done_antigen,
                    'RAT_vs_T_per':RAT_vs_T_per,
                    'Antigen_positivity':Antigen_positivity,
                    'Total_Antigen_positivity_per':Total_Antigen_positivity_per,

                    'Test_done_RTPCR_other':Test_done_RTPCR_other,
                    'RTPCR_other_vs_T_per':RTPCR_other_vs_T_per,
                    'RTPCR_other_positivity':RTPCR_other_positivity,
                    'Total_RTPCR_other_positivity_per':Total_RTPCR_other_positivity_per,

                    'Total_Positives':Positives_total,
                    'Total_positivity_per':Total_positivity_per

                    })
                return Response({
                    'data':Arr,
                    'total_pg_count': master_dist_count,
                    'result':' Sucessfully'})


        else:
            return Response("user not found")

    




#########################      TLAB ALL ACCEPTED PACKAGES              #########################
class TlabAllAcceptedPackagesReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)
        
        # sc = Package_Sampling.objects.filter(test_lab_id=user_id).values()
        test_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
        
        sc_data = Package_Sampling.objects.filter(test_lab_id=test_lab_data.id, lab_master_id= test_lab_data.testing_lab_master_id, lab_accept_reject_status= 1).values().order_by('-id')
        sc_count = Package_Sampling.objects.filter(test_lab_id=test_lab_data.id, lab_master_id= test_lab_data.testing_lab_master_id, lab_accept_reject_status= 1).count()
        
        
        sc_details = paginatorCreation(sc_data, selected_page_no)

        for i in sc_details:
            i['testing_lab_name'] = test_lab_data.testing_lab_facility_name
            check_swb_col = Swab_Collection_Centre.objects.filter(id= i['swab_cc_id'])
            if check_swb_col:
                check_swb_col = Swab_Collection_Centre.objects.get(id= i['swab_cc_id'])
                phc_data = Master_PHC.objects.get(id= check_swb_col.phc_master_id)
                i['phc_name'] = phc_data.phc_name
            else:
                i['phc_name'] = Master_Labs.objects.filter(id= test_lab_data.testing_lab_master_id).values_list('lab_id', flat=True)[0]
        
        return Response({'details':list(sc_details), 'total_pg_count': sc_count,'result':'successfull '})







#########################      TLAB OPS DATE WISE REPORT              #########################
class TlabOpsDateWiseReport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        check_lab_user = list(Testing_Lab_Facility.objects.filter(user_id= user_id).values('id', 'testing_lab_master_id'))

        print(check_lab_user)
        print(check_lab_user[0]['testing_lab_master_id'])

        if check_lab_user:

            all_packages = Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id'])).values('lab_received_datetime__date').distinct().order_by('-lab_ops_received_datetime')

            response_data = []

            for date in all_packages:
                res = {}
                print(date['lab_received_datetime__date'])

                if date['lab_received_datetime__date']:

                    package_details = Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= asdatetime.strftime(date['lab_received_datetime__date'], '%Y-%m-%d'))).values_list('id', flat=True)
                    
                    patient_details = Patient.objects.filter(package_sampling_id__in= package_details).values()

                    samples_received_total_count = Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= asdatetime.strftime(date['lab_received_datetime__date'], '%Y-%m-%d'))).aggregate(total_samples= Sum('samples_count'))
                        
                    if samples_received_total_count['total_samples']:
                        pass
                    else:
                        samples_received_total_count['total_samples'] = 0

                    individual_testing = Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= asdatetime.strftime(date['lab_received_datetime__date'], '%Y-%m-%d'))).values_list('id', flat=True)
                    check_patients = Patient.objects.filter(package_sampling_id__in= individual_testing).values()
                    
                    individual_testing_under_testing = 0
                    pool_testing_under_testing = 0
                    result_not_declared = 0
                    result_declared = 0
                    total_c_positive = 0
                    total_inconclusive = 0
                    total_rejected_samples = 0

                    for i in check_patients:
                        

                        result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                        if i['group_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            individual_testing_under_testing += 1

                        if i['pool_samples'] == 1 and result_declared_check:
                            result_declared += 1
                        else:
                            pool_testing_under_testing += 1
                        
                        total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                        total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                        total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(samples_rejected= 1)).count()

                    response_data.append({'date':date['lab_received_datetime__date'], 'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})

            return Response({'result': response_data})



#########################      TLAB OPS DATE WISE REPORT VIEW1              #########################
class TlabOpsDateWiseTHOReportView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        selected_date = data.get('date')

        check_lab_user = list(Testing_Lab_Facility.objects.filter(user_id= user_id).values('id', 'testing_lab_master_id'))


        if check_lab_user:

            all_packages_user = list(set(Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id'])& Q(lab_received_datetime__date= selected_date)).values_list('user_id', flat=True)))

            tho_details = Swab_Collection_Centre.objects.filter(user_id__in= all_packages_user).values_list('tho_id', flat=True)
            
            response_data = []
            

            for td in tho_details:
                # res = {}
                chek_block_master_details = Master_Block.objects.get(id= THO.objects.get(id= td).city_id)
                # res['block_code'] = chek_block_master_details.block_code
                # res['block_name_eng'] = chek_block_master_details.block_name_eng
                # res['tho_id'] = td

                tho_scc_user = list(set(Swab_Collection_Centre.objects.filter(tho_id= td).values_list('user_id', flat=True)))



                samples_received_total_count = Package_Sampling.objects.filter(Q(user_id__in= tho_scc_user) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).aggregate(total_samples= Sum('samples_count'))
                        
                if samples_received_total_count['total_samples']:
                    pass
                else:
                    samples_received_total_count['total_samples'] = 0

                individual_testing = Package_Sampling.objects.filter(Q(user_id__in= tho_scc_user) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).values_list('id', flat=True)
                check_patients = Patient.objects.filter(package_sampling_id__in= individual_testing).values()
                
                individual_testing_under_testing = 0
                pool_testing_under_testing = 0
                result_not_declared = 0
                result_declared = 0
                total_c_positive = 0
                total_inconclusive = 0
                total_rejected_samples = 0

                for i in check_patients:
                    
                    result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                    if i['group_samples'] == 1 and result_declared_check:
                        result_declared += 1
                    else:
                        individual_testing_under_testing += 1

                    if i['pool_samples'] == 1 and result_declared_check:
                        result_declared += 1
                    else:
                        pool_testing_under_testing += 1
                    
                    total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                    total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                    total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(samples_rejected= 1)).count()

                response_data.append({'block_code': chek_block_master_details.block_code, 'block_name_eng': chek_block_master_details.block_name_eng, 'tho_id': td,'date':selected_date, 'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})
            print(response_data)
            print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
            return Response({'result': response_data}, status= status.HTTP_200_OK)

        else:
            return Response({'result': 'Something went wrong'}, status= status.HTTP_406_NOT_ACCEPTABLE)




#########################      TLAB OPS DATE WISE REPORT VIEW2              #########################
class TlabOpsDateWiseTHOMOReportView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        selected_tho = data.get('selected_tho')
        selected_date = data.get('date')

        check_lab_user = list(Testing_Lab_Facility.objects.filter(user_id= user_id).values('id', 'testing_lab_master_id'))


        if check_lab_user:

            # all_packages_user = list(set(Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id'])& Q(lab_received_datetime__date= selected_date)).values_list('user_id', flat=True)))

            mo_details = list(set(Swab_Collection_Centre.objects.filter(tho_id= selected_tho).values_list('phc_master_id', flat=True)))
            
            response_data = []

            for md in mo_details:
                # res = {}
                check_master_phc_details = Master_PHC.objects.get(id= md)
                # res['block_code'] = chek_block_master_details.block_code
                # res['block_name_eng'] = chek_block_master_details.block_name_eng
                # res['tho_id'] = td

                tho_scc_user = list(set(Swab_Collection_Centre.objects.filter(phc_master_id= md).values_list('user_id', flat=True)))


                samples_received_total_count = Package_Sampling.objects.filter(Q(user_id__in= tho_scc_user) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).aggregate(total_samples= Sum('samples_count'))
                        
                if samples_received_total_count['total_samples']:
                    pass
                else:
                    samples_received_total_count['total_samples'] = 0

                individual_testing = Package_Sampling.objects.filter(Q(user_id__in= tho_scc_user) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).values_list('id', flat=True)
                check_patients = Patient.objects.filter(package_sampling_id__in= individual_testing).values()
                
                individual_testing_under_testing = 0
                pool_testing_under_testing = 0
                result_not_declared = 0
                result_declared = 0
                total_c_positive = 0
                total_inconclusive = 0
                total_rejected_samples = 0

                for i in check_patients:
                    
                    result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                    if i['group_samples'] == 1 and result_declared_check:
                        result_declared += 1
                    else:
                        individual_testing_under_testing += 1

                    if i['pool_samples'] == 1 and result_declared_check:
                        result_declared += 1
                    else:
                        pool_testing_under_testing += 1
                    
                    total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                    total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                    total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(samples_rejected= 1)).count()

                response_data.append({'phc_code': check_master_phc_details.phc_code, 'phc_name': check_master_phc_details.phc_name, 'mo_id': md,'date':selected_date, 'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})

            return Response({'result': response_data})




#########################      TLAB OPS DATE WISE REPORT VIEW3              #########################
class TlabOpsDateWiseTHOMOIndetailReportView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        selected_mo = data.get('selected_mo')
        selected_date = data.get('date')

        check_lab_user = list(Testing_Lab_Facility.objects.filter(user_id= user_id).values('id', 'testing_lab_master_id'))


        if check_lab_user:

            # all_packages_user = list(set(Package_Sampling.objects.filter(Q(lab_master_id= check_lab_user[0]['testing_lab_master_id'])& Q(lab_received_datetime__date= selected_date)).values_list('user_id', flat=True)))

            mo_user_details = list(set(Swab_Collection_Centre.objects.filter(phc_master_id= selected_mo).values_list('user_id', flat=True)))
            
            response_data = []

            # res = {}
            check_master_phc_details = Master_PHC.objects.get(id= selected_mo)
            # res['block_code'] = chek_block_master_details.block_code
            # res['block_name_eng'] = chek_block_master_details.block_name_eng
            # res['tho_id'] = td


            samples_received_total_count = Package_Sampling.objects.filter(Q(user_id__in= mo_user_details) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).aggregate(total_samples= Sum('samples_count'))
                    
            if samples_received_total_count['total_samples']:
                pass
            else:
                samples_received_total_count['total_samples'] = 0

            individual_testing = Package_Sampling.objects.filter(Q(user_id__in= mo_user_details) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(lab_received_datetime__date= selected_date)).values_list('id', flat=True)
            check_patients = Patient.objects.filter(package_sampling_id__in= individual_testing).values()
            
            individual_testing_under_testing = 0
            pool_testing_under_testing = 0
            result_not_declared = 0
            result_declared = 0
            total_c_positive = 0
            total_inconclusive = 0
            total_rejected_samples = 0

            for i in check_patients:
                
                result_declared_check = Patient_Testing.objects.filter(patient_id= i['id'])

                if i['group_samples'] == 1 and result_declared_check:
                    result_declared += 1
                else:
                    individual_testing_under_testing += 1

                if i['pool_samples'] == 1 and result_declared_check:
                    result_declared += 1
                else:
                    pool_testing_under_testing += 1
                
                total_c_positive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & (Q(testing_status= 3) | Q(testing_status= 1))).count()
                total_inconclusive += Patient_Testing.objects.filter(Q(patient_id= i['id']) & Q(testing_status= 5)).count()
                total_rejected_samples += Patient.objects.filter(Q(id= i['id']) & Q(lab_master_id= check_lab_user[0]['testing_lab_master_id']) & Q(samples_rejected= 1)).count()

            response_data.append({'phc_code': check_master_phc_details.phc_code, 'phc_name': check_master_phc_details.phc_name,'date':selected_date, 'samples_received_total_count': samples_received_total_count['total_samples'],'individual_testing_under_testing':individual_testing_under_testing, 'pool_testing_under_testing':pool_testing_under_testing, 'result_not_declared':samples_received_total_count['total_samples'] - result_declared, 'result_declared':result_declared, 'total_c_positive':total_c_positive, 'total_inconclusive':total_inconclusive, 'total_rejected_samples':total_rejected_samples})

            return Response({'result': response_data})







#########################      SSU TARGET SETUP      #########################
class GetSSUTargetSetup(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        date = data.get('target_date')

        mast_dist_data = Master_District.objects.all().values()

        all_dist_data = []

        for i in mast_dist_data:

            if date:

                if datetime.datetime(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])).date() >= asdatetime.now().date():
                    
                    print("HHHHHHHHHHHHHHH")
                    print(asdatetime.now().date())
                    print(datetime.datetime(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])).date())

                    selected_date = date.split('-')
                
                    dist_data_details = {'district_code': i['district_code'], 'district_name_eng':i['district_name_eng']}
                    dso_target_data = PHCTargetAssignment.objects.filter(Q(dso_created_datetime__date= datetime.datetime(int(selected_date[0]), int(selected_date[1]), int(selected_date[2])).date()) & Q(district_code= i['district_code'])).values()

                    print(dso_target_data)
                    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

                    if dso_target_data:
                        for j in dso_target_data:
                            
                            dist_data_details['id'] = j['id']
                            dist_data_details['dso_id']= j['dso_id']
                            dist_data_details['dso_target']= j['dso_target']
                            dist_data_details['edit'] = True
                    else:
                        dist_data_details['id'] = ''
                        dist_data_details['dso_id']= ''
                        dist_data_details['dso_target']= ''
                        dist_data_details['edit'] = False
                else:
                    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
                    return Response({'result':[], 'message':'Please Select Current Date or Future Dates only'}, status=status.HTTP_200_OK)
            else:

                dist_data_details = {'district_code': i['district_code'], 'district_name_eng':i['district_name_eng']}
                dso_target_data = PHCTargetAssignment.objects.filter(Q(dso_created_datetime__date= asdatetime.now().date()) & Q(district_code= i['district_code'])).values()

                if dso_target_data:
                    for j in dso_target_data:
                        
                        dist_data_details['id'] = j['id']
                        dist_data_details['dso_id']= j['dso_id']
                        dist_data_details['dso_target']= j['dso_target']
                        dist_data_details['edit'] = True
                else:
                    dist_data_details['id'] = ''
                    dist_data_details['dso_id']= ''
                    dist_data_details['dso_target']= ''
                    dist_data_details['edit'] = False

            all_dist_data.append(dist_data_details)
        
        return Response({'result':all_dist_data, 'message':'Sucessfully'}, status=status.HTTP_200_OK)






#########################      TARGET FOR DSO      #########################
class TargetForDSO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        user_id = data.get('user_id')

        dist_codes = data.get('district_code')
        dis_targets = data.get('contact_testing_count')

        id = data.get('id')
        date = data.get('target_date')

        

        dist_data = Master_District.objects.get(district_code= dist_codes)

        dso_data = DSO.objects.get(district_id= dist_data.id)

        if id:
            if date:
                print("DDDDDDDDDDDDDDDDDDD", date)
                split_date = date.split('-')

                PHCTargetAssignment.objects.filter(id= id).update(dso_target= dis_targets, dso_created_datetime= datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])))
            else:
                PHCTargetAssignment.objects.filter(id= id).update(district_code= dist_codes, dso_target= dis_targets, dso_created_datetime= asdatetime.now())
            # dist_data = Master_District.objects.get(district_code= dist_codes)
            # dso_data = DSO.objects.get(district_id= dist_data.id)
            return Response({'result': 'Updated Sucessfully'})

        else:
            if date:
                print("DDDDDDDDDDDDDDDDDDD", date)
                split_date = date.split('-')

                target_ass_dso = PHCTargetAssignment.objects.create(district_code= dist_codes, dso_id= dso_data.id, dso_target= dis_targets, dso_created_datetime= datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])))
            else:
                target_ass_dso = PHCTargetAssignment.objects.create(district_code= dist_codes, dso_id= dso_data.id, dso_target= dis_targets, dso_created_datetime= asdatetime.now())

            return Response({'result': 'Target Assigned Sucessfully'})






#########################      GET DSO TARGET      #########################
class GetDSOTarget(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
    
        user_id = data.get('user_id')

        dso_details = DSO.objects.get(user_id= user_id)

        check_dist_data = Master_District.objects.get(id= dso_details.district_id)

        get_all_thos = Master_PHC.objects.filter(district_code = check_dist_data.district_code).values('block_code', 'block_name_eng').distinct()

        # get_thos_data = THO.objects.filter(dso_id= dso_details.id).values_list('id', flat=True)
        print("ALL THO DATA  ",get_all_thos)
        for i in get_all_thos:

            if i['block_code'] != ' NULL':
                print(i['block_code'])
                taluk_data_data = Master_Block.objects.filter(block_code= i['block_code'])
                if taluk_data_data:
                    taluk_data = Master_Block.objects.get(block_code= i['block_code'])
                    print(i['block_code'])
                    get_tho_data_filter = THO.objects.filter(Q(dso_id= dso_details.id) & Q(city= taluk_data.id))
                    print(get_tho_data_filter)
                    if get_tho_data_filter:
                        get_tho_data = THO.objects.get(Q(dso_id= dso_details.id) & Q(city= taluk_data.id))

                        get_already_assigned_tho_targets = PHCTargetAssignment.objects.filter(Q(tho_id= get_tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date())).values()

                        print(get_already_assigned_tho_targets)

                        if get_already_assigned_tho_targets:
                            get_already_assigned_tho_targets_get = PHCTargetAssignment.objects.get(Q(tho_id= get_tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date()))
                            print(get_already_assigned_tho_targets_get.tho_target)
                            i['edit'] = True
                            i['tho_target'] = get_already_assigned_tho_targets_get.tho_target
                        else:
                            i['edit'] = False
                            i['tho_target'] = 0
                    else:
                        i['edit'] = False
                        i['tho_target'] = 0

        target_ass_dso = PHCTargetAssignment.objects.filter(Q(dso_id= dso_details.id) & Q(dso_created_datetime__date= asdatetime.now().date())).values()

        return Response({'result': get_all_thos, 'dso_target':target_ass_dso}, status=status.HTTP_200_OK)





#########################      TARGET FOR THO      #########################
class TargetForTHO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        taluk_codes = data.get('taluk_code')
        taluk_targets = data.get('contact_testing_count')

        print(data)

        tal_data = Master_Block.objects.get(block_code= taluk_codes)

        tho_data = THO.objects.get(city_id= tal_data.id)

        
        dso_data = DSO.objects.get(user_id= user_id)
        
        # target_ass_tho = PHCTargetAssignment.objects.create(tho_id= tho_data.id, tho_target= taluk_targets, tho_created_datetime= asdatetime.now().date())

        get_target_ass_tho = PHCTargetAssignment.objects.filter(Q(dso_id= dso_data.id) & Q(dso_created_datetime__date= asdatetime.now().date())).values()
        print(get_target_ass_tho)
        if get_target_ass_tho:
            check_assigned_tgt = PHCTargetAssignment.objects.filter(Q(tho_id= tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date()) & Q(dso_id= dso_data.id))
            if check_assigned_tgt:
                target_ass_tho = PHCTargetAssignment.objects.filter(Q(tho_id= tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date()) & Q(dso_id= dso_data.id)).update(tho_target= taluk_targets, tho_created_datetime= asdatetime.now())
                return Response({'result': 'Update Target Assigned Sucessfully'})
            else:
                get_target_ass_tho = PHCTargetAssignment.objects.filter(Q(dso_id= dso_data.id) & Q(dso_created_datetime__date= asdatetime.now().date())).values().order_by('id')[:1]
                print(get_target_ass_tho)
                for i in get_target_ass_tho:
                    target_ass_tho = PHCTargetAssignment.objects.create(tho_id= tho_data.id, tho_target= taluk_targets, tho_created_datetime= asdatetime.now(), dso_id= dso_data.id, dso_created_datetime= i['dso_created_datetime'], dso_target= i['dso_target'], district_code= i['district_code'])
                return Response({'result': 'Target Assigned Sucessfully'})
        else:
            return Response({'result': 'Something went wrong'})







#########################      GET THO TARGET      #########################
class GetTHOTarget(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        tho_details = THO.objects.get(user_id= user_id)

        # swb_coll_data = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_details.id) & Q(role_id= 6)).values()

        # phc_ids = []

        # for i in swb_coll_data:
        #     phc_ids.append(i['phc_master_id'])

        phc_ids = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_details.id) & Q(role_id= 6)).values_list('phc_master_id', flat=True)

        # check_dist_data = Master_District.objects.get(district_code= dso_details.district_id)

        get_all_phc = Master_PHC.objects.filter(id__in= phc_ids).values()

        target_asgn_dso = PHCTargetAssignment.objects.filter(Q(tho_id= tho_details.id) & Q(tho_created_datetime__date= asdatetime.now().date())).values()
        
        for i in get_all_phc:
            target_assigned_dso = PHCTargetAssignment.objects.filter(Q(tho_id= tho_details.id) & Q(phc_id= i['id']) & Q(tho_created_datetime__date= asdatetime.now().date())).values()
            if target_assigned_dso:
                target_assigned_dso_get = PHCTargetAssignment.objects.get(Q(tho_id= tho_details.id) & Q(phc_id= i['id']) & Q(tho_created_datetime__date= asdatetime.now().date()))
                i['phc_target'] = target_assigned_dso_get.phc_target
                i['edit'] = True
            else:
                i['phc_target'] = 0
                i['edit'] = False

        return Response({'result': get_all_phc, 'tho_target':target_asgn_dso}, status=status.HTTP_200_OK)







#########################      TARGET FOR PHC      #########################
class TargetForPHC(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)
        print("JHHHHHHHHHHHHHHHHHHHHHHH")

        user_id = data.get('user_id')

        phc_codes = data.get('phc_code')
        phc_targets = data.get('contact_testing_count')

        id = data.get('id')
        edit_id = data.get('edit_id')

        tho_data = THO.objects.get(user_id= user_id)

        # tal_data = Master_Block.objects.get(block_code= taluk_codes)

        # check_phc = Master_PHC.objects.get(phc_code= phc_codes)

        get_all_phc_ck = Master_PHC.objects.filter(id= id)
        if get_all_phc_ck:

            get_all_phc = Master_PHC.objects.get(id= id)

            check_assigned_data =  PHCTargetAssignment.objects.filter(Q(tho_id= tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date()) & Q(phc_id= get_all_phc.id))

            if check_assigned_data:

                # get_all_phc = Master_PHC.objects.get(id= id)
                # phc_data = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data.id) & Q(role_id= 6) & Q(phc_master_id= get_all_phc))
                # phc_data = Swab_Collection_Centre.objects.get(Q(tho_id= tho_data.id) & Q(role_id= 6) & Q(phc_master_id= id))
                
                target_ass_phc = PHCTargetAssignment.objects.filter(Q(tho_id= tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date()) & Q(phc_id= get_all_phc.id)).update(phc_target= phc_targets, phc_created_datetime= asdatetime.now())

                return Response({'result': 'Target Updated Sucessfully'})

            else:
                # get_all_phc = Master_PHC.objects.get(id= phc_data.phc_master_id)
                # phc_data = Swab_Collection_Centre.objects.filter(Q(tho_id= tho_data.id) & Q(role_id= 6) & Q(phc_master_id= id))
                # phc_data = Swab_Collection_Centre.objects.get(Q(tho_id= tho_data.id) & Q(role_id= 6) & Q(phc_master_id= id))
                # target_ass_phc = PHCTargetAssignment.objects.create(phc_id= get_all_phc.id, phc_target= phc_targets)
                # target_ass_phc = PHCTargetAssignment.objects.filter(Q(tho_id= tho_data.id) & Q(tho_created_datetime__date= asdatetime.now().date())).update(phc_id= get_all_phc.id, phc_target= phc_targets, phc_created_datetime= asdatetime.now())
                target_ass_phc = PHCTargetAssignment.objects.create(tho_id= tho_data.id, tho_created_datetime= asdatetime.now(), phc_id= get_all_phc.id, phc_target= phc_targets, phc_created_datetime= asdatetime.now())

                return Response({'result': 'Target Assigned Sucessfully'})
        else:
            return Response({'result': 'Something Went Wrong'})








#########################      GET PHC TARGETS      #########################
class PHCTargets(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        user_id      = data.get('user_id')

        get_user = Swab_Collection_Centre.objects.get(user_id = user_id)


        # target_assign_contact_tracing =  Contact_Tracing.objects.filter(Q(assigned_phc=get_user.phc_master_id) & Q(date_of_contact_created__date=asdatetime.now().date())).count()

        # target_assign_ili          =  ILI.objects.filter(Q(assigned_phc=get_user.phc_master_id) & Q(date_of_contact_created__date= asdatetime.now().date())).count()

        target_assign_contact_tracing =  Contact_Tracing.objects.filter(Q(assigned_phc=get_user.phc_master_id) & Q(assigned_date__date=asdatetime.now().date())).count()

        target_assign_ili          =  ILI.objects.filter(Q(assigned_phc=get_user.phc_master_id) & Q(assigned_date__date= asdatetime.now().date())).count()

        # total_phc_target    =   PHCTargetAssignment.objects.filter(Q(phc_id=get_user.phc_master_id) & Q(created_datetime__date= asdatetime.now().date()))
        total_phc_target    =   PHCTargetAssignment.objects.filter(Q(phc_id=get_user.phc_master_id) & Q(phc_created_datetime__date= asdatetime.now().date()))
        
        phc_target = 0
        if total_phc_target:
            total_phc_target_details    =   PHCTargetAssignment.objects.get(Q(phc_id=get_user.phc_master_id) & Q(phc_created_datetime__date= asdatetime.now().date()))
            phc_target = total_phc_target_details.phc_target


        random_target       =  int(phc_target) - int(target_assign_contact_tracing) - int(target_assign_ili)


        return Response({'result':[{'total_phc_target':phc_target, 'assign_contact_tracing':target_assign_contact_tracing, 'assign_ili':target_assign_ili, 'random_target':random_target,}], 'message' :'Sucessfull'})




#########################          TARGET ASSIGN TO USER          #########################
class TargetAssigntoUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)

        user_details = data.get('user_data')
        contact_testing = data.get('contact_testing')
        ili = data.get('ili')
        random = data.get('random')
        user_id = data.get('user_id')
        
        # assigned_user = data.get('assigned_user')
        # contact_testing_target = data.get('contact_testing_target')
        # ili_target = data.get('ili_target')
        # random_testing_target = data.get('random_testing_target')
        for i in range(len(user_details)):
            assign_target_to_user = TargetAssignToUser.objects.create(user_id= user_details[i]['user_id'], contact_tracing_target= contact_testing[i]['ct_assigned_target'], 
                                                                        ili_target= ili[i]['ili_assigned_target'], random_other_target= random[i]['rnd_assigned_target'])    

        # assign_target_to_user = TargetAssignToUser.objects.create(user_id= assigned_user, contact_tracing_target= contact_testing_target, ili_target= ili_target, random_other_target= random_testing_target)

        return Response({'message': 'Target Assigned Sucessfully'})




#########################          GET USER ASSIGNED TARGETS          #########################
class GetAssignedUserTargets(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        print(data)

        user_id = data.get('user_id')

        print(user_id)

        user_assigned_targets = TargetAssignToUser.objects.filter(Q(user_id= user_id) & Q(created_datetime__date= asdatetime.now().date())).values()
        print(user_assigned_targets)

        return Response({'result':user_assigned_targets, 'message':'Sucessfully'})





#########################          GROUP SAMPLES          #########################
class GroupSmaples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        test_lab_data_get = Testing_Lab_Facility.objects.get(user_id= user_id)
        # master_lab_data = Master_Labs.objects.get(id= test_lab_data_get.testing_lab_master_id)

        get_patient = Patient.objects.filter(Q(lab_master_id= test_lab_data_get.testing_lab_master_id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 1) & Q(group_samples_result= 0) & Q(submit_for_individual_testing = 0)).values()[:94]#.order_by('-lab_ops_received_datetime')[:93]

        last_plate_no_details = GroupPlate.objects.filter(Q(test_lab_id= test_lab_data_get.id) & Q(master_lab_id= test_lab_data_get.testing_lab_master_id)).order_by('-id')[:1]

        last_plate_no = '0'
        if last_plate_no_details:
            for i in last_plate_no_details:
                last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        else:
            last_plate_no = str(1).zfill(3)

        res_list = []
        static_apl_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',]

        total_no_of_single_samples = 0

        sub_lis_data = []
        obj_data = {}

        key_names = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9', 'name10', 'name11', 'name12', 'name13', 'name14']

        key_cnt = 0

        cnt = 1
        loop_count = 0
        for i in get_patient:
            if cnt <= 96:
                if (cnt == 1):
                    obj_data[key_names[loop_count]] = 'EC'

                    cnt += 1
                    loop_count += 1

                    obj_data[key_names[loop_count]] = i['test_lab_id']
                    total_no_of_single_samples += 1

                    cnt += 1
                    loop_count += 1
                
                elif (cnt == 96):
                    obj_data[key_names[loop_count]] = 'PC'

                    cnt += 1
                    loop_count += 1

                else:
                    obj_data[key_names[loop_count]] = i['test_lab_id']
                    total_no_of_single_samples += 1

                    cnt += 1
                    loop_count += 1

                if loop_count == 12:
                    sub_lis_data.append(obj_data)
                    res_list.append(sub_lis_data)
                    sub_lis_data = []
                    obj_data = {}
                    loop_count = 0
            else:
                break

        flag = True
        if cnt <= 96:
            while flag:
                if cnt <= 96:
                    if cnt == 1:
                        obj_data[key_names[loop_count]] = 'EC'

                        cnt += 1
                        loop_count += 1

                        obj_data[key_names[loop_count]] = ''

                        cnt += 1
                        loop_count += 1
                    
                    if cnt == 96:
                        obj_data[key_names[loop_count]] = 'PC'

                        cnt += 1
                        loop_count += 1

                        flag = False
                    else:
                        obj_data[key_names[loop_count]] = ''

                        cnt += 1
                        loop_count += 1

                    if loop_count == 12:
                        sub_lis_data.append(obj_data)
                        res_list.append(sub_lis_data)
                        sub_lis_data = []
                        obj_data = {}
                        loop_count = 0

                else:
                    flag = False


        alp_cnt = 0
        for i in res_list:
            i[0]['name'] = static_apl_data[alp_cnt]
            alp_cnt += 1


        get_patient_ids = Patient.objects.filter(Q(lab_master_id= test_lab_data_get.testing_lab_master_id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 1) & Q(group_samples_result= 0) & Q(submit_for_individual_testing = 0)).values_list('id', flat=True)[:94]
        print(get_patient_ids)
        return Response({'result':res_list, 'total_no_of_single_samples':total_no_of_single_samples, 'last_plate_no':last_plate_no, 'get_patient_ids':get_patient_ids})





#########################          POOL SAMPLES          #########################
class PoolSmaples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        test_lab_data_get = Testing_Lab_Facility.objects.get(user_id= user_id)
        master_lab_data = Master_Labs.objects.get(id= test_lab_data_get.testing_lab_master_id)

        # get_patient = Patient.objects.filter(Q(lab_master_id= master_lab_data.id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 0)).values()#.order_by('-lab_ops_received_datetime')[:93]

        # get_pool_data = PoolSamples.objects.filter(Q(test_lab_id= test_lab_data_get.id) & Q(master_lab_id= master_lab_data.id) & Q(test_result__isnull= True)).values('plate_id', 'pool_id').distinct()
        get_patient = PoolSamples.objects.filter(Q(test_lab_id= test_lab_data_get.id) & Q(master_lab_id= master_lab_data.id) & Q(test_result__isnull= True) & Q(submit_for_pool_testing= 0)).values('plate_id', 'pool_id').distinct()


        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        print(get_patient)
        print(len(get_patient))

        last_plate_no_details = PoolPlate.objects.filter(Q(test_lab_id= test_lab_data_get.id) & Q(master_lab_id= master_lab_data.id)).order_by('-id')[:1]

        last_plate_no = '0'
        if last_plate_no_details:
            for i in last_plate_no_details:
                last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        else:
            last_plate_no = str(1).zfill(3)

        
        res_list = []

        static_apl_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',]
        total_no_of_single_samples = 0

        sub_lis_data = []
        obj_data = {}

        key_names = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8', 'name9', 'name10', 'name11', 'name12', 'name13', 'name14']

        key_cnt = 0
        cnt= 1
        loop_count = 0

        patient_ids = []
        plate_ids = []

        for i in get_patient:
            if cnt <= 96:
                if (cnt == 1):
                    obj_data[key_names[loop_count]] = 'EC'

                    cnt += 1
                    loop_count += 1

                    obj_data[key_names[loop_count]] = i['pool_id']
                    total_no_of_single_samples += 1

                    patient_id_details = PoolSamples.objects.filter(plate_id = i['plate_id']).values_list('patient_id', flat= True)
                    patient_ids.extend(patient_id_details)
                    plate_ids.append(i['plate_id'])

                    cnt += 1
                    loop_count += 1
                
                elif (cnt == 96):
                    obj_data[key_names[loop_count]] = 'PC'

                    cnt += 1
                    loop_count += 1

                else:
                    obj_data[key_names[loop_count]] = i['pool_id']
                    total_no_of_single_samples += 1

                    patient_id_details = PoolSamples.objects.filter(plate_id = i['plate_id']).values_list('patient_id', flat= True)
                    patient_ids.extend(patient_id_details)
                    plate_ids.append(i['plate_id'])

                    cnt += 1
                    loop_count += 1

                if loop_count == 12:
                    sub_lis_data.append(obj_data)
                    res_list.append(sub_lis_data)
                    sub_lis_data = []
                    obj_data = {}
                    loop_count = 0
            else:
                break

        
        flag = True
        if cnt <= 96:
            while flag:
                if cnt <= 96:
                    if cnt == 1:
                        obj_data[key_names[loop_count]] = 'EC'

                        cnt += 1
                        loop_count += 1

                        obj_data[key_names[loop_count]] = ''

                        cnt += 1
                        loop_count += 1
                    
                    if cnt == 96:
                        obj_data[key_names[loop_count]] = 'PC'

                        cnt += 1
                        loop_count += 1

                        flag = False
                    else:
                        obj_data[key_names[loop_count]] = ''

                        cnt += 1
                        loop_count += 1

                    if loop_count == 12:
                        sub_lis_data.append(obj_data)
                        res_list.append(sub_lis_data)
                        sub_lis_data = []
                        obj_data = {}
                        loop_count = 0

                else:
                    flag = False


        alp_cnt = 0
        for i in res_list:
            i[0]['name'] = static_apl_data[alp_cnt]
            alp_cnt += 1


        return Response({'result':res_list, 'total_no_of_pool_samples':total_no_of_single_samples * 5, 'last_plate_no':last_plate_no, 'patient_ids':patient_ids, 'plate_ids':plate_ids})


    
    

#########################          SUBMIT FOR INDIVIDUAL TESTING          #########################
class SubmitForIndividualTesting(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        patient_ids = data.get('patient_ids')

        patient_details = Patient.objects.filter(id__in= patient_ids).update(submit_for_individual_testing= 1)

        return Response({'result':'Plate Submitted For Testing'}, status= status.HTTP_200_OK)




#########################          SUBMIT FOR POOL TESTING          #########################
class SubmitForPoolTesting(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        patient_ids = data.get('patient_ids')
        pool_ids = data.get('pool_ids')

        patient_details = Patient.objects.filter(id__in= patient_ids).update(submit_for_pool_testing= 1)
        patient_details = PoolSamples.objects.filter(plate_id__in= pool_ids).update(submit_for_pool_testing= 1)

        return Response({'result':'Plate Submitted For Testing'}, status= status.HTTP_200_OK)

    
    
    
    
#########################          UPDATE LAB ID / GENERATE LAB ID          #########################
class UpdatePatientLabId(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        user_id = data.get('user_id')
        package_id = data.get('package_id')


        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        
        package_data = Package_Sampling.objects.get(id= package_id)

        update_package_data = Package_Sampling.objects.filter(id= package_id).update(created_group_pool_data= 1)

        patient_data_update = Patient.objects.filter(package_sampling_id= package_data.id).update(lab_ops_received_datetime= asdatetime.now(),)

        patient_data = Patient.objects.filter(package_sampling_id= package_data.id).values()


        last_plate_no_details = GroupPlate.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id)).order_by('-id')[:1]

        print(last_plate_no_details)

        last_plate_no = '0'
        if last_plate_no_details:
            for i in last_plate_no_details:
                last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        else:
            last_plate_no = str(1).zfill(3)

        create_plate = GroupPlate.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_no= last_plate_no)

        count = 1
        for i in patient_data:
            print(count)
            count += 1

            print(i['id'])

            master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

            lab_max_cap= int(master_lab_data.max_capacity) - 1

            split_gen_lab_id = ''
            if master_lab_data.last_genearte_lab_id:
                # print("CHECK LAB ID PRESENT")
                split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
            else:
                # print("CHECK LAB ID NOT")
                len_of_cap = str(master_lab_data.max_capacity)
                split_gen_lab_id = '0000'

            

            if int(split_gen_lab_id) == lab_max_cap:
                # print("IF MAX LAB REACHED")
                patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'A0001')

                GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
            
            else:
                
                update_lab_id_data = int(split_gen_lab_id) + 1

                last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now())
                patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)
                test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])

        return Response({'result': 'Updated Sucessfully'}, status=status.HTTP_200_OK)



#########################      GET LAB PLATE DATA      #########################
class GetTlabOPSPlateData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        get_plate_details = GroupPlate.objects.filter(Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values().order_by('id')

        for i in get_plate_details:
            master_lab_data = Master_Labs.objects.get(id= i['master_lab_id'])
            i['lab_name'] = master_lab_data.lab_name
            i['lab_id'] = master_lab_data.lab_id

        return Response(get_plate_details)



#########################      GET PLATE SAMPLES DETAILS       #########################
class GetTlabOPSPlatePatientDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        plate_id = data.get('plate_id')

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        master_data = Master_Labs.objects.get(id= get_tlf_data.testing_lab_master_id)

        get_group_sam_plate_id = GroupPlate.objects.get(id= plate_id)

        get_plate_details = GroupSamples.objects.filter(Q(plate_id= plate_id) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values()

        for i in get_plate_details:

            get_patient_data = Patient.objects.get(id= i['patient_id'])

            check_data = Patient_Testing.objects.filter(Q(patient_id= i['patient_id']) & Q(rtpcr_test= 1))
            if check_data:
                get_patient_test_data = Patient_Testing.objects.get(Q(patient_id= i['patient_id']) & Q(rtpcr_test= 1))
                i['test_result'] = get_patient_test_data.testing_status
                i['test_result_id'] = get_patient_test_data.id

                # Patient.objects.filter(id= i['patient_id']).update(group_samples_result= 1)
                Patient.objects.filter(id= i['patient_id']).update(group_samples_result= 0)

            else:
                # test_result_create = Patient_Testing.objects.create(patient_id= i['patient_id'], testing_status= 2, rtpcr_test= 1)
                test_result_create = Patient_Testing.objects.create(patient_id= i['patient_id'], testing_status= 4, rtpcr_test= 1)
                i['test_result'] = 4
                i['test_result_id'] = test_result_create.id
                # Patient.objects.filter(id= i['patient_id']).update(group_samples_result= 1)
                Patient.objects.filter(id= i['patient_id']).update(group_samples_result= 0)

            GroupSamples.objects.filter(id= i['id']).update(test_result= 4)

            i['srf_id'] = get_patient_data.srf_id
            i['patient_name'] = get_patient_data.patient_name
            i['mobile_number'] = get_patient_data.mobile_number
            i['rat_created_id'] = get_patient_data.rat_created_id
            i['lab_id'] = get_patient_data.test_lab_id
            i['plate_no']= get_group_sam_plate_id.plate_no
            i['patient_id']= i['patient_id']
            i['age']= str(get_patient_data.age) +' '+ get_patient_data.age_type
            i['patient_status'] = get_patient_data.patient_status

        
        return Response(get_plate_details)







#########################      UPDATE GROUP SAMPLES TEST RESULT       #########################
class UpdateGroupSamplesTestResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        patient_id = data.get('patient_id')
        test_result_id = data.get('test_result_id')
        result_status= data.get('result_status')

        check_data = Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= patient_id))

        if check_data:
            Patient.objects.filter(id= patient_id).update(group_samples_result= 1)
            Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= patient_id)).update(testing_status= result_status, last_update_timestamp= asdatetime.now())
            
        else:
            Patient.objects.filter(id= patient_id).update(group_samples_result= 1)
            Patient_Testing.objects.create(Q(id= test_result_id) & Q(patient_id= patient_id)).update(testing_status= result_status)
            
        if user_id:
            check_lab_data = Testing_Lab_Facility.objects.get(user_id= user_id)
            Master_Labs.objects.filter(id = check_lab_data.testing_lab_master_id).update(closing_balance = F('closing_balance') + 1)

        return Response({'result': 'Group Result Updated'})



#########################      GET LAB POOL PLATE DATA      #########################
class GetTlabOPSPoolPlateData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        get_plate_details = PoolPlate.objects.filter(Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values().order_by('-id')

        for i in get_plate_details:
            master_lab_data = Master_Labs.objects.get(id= i['master_lab_id'])
            i['lab_name'] = master_lab_data.lab_name

        return Response(get_plate_details)



#########################      GET POOL PLATE SAMPLES DETAILS       #########################
class GetTlabOPSPoolPlatePatientDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        plate_id = data.get('plate_id')

        get_tlf_data = Testing_Lab_Facility.objects.get(user_id= user_id)

        master_data = Master_Labs.objects.get(id= get_tlf_data.testing_lab_master_id)

        get_group_sam_plate_id = PoolPlate.objects.get(id= plate_id)

        # get_plate_details = PoolSamples.objects.filter(Q(plate_id= plate_id) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values()

        # for i in get_plate_details:

        #     get_patient_data = Patient.objects.get(id= i['patient_id'])

        #     check_data = Patient_Testing.objects.filter(Q(patient_id= i['patient_id']) & Q(rtpcr_test= 1))
        #     if check_data:
        #         get_patient_test_data = Patient_Testing.objects.get(Q(patient_id= i['patient_id']) & Q(rtpcr_test= 1))
        #         i['test_result'] = get_patient_test_data.testing_status
        #         i['test_result_id'] = get_patient_test_data.id

        #     else:
        #         test_result_create = Patient_Testing.objects.create(patient_id= i['patient_id'], testing_status= 2, rtpcr_test= 1)
        #         i['test_result'] = 2
        #         i['test_result_id'] = test_result_create.id

        #     PoolSamples.objects.filter(id= i['id']).update(test_result= 2)

        #     i['srf_id'] = get_patient_data.srf_id
        #     i['patient_name'] = get_patient_data.patient_name
        #     i['mobile_number'] = get_patient_data.mobile_number
        #     i['rat_created_id'] = get_patient_data.rat_created_id
        #     i['lab_id'] = get_patient_data.test_lab_id
        #     i['plate_no']= get_group_sam_plate_id.plate_no
        #     i['patient_id']= i['patient_id']
            
        get_pool_plate_details = PoolSamples.objects.filter(Q(plate_id= plate_id) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id)).values('plate_id', 'pool_id', 'test_result').distinct()

        for j in get_pool_plate_details:
            print(j)
            plate_no_details = PoolPlate.objects.get(id= j['plate_id'])

            j['plate_no']= plate_no_details.plate_no
            j['create_datetime']= str(plate_no_details.create_datetime)

            check_test_result = j['test_result']
            if check_test_result:
                j['test_result'] = j['test_result']
            else:
                j['test_result'] = 2
            

            # get_pool_sam_data = PoolSamples.objects.filter(Q(plate_id= j['plate_id']) & Q(pool_id= j['pool_id']) & Q(test_lab_id= get_tlf_data.id) & Q(master_lab_id= get_tlf_data.testing_lab_master_id))
            # check_test_result = get_pool_sam_data.test_result
            # if check_test_result:
            #     j['test_result'] = get_pool_sam_data.test_result
            # else:
            #     j['test_result'] = 2


        print("GET POOL DATA")
        print("GET POOL DATA", get_pool_plate_details)
        print("GET POOL DATA", len(get_pool_plate_details))

        return Response(get_pool_plate_details)






#########################      UPDATE POOL SAMPLES TEST RESULT       #########################
class UpdatePoolSamplesTestResult(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        pool_id = data.get('pool_id')
        plate_id = data.get('plate_id')
        test_result_id = data.get('test_result_id')
        result_status= data.get('result_status')

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        master_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

        check_data = PoolPlate.objects.filter(id= plate_id)

        test_pool_patients = PoolSamples.objects.filter(Q(plate_id= plate_id) & Q(pool_id= pool_id)).update(test_result= result_status)

        test_pool_patients = PoolSamples.objects.filter(Q(plate_id= plate_id) & Q(pool_id= pool_id)).values()


        for i in test_pool_patients:

            if int(result_status) == 2:

                check_data = Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id']))

                if check_data:
                    Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id'])).update(testing_status= result_status, last_update_timestamp= asdatetime.now())
                    Patient.objects.filter(id= i['patient_id']).update(pool_samples_result= 1)
                else:
                    Patient_Testing.objects.create(patient_id= i['patient_id'], testing_status= result_status)
                    Patient.objects.filter(id= i['patient_id']).update(pool_samples_result= 1)
            
            if int(result_status) == 3:

                print(i['patient_id'])
                print("PATIENT IDE")

                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                split_gen_lab_id = ''
                if master_lab_data.last_genearte_lab_id:
                    # print("CHECK LAB ID PRESENT")
                    split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
                else:
                    # print("CHECK LAB ID NOT")
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'


                if int(split_gen_lab_id) == lab_max_cap:
                    print("IF MAX LAB REACHED")
                    patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, test_lab_id= master_lab_data.last_genearte_lab_id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'A0001')
                
                else:
                    print("HELLO HELLO HELLO")
                    update_lab_id_data = int(split_gen_lab_id) + 1
                    last_lab_id = 'A'+str(update_lab_id_data).zfill(4)

                    patient_data_update = Patient.objects.filter(id= i['patient_id']).update(lab_master_id= master_lab_data.id, test_lab_id= last_lab_id, last_update_timestamp= asdatetime.now(), group_samples= 1, pool_samples_result= 1, submit_for_pool_testing =0)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)

                    # check_data = Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id']))
                    # if check_data:
                    #     Patient_Testing.objects.filter(Q(id= test_result_id) & Q(patient_id= i['patient_id'])).update(testing_status= result_status, last_update_timestamp= asdatetime.now())
                    # else:
                    #     Patient_Testing.objects.create(Q(id= test_result_id) & Q(patient_id= i['patient_id'])).update(testing_status= result_status)


            # inc_closeing_blc = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id).update(closing_balance = F('closing_balance') + 1)

        return Response({'result': 'Updated'})


    
    
    

#########################          GET DE-SAMPLED PATIENT DETAILS          #########################
class GetDesampledPatientDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        page_no = data.get('page_no')

        selected_page_no = 1
        if page_no:
            selected_page_no = int(page_no)

        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        get_patient_data = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 1) & Q(pool_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples_result = 1) & Q(submit_for_individual_testing= 1) & Q(group_samples_result= 0)).values()
        get_patient_data_count = Patient.objects.filter(Q(lab_master_id= check_user_details.testing_lab_master_id) & Q(lab_ops_received_datetime__isnull= False) & Q(group_samples= 1) & Q(pool_samples= 1) & Q(group_samples_result= 0) & Q(pool_samples_result = 1) & Q(submit_for_individual_testing= 1) & Q(group_samples_result= 0)).count()

        get_patient_details = paginatorCreation(get_patient_data, selected_page_no)

        for i in get_patient_details:
            check_patient_test_result = list(Patient_Testing.objects.filter(Q(patient_id= i['id'])).values('testing_status','id'))
            print(check_patient_test_result)
            if check_patient_test_result:
                i['test_result'] = check_patient_test_result[0]['testing_status']
                i['test_result_id'] = check_patient_test_result[0]['id']
            else:
                test_result_create = Patient_Testing.objects.create(patient_id= i['id'], testing_status= 4, rtpcr_test= 1)
                
                i['test_result'] = 4
                i['test_result_id'] = test_result_create.id


        return Response({'patient_details':list(get_patient_details), 'total_pg_count':get_patient_data_count}, status= status.HTTP_200_OK)

    
    
    


#########################          CREATE POOL IDS          #########################
class UpdatePatientPoolLabId(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        data = request.data

        user_id = data.get('user_id')
        package_id = data.get('package_id')

        print(data)


        check_user_details = Testing_Lab_Facility.objects.get(user_id= user_id)

        package_data = Package_Sampling.objects.get(id= package_id)

        update_package_data = Package_Sampling.objects.filter(id= package_id).update(created_group_pool_data= 1)

        patient_data_update = Patient.objects.filter(package_sampling_id= package_data.id).update(lab_ops_received_datetime= asdatetime.now(),)

        patient_data = Patient.objects.filter(package_sampling_id= package_data.id).values()


        last_plate_no_details = PoolPlate.objects.filter(Q(test_lab_id= check_user_details.id) & Q(master_lab_id= check_user_details.testing_lab_master_id)).order_by('-id')[:1]

        print(last_plate_no_details)

        last_plate_no = '0'
        if last_plate_no_details:
            for i in last_plate_no_details:
                last_plate_no = str(int(i.plate_no) + 1).zfill(3)
        else:
            last_plate_no = str(1).zfill(3)

        create_plate = PoolPlate.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_no= last_plate_no)

        check_package_samples_count = package_data.samples_count
        check_pool_count = int(package_data.samples_count) / 5
        main_pool_sam = int(str(check_pool_count).split('.')[0])
        sub_pool_sam = int(str(check_pool_count).split('.')[1])

        if sub_pool_sam == 2:
            sub_pool_sam = 1

        if sub_pool_sam == 4:
            sub_pool_sam = 2

        if sub_pool_sam == 6:
            sub_pool_sam = 3

        if sub_pool_sam == 8:
            sub_pool_sam = 4
        
        pat_iteration = 0

        check_sub_sam_def = 1
        split_gen_lab_id = ''


        for i in patient_data:

            print(i['id'])

            if main_pool_sam != 0 and pat_iteration == 0:
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                if master_lab_data.last_genearte_lab_id:
                    split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
                else:
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'

                update_lab_id_data = int(split_gen_lab_id) + 1
                last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)


            # Extra Access Data Here We are Generating POOL id for that too e.g: 12/5 = 2.4 => (2 complete POOL id (2*5= 10) 2 extra sample here we are creating one pool id for 2 samples) 1 pool id = 5 samples
            if main_pool_sam == 0 and pat_iteration == 0 and check_sub_sam_def == 1:
                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                if master_lab_data.last_genearte_lab_id:
                    split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
                else:
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'

                update_lab_id_data = int(split_gen_lab_id) + 1
                # last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                last_lab_id = 'A'+str(update_lab_id_data).zfill(4)
                Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)

                check_sub_sam_def = 0



            if pat_iteration <= 4 and check_sub_sam_def == 1:

                if int(split_gen_lab_id) == lab_max_cap:

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'P0001')

                    PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)
                
                else:
                    
                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                    print(check_user_details.id)
                    print(check_user_details.testing_lab_master_id)
                    print(create_plate.id)
                    print(i['id'])
                    print(get_mas_lab_data.last_genearte_lab_id)

                    PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)


            if main_pool_sam == 0 and check_sub_sam_def == 0:

                # if int(split_gen_lab_id) == lab_max_cap:

                #     get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)
                #     patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                #     Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'P0001')

                #     PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)
                
                # else:
                    
                #     get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                #     # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now())
                #     patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= get_mas_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now(), pool_samples= 1)
                #     test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                #     PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)

                master_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id)

                lab_max_cap= int(master_lab_data.max_capacity) - 1

                if master_lab_data.last_genearte_lab_id:
                    split_gen_lab_id = master_lab_data.last_genearte_lab_id[1:]
                else:
                    len_of_cap = str(master_lab_data.max_capacity)
                    split_gen_lab_id = '0000'

                update_lab_id_data = int(split_gen_lab_id) + 1
                # last_lab_id = 'P'+str(update_lab_id_data).zfill(4)
                last_lab_id = 'A'+str(update_lab_id_data).zfill(4)
                Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= last_lab_id)


                if int(split_gen_lab_id) == lab_max_cap:

                    print("CHACK UPDATE ID")

                    get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)
                    change_p_to_a = 'A'+(str(get_mas_lab_data.last_genearte_lab_id)[1:])
                    print(change_p_to_a)
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= change_p_to_a, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    Master_Labs.objects.filter(id= check_user_details.testing_lab_master_id).update(last_genearte_lab_id= 'A0001')

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)
                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])
                    
                    GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, patient_id= i['id'])
                
                else:
                    
                    # get_mas_lab_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                    # patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= master_lab_data.last_genearte_lab_id, lab_ops_received_datetime= asdatetime.now())
                    patient_data_update = Patient.objects.filter(id= i['id']).update(lab_master_id= check_user_details.testing_lab_master_id, test_lab_id= last_lab_id, lab_ops_received_datetime= asdatetime.now(), group_samples= 1)
                    test_data = Master_Labs.objects.get(id= check_user_details.testing_lab_master_id) #.update(last_genearte_lab_id= last_lab_id)

                    # PoolSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'], pool_id= get_mas_lab_data.last_genearte_lab_id,)
                    # GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, plate_id= create_plate.id, patient_id= i['id'])

                    GroupSamples.objects.create(test_lab_id= check_user_details.id, master_lab_id= check_user_details.testing_lab_master_id, patient_id= i['id'])


            if pat_iteration == 4:
                pat_iteration = 0
                main_pool_sam -= 1
            else:
                pat_iteration += 1

        return Response({'result': 'Pool Updated Sucessfully'}, status=status.HTTP_200_OK)



#########################          POOL PATIENT TEST RESULT VIEW          #########################
class PatientPoolTestResultView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        plate_id = data.get('plate_id')
        pool_id = data.get('pool_id')

        user_test_lab_details = Testing_Lab_Facility.objects.get(user_id= user_id)
        master_lab_data = Master_Labs.objects.get(id= user_test_lab_details.testing_lab_master_id)

        plate_data = PoolPlate.objects.get(id= plate_id)
        check_all_patient_details = PoolSamples.objects.filter(Q(test_lab_id= user_test_lab_details.id) & Q(master_lab_id= user_test_lab_details.testing_lab_master_id) & Q(plate_id= plate_id) & Q(pool_id= pool_id)).values()

        for i in check_all_patient_details:

            patient_data = Patient.objects.get(id= i['patient_id'])

            i['plate_no'] = plate_data.plate_no
            i['lab_id'] = master_lab_data.id
            i['srf_id'] = patient_data.srf_id
            i['patient_name'] = patient_data.patient_name
            i['retest'] = True

        return Response(check_all_patient_details)



#########################          ACCEPT PACKAGE THO DSO SSU          #########################
class AcceptPackageSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        package_id = data.get('package_id')

        check_ssu_data = SSU.objects.filter(user_id= user_id)
        check_dso_data = DSO.objects.filter(user_id= user_id)
        check_tho_data = THO.objects.filter(user_id= user_id)

        if check_ssu_data:

            ssu_data = Package_Sampling.objects.filter(id=package_id)#.update(package_type_action= 13, package_type_status= 3)

        if check_dso_data:

            dso_data = Package_Sampling.objects.filter(id=package_id).update(package_type_action= 20, package_type_status= 10)

        if check_tho_data:
            
            tho_data = Package_Sampling.objects.filter(id=package_id).update(package_type_action= 19, package_type_status= 9)

        return Response({'result':'Accepted'})



#########################          ICMR ACCESS TOKEN          #########################
class ICMRGetAccessToken(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        username = data.get('username')
        password = data.get('password')

        if username and password:
            json_body = json.dumps({'username': username, 'password': password})

            url = 'https://cvstatus.icmr.gov.in/api/nic/icmr_api/index.php/login'

            response = requests.post(url, data= json_body)

            res_json = response.json()

            return Response({'result': res_json}, status= status.HTTP_200_OK)


        else:
            return Response({'result':'Please Enter Username and Password'}, status=status.HTTP_400_BAD_REQUEST)



#########################          ICMR ADD RECORD          #########################
class ICMRAddPatientRecord(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        print(data)


        auth_token = data.get('token')

        url = 'https://cvstatus.icmr.gov.in/api/nic/icmr_api/index.php/add-record'

        get_icmr_data = ICMRDataPush.objects.filter(updated_samples_status= 0).values()
        
        result = []
        cnt = 0
        for i in get_icmr_data:

            if cnt == 0:

                body_data = {
                            "patient_id":i['patient_id'],
                            "patient_name": i['patient_name'],
                            "gender": i['gender'],
                            "age": i['age'],
                            "age_in": i['age_in'],
                            "contact_number": i['contact_number'],
                            "contact_number_belongs_to": i['contact_number_belongs_to'],
                            "nationality": i['nationality'],
                            "state": i['state'],
                            "district": i['district'],
                            "pincode":"",
                            "aadhar_number":"",
                            "passport_number":"",
                            "patient_category": i['patient_category'],
                            "address": i['address'],
                            "patient_area": i['patient_area'],
                            "occupation": i['occupation'],
                            "aarogya_setu_app_downloaded": i['aarogya_setu_app_downloaded'],
                            "contact_with_lab_confirmed_patient": i['contact_with_lab_confirmed_patient'],
                            "srf_id": i['srf_id'],
                            "sample_cdate": i['sample_cdate'],
                            "sample_rdate": i['sample_rdate'],
                            "sample_type": i['sample_type'],
                            "sample_id": i['sample_id'],
                            "sample_collected_from": i['sample_collected_from'],
                            "status": i['status'],
                            "symptoms": i['symptoms'],
                            "date_of_onset_of_symptoms":"",
                            "underlying_medical_condition": i['underlying_medical_condition'],
                            "vaccine_recevied": i['vaccine_recevied'],
                            "vaccine_type": i['vaccine_type'],
                            "vaccine_dose1_date": i['vaccine_dose1_date'],
                            "vaccine_dose2_date":"",
                            "hospitalized" : i['hospitalized'],
                            "hospital_name" : "",
                            "hospitalization_date" : "",
                            "hospital_state" : "",
                            "hospital_district" : "",
                            "sample_tdate": i['sample_tdate'],
                            "testing_kit_used" : i['testing_kit_used'],
                            "covid19_result_egene" : i['covid19_result_egene'],
                            "ct_value_screening" : "",
                            "orf1b_confirmatory" : "",
                            "ct_value_orf1b" : "",
                            "rdrp_confirmatory" : i['rdrp_confirmatory'],
                            "ct_value_rdrp" : "",
                            "final_result_of_sample": i['final_result_of_sample'],
                            "repeat_sample": i['repeat_sample'],
                            "transport_mode_used_to_visit_testing_facility" : i['transport_mode_used_to_visit_testing_facility'],
                            "remarks":"",
                            "lab_id" : i['lab_id'],
                            "lab_code" : i['lab_code']
                        }

                header = {'Authorization': 'Bearer ' + auth_token}

                json_body = json.dumps(body_data)
                json_header = json.dumps(header)

                response = requests.post(url, data= json_body, headers= header)

                res_text = response.text
                res_json = response.json()


                result.append({'response': res_json})

                cnt += 1

                ICMRDataPush.objects.filter(id= i['id']).update(updated_samples_status= 1)


        return Response({'result':result,}, status= status.HTTP_200_OK)
        




#########################          Universal Search          #########################
class UniversalSearch(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        srf_id = data.get('srf_id')
        mobile_number = data.get('mobile_number')

        if srf_id and mobile_number:
            fil_data = Patient.objects.filter(Q(mobile_number= mobile_number) & Q(srf_id= srf_id)).values()

            for i in fil_data:
                # loc_add_data = Patient_Address.objects.filter(patient_id = i['id'])
                # out_add_data = Outside_Patient_Address.objects.filter(patient_id= i['id'])

                # if loc_add_data:
                #     for j in loc_add_data:
                #         i['state_name'] = j.state_name
                #         i['']

                test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                spcm_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])

                i['test_type_name'] = test_type_data.test_type_name
                i['specimen_type_name'] = spcm_type_data.specimen_type_name

                if test_type_data.test_type_name == 'RAT':
                    test_kit_details = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if test_kit_details:
                        i['testing_kit_name'] = test_kit_details[0]
                    else:
                        i['testing_kit_name'] = '-'



                pt_data = Patient_Testing.objects.filter(patient_id= i['id'])
                if pt_data:
                    for j in pt_data:
                        i['lab_received_date'] = str(j.lab_received_date)
                        i['rtpcr_test'] = j.rtpcr_test
                        i['testing_status'] = j.testing_status
                        i['test_date'] = j.create_timestamp
                else:
                    i['lab_received_date'] = '-'
                    i['rtpcr_test'] = '-'
                    i['testing_status'] = 4
                    i['test_date'] = '-'

                # pckg_data = Package_Sampling.objects.filter(id = i['package_sampling_id'])
                # if pckg_data:
                #     for j in pckg_data:
                #         i['package_sampling_name'] = j.package_sampling_name
                #         i['package_sampling_barcode'] = j.package_sampling_barcode
                #         i['package_type_status'] = j.package_type_status
                #         i['package_type_action'] = j.package_type_action

                pckg_data = list(Package_Sampling.objects.filter(id = i['package_sampling_id']).values('package_sampling_name', 'package_sampling_barcode', 'package_type_status', 'package_type_action', 'lab_master__lab_name'))
                if pckg_data:
                    # for j in pckg_data:
                    i['package_sampling_name'] = pckg_data[0]['package_sampling_name']
                    i['package_sampling_barcode'] = pckg_data[0]['package_sampling_barcode']
                    i['package_type_status'] = pckg_data[0]['package_type_status']
                    i['package_type_action'] = pckg_data[0]['package_type_action']

                    if pckg_data[0]['package_type_status'] and pckg_data[0]['package_type_action']:
                        i['lab_name'] = pckg_data[0]['lab_master__lab_name']
                    else:
                        i['lab_name'] = '-'

                else:
                    i['package_sampling_name'] = '-'
                    i['package_sampling_barcode'] = '-'
                    i['package_type_status'] = 33
                    i['package_type_action'] = 33
                    i['lab_name'] = '-'


            return Response({'result':fil_data, 'message':'Sucess'}, status= status.HTTP_200_OK)



        if mobile_number:
            fil_data = Patient.objects.filter(Q(mobile_number= mobile_number)).values()

            for i in fil_data:
                # loc_add_data = Patient_Address.objects.filter(patient_id = i['id'])
                # out_add_data = Outside_Patient_Address.objects.filter(patient_id= i['id'])

                # if loc_add_data:
                #     for j in loc_add_data:
                #         i['state_name'] = j.state_name
                #         i['']

                test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                spcm_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])

                i['test_type_name'] = test_type_data.test_type_name
                i['specimen_type_name'] = spcm_type_data.specimen_type_name

                if test_type_data.test_type_name == 'RAT':
                    check_test_kit = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_test_kit:
                        i['testing_kit_name'] = check_test_kit[0]
                    else:
                        i['testing_kit_name'] = '-'

                    # i['testing_kit_name'] = (Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True))[0]

                pt_data = Patient_Testing.objects.filter(patient_id= i['id'])
                if pt_data:
                    for j in pt_data:
                        i['lab_received_date'] = str(j.lab_received_date)
                        i['rtpcr_test'] = j.rtpcr_test
                        i['testing_status'] = j.testing_status
                        i['test_date'] = j.create_timestamp
                else:
                    i['lab_received_date'] = '-'
                    i['rtpcr_test'] = '-'
                    i['testing_status'] = 4
                    i['test_date'] = '-'

                pckg_data = list(Package_Sampling.objects.filter(id = i['package_sampling_id']).values('package_sampling_name', 'package_sampling_barcode', 'package_type_status', 'package_type_action', 'lab_master__lab_name'))
                
                if pckg_data:
                    # for j in pckg_data:
                    i['package_sampling_name'] = pckg_data[0]['package_sampling_name']
                    i['package_sampling_barcode'] = pckg_data[0]['package_sampling_barcode']
                    i['package_type_status'] = pckg_data[0]['package_type_status']
                    i['package_type_action'] = pckg_data[0]['package_type_action']

                    if pckg_data[0]['package_type_status'] and pckg_data[0]['package_type_action']:
                        i['lab_name'] = pckg_data[0]['lab_master__lab_name']
                    else:
                        i['lab_name'] = '-'
                else:
                    i['package_sampling_name'] = '-'
                    i['package_sampling_barcode'] = '-'
                    i['package_type_status'] = 33
                    i['package_type_action'] = 33
                    i['lab_name'] = '-'

            return Response({'result':fil_data, 'message':'Sucess'}, status= status.HTTP_200_OK)



        if srf_id:
            fil_data = Patient.objects.filter(Q(srf_id= srf_id)).values()

            for i in fil_data:
                # loc_add_data = Patient_Address.objects.filter(patient_id = i['id'])
                # out_add_data = Outside_Patient_Address.objects.filter(patient_id= i['id'])

                # if loc_add_data:
                #     for j in loc_add_data:
                #         i['state_name'] = j.state_name
                #         i['']

                test_type_data = Test_Type_Ref.objects.get(id= i['test_type_id'])
                spcm_type_data = Specimen_Type_Ref.objects.get(id= i['specimen_type_id'])

                i['test_type_name'] = test_type_data.test_type_name
                i['specimen_type_name'] = spcm_type_data.specimen_type_name

                if test_type_data.test_type_name == 'RAT':

                    check_test_kit = Testing_Kit_Barcode.objects.filter(id= i['testing_kit_barcode_id']).values_list('testing_kit_barcode_name', flat=True)
                    if check_test_kit:
                        i['testing_kit_name'] = check_test_kit[0]
                    else:
                        i['testing_kit_name'] = '-'


                pt_data = Patient_Testing.objects.filter(patient_id= i['id'])
                if pt_data:
                    for j in pt_data:
                        i['lab_received_date'] = str(j.lab_received_date)
                        i['rtpcr_test'] = j.rtpcr_test
                        i['testing_status'] = j.testing_status
                        i['test_date'] = j.create_timestamp
                else:
                    i['lab_received_date'] = '-'
                    i['rtpcr_test'] = '-'
                    i['testing_status'] = 4
                    i['test_date'] = '-'

                # pckg_data = Package_Sampling.objects.filter(id = i['package_sampling_id'])
                # if pckg_data:
                #     for j in pckg_data:
                #         i['package_sampling_name'] = j.package_sampling_name
                #         i['package_sampling_barcode'] = j.package_sampling_barcode
                #         i['package_type_status'] = j.package_type_status
                #         i['package_type_action'] = j.package_type_action

                pckg_data = list(Package_Sampling.objects.filter(id = i['package_sampling_id']).values('package_sampling_name', 'package_sampling_barcode', 'package_type_status', 'package_type_action', 'lab_master__lab_name'))
                
                if pckg_data:
                    # for j in pckg_data:
                    i['package_sampling_name'] = pckg_data[0]['package_sampling_name']
                    i['package_sampling_barcode'] = pckg_data[0]['package_sampling_barcode']
                    i['package_type_status'] = pckg_data[0]['package_type_status']
                    i['package_type_action'] = pckg_data[0]['package_type_action']

                    if pckg_data[0]['package_type_status'] and pckg_data[0]['package_type_action']:
                        i['lab_name'] = pckg_data[0]['lab_master__lab_name']
                    else:
                        i['lab_name'] = '-'
                else:
                    i['package_sampling_name'] = '-'
                    i['package_sampling_barcode'] = '-'
                    i['package_type_status'] = 33
                    i['package_type_action'] = 33
                    i['lab_name'] = '-'

            return Response({'result':fil_data, 'message':'Sucess'}, status= status.HTTP_200_OK)
        else:
            return Response({'result':[], 'message': 'Something went Wrong'}, status= status.HTTP_400_BAD_REQUEST)























#**********************************************************************************************************************************************************************************************************************************************************************************














#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      Testing_Lab_Facility       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------










class GetPostTesting_Lab_Facility(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_Testing_Lab_Facility = Testing_Lab_Facility.objects.all().values()
        count=Testing_Lab_Facility.objects.all().count()
        print(count)
        return Response(all_Testing_Lab_Facility)
    


    def post(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        package_sampling_id         = data.get('package_sampling_id')
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        testing_lab_facility_name   = data.get('testing_lab_facility_name')
        testing_lab_facility_desc   = data.get('testing_lab_facility_desc')
        address_line_1              = data.get('address_line_1')
        address_line_2              = data.get('address_line_2')
        district_name               = data.get('district_name')
        city_name                   = data.get('city_name')
        ward_name                   = data.get('ward_name')
        taluk_name                  = data.get('taluk_name')
        village_name                = data.get('village_name')
        pincode                     = data.get('pincode')
        current_count               = data.get('current_count')
        availability_limit          = data.get('availability_limit')
        create_timestamp            = data.get('create_timestamp')
        last_update_timestamp       = data.get('last_update_timestamp')
        user_role_id                = data.get('user_role_id')

    
        if password == confirm_password:
            if Testing_Lab_Facility.objects.filter(username=username).exists():
                return Response({
                        'result': 'username already exists'
                    })
            else:  
                Testing_Lab_Facility_create = Testing_Lab_Facility.objects.create(username=username,password=password,package_sampling_id=package_sampling_id,testing_lab_facility_id=testing_lab_facility_id,testing_lab_facility_name=testing_lab_facility_name,testing_lab_facility_desc=testing_lab_facility_desc,address_line_1=address_line_1,address_line_2=address_line_2,district_name=district_name,city_name=city_name,ward_name=ward_name,taluk_name=taluk_name,village_name=village_name,pincode=pincode,current_count=current_count,availability_limit=availability_limit,create_timestamp=create_timestamp,last_update_timestamp=last_update_timestamp,user_role_id=user_role_id)
                return Response({
                        'result': 'Created Testing_Lab_Facility Successfully'
                    })
        else:
            return Response({
                    'result': 'password not matching'
                })



    

class GetPutPatchTesting_Lab_Facility(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
       
        try:
            cc = Testing_Lab_Facility.objects.get(id=pk)
        except Testing_Lab_Facility.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = Testing_Lab_FacilitySerializer(cc)
            return Response(serializer.data)
 

    def patch(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        
        package_sampling_id         = data.get('package_sampling_id')
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        testing_lab_facility_name   = data.get('testing_lab_facility_name')
        testing_lab_facility_desc   = data.get('testing_lab_facility_desc')
        address_line_1              = data.get('address_line_1')
        address_line_2              = data.get('address_line_2')
        district_name               = data.get('district_name')
        city_name                   = data.get('city_name')
        ward_name                   = data.get('ward_name')
        taluk_name                  = data.get('taluk_name')
        village_name                = data.get('village_name')
        pincode                     = data.get('pincode')
        current_count               = data.get('current_count')
        availability_limit          = data.get('availability_limit')
        create_timestamp            = data.get('create_timestamp')
        last_update_timestamp       = data.get('last_update_timestamp')
        user_role_id                = data.get('user_role_id')


        if Testing_Lab_Facility.objects.filter(id=pk).exists():
            Testing_Lab_Facility.objects.filter(id = pk).update(package_sampling_id=package_sampling_id,testing_lab_facility_id=testing_lab_facility_id,testing_lab_facility_name=testing_lab_facility_name,testing_lab_facility_desc=testing_lab_facility_desc,address_line_1=address_line_1,address_line_2=address_line_2,district_name=district_name,city_name=city_name,ward_name=ward_name,taluk_name=taluk_name,village_name=village_name,pincode=pincode,current_count=current_count,availability_limit=availability_limit,create_timestamp=create_timestamp,last_update_timestamp=last_update_timestamp,user_role_id=user_role_id)
            return Response({
                'result': 'Updated Successfully'
            })
        else:
            return Response({'result': 'Invalid ID'})


    def put(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        package_sampling_id         = data.get('package_sampling_id')
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        testing_lab_facility_name   = data.get('testing_lab_facility_name')
        testing_lab_facility_desc   = data.get('testing_lab_facility_desc')
        address_line_1              = data.get('address_line_1')
        address_line_2              = data.get('address_line_2')
        district_name               = data.get('district_name')
        city_name                   = data.get('city_name')
        ward_name                   = data.get('ward_name')
        taluk_name                  = data.get('taluk_name')
        village_name                = data.get('village_name')
        pincode                     = data.get('pincode')
        current_count               = data.get('current_count')
        availability_limit          = data.get('availability_limit')
        create_timestamp            = data.get('create_timestamp')
        last_update_timestamp       = data.get('last_update_timestamp')
        user_role_id                = data.get('user_role_id')

    
        if password == confirm_password:
            if Testing_Lab_Facility.objects.filter(username=username).exists():
                return Response({
                        'result': 'username already exists'
                    })
            else:  
                Testing_Lab_Facility_create = Testing_Lab_Facility.objects.create(username=username,password=password,package_sampling_id=package_sampling_id,testing_lab_facility_id=testing_lab_facility_id,testing_lab_facility_name=testing_lab_facility_name,testing_lab_facility_desc=testing_lab_facility_desc,address_line_1=address_line_1,address_line_2=address_line_2,district_name=district_name,city_name=city_name,ward_name=ward_name,taluk_name=taluk_name,village_name=village_name,pincode=pincode,current_count=current_count,availability_limit=availability_limit,create_timestamp=create_timestamp,last_update_timestamp=last_update_timestamp,user_role_id=user_role_id)
                return Response({
                        'result': 'Created Testing_Lab_Facility Successfully'
                    })
        else:
            return Response({
                    'result': 'password not matching'
                })



#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      SSU       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostSSU(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_SSU = SSU.objects.all().values()
        return Response(all_SSU)
    
    def post(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        ssu_id                      = data.get('ssu_id') 
        ssu_name                    = data.get('ssu_name') 
        ssu_desc                    = data.get('ssu_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')

    
        if password == confirm_password:
    
        
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                # lab_name  = Testing_Lab_Facility.objects.get(id=testing_lab_facility_id)
                # print(lab_name)
                if SSU.objects.filter(username=username).exists():
                    return Response({
                            'result': 'username already exists'
                        })
                else:
                    SSU.objects.create(username=username,password=password ,ssu_id =ssu_id  ,ssu_name =ssu_name  ,ssu_desc =ssu_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id)
                    return Response({
                        'result': ' SSU create Successfully'
                    })

            else:
                return Response({'result': 'Invalid SSU'})
        else:
            return Response({
                    'result': 'password not matching'
                })


class GetPutPatchSSU(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
       
        try:
            cc = SSU.objects.get(id=pk)
        except SSU.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = SSUSerializer(cc)
            return Response(serializer.data)
 

    def patch(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        ssu_id                      = data.get('ssu_id') 
        ssu_name                    = data.get('ssu_name') 
        ssu_desc                    = data.get('ssu_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')

        if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
            # lab_name  = Testing_Lab_Facility.objects.get(testing_lab_facility_name)
        
            if SSU.objects.filter(id=pk).exists():
                SSU.objects.filter(id = pk).update(ssu_id =ssu_id  ,ssu_name =ssu_name  ,ssu_desc =ssu_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id)
                return Response({
                    'result': 'Updated Successfully'
                })
            else:
                return Response({'result': 'Invalid ID'})
        else:
            return Response({'result': 'Invalid Testing Lab'})


    def put(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        ssu_id                      = data.get('ssu_id') 
        ssu_name                    = data.get('ssu_name') 
        ssu_desc                    = data.get('ssu_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')

    
        if password == confirm_password:
    
        
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                # lab_name  = Testing_Lab_Facility.objects.get(id=testing_lab_facility_id)
                # print(lab_name)
                if SSU.objects.filter(username=username).exists():
                    return Response({
                            'result': 'username already exists'
                        })
                else:
                    SSU.objects.create(username=username,password=password ,ssu_id =ssu_id  ,ssu_name =ssu_name  ,ssu_desc =ssu_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id)
                    return Response({
                        'result': ' SSU create Successfully'
                    })

            else:
                return Response({'result': 'Invalid SSU'})
        else:
            return Response({
                    'result': 'password not matching'
                })


#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      DSO       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostDSO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_DSO = DSO.objects.all().values()
        return Response(all_DSO)
    
    def post(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        dso_id                      = data.get('dso_id') 
        dso_name                    = data.get('dso_name') 
        dso_desc                    = data.get('dso_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        ssu_id                      = data.get('ssu_id')
    
        if password == confirm_password:
    
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                if SSU.objects.filter(id=ssu_id).exists():
                    if DSO.objects.filter(username=username).exists():
                        return Response({
                                'result': 'username already exists'
                            })
                    else:
                        DSO.objects.create(username=username,password=password ,dso_id =dso_id  ,dso_name =dso_name  ,dso_desc =dso_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,ssu_id=ssu_id)
                        return Response({
                            'result': 'DSO created Successfully'
                        })
                else:
                    return Response({'result': 'Invalid SSU'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })


class GetPutPatchDSO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
       
        try:
            cc = DSO.objects.get(id=pk)
        except DSO.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = DSOSerializer(cc)
            return Response(serializer.data)
 

    def patch(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        dso_id                      = data.get('dso_id') 
        dso_name                    = data.get('dso_name') 
        dso_desc                    = data.get('dso_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        ssu_id                      = data.get('ssu_id')

        if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
            # lab_name  = Testing_Lab_Facility.objects.get(testing_lab_facility_name)
            if SSU.objects.filter(id=ssu_id).exists():
                if DSO.objects.filter(id=pk).exists():
                    DSO.objects.filter(id = pk).update(dso_id =dso_id  ,dso_name =dso_name  ,dso_desc =dso_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,ssu_id=ssu_id)
                    return Response({
                        'result': 'Updated Successfully'
                    })
                else:
                    return Response({'result': 'Invalid DSO ID'})
            else:
                    return Response({'result': 'Invalid SSU ID'})
        else:
            return Response({'result': 'Invalid Testing Lab'})


    def put(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        dso_id                      = data.get('dso_id') 
        dso_name                    = data.get('dso_name') 
        dso_desc                    = data.get('dso_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        ssu_id                      = data.get('ssu_id')
    
        if password == confirm_password:
    
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                if SSU.objects.filter(id=ssu_id).exists():
                    if DSO.objects.filter(username=username).exists():
                        return Response({
                                'result': 'username already exists'
                            })
                    else:
                        DSO.objects.update(username=username,password=password ,dso_id =dso_id  ,dso_name =dso_name  ,dso_desc =dso_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,ssu_id=ssu_id)
                        return Response({
                            'result': 'DSO created Successfully'
                        })
                else:
                    return Response({'result': 'Invalid SSU'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })

#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      THO       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostTHO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_THO = THO.objects.all().values()
        return Response(all_THO)
    
    def post(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        tho_id                      = data.get('tho_id') 
        tho_name                    = data.get('tho_name') 
        tho_desc                    = data.get('tho_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        dso_id                      = data.get('dso_id')
    
        if password == confirm_password:

            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                if DSO.objects.filter(id=dso_id).exists():
                    if THO.objects.filter(username=username).exists():
                        return Response({
                                'result': 'username already exists'
                            })
                    else:
                        THO.objects.create(username=username,password=password ,tho_id =tho_id  ,tho_name =tho_name  ,tho_desc =tho_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,dso_id=dso_id)
                        return Response({
                            'result': 'DSO created Successfully'
                        })
                else:
                    return Response({'result': 'Invalid DSO'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })


class GetPutPatchTHO(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
       
        try:
            cc = THO.objects.get(id=pk)
        except THO.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = THOSerializer(cc)
            return Response(serializer.data)
 

    def patch(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        tho_id                      = data.get('tho_id') 
        tho_name                    = data.get('tho_name') 
        tho_desc                    = data.get('tho_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        dso_id                      = data.get('dso_id')

        if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
            # lab_name  = Testing_Lab_Facility.objects.get(testing_lab_facility_name)
            if DSO.objects.filter(id=ssu_id).exists():
                if THO.objects.filter(id=pk).exists():
                    THO.objects.filter(id = pk).update(tho_id =tho_id  ,tho_name =tho_name  ,tho_desc =tho_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,dso_id=dso_id)
                    return Response({
                        'result': 'Updated Successfully'
                    })
                else:
                    return Response({'result': 'Invalid THO ID'})
            else:
                    return Response({'result': 'Invalid DSO ID'})
        else:
            return Response({'result': 'Invalid Testing Lab'})


    def put(self, request):
        
        data = request.data
        print(data)

        username                    = data.get('username')
        password                    = data.get('password')
        confirm_password            = data.get('confirm_password')

        tho_id                      = data.get('tho_id') 
        tho_name                    = data.get('tho_name') 
        tho_desc                    = data.get('tho_desc') 
        address_line_1              = data.get('address_line_1') 
        address_line_2              = data.get('address_line_2') 
        district_name               = data.get('district_name') 
        city_name                   = data.get('city_name') 
        ward_name                   = data.get('ward_name') 
        taluk_name                  = data.get('taluk_name') 
        panchayat_name              = data.get('panchayat_name') 
        village_name                = data.get('village_name') 
        pincode                     = data.get('pincode') 
        create_timestamp            = data.get('create_timestamp') 
        last_update_timestamp       = data.get('last_update_timestamp') 
        user_role_id                = data.get('user_role_id') 
        testing_lab_facility_id     = data.get('testing_lab_facility_id')
        dso_id                      = data.get('dso_id')
    
        if password == confirm_password:

            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                if DSO.objects.filter(id=dso_id).exists():
                    if THO.objects.filter(username=username).exists():
                        return Response({
                                'result': 'username already exists'
                            })
                    else:
                        THO.objects.update(username=username,password=password ,tho_id =tho_id  ,tho_name =tho_name  ,tho_desc =tho_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,dso_id=dso_id)
                        return Response({
                            'result': 'DSO Updated Successfully'
                        })
                else:
                    return Response({'result': 'Invalid DSO'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })


#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      Swab_Collection_Centre       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostSwab_Collection_Centre(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_Swab_Collection_Centre = Swab_Collection_Centre.objects.all().values()
        count=Swab_Collection_Centre.objects.all().count()
        print(count)
        return Response(all_Swab_Collection_Centre)
    
    def post(self, request):
        
        data = request.data
        print(data)

        username                        = data.get('username')
        password                        = data.get('password')
        confirm_password                = data.get('confirm_password')

        swab_collection_centre_id       = data.get('tho_id') 
        swab_collection_centre_name     = data.get('tho_name') 
        swab_collection_centre_desc     = data.get('tho_desc') 
        address_line_1                  = data.get('address_line_1') 
        address_line_2                  = data.get('address_line_2') 
        district_name                   = data.get('district_name') 
        city_name                       = data.get('city_name') 
        ward_name                       = data.get('ward_name') 
        taluk_name                      = data.get('taluk_name') 
        panchayat_name                  = data.get('panchayat_name') 
        village_name                    = data.get('village_name') 
        pincode                         = data.get('pincode') 
        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        user_role_id                    = data.get('user_role_id') 
        testing_lab_facility_id         = data.get('testing_lab_facility_id')
        tho_id                          = data.get('tho_id')
    
        if password == confirm_password:
            
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                if THO.objects.filter(id=tho_id).exists():
                    if Swab_Collection_Centre.objects.filter(username=username).exists():
                        return Response({
                                'result': 'username already exists'
                            })
                    else:
                        Swab_Collection_Centre.objects.create(username=username,password=password ,swab_collection_centre_id =swab_collection_centre_id  ,swab_collection_centre_name =swab_collection_centre_name  ,swab_collection_centre_desc =swab_collection_centre_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,tho_id=tho_id)
                        return Response({
                            'result': 'Swab_Collection_Centre created Successfully'
                        })
                else:
                    return Response({'result': 'Invalid THO'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })


class GetPutPatchSwab_Collection_Centre(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk,):
       
        try:
            cc = Swab_Collection_Centre.objects.get(id=pk)
        except Swab_Collection_Centre.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = Swab_Collection_CentreSerializer(cc)
            return Response(serializer.data)
 

    def put(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        username                        = data.get('username')
        password                        = data.get('password')
        confirm_password                = data.get('confirm_password')

        swab_collection_centre_id       = data.get('tho_id') 
        swab_collection_centre_name     = data.get('tho_name') 
        swab_collection_centre_desc     = data.get('tho_desc') 
        address_line_1                  = data.get('address_line_1') 
        address_line_2                  = data.get('address_line_2') 
        district_name                   = data.get('district_name') 
        city_name                       = data.get('city_name') 
        ward_name                       = data.get('ward_name') 
        taluk_name                      = data.get('taluk_name') 
        panchayat_name                  = data.get('panchayat_name') 
        village_name                    = data.get('village_name') 
        pincode                         = data.get('pincode') 
        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        user_role_id                    = data.get('user_role_id') 
        testing_lab_facility_id         = data.get('testing_lab_facility_id')
        tho_id                          = data.get('tho_id')

        last_update_timestamp= datetime.now()
        print(last_update_timestamp)

        if password == confirm_password:
            if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
                # lab_name  = Testing_Lab_Facility.objects.get(testing_lab_facility_name)
                if THO.objects.filter(id=tho_id).exists():
                    if Swab_Collection_Centre.objects.filter(id=pk).exists():
                        Swab_Collection_Centre.objects.filter(id = pk).update(username=username,password=password,swab_collection_centre_id =swab_collection_centre_id  ,swab_collection_centre_name =swab_collection_centre_name  ,swab_collection_centre_desc =swab_collection_centre_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,tho_id=tho_id)
                        return Response({
                            'result': 'Updated Successfully'
                        })
                    else:
                        return Response({'result': 'Invalid Swab_Collection_Centre ID'})
                else:
                        return Response({'result': 'Invalid THO ID'})
            else:
                return Response({'result': 'Invalid Testing Lab'})
        else:
            return Response({
                    'result': 'password not matching'
                })


    def patch(self, request,pk):
        data            = request.data
        
        data = request.data
        print(data)

        swab_collection_centre_id       = data.get('tho_id') 
        swab_collection_centre_name     = data.get('tho_name') 
        swab_collection_centre_desc     = data.get('tho_desc') 
        address_line_1                  = data.get('address_line_1') 
        address_line_2                  = data.get('address_line_2') 
        district_name                   = data.get('district_name') 
        city_name                       = data.get('city_name') 
        ward_name                       = data.get('ward_name') 
        taluk_name                      = data.get('taluk_name') 
        panchayat_name                  = data.get('panchayat_name') 
        village_name                    = data.get('village_name') 
        pincode                         = data.get('pincode') 
        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        user_role_id                    = data.get('user_role_id') 
        testing_lab_facility_id         = data.get('testing_lab_facility_id')
        tho_id                          = data.get('tho_id')

        last_update_timestamp= datetime.now()
        print(last_update_timestamp)

        if Testing_Lab_Facility.objects.filter(id=testing_lab_facility_id).exists():
            # lab_name  = Testing_Lab_Facility.objects.get(testing_lab_facility_name)
            if THO.objects.filter(id=tho_id).exists():
                if Swab_Collection_Centre.objects.filter(id=pk).exists():
                    Swab_Collection_Centre.objects.filter(id = pk).update(swab_collection_centre_id =swab_collection_centre_id  ,swab_collection_centre_name =swab_collection_centre_name  ,swab_collection_centre_desc =swab_collection_centre_desc ,address_line_1=address_line_1 ,address_line_2=address_line_2 ,district_name=district_name ,city_name =city_name ,ward_name =ward_name,taluk_name=taluk_name,panchayat_name=panchayat_name,village_name=village_name ,pincode=pincode,create_timestamp =create_timestamp      ,last_update_timestamp=last_update_timestamp  ,user_role_id =user_role_id ,testing_lab_facility_id=testing_lab_facility_id,tho_id=tho_id)
                    return Response({
                        'result': 'Updated Successfully'
                    })
                else:
                    return Response({'result': 'Invalid Swab_Collection_Centre ID'})
            else:
                    return Response({'result': 'Invalid THO ID'})
        else:
            return Response({'result': 'Invalid Testing Lab'})



#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      Testing_Kit_Barcode       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostTesting_Kit_Barcode(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_Swab_Testing_Kit_Barcode = Testing_Kit_Barcode.objects.all().values()
        count=Testing_Kit_Barcode.objects.all().count()
        print(count)
        return Response(all_Swab_Testing_Kit_Barcode)
    
    def post(self, request):

        data = request.data
        print(data)

        testing_kit_barcode_id          = data.get('testing_kit_barcode_id')
        testing_kit_barcode_name        = data.get('testing_kit_barcode_name')
        testing_kit_barcode_value       = data.get('testing_kit_barcode_value')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp= datetime.now()
        print(last_update_timestamp) 


        if Testing_Kit_Barcode.objects.filter(testing_kit_barcode_id=testing_kit_barcode_id).exists():
            return Response({'result': 'testing_kit_barcode_id Already present'})
        else:
            Testing_Kit_Barcode.objects.create(testing_kit_barcode_id=testing_kit_barcode_id, testing_kit_barcode_name=testing_kit_barcode_name, testing_kit_barcode_value=testing_kit_barcode_value, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': 'testing_kit_barcode_id Created Successfully'})

        
class GetPutPatchTesting_Kit_Barcode(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk): 
        try:
            cc = Testing_Kit_Barcode.objects.get(id=pk)
        except Testing_Kit_Barcode.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = Testing_Kit_BarcodeSerializer(cc)
            return Response(serializer.data)
 

    def put(self, request,pk):
        data = request.data
        print(data)

        testing_kit_barcode_id          = data.get('testing_kit_barcode_id')
        testing_kit_barcode_name        = data.get('testing_kit_barcode_name')
        testing_kit_barcode_value       = data.get('testing_kit_barcode_value')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp = datetime.now()
        print(last_update_timestamp) 



        if Testing_Kit_Barcode.objects.filter(id=pk).exists():
            Testing_Kit_Barcode.objects.update(testing_kit_barcode_id=testing_kit_barcode_id, testing_kit_barcode_name=testing_kit_barcode_name, testing_kit_barcode_value=testing_kit_barcode_value, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': ' FULL testing_kit_barcode_id Updated Successfully'})
        else:
            return Response({'result': 'testing_kit_barcode Not present please check!!!!!'})
            


    def patch(self, request,pk):
        data = request.data
        print(data)

        testing_kit_barcode_id          = data.get('testing_kit_barcode_id')
        testing_kit_barcode_name        = data.get('testing_kit_barcode_name')
        testing_kit_barcode_value       = data.get('testing_kit_barcode_value')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp = datetime.now()
        print(last_update_timestamp) 



        if Testing_Kit_Barcode.objects.filter(id=pk).exists():
            Testing_Kit_Barcode.objects.update(testing_kit_barcode_id=testing_kit_barcode_id, testing_kit_barcode_name=testing_kit_barcode_name, testing_kit_barcode_value=testing_kit_barcode_value, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': ' testing_kit_barcode_id Updated Successfully'})
        else:
            return Response({'result': 'testing_kit_barcode Not present please check!!!!!'})




#?-----------------------------------------------------------------------------------------------------------------------------------------------
#!------------------------      Package_Sampling       -------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------------


class GetPostPackage_Sampling(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get (self,request):
        all_Package_Sampling = Package_Sampling.objects.all().values()
        count=Package_Sampling.objects.all().count()
        print(count)
        return Response(all_Package_Sampling)
    
    def post(self, request):

        data = request.data
        print(data)

        package_sampling_id             = data.get('package_sampling_id')
        package_sampling_name           = data.get('package_sampling_name')
        package_sampling_barcode        = data.get('package_sampling_barcode')
        testing_kit_barcodes_list       = data.get('testing_kit_barcodes_list')
        dispatch_status                 = data.get('dispatch_status')
        swab_collection_centre_id          = data.get('swab_collection_centre_id')
        tho_id                             = data.get('tho_id')
        dso_id                             = data.get('dso_id')
        ssu_id                             = data.get('ssu_id')
        testing_lab_facility_id            = data.get('testing_lab_facility_id')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp= datetime.now()
        print(last_update_timestamp) 


        if Package_Sampling.objects.filter(package_sampling_id=package_sampling_id).exists():
            return Response({'result': 'package_sampling_id Already present'})
        else:
            Package_Sampling.objects.create(package_sampling_id=package_sampling_id,  package_sampling_name=package_sampling_name,  package_sampling_barcode=package_sampling_barcode,  testing_kit_barcodes_list=testing_kit_barcodes_list,  dispatch_status=dispatch_status, swab_collection_centre_id=swab_collection_centre_id, tho_id=tho_id, dso_id=dso_id, ssu_id=ssu_id, testing_lab_facility_id=testing_lab_facility_id, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': 'Package_Sampling Created Successfully'})

        
class GetPutPatchPackage_Sampling(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,pk): 
        try:
            cc = Package_Sampling.objects.get(id=pk)
        except Package_Sampling.DoesNotExist:
            return Response({'result': 'Invalid ID '})
        if request.method == 'GET':
            serializer = Package_SamplingSerializer(cc)
            return Response(serializer.data)
        

        
 

    def put(self, request,pk):
        data = request.data
        print(data)

        package_sampling_id             = data.get('package_sampling_id')
        package_sampling_name           = data.get('package_sampling_name')
        package_sampling_barcode        = data.get('package_sampling_barcode')
        testing_kit_barcodes_list       = data.get('testing_kit_barcodes_list')
        dispatch_status                 = data.get('dispatch_status')
        swab_collection_centre          = data.get('swab_collection_centre')
        tho                             = data.get('tho')
        dso                             = data.get('dso')
        ssu                             = data.get('ssu')
        testing_lab_facility            = data.get('testing_lab_facility')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp= datetime.now()
        print(last_update_timestamp) 



        if Package_Sampling.objects.filter(id=pk).exists():
            Package_Sampling.objects.update(package_sampling_id=package_sampling_id,  package_sampling_name=package_sampling_name3,  package_sampling_barcode=package_sampling_barcode,  testing_kit_barcodes_list=testing_kit_barcodes_list,  dispatch_status=dispatch_status, swab_collection_centre=swab_collection_centre, tho=tho, dso=dso, ssu=ssu, testing_lab_facility=testing_lab_facility, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': ' FULL Package_Sampling Updated Successfully'})
        else:
            return Response({'result': 'Package_Sampling Not present please check!!!!!'})
            


    def patch(self, request,pk):
        data = request.data
        print(data)

        package_sampling_id             = data.get('package_sampling_id')
        package_sampling_name           = data.get('package_sampling_name')
        package_sampling_barcode        = data.get('package_sampling_barcode')
        testing_kit_barcodes_list       = data.get('testing_kit_barcodes_list')
        dispatch_status                 = data.get('dispatch_status')
        swab_collection_centre          = data.get('swab_collection_centre')
        tho                             = data.get('tho')
        dso                             = data.get('dso')
        ssu                             = data.get('ssu')
        testing_lab_facility            = data.get('testing_lab_facility')

        create_timestamp                = data.get('create_timestamp') 
        last_update_timestamp           = data.get('last_update_timestamp') 
        
        last_update_timestamp= datetime.now()
        print(last_update_timestamp) 



        if Package_Sampling.objects.filter(id=pk).exists():
            Package_Sampling.objects.update(package_sampling_id=package_sampling_id,  package_sampling_name=package_sampling_name3,  package_sampling_barcode=package_sampling_barcode,  testing_kit_barcodes_list=testing_kit_barcodes_list,  dispatch_status=dispatch_status, swab_collection_centre=swab_collection_centre, tho=tho, dso=dso, ssu=ssu, testing_lab_facility=testing_lab_facility, create_timestamp=create_timestamp, last_update_timestamp=last_update_timestamp)
            return Response({'result': ' FULL Package_Sampling Updated Successfully'})
        else:
            return Response({'result': 'Package_Sampling Not present please check!!!!!'})





# 1) Ready For Dispatch
# 2) Lab Allocated
# 3) Notified to DSO
# 4) Notfied to SSU
# 5) Package arrived to lab
# 6) Package Created
# 7) Packge Received


# 11)  Dispatch --> Button
# 12)  Dispatched to Lab
# 13)  Dispatched to THO
# 14)  Dispatched to DSO
# 15)  (Display Lab Name)  -- >  {{data.lab_name}}
# 16)
# 17)


# 31) Collection Pending
# 32) Samples Collected






























class AutomatePatientCreate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        iteration_count = data.get('count')
        added_user = data.get('added_user_id')
        status = data.get('status')


        typeD = ''
        list_data = []
        if status == 1:
            typeD = 'Symptomatic'
            list_data = ['Breathlessness']

        else:
            typeD = 'Asymptomatic'
            list_data = []

        for i in range(1,int(iteration_count)+1):

            pt_data = Patient.objects.create(reason_for_testing= 'on-demand', reason_for_testing_description= 'on-demand', patient_type_id= 1,
                                            added_by_id= added_user,
                                            patient_name= 'Test'+str(i), 
                                            mobile_number= str(900008)+str(i).zfill(4), 
                                            mobile_number_belongs_to= 'Family',
                                            gender= 'male', 
                                            age= '25',
                                            id_proof_type= 'Aadhaar', 
                                            aadhar_number= random.randint(100000000000, 999999999999), 
                                            # ration_card_number= '', 
                                            vaccine_status= 'Yes', 
                                            # vaccine_mobile_registered= vaccine_mobile_registered,
                                            specimen_type_id= 3, 
                                            co_morbidity= 'no',
                                            co_morbidity_type= [],
                                            patient_status = typeD,
                                            # specimen_collection_date= specimen_collection_date, 
                                            #testing_kit_barcode_id= testing_type_ref_data.id,
                                            # symptoms_list= symptoms, 
                                            symptoms_list= list_data, 
                                            test_type_id= 2, 
                                            srf_id= random.randint(100000000, 999999999), #swab_collection_status= swab_collection_status_ref_data.id,
                                            barcode= 'KA-'+str(random.randint(100000000, 999999999)),
                                        )
            Patient_Address.objects.create(patient_id= pt_data.id, 
                                                state_name= 'Karnataka', 
                                                district_name= 1504, #district_type= district_type, 
                                                # city_name= city_name,
                                                # zone_type= zone_name,
                                                # ward_name= ward_name,
                                                taluk_name= 1504007, 
                                                panchayat_name= 1504007023, 
                                                village_name= 1504007023003, 
                                                resident_type= 'Local', 
                                                ward_type= 'rural', 
                                                flat_door_no= '111', 
                                                main_road_no= 'Main Road',
                                                pincode= 541263,
                                                locality= 'locality',
                                                landmark= 'landmark')

        return Response({'result':'Created '+str(iteration_count)+' Patient Details'})




    



class CompleteCreatedSamples(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data

        user_id = data.get('user_id')
        status = data.get('symp_type')
        count = data.get('count')

        typeD = ''
        if status == 1:
            typeD = 'Symptomatic'

        else:
            typeD = 'Asymptomatic'


        filter_data = Patient.objects.filter(Q(added_by_id= user_id) & Q(patient_status= typeD) & Q(swab_collection_status= 31)).values()
        cnt = 0
        for i in filter_data:

            if cnt < int(count):

                Patient.objects.filter(id= i['id']).update(swab_collection_status= 32)

                cnt += 1

        return Response({'result': 'Updated Sucessfully'})






class DeleteMasterPHC(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        Master_PHC.objects.filter(district_code= 1525).delete()

        return Response('Deleted')



class GetPatientDetails(APIView):

    """
    In this class details from Patient, PatientAddress, 
    PatientTesting models
    are combined and returned.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dat_from = request.data.get('fromDate')
        dat_to = request.data.get('toDate')
        try:
            #creating connection
            rst_patient = Patient.objects.filter(create_timestamp__gte=dat_from, create_timestamp__lte=dat_to).values()
            
            for data in rst_patient:
                rst_outside_add = list(Outside_Patient_Address.objects.annotate(address_create_timestamp= F('create_timestamp')).filter(patient_id= data['id']).values())
                rst_add = list(Patient_Address.objects.annotate(address_create_timestamp= F('create_timestamp')).filter(patient_id= data['id']).values())
                patient_testing_details = list(Patient_Testing.objects.annotate(testing_create_timestamp= F('create_timestamp')).filter(patient_id= data['id']).values())

                if rst_outside_add:
                    data.update(rst_outside_add[0])

                if rst_add:
                    data.update(rst_add[0])

                if patient_testing_details:
                    data.update(patient_testing_details[0])
            return Response({'status':1, 'message': 'success', 'result': rst_patient})
        except Exception as e:
            return Response({'status':0, 'message': str(e)})



    


    







