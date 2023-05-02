from django.shortcuts import render
from crm.models import Employee
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        exclude=("id",)


class EmployeesView(ViewSet):
    # localhost:8000/employee/
    # method=get
    def list(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
   
    # localhost:8000/api/employee/
    # method=post
    def create(self,request,*args,**kwargs):
        return Response(data={"result":"create a employee record"})
    
   
    # localhost:8000/api/employee/1/
    # method=get
    def retrieve(self,request,*args,**kwargs):
        return Response(data={"result":"fetching a  specific employee record"})
    

    
    # localhost:8000/api/employee/3/
    # method=put
    def update(self,request,*args,**kwargs):
        return Response(data={"result":"update a specific  employee record"})
    

   
    # localhost:8000/api/employee/2/
    # method=delete
    def destroy(self,request,*args,**kwargs):
        return Response(data={"result":"remove a employee record"})
