from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from objects.serializers.course import CourseSerializer, CourseIndividualSerializer
from objects.serializers.section import SectionSerializer
from objects.serializers.video import VideoSerializer
from objects.models import Course, Section, Video
from objects.util.metadataFetch import MetadataFetch
from userauth.permissions import IsDosen, IsMahasiswa
from rest_framework.permissions import IsAdminUser



class ListCourse(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Course.objects.all()
        serializer_class = CourseSerializer(queryset, many=True,context={'isnotadmin':False})
        return Response({"courses": serializer_class.data})

    def post(self, request):

        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListSection(APIView):

    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]

    def get(self, request, format=None):

        course_id = self.request.query_params.get('courseId')
        queryset = Section.objects.filter(course_object__id = course_id) \
            if course_id else Section.objects.all()
        serializer_class = SectionSerializer(queryset, many=True)
        return Response({"sections": serializer_class.data})

    def post(self, request):
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = SectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_delete_update_section(APIView):
    serializer_class = SectionSerializer

    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]


    def get_queryset(self, pk):
        try:
            section = Section.objects.get(id=pk)
        except Section.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return section

    def get(self, request, pk):

        section = self.get_queryset(pk)
        try:
            serializer = SectionSerializer(section)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    # Update a section
    def put(self, request, pk):

        section = self.get_queryset(pk)

        if True:
            data = request.data.copy()
            data['created_by'] = request.user.id
            serializer = SectionSerializer(section, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a section
    def delete(self, request, pk):

        section = self.get_queryset(pk)
        try:
            if True:
                section.delete()
                content = {
                    'status': 'NO CONTENT'
                }
                return Response(content, status=status.HTTP_204_NO_CONTENT)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class get_delete_update_course(APIView):
    serializer_class = CourseSerializer

    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]


    def get_queryset(self, pk):
        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return course

    def get(self, request, pk):

        course = self.get_queryset(pk)
        try:
            serializer = CourseIndividualSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        course = self.get_queryset(pk)

        if True:
            data = request.data.copy()
            data['created_by'] = request.user.id
            serializer = CourseSerializer(course, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        course = self.get_queryset(pk)
        try:
            if True:
                course.delete()
                content = {
                    'status': 'NO CONTENT'
                }
                return Response(content, status=status.HTTP_204_NO_CONTENT)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class UpdateDuration(APIView):

    def get(self, request, pk):
        try:
            video_obj = MetadataFetch.getVideoDuration(pk)
            content = {
                'status': 'Updated'
            }
            return Response(content, status=status.HTTP_200_OK)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class get_delete_update_video(APIView):
    serializer_class = VideoSerializer

    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]


    def get_queryset(self, pk):
        try:
            video = Video.objects.get(id=pk)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return video

    def get(self, request, pk):
        video = self.get_queryset(pk)
        try:
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        video = self.get_queryset(pk)

        if True:
            if 'video_file' in request.data:
                data = request.data
            else:
                data = request.data.copy()
            data['created_by'] = request.user.id
            serializer = VideoSerializer(video, data=data)
            if serializer.is_valid():
                serializer.save()
                id = serializer.data['id']
                video_obj = MetadataFetch.getVideoDuration(id)
                serializer = VideoSerializer(video_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        section = self.get_queryset(pk)
        try:
            if True:
                section.delete()
                content = {
                    'status': 'NO CONTENT'
                }
                return Response(content, status=status.HTTP_204_NO_CONTENT)
        except:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class ListVideo(APIView):

    permission_classes = [IsMahasiswa | IsDosen | IsAdminUser]

    def get(self, request, format=None):

        section_id = self.request.query_params.get('sectionId')
        queryset = Video.objects.filter(course_object__id = section_id) \
            if section_id else Video.objects.all()
        serializer_class = VideoSerializer(queryset, many=True)
        return Response({"videos": serializer_class.data})

    def post(self, request):
        data = request.data
        data['created_by'] = request.user.id
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['id']
            video_obj = MetadataFetch.getVideoDuration(id)
            serializer = VideoSerializer(video_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


