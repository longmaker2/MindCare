from django.urls import path
from . import views
from .views import cancel_appointment_by_professional, change_language, clear_notificationsss, delete_quiz, edit_quiz, fetch_notifications, fetch_updates, language_settings, professionals_list, quizzes, remove_appointment, translate_page, translate_text, translate_view, update_availability, upload_quiz
from .views import index, appointment_success
from .views import book_appointment
from django.shortcuts import render
from .views import get_available_slots
from django.urls import path
from .views import chat_room, get_messages, send_message
from .views import training_materials, upload_video
from .views import professional_detail
from .views import professional_dashboard
from .views import quizzes_api, quiz_detail 
from .views import appointments_view
from myapp.views import clear_messages

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('training_materials', views.training_materials, name='training_materials'),
    path('home', views.home, name='home.html'),
    path('room', views.room, name='room.html'),
    path('all', views.all_videos, name='all.html'),  # ✅ Corrected function name
    path('mentorship/', views.mentorship_application, name='mentorship_application'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('send-info/', views.send_info, name='send_info'),
    path('contact', views.contact, name='contact'),
    path('professionals/create/', views.create_professional, name='create_professional'),
    #path('professionals/<int:pk>/', views.professional_detail, name='professional_detail'),
    path('professionals/', professionals_list, name='professionals_list'),
    path('appointment-success/', appointment_success, name='appointment_success'),
    path("book-appointment/", book_appointment, name="book_appointment"),
    path("appointment-success/", lambda request: render(request, "appointment_success.html"), name="appointment_success"),
    path('api/get-available-slots/<int:professional_id>/<str:date>/', get_available_slots, name='get_available_slots'),
    #path("chat/<str:room_name>/", chat_room, name="chat_room"),
    path("anonymous_chat/", views.anonymous_chat, name="anonymous_chat"),
    path("get-messages/", views.get_messages, name="get_messages"),
    path("send-message/", views.send_message, name="send_message"),
    path("training_materials/", training_materials, name="training_materials"),
    path("upload_video/", upload_video, name="upload_video"),  # Admin-only upload page
    path("professionals/<int:professional_id>/", professional_detail, name="professional_detail"),
    path("professional_dashboard", views.professional_dashboard, name="professional_dashboard"),
    #path('professional/dashboard/', views.professional_dashboard, name='professional_dashboard'),
    #path('login/', views.login_view, name='login'),
    path('professional/', views.professional_dashboard, name='professional_dashboard'),
    path('regular_user.html', views.regular_user_dashboard, name='regular_user_dashboard'),
    path('professional_detail/', views.professional_detail, name='professional_detail'),  # No ID required
    path('upload_book/', views.upload_book, name='upload_book'),
    path('upload_article/', views.upload_article, name='upload_article'),
    path('upload_course/', views.upload_course, name='upload_course'),  # Ensure this exists
    path('training_materials_prof/', views.training_materials_prof, name='training_materials_prof'),  # Ensure this exists
    path('quizzes/', views.quizzes, name='quizzes'),
    path('user-appointments/', views.user_appointments, name='user_appointments'),
    path('user-appointments/', views.user_appointments, name='user_appointments'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('completed-courses/', views.completed_courses, name='completed_courses'),
    path('course-detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('achievements/', views.achievements, name='achievements'), 
    path('quiz-category/<str:category>/', views.quiz_category, name='quiz_category'),
    path('professional_home/', views.professional_home, name='professional_home'),
    path('api/quizzes/', quizzes_api, name='quizzes_api'),  # ✅ Fetch all quizzes
    path('api/quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),  # ✅ Fetch a single quiz
    path('quizzes/', views.quizzes, name='quizzes'),
    path('appointments/<int:professional_id>/', appointments_view, name='appointments'),
    path('professionals/<int:professional_id>/message/', views.message_professional, name='message_professional'),
    path('clear-messages/', clear_messages, name='clear_messages'),
    path('remove-appointment/<int:appointment_id>/', remove_appointment, name='remove_appointment'),
    path('update-availability/', update_availability, name='update_availability'),
    path('appointments/<int:professional_id>/', views.appointments_view, name='appointments'),
    path('clear-notifications/', views.clear_notifications, name='clear_notifications'),
    path('translate/', translate_view, name='translate'),
    path('translate-page/', translate_page, name='translate_page'),
    path('settings/', views.settings_view, name='settings'), 
    path('settings/', views.settings_professional, name='settings_professional'),
    path('clear-notifications/', clear_notificationsss, name='clear_notificationsss'),
    path('cancel-appointment/<int:appointment_id>/', cancel_appointment_by_professional, name="cancel_appointment_by_professional"),
    path('fetch-updates/', fetch_updates, name='fetch_updates'),
    path('fetch-notifications/', fetch_notifications, name="fetch_notifications"),
    path('api/quizzes/upload/', upload_quiz, name='upload_quiz'),
    path('language-settings/', language_settings, name='language_settings'),
    path('change-language/', change_language, name='change_language'),
    path('set-language/<str:lang_code>/', views.set_language, name='set_language'),
    path('about/', views.about, name='about'), 
    path("available_slots/", views.available_slots, name="available_slots"),
    path('quizzes/', quizzes, name='quizzes'),
    path('quizzes/upload/', upload_quiz, name='upload_quiz'), 
    path('quizzes/edit/<int:quiz_id>/', edit_quiz, name='edit_quiz'),  # Edit Quiz URL
    path('quizzes/delete/<int:quiz_id>/', delete_quiz, name='delete_quiz'),  # Delete Quiz URL
    path('check_user_role/', views.check_user_role, name='check_user_role'),
    


   
] 







    