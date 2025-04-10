import logging
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import User
from student_performance.models import TeacherLevelClass
from school.models import School, Campus


logger = logging.getLogger(__name__)

class IsRole(BasePermission):
    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role(self.role)

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role('Teacher')

class IsParent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role('Parent')

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role('Student')

class IsHeadmaster(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role('Headmaster')

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_role('Admin')

class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            (request.user.has_role('Teacher') or request.user.has_role('Admin'))
        )

class IsAssignedTeacher(BasePermission):
    """
    Allows access only to teachers assigned to a class.
    Ensures tenancy by checking if the teacher belongs to the same school and campus.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Retrieve class_id from request data
        class_id = request.data.get('class_id')
        if not class_id:
            return False

        # Get user school and campus
        user = request.user
        user_school_id = user.school_id
        user_campus_id = user.campus_id

        # Check if teacher is assigned to the class AND belongs to the same school/campus
        return TeacherLevelClass.objects.filter(
            teacher=user,
            class_id=class_id,
            class_id__school_id=user_school_id,
            class_id__campus_id=user_campus_id
        ).exists()

class IsAdminOrAssignedTeacher(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.has_role('Admin'):
            return True
        return IsAssignedTeacher().has_permission(request, view)

class IsRegisteredInSchoolOrCampus(BasePermission):
    """
    Restricts actions to users registered in the same school and/or campus as the resource.
    Can be combined with role-based permissions.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True

        # Allow GET requests (read-only) without strict tenancy check
        if request.method in SAFE_METHODS:
            return True

        # For write actions (POST, PUT, PATCH, DELETE), enforce tenancy
        token = request.auth
        user_school_id = token.get('school_id') if token else request.user.school_id
        user_campus_id = token.get('campus_id') if token else request.user.campus_id

        if not user_school_id and not user_campus_id:
            logger.warning(f"User {request.user} has no school/campus")
            return False

        # Handle POST (create) - check request.data
        if request.method == 'POST':
            data = request.data
            is_many = isinstance(data, list)
            items = data if is_many else [data]

            for item in items:
                school_id = item.get('school')
                campus_id = item.get('campus')

                if school_id and str(user_school_id) != str(school_id):
                    return False

                if campus_id and str(user_campus_id) != str(campus_id):
                    campus = Campus.objects.filter(id=campus_id).first()
                    if not campus or user_school_id != campus.school_id:
                        return False
            return True

        # For other methods, rely on has_object_permission
        return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True

        # Allow GET requests (read-only)
        if request.method in SAFE_METHODS:
            return True

        # For write actions, check school/campus match
        user = request.user
        if not user.school and not user.campus:
            logger.warning(f"User {user} has no school/campus, denied {request.method} {request.path}")
            return False

        token = request.auth
        user_school_id = token.get('school_id') if token else request.user.school_id
        user_campus_id = token.get('campus_id') if token else request.user.campus_id

        if not user_school_id and not user_campus_id:
            return False

        if obj.school and user_school_id != obj.school_id:
            return False
        if obj.campus and user_campus_id != obj.campus_id:
            if user_school_id != obj.campus.school_id:
                return False
        return True

class IsTeacherOrAdminInSchoolOrCampus(IsTeacherOrAdmin, IsRegisteredInSchoolOrCampus):
    """
    Combines role-based (Teacher or Admin) and tenancy-based permissions.
    """
    def has_permission(self, request, view):
        return (
            IsTeacherOrAdmin.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_permission(self, request, view)
        )

    def has_object_permission(self, request, view, obj):
        return (
            IsTeacherOrAdmin.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_object_permission(self, request, view, obj)
        )
    

class IsHeadmasterInSchoolOrCampus(IsHeadmaster, IsRegisteredInSchoolOrCampus):
    def has_permission(self, request, view):
        return (
            IsHeadmaster.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_permission(self, request, view)
        )

    def has_object_permission(self, request, view, obj):
        return (
            IsHeadmaster.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_object_permission(self, request, view, obj)
        )
    

class IsTeacherInSchoolOrCampus(IsTeacher, IsRegisteredInSchoolOrCampus):
    def has_permission(self, request, view):
        return (
            IsTeacher.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_permission(self, request, view)
        )

    def has_object_permission(self, request, view, obj):
        return (
            IsTeacher.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_object_permission(self, request, view, obj)
        )
    

class IsParentInSchoolOrCampus(IsParent, IsRegisteredInSchoolOrCampus):
    def has_permission(self, request, view):
        return (
            IsParent.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_permission(self, request, view)
        )

    def has_object_permission(self, request, view, obj):
        return (
            IsParent.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_object_permission(self, request, view, obj)
        )
    

class IsStudentInSchoolOrCampus(IsStudent, IsRegisteredInSchoolOrCampus):
    def has_permission(self, request, view):
        return (
            IsStudent.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_permission(self, request, view)
        )

    def has_object_permission(self, request, view, obj):
        return (
            IsStudent.has_permission(self, request, view) and
            IsRegisteredInSchoolOrCampus.has_object_permission(self, request, view, obj)
        )