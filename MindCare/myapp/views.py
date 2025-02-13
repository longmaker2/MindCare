from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .forms import Video_form
from .forms import Video
from .forms import MentorshipApplication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Professional
from .forms import ProfessionalForm
from django.db import models



def index(request):
    features = Feature.objects.all()
    return  render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exist')
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, email=email, password=password),
                messages.success(request, 'User created successfully')
                return redirect('login')
                
            
        else:
            messages.info(request, 'password is not the same')
            return redirect('register')
    else:
        return render (request, 'register.html')
    


#def login(request):
    ##if request.method == 'POST':
      #  username = request.POST['username']
       # password = request.POST['password']

        #user = auth.authenticate(username=username, password=password)

        #if user is not None:
         #   auth.login(request, user)
          #  return redirect('/')
        #else:
          #  messages.info(request, 'Credentials Invalid')
           # return redirect('login')

    #else:
     #  return render (request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')


  

def counter(request):
    posts =[1, 2, 3, 4, 'erica', 'ange', 'franck']
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def dashboard(request):
    return render(request, 'dashboard.html' )

def training_materials(request):
    return render(request, 'training_materials.html' )

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Debugging log to ensure data is received
        print(f"📩 New Message from {name} ({email}): {message}")

        if not name or not email or not subject or not message:
            return JsonResponse({"error": "All fields are required."}, status=400)

        messages.success(request, "Message sent successfully!")

        # ✅ Make sure to return JSON format
        return JsonResponse({"message": "Message sent successfully!"}, status=200)

    return render(request, "index.html")

def home(request):
    return render(request, 'home.html')

def room(request):
    return room(request, 'room.html')

def all(request):
    if request.method == "POST":
        all_video=Video.objects.all()
        form=Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>uploaded successfully")
    else:
        form=Video_form()
    return render(request,'all.html',{"form":form,"all":all_video})

def mentorship_application(request):
    if request.method == 'POST':
        form = MentorshipApplication(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
            
    else:
        form = MentorshipApplication()

    
    all_data = MentorshipApplication.objects.all()

    return render(request, 'training_materials.html', {'form': form, 'all': all_data})




def upload_video(request):
    if request.method == 'POST' and request.FILES['video_file']:
        video_file = request.FILES['video_file']
        video = Video_form(video_file=video_file)
        video.save()
        return JsonResponse({'message': 'Video uploaded successfully'})
    else:
        return JsonResponse({'error': 'Upload failed'})

def index(request):
    return render(request, 'index.html')
def send_info(request):
    if request.method == 'POST':
        info = request.POST.get('info')
        
        return JsonResponse({'info': info})
    return JsonResponse({'error': 'Invalid request'})

##def professional_detail(request, pk):
    #professional = get_object_or_404(Professional, pk=pk)
    #return render(request, 'professional_detail.html', {'professional': professional})
# ✅ Book Model

    

def create_professional(request):
    if request.method == "POST":
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_success_page')
    else:
        form = ProfessionalForm()
    return render(request, 'professionals/create.html', {'form': form})
from django.shortcuts import render
from .models import Professional

def professionals_list(request):
    professionals = Professional.objects.all()  # Fetch all professionals from DB
    return render(request, 'professionals/list.html', {'professionals': professionals})
from django.shortcuts import render
from .models import Professional  # Import your Professional model

def index(request):
    professionals = Professional.objects.all()  # Fetch professionals from DB
    return render(request, 'index.html', {'professionals': professionals})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Professional, Appointment
from .forms import AppointmentForm

@login_required
def index(request):
    professionals = Professional.objects.all()  # Fetch all professionals
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Assign logged-in user
            appointment.save()
            return redirect('appointment_success')  # Redirect after successful booking

    return render(request, 'index.html', {'professionals': professionals, 'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')
from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Appointment, Professional
from django.contrib.auth.decorators import login_required 

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Professional, Appointment

def book_appointment(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "You must be logged in to book an appointment."}, status=403)

        professional_id = request.POST.get("professional")
        date = request.POST.get("date")
        time = request.POST.get("time")
        reason = request.POST.get("reason")

        if not professional_id or not date or not time or not reason:
            return JsonResponse({"error": "All fields are required."}, status=400)

        # Get Professional
        try:
            professional = Professional.objects.get(id=professional_id)
        except Professional.DoesNotExist:
            return JsonResponse({"error": "Selected professional does not exist."}, status=400)

        # Check Slot Availability
        if time in professional.booked_slots:
            return JsonResponse({"error": "Selected time slot is already booked."}, status=400)

        # ✅ Book the appointment and link the user
        appointment = Appointment.objects.create(
            user=request.user,  # Attach the logged-in user
            professional=professional,
            date=date,
            time=time,
            reason=reason
        )

        # ✅ Mark slot as booked and save
        professional.booked_slots.append(time)
        professional.save()

        return render(request, "appointment_success.html", {"appointment": appointment})

    return render(request, "appointment_form.html")


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Professional

def get_available_slots(request, professional_id, date):
    """Returns available slots for a professional on a given date."""
    professional = get_object_or_404(Professional, id=professional_id)

    return JsonResponse({'available_slots': professional.available_slots})

from django.shortcuts import render
from myapp.models import Professional

from django.shortcuts import render
from myapp.models import Professional, Appointment

from django.shortcuts import render
from myapp.models import Professional, Appointment

from django.shortcuts import render
from myapp.models import Professional, Appointment

def index(request):
    professionals = Professional.objects.all()

    for professional in professionals:
        # Get all booked slots for the professional
        booked_slots = Appointment.objects.filter(professional_name=professional).values_list('time', flat=True)

        # Store available slots with booking status
        professional.available_slots_status = [
            {"time": slot, "is_booked": slot in booked_slots} for slot in professional.available_slots
        ]

    return render(request, 'index.html', {'professionals': professionals})

from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
from django.views.decorators.csrf import csrf_exempt

def get_messages(request, room_id):
    """ Fetch latest messages for AJAX polling """
    messages = ChatMessage.objects.filter(room_id=room_id).order_by("timestamp")
    data = ""
    
    for message in messages:
        alignment = "message-right" if message.username == request.user.username else "message-left"
        data += f'<div class="message {alignment}"><p>{message.content}</p><span class="timestamp">{message.timestamp}</span></div>'
    
    return JsonResponse(data, safe=False)

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatMessage
import random

# Generate random anonymous username
def generate_anonymous_username():
    adjectives = ["Brave", "Smart", "Quick", "Happy", "Clever"]
    nouns = ["Panda", "Tiger", "Dolphin", "Eagle", "Fox"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json

from django.shortcuts import render, redirect
from .models import ChatMessage

from django.shortcuts import render, redirect
from .models import ChatMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import ChatMessage

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            message = request.POST.get("message", "").strip()

            if not message:
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            # Save message with "Anonymous" as default username
            chat_message = ChatMessage.objects.create(username="Anonymous", content=message, timestamp=now())
            chat_message.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


def chat_room(request):
    messages = ChatMessage.objects.all()
    return render(request, "anonymous_chat.html", {"messages": messages})
from django.http import JsonResponse
from .models import ChatMessage

def get_messages(request):
    messages = ChatMessage.objects.order_by("-timestamp")[:50]  # Get latest 50 messages
    return JsonResponse([{"content": msg.content, "timestamp": msg.timestamp} for msg in messages], safe=False)

from django.shortcuts import render, redirect
from .models import ChatMessage

def anonymous_chat(request):
    if request.method == "POST":
        message_content = request.POST.get("message")
        if message_content:
            ChatMessage.objects.create(username="Anonymous", content=message_content)
        return redirect("anonymous_chat")  # Redirect to clear form

    messages = ChatMessage.objects.all().order_by("-timestamp")
    return render(request, "anonymous_chat.html", {"messages": messages})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Video
from .forms import VideoUploadForm

# Function to check if user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def upload_video(request):
    """Allow only admin users to upload videos"""
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("training_materials")
    else:
        form = VideoUploadForm()
    
    return render(request, "upload_video.html", {"form": form})

def training_materials(request):
    """Allow all users to view and filter uploaded videos"""
    videos = Video.objects.all()
    return render(request, "training_materials.html", {"videos": videos})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Video
from .forms import VideoUploadForm

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("training_materials")
    else:
        form = VideoUploadForm()
    
    return render(request, "upload_video.html", {"form": form})

def training_materials(request):
    videos = Video.objects.all()
    return render(request, "training_materials.html", {"videos": videos})

from django.shortcuts import render, get_object_or_404
from .models import Professional  # Assuming you have a Professional model

def professional_detail(request, professional_id=None):
    if professional_id is None:
        # Get the logged-in user (assuming professionals are users)
        professional = request.user
    else:
        # Retrieve the professional from the database
        professional = get_object_or_404(Professional, id=professional_id)

    return render(request, "professional_detail.html", {"professional": professional})


from django.shortcuts import render

def professional_dashboard(request):
    return render(request, "professional_dashboard.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # Get the role from the form
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if role == 'professional':
                return render(request, 'professional.html')  # Render professional.html
            else:
                return render(request, 'index.html')  # Render index.html
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Article, Course
from .forms import BookForm, ArticleForm, CourseForm

@login_required
def upload_book(request):
    if not request.user.is_superuser:
        return redirect('training_materials')  # Redirect non-superusers
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('training_materials')
    else:
        form = BookForm()
    
    return render(request, 'upload_book.html', {'form': form})


@login_required
def upload_article(request):
    if not request.user.is_superuser:
        return redirect('training_materials')
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_materials')
    else:
        form = ArticleForm()
    
    return render(request, 'upload_article.html', {'form': form})


@login_required
def upload_course(request):
    if not request.user.is_superuser:
        return redirect('training_materials')
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_materials')
    else:
        form = CourseForm()
    
    return render(request, 'upload_course.html', {'form': form})


def training_materials_prof(request):
    return render(request, 'training_materials_prof.html')  # Ensure the template exists
from django.shortcuts import render
from .models import Book, Article, Course, Video

def training_materials(request):
    books = Book.objects.all()
    articles = Article.objects.all()
    courses = Course.objects.all()
    videos = Video.objects.all()  
    
    return render(request, 'training_materials.html', {
        'books': books,
        'articles': articles,
        'courses': courses,
        "videos": videos
    })
from django.shortcuts import render
from .models import Appointment, CompletedCourse, Achievement, QuizResult

def user_dashboard(request):
    user = request.user

    # Fetch user-specific data
    appointments = Appointment.objects.filter(user=user).order_by('date')
    completed_courses = CompletedCourse.objects.filter(user=user)
    achievements = Achievement.objects.filter(user=user)
    
    # Calculate progress (e.g., % of completed courses)
    total_courses = 10  # Set this dynamically if needed
    progress = (completed_courses.count() / total_courses) * 100 if total_courses > 0 else 0

    return render(request, "dashboard.html", {
        "appointments": appointments,
        "completed_courses": completed_courses,
        "achievements": achievements,
        "progress": round(progress, 2)
    })
from .models import Appointment, CompletedCourse, Achievement, QuizResult
def my_view(request):
    from .models import CompletedCourse  # Move import inside function
    ...
from django.shortcuts import render

from django.shortcuts import render
from .models import Quiz

def quizzes(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quizzes.html', {'quizzes': quiz_list})

from django.shortcuts import render

from django.shortcuts import render
from .models import Appointment

def user_appointments(request):
    user_appointments = Appointment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'user_appointments.html', {'appointments': user_appointments})

from django.shortcuts import redirect, get_object_or_404
from .models import Appointment

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    appointment.status = "Canceled"
    appointment.save()
    return redirect('user_appointments')

from django.shortcuts import render
from .models import CompletedCourse

def completed_courses(request):
    courses = CompletedCourse.objects.filter(user=request.user)
    return render(request, 'completed_courses.html', {'completed_courses': courses})

from django.shortcuts import render
from .models import CompletedCourse

def completed_courses(request):
    courses = CompletedCourse.objects.filter(user=request.user)
    return render(request, 'completed_courses.html', {'completed_courses': courses})

from django.shortcuts import render, get_object_or_404
from .models import CompletedCourse

def course_detail(request, course_id):
    course = get_object_or_404(CompletedCourse, id=course_id)
    return render(request, 'course_detail.html', {'course': course})
from django.shortcuts import render

def achievements(request):
    return render(request, 'achievements.html', {})

from django.shortcuts import render

def quiz_category(request, category):
    return render(request, 'quiz_category.html', {'category': category})
