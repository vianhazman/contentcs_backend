from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from objects.serializers import CourseSerializer, SectionSerializer
from .models import Course, Section


class ListCourse(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Course.objects.all()
        serializer_class = CourseSerializer(queryset, many=True)
        return Response({"courses": serializer_class.data})

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListSection(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        course_id = self.request.query_params.get('courseId')
        queryset = Section.objects.filter(course_object__id = course_id) \
            if course_id else Section.objects.all()
        serializer_class = SectionSerializer(queryset, many=True)
        return Response({"sections": serializer_class.data})

    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_delete_update_section(APIView):
    serializer_class = SectionSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            section = Section.objects.get(id=pk)
        except Section.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return section

    # Get a section
    def get(self, request, pk):

        section = self.get_queryset(pk)
        serializer = SectionSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a section
    def put(self, request, pk):

        section = self.get_queryset(pk)

        # if (request.user == section.creator):  # If creator is who makes request
        if True:
            serializer = SectionSerializer(section, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a section
    def delete(self, request, pk):

        section = self.get_queryset(pk)

        # if (request.user == section.creator):  # If creator is who makes request
        if True:
            section.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)

class get_delete_update_course(APIView):
    serializer_class = CourseSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return course

    # Get a course
    def get(self, request, pk):

        course = self.get_queryset(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a course
    def put(self, request, pk):

        course = self.get_queryset(pk)

        # if (request.user == section.creator):  # If creator is who makes request
        if True:
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a course
    def delete(self, request, pk):

        course = self.get_queryset(pk)

        # if (request.user == section.creator):  # If creator is who makes request
        if True:
            course.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     content = {
        #         'status': 'UNAUTHORIZED'
        #     }
        #     return Response(content, status=status.HTTP_401_UNAUTHORIZED)


