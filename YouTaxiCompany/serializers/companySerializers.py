from rest_framework import serializers
from ..models import Company, Workers



class CreateWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ['phoneNo', 'firstName', 'lastName', 'email', 'status', 'isDeleted']


class CreateCompanySerializer(serializers.ModelSerializer):
    Worker = CreateWorkerSerializer(many=True)

    class Meta:
        model = Company
        fields = ['name', 'address', 'city', 'postalCode', 'nif', 'administrators', 'addDate',\
            'removeDate', 'status', 'bankCardDetails', 'bankAccountDetails', 'Worker']
    

    def create(self, validated_data):
        worker_list = validated_data.pop('Worker')
        company_instance = Company.objects.create(**validated_data)
        for i in worker_list:
            Workers.objects.create(**i)
        return company_instance
    


class GetAllCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'city', 'postalCode', 'status']


class GetCompanyByIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'city', 'postalCode', 'nif', 'administrators', \
            'bankCardDetails', 'bankAccountDetails', 'addDate', 'removeDate', 'status']


class UpdateCompanyByIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['address', 'city', 'postalCode', 'nif', 'administrators', \
            'bankCardDetails', 'bankAccountDetails', 'addDate', 'removeDate', 'status']

