import csv
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import File
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, FileSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
from Language_detection.classify import predict_lang
from django.http import FileResponse
#class Languagecheck(APIView)


class FileView(APIView):
    # queryset = File.objects.all()
    serializer_class = FileSerializer
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)


    def put(self, request, format=None):
        file_obj = request.data['file']
        for line in file_obj.readlines():
            print(line)
        return Response(status=204)


    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            uploaded_file = self.request.FILES['file']
            # for line in uploaded_file:
            #     print(line.decode().strip())

            # print(type(self.request.FILES['file']))

            # Create a Python file object using open() and the with statement
            i = 0
            j=0
            with open('result.csv', "w", encoding="utf-8", newline='') as result_file:
                # writer = csv.writer(result_file, dialect='excel', delimiter=',')
                for line in uploaded_file:
                    result_file.write(predict_lang(line.decode("utf-8").strip()))

                    result_file.write("\n")
                    i += 1
                print(i)
            # with open('result.csv', "r", encoding="utf-8", newline='') as result_file:
            #     # writer = csv.writer(result_file, dialect='excel', delimiter=',')
            #     for line in result_file:
            #         print(line)
            #         j+= 1
            #         if j==10 : break
            print(result_file.closed)
            response = FileResponse(open('result.csv', 'rb'))
            # response['Content_type'] = 'text/csv'
            # response['Content-Disposition'] = 'attachment; filename="result.csv"'
            print(result_file.closed)
            return response
            # return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Languagecheck(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer