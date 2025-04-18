from django.urls import path

from . import views

urlpatterns = [
    # API endpoints for Class
    path('create-class/', views.create_class, name='create_class'),
    path('get-class/<uuid:class_id>/', views.retrieve_class, name='retrieve_class'),
    path('get-all-classes/<uuid:level_id>/', views.get_all_classes, name='retrieve_class'),
    path('update-class/<uuid:class_id>/', views.update_class, name='update_class'),
    path('delete-class/<uuid:class_id>/', views.delete_class, name='delete_class'),

    # API endpoints for Level
    path('levels/', views.LevelCRUDView.as_view(), name='level-list-create'),
    path('levels/<uuid:pk>/', views.LevelCRUDView.as_view(), name='level-detail'),

    # API endpoints for Terms
    path('terms/', views.TermsCRUDView.as_view(), name='term-list-create'),
    path('terms/<uuid:pk>/', views.TermsCRUDView.as_view(), name='term-detail'),

    # API endpoints for Subject
    path('subjects/', views.SubjectCRUDView.as_view(), name='subject-list-create'),
    path('subjects/<uuid:pk>/', views.SubjectCRUDView.as_view(), name='subject-detail'),

    # API endpoints for Class Subjects
    path('class-subjects/<uuid:class_id>/', views.ManageClassSubjectsView.as_view(), name='view_class_subjects'),
    path('class-subjects/', views.ManageClassSubjectsView.as_view(), name='assign_class_subjects'),
    path('class-subjects/<uuid:pk>/', views.ManageClassSubjectsView.as_view(), name='update_delete_class_subject'),

    # API endpoints for Student
    path('get-students/', views.get_students_by_class_id, name='get_students_by_class_id'),
    path('get-student/<int:student_id>/', views.get_student, name='get_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),

    # API endpoints for Student Assessment
    path('create-student-assessments/', views.create_assessments, name='create_assessments'),
    path('get-student-assessments/<int:student_id>/<int:term>/<int:subject_id>/<int:assessment_name>/<int:school_id>/<int:campus_id>/', views.get_student_assessments, name='get_student_assessments'),
    path('get-student-assessment/<int:student_id>/<int:assessment_id>/<int:school_id>/<int:campus_id>/', views.get_student_assessment, name='get_student_assessment'),
    path('student-parent-info/<int:student_id>/', views.StudentParentRelationView.as_view(), name='student-relations'),
    path('update-student-assessments/', views.update_assessments, name='update_assessments'),
    path('delete-student-assessment/<int:student_id>/<int:assessment_id>/<int:school_id>/<int:campus_id>/', views.delete_assessment, name='delete_assessment'),

    # Endpoint for fetching historical and current student assessment data
    path('fetch-historical-assessment-data/', views.fetch_historical_assessment_data, name='fetch_historical_assessment_data'),
    path('get-student-exams-assessments/<int:student_id>/<int:subject_id>/<int:assessment_name>/<int:school_id>/<int:campus_id>/', views.get_student_exams_assessments, name='get_student_exams_assessments'),
    path('student/<int:student_id>/performance/', views.HistoricalPerformanceView.as_view(), name='student-performance'),
    
    # Endpoint for fetching exercise and assignment topic performance and comparing them
    path('exercise-assignment-topic-comparison/<int:student_id>/<int:class_id>/<int:subject_id>/<str:semester>/', views.WeightedTopicPerformanceView.as_view(), name='exercise-assignment-topic-comparison'),

    # Endpoint for fetching topics in either exercise or assignment and comparing performances in each topic
    path('topic-performance-comparison/<int:student_id>/<int:class_id>/<int:subject_id>/<str:semester>/<str:assessment_type>/', views.TopicPerformanceByTypeView.as_view(), name='topic-performance-comparison'),

    # Endpoint for fetching Mid-Term or Final Exam performance data
    path('get-midTerm-final-exam-assessmentData/<int:student_id>/<int:class_id>/<int:subject_id>/<str:assessment_type>/', views.MidTermFinalExamAssessmentComparisonView.as_view(), name='midTerm-final-exam-assessmentData'),
    # path('students-end-of-semester-assessments/<int:class_id>/<str:semester>/', views.ProcessedMarksView.as_view(), name='student-end-of-semester-assessments'),
    path('student-result/<int:class_id>/<int:student_id>/<str:semester>/', views.StudentEndOfSemesterResultView.as_view(), name='student-result'),

    # Fetch End of Semester Results by academic year and semester
    path('end-of-semester-results-by-academic-year/', views.SemesterResultsView.as_view(), name='end_of_semester_results'),

    # Fetch Historical Subject Performances
    path('historical-subject-performances/<int:student_id>/', views.HistoricalSubjectPerformanceView.as_view(), name='historical-subject-performances'),

    # Endpoints for Student Promotions
    path('promote-students/', views.promote_students, name='promote_students'),
    path('get-promoted-existing-repeated-students/<int:class_id>/', views.get_promoted_existing_repeated_students, name='get_promoted_existing_repeated_students'),
    path('merge-promoted-repeated-students/', views.merge_promoted_repeated_students, name='merge_promoted_repeated_students'),
    path('repeat-students/', views.repeat_students, name='repeat_students'),

    # Endpoint for fetching a teacher's class in which he/she teaches a subject
    path('get-teacher-classes/', views.get_teacher_classes, name='get_teacher_classes'),

    # Get Subjects Registered to a Teacher
    path('teacher-subjects-by-teacherId/<int:class_id>/', views.get_teacher_registered_subjects, name='get_teacher_registered_subjects'),

    # Update Subjects Registered to a Teacher
    path('update-teacher-subjects/<int:class_id>/', views.update_teacher_subjects, name='update_teacher_subjects'),

    path('filter-topics/', views.filter_topics, name='filter_topics'),

    # Assigning Students to Parents endpoint
    path('assign-students-to-parents/', views.assign_students_to_parents, name='assign_students_to_parents'),

    # Get Assigned Students to Parents endpoint
    path('get-assigned-students-to-parent/', views.get_students_assigned_to_parent, name='get_students_assigned_to_parent'),

    # Get Children Performance 
    path(
        'get-children-performance/<int:class_id>/<int:student_id>/<str:semester>/<str:assessment_type>/<int:subject_id>/',
        views.ChildrenPerformanceView.as_view(),
        name='children-performance'
    ),

    # New POST endpoint
    path('get-children-performance/', 
        views.ChildrenPerformanceView.as_view(), 
        name='children-performance-post'
    ),

    path('delete_child/<int:student_id>/', views.delete_child, name='delete_child'),
    # Get overall topic performances of all students in a class per subject
    path('topic-performance-per-subject/<int:class_id>/<int:subject_id>/<str:semester>/', views.TopicPerformanceView.as_view(), name='topic-performance'),

    # Endpoint for TimeTable requests
    path('create-timetable/', views.create_timetable, name='create_timetable'),
    path('view-timetable/<int:class_id>/', views.view_timetable, name='view_timetable'),
    path('update-timetable/<int:pk>/', views.update_timetable, name='update-timetable'),
    path('delete-timetable/<int:pk>/', views.delete_timetable, name='delete-timetable'),

    # Endpoints for Assessment CRUD operations
    path('assessment-names/', views.AssessmentNameListCreateView.as_view(), name='assessment-name-list-create'),
    path('assessment-names/<int:pk>/', views.AssessmentNameDetailView.as_view(), name='assessment-name-detail'),
]