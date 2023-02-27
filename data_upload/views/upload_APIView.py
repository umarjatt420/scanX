import os
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.conf import settings
from ..serializers.upload_serializer import UploadSerializer
from django.core.files.storage import FileSystemStorage
from utils.write_text_file import write_text_lines


class UploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
      upload_serializer = UploadSerializer(data=request.data)
      if upload_serializer.is_valid():
          data = upload_serializer.save()
          root_dir = os.path.join(settings.MEDIA_ROOT, f'{data.pk}')
          os.makedirs(root_dir, exist_ok=True)

          # SAVING FILES
          upload_files = request.FILES.getlist('file')
          fs = FileSystemStorage(location=root_dir)
          for file in upload_files:
              fs.save(file.name, file)

          # SAVING OTHER DATA
          exclude_keys = ['csrfmiddlewaretoken', 'upload_file']
          for k in request.POST.keys():
              # GETTING FILE PATH
              if k not in exclude_keys:
                  file_path = os.path.join(root_dir, f'{k}.txt')

                  # GETTING VALUE
                  value = request.POST.getlist(k)

                  # SAVING FILE
                  write_text_lines(file_path, value)
          return Response(upload_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
