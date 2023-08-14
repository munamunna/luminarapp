import random
from twilio.rest import Client
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Batch,WaitingList,AddStudent,Student
from .serializer import BatchSerializer,StudentSerializer,WaitingListSerializer,AddStudentSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin




class BatchView(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()

    # ... (other methods)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)

            response_data = {
                'status': 'ok',
                'data': {
                    'count': queryset.count(),
                    'results': serializer.data
                }
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # ... (other methods)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response_data = {
                'status': 'ok',
                'data': {
                    'count': Batch.objects.count(),
                    'results': BatchSerializer(Batch.objects.all(), many=True).data
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    # ... (other methods)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)

            response_data = {
                'status': 'ok',
                'data': serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    # ... (other methods)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                'status': 'ok',
                'data': {
                    'message': 'Batch updated successfully',
                    'batch': serializer.data
                }
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    # ... (other methods)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

            response_data = {
                'status': 'ok',
                'data': {
                    'message': 'Batch deleted successfully'
                }
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            response_data = {
                'status': 'err',
                'message': str(e)
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







# class AddStudentToBatch(APIView):
#     def post(self, request, batch_id):
#         try:
#             batch = Batch.objects.get(pk=batch_id)
#         except Batch.DoesNotExist:
#             return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = AddStudentSerializer(data=request.data)
        
#         if serializer.is_valid():
#             student = serializer.save(batch=batch)
#             return Response({'message': 'Student added to batch successfully', 'student_id': student.id}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class StudentRegistrationView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = StudentSerializer(data=data)

#         if serializer.is_valid():
#             student = serializer.save()

#             # Add student to waiting list with name and ID
#             waiting_list_entry = WaitingList(
#                 student=student,
#                 username=student.username,
#                 phone=student.phone,
#                 selected_course=student.selected_course
                
#             )
#             waiting_list_entry.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentRegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            student = serializer.save()

            # Add student to waiting list with name and ID
            waiting_list_entry = WaitingList(
                student=student,
                username=student.username,
                phone=student.phone,
                selected_course=student.selected_course
            )
            waiting_list_entry.save()
            total_registered_users = Student.objects.count()
            response_data = {
                "status": "ok",
                "data": [
                    {
                        "id": student.id,
                        "username": student.username,
                        "password":student.password,
                        "gender":student.gender,
                        "dob":student.dob,
                        "phone":student.phone,
                        "parent_no":student.parent_no,
                        "full_name":student.full_name,
                        "selected_course":student.selected_course,
                    },
                ],
                "totalResults": total_registered_users
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors, "totalResults": 0}, status=status.HTTP_400_BAD_REQUEST)




class WaitingListView(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = WaitingListSerializer
    queryset = WaitingList.objects.all()


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddStudentToBatch(APIView):
    def post(self, request, batch_id):
        try:
            batch = Batch.objects.get(pk=batch_id)
        except Batch.DoesNotExist:
            return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AddStudentSerializer(data=request.data)
        
        if serializer.is_valid():
            student = serializer.save(batch=batch)
            
            # Remove student from waiting list
            try:
                waiting_list_entry = WaitingList.objects.get(student_id=student.id)
                waiting_list_entry.delete()
            except WaitingList.DoesNotExist:
                pass  # The student was not found in the waiting list
            
            return Response({'message': 'Student added to batch successfully', 'student_id': student.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddedView(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = AddStudentSerializer
    queryset = AddStudent.objects.all()