from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import signupSerializer,medicineSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from catalog.models import medicine


from rest_framework.response import Response
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny,])
def register(request):
    obj=signupSerializer(data=request.data)
    if obj.is_valid():
        obj.save()
        return Response({'message':'Successfully Registerd'},status=HTTP_200_OK)
    return Response(obj.errors,status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny,])
def login(request):
    name = request.data.get('username')
    password= request.data.get('password')
    if name is None or password is None:
        return Response({'message':'Enter correct Username and Password'},status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=name, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated,])
def create(request):
    serializer = medicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(serializer.data,HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["PUT"])
@permission_classes([IsAuthenticated,])
def edit(request):
    up= medicine.objects.get(pk=id)
    update=medicineSerializer(up,data=request.data)
    if update.is_valid:
        update.save()
        return Response(update.data)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,])
def delete(request):
    de = medicine.objects.get(pk=id)
    de.delete()
    return Response(status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated,])
def logout(request):
    request.user.auth_token.delete()
    return Response('User LOgged out successfully')













# {"token":"e6000fff443d8e4d15551ae53b7b6c0adbe6dd54"}