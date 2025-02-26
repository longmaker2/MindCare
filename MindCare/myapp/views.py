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
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


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

def all_videos(request):  # ✅ Renamed function
    if request.method == "POST":
        all_video = Video.objects.all()
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>uploaded successfully</h1>")
    else:
        form = Video_form()
    return render(request, 'all.html', {"form": form, "all": all_video})

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
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Professional, Appointment
import random

import json
import random
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Professional, Appointment
from myapp.utils import send_email_async  # ✅ Absolute import

@csrf_exempt  # ⚠️ Remove if using CSRF protection in production
def book_appointment(request):
    if request.method == "GET":
        professional_id = request.GET.get("professional")

        if not professional_id:
            return JsonResponse({"error": "Missing 'professional' parameter"}, status=400)

        professional = get_object_or_404(Professional, id=professional_id)
        professional.refresh_from_db()  # ✅ Ensure fresh data

        all_slots = sorted(set(professional.available_slots + professional.booked_slots))

        return render(request, "book_appointment.html", {
            "professional": professional,
            "all_slots": all_slots,
            "booked_slots": professional.booked_slots,
        })

    elif request.method == "POST":
        # ✅ Debugging - Print content type and raw request body
        print("📌 Received Content-Type:", request.content_type)
        print("📌 Raw Body:", request.body)  

        # ✅ Detect whether request contains JSON or form data
        try:
            if request.content_type == "application/json":
                data = json.loads(request.body)  # Parse JSON data
            else:
                data = request.POST.dict()  # Parse form data
        except json.JSONDecodeError:
            print("❌ JSON Parse Error")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        print("📌 Parsed Data:", json.dumps(data, indent=4))

        # ✅ Extract required fields
        professional_id = data.get("professional")
        date = data.get("date")
        time = data.get("time")
        reason = data.get("reason")

        # ✅ Validate required fields
        if not all([professional_id, date, time, reason]):
            print("❌ Missing fields in request!")
            return JsonResponse({"error": "All fields are required!"}, status=400)

        # ✅ Validate professional exists
        try:
            professional = Professional.objects.get(id=professional_id)
        except Professional.DoesNotExist:
            print("❌ Professional not found!")
            return JsonResponse({"error": "Professional not found"}, status=400)

        professional.refresh_from_db()  # ✅ Ensure fresh data before modifying slots

        # ✅ Ensure slot is available
        if time in professional.booked_slots:
            print("❌ Time slot already booked!")
            return JsonResponse({"error": "This time slot is already booked. Please choose another."}, status=400)

        # ✅ Move the slot from available to booked
        updated_available_slots = professional.available_slots.copy()
        updated_booked_slots = professional.booked_slots.copy()

        if time in updated_available_slots:
            updated_available_slots.remove(time)
        updated_booked_slots.append(time)

        # ✅ Update Professional's slots
        professional.available_slots = updated_available_slots
        professional.booked_slots = updated_booked_slots
        professional.save()

        # ✅ Create the Appointment
        appointment = Appointment.objects.create(
            client=request.user,
            professional_name=professional.name,
            date=date,
            time=time,
            reason=reason
        )

        # ✅ Generate Google Meet link
        google_meet_link = f"https://meet.google.com/{random.choice(['abc', 'xyz', 'lmn'])}-{random.randint(100,999)}-{random.randint(100,999)}"

        # ✅ Prepare email content
        subject = "Your Appointment Confirmation"
        user_message = f"""
        Hello {request.user.username},

        Your appointment with {professional.name} has been confirmed.

        📅 Date: {date}
        ⏰ Time: {time}

        Join the meeting via Google Meet:
        🔗 {google_meet_link}

        If you have any questions, feel free to contact {professional.name} at {professional.contact_email}.

        Best regards,  
        Your Website Team
        """

        professional_message = f"""
        Hello {professional.name},

        A new appointment has been booked with you.

        📅 Date: {date}
        ⏰ Time: {time}
        👤 Client: {request.user.username} ({request.user.email})

        The meeting will take place via Google Meet:
        🔗 {google_meet_link}

        Please be prepared for the session.

        Best regards,  
        Your Website Team
        """

        # ✅ Send exactly 2 emails
        send_email_async(subject, user_message, request.user.email)
        send_email_async(f"New Appointment: {request.user.username}", professional_message, professional.contact_email)

        return JsonResponse({
            "message": "Appointment successfully booked! A confirmation email has been sent to you",
            "google_meet_link": google_meet_link,
            "booked_slots": updated_booked_slots
        }, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)

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

from django.http import JsonResponse
from .models import AnonymousPrivateMessage

def get_messages(request):
    """Fetch messages in descending order (newest at the bottom)"""
    user = request.user.username  # Get the logged-in user

    # ✅ Fetch messages meant for Everyone or the logged-in user
    messages = AnonymousPrivateMessage.objects.filter(
        recipient__in=["Everyone", user]
    ).order_by("-timestamp")  # ✅ Order messages from newest to oldest

    # ✅ Convert messages into JSON format
    message_list = [
        {
            "id": msg.id,
            "sender": msg.sender,
            "recipient": msg.recipient,
            "content": msg.content,
            "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for msg in messages
    ]

    return JsonResponse(message_list[::-1], safe=False)  # ✅ Reverse to show newest at the bottom




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
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Message
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Message

from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.db import transaction  # ✅ Force commit messages immediately
from .models import AnonymousPrivateMessage

@csrf_exempt
@login_required
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message_content = data.get("message", "").strip()
            recipient = data.get("recipient", "").strip()
            is_anonymous = data.get("anonymous", False)

            if not message_content:
                return JsonResponse({"success": False, "error": "Message cannot be empty"}, status=400)

            sender = request.user.username  # Default sender

            # ✅ Handle Anonymous Messaging
            if is_anonymous:
                sender = "Anonymous"

            # ✅ Ensure recipient exists
            if recipient != "Everyone":
                try:
                    recipient_user = User.objects.get(username=recipient)
                except User.DoesNotExist:
                    return JsonResponse({"success": False, "error": "Recipient not found"}, status=400)

            # ✅ Force immediate database commit
            with transaction.atomic():
                message = AnonymousPrivateMessage.objects.create(
                    sender=sender,
                    recipient=recipient,
                    content=message_content,
                    timestamp=now()
                )

            return JsonResponse({
                "success": True,
                "message_id": message.id,
                "sender": sender,
                "recipient": recipient,
                "content": message_content,
                "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            })

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON format"}, status=400)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)


from .models import Message
from django.contrib.auth.models import User

def chat_room(request):
    if request.user.is_authenticated:
        # Show messages for 'Everyone' + messages sent directly to the user
        messages = Message.objects.filter(recipient__in=["Everyone", request.user.username]).order_by("-timestamp")
    else:
        # Show only public messages
        messages = Message.objects.filter(recipient="Everyone").order_by("-timestamp")

    # Get all users **except the current logged-in user**
    users = User.objects.exclude(username=request.user.username) 

    return render(request, "anonymous_chat.html", {"messages": messages, "users": users})


from django.http import JsonResponse
from .models import AnonymousPrivateMessage

def get_messages(request):
    """Fetch messages immediately without delay"""
    messages = AnonymousPrivateMessage.objects.order_by("timestamp")
    
    # ✅ Ensure messages are always fresh
    message_list = [
        {
            "sender": msg.sender,
            "recipient": msg.recipient,
            "content": msg.content,
            "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for msg in messages
    ]
    
    return JsonResponse(message_list, safe=False, headers={'Cache-Control': 'no-store'})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AnonymousPrivateMessage
from django.contrib.auth.models import User

@login_required
def anonymous_chat(request):
    # ✅ Fetch messages for "Everyone" AND private messages sent to the logged-in user
    messages = AnonymousPrivateMessage.objects.filter(
        recipient__in=["Everyone", request.user.username]
    ).order_by('-timestamp')  # Show newest messages first

    # ✅ Get all users **except the current logged-in user**
    users = User.objects.exclude(username=request.user.username)

    return render(request, 'anonymous_chat.html', {
        'messages': messages,
        'users': users
    })


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


from django.shortcuts import render, get_object_or_404
from myapp.models import Professional, Appointment, Message

from django.shortcuts import render
from django.utils.timezone import now
from myapp.models import Professional, Appointment, Message

def professional_dashboard(request):
    professional = request.user.professional_profile

    # ✅ Retrieve only future appointments (including today)
    upcoming_appointments = Appointment.objects.filter(
        professional_name=professional.name,
        date__gte=now().date(),  # Exclude past appointments
        status='Upcoming'  # Keep only "Upcoming" appointments
    ).order_by('date', 'time')

    # ✅ Retrieve messages where the professional is the receiver
    messages = Message.objects.filter(receiver=professional).order_by('-timestamp')

    return render(request, 'professional_dashboard.html', {
        'professional': professional,
        'upcoming_appointments': upcoming_appointments,
        'messages': messages  # ✅ Ensure messages are passed to the template
    })


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .models import Professional

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if role == 'professional':
                if hasattr(user, 'professional_profile'):  # Check if the user has a Professional profile
                    return redirect(reverse('professional_home'))
                else:
                    messages.error(request, 'No professional profile found. Contact support.')
                    return redirect('login')

            return redirect(reverse('index'))  # Redirect regular users
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
    completed_courses = CompletedCourse.objects.all()  # or another valid filter
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
    user_appointments = Appointment.objects.filter(client=request.user).order_by('-date')
    return render(request, 'user_appointments.html', {'appointments': user_appointments})

from django.shortcuts import redirect, get_object_or_404
from .models import Appointment

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, client=request.user)
    appointment.status = "Canceled"
    appointment.save()
    return redirect('user_appointments')

from django.shortcuts import render
from .models import CompletedCourse

def completed_courses(request):
    courses = CompletedCourse.objects.filter(user=request.user)  # Now valid
    return render(request, 'completed_courses.html', {'courses': courses})

    

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
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensures only logged-in users can access it
def regular_user_dashboard(request):
    return render(request, 'regular_user.html')  # ✅ Make sure this template exists

from django.shortcuts import render
from .models import Professional  # Ensure Professional model is imported

def professional_home(request):
    professionals = Professional.objects.all()  # Fetch professionals
    return render(request, 'professional_home.html', {'professionals': professionals})


from django.http import JsonResponse
from django.shortcuts import render
from .models import Quiz

def quizzes_api(request):
    quizzes = list(Quiz.objects.values("id", "title", "description", "category"))  # Convert QuerySet to list of dicts
    return JsonResponse({"quizzes": quizzes})  # ✅ JSON response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Quiz, Question  # ✅ Ensure Question model is imported

def quiz_detail(request, quiz_id):
    """Fetches quiz details based on ID, including questions"""
    try:
        quiz = Quiz.objects.get(id=quiz_id)
        questions = list(Question.objects.filter(quiz=quiz).values("id", "text", "options", "correct_answer"))

        return JsonResponse({
            "id": quiz.id,
            "title": quiz.title,
            "description": quiz.description,
            "category": quiz.category,
            "questions": questions  # ✅ Add questions to response
        })

    except Quiz.DoesNotExist:
        return JsonResponse({"error": f"Quiz with ID {quiz_id} not found."}, status=404)


def get_quizzes(request):
    quizzes = [
        {
            "id": 1,
            "title": "General Anxiety Quiz",
            "description": "Assess your anxiety levels",
            "questions": [
                {"text": "How often do you feel anxious?", "options": ["Never", "Sometimes", "Often", "Always"], "correct_answer": "Often"},
                {"text": "Do you struggle to control worry?", "options": ["No", "Rarely", "Sometimes", "Frequently"], "correct_answer": "Frequently"}
            ]
        }
    ]
    return JsonResponse({"quizzes": quizzes})
def get_quiz_details(request, quiz_id):
    quiz = next((q for q in quizzes if q["id"] == quiz_id), None)
    return JsonResponse(quiz if quiz else {"error": "Quiz not found"})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Sample Quiz Data (This can be replaced with a database later)
quizzes = [
    {
        "id": 1,
        "title": "General Anxiety Quiz",
        "category": "Anxiety",
        "description": "Assess your anxiety levels.",
        "questions": [
            {
                "text": "How often do you feel anxious?",
                "options": ["Never", "Sometimes", "Often", "Always"],
                "correct_answer": "Often"
            },
            {
                "text": "Do you struggle to control worry?",
                "options": ["No", "Rarely", "Sometimes", "Frequently"],
                "correct_answer": "Frequently"
            }
        ]
    },
    {
        "id": 2,
        "title": "Social Anxiety Quiz",
        "category": "Anxiety",
        "description": "Evaluate your comfort in social situations.",
        "questions": [
            {
                "text": "Do you avoid social gatherings?",
                "options": ["Never", "Occasionally", "Often", "Always"],
                "correct_answer": "Often"
            },
            {
                "text": "Do you fear public speaking?",
                "options": ["Not at all", "A little", "Very much", "Extremely"],
                "correct_answer": "Very much"
            }
        ]
    }
]


# Sample view for quizzes page
def quizzes(request):
    return render(request, 'quizzes.html')  # Ensure 'quizzes.html' exists in templates

# Sample quiz API views
@csrf_exempt
def get_quizzes(request):
    return JsonResponse({"message": "List of quizzes"}, safe=False)

@csrf_exempt
def get_quiz_details(request, quiz_id):
    return JsonResponse({"message": f"Details for quiz {quiz_id}"}, safe=False)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Professional

@receiver(post_save, sender=User)
def create_professional_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff:  # Assuming professionals are staff users
        Professional.objects.get_or_create(user=instance, name=instance.username, contact_email=instance.email)


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Professional, Appointment

@login_required
def appointments_view(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id)

    # ✅ Fetch all appointments for the professional (both past & upcoming)
    appointments = Appointment.objects.filter(professional_name=professional.name).select_related('client')

    context = {
        'professional': professional,
        'appointments': appointments,
        'today': now().date()  # ✅ Pass today's date to the template
    }
    return render(request, 'appointments.html', context)


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Quiz, Question

class QuizListView(View):
    def get(self, request):
        quizzes = list(Quiz.objects.values("id", "title", "description"))  # REMOVE 'category'
        return JsonResponse({"quizzes": quizzes})

class QuizDetailView(View):
    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = list(quiz.questions.values("id", "text", "options", "correct_answer"))
        return JsonResponse({"title": quiz.title, "questions": questions})
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Professional, Message

def message_professional(request, professional_id):
    professional = get_object_or_404(Professional, id=professional_id)
    success = False  # Default value for success message

    if request.method == "POST":
        message_content = request.POST.get("message")

        if not message_content:
            return render(request, "message_professional.html", {
                "professional": professional,
                "error": "Message cannot be empty."
            })

        # ✅ Ensure `receiver` is a User instance (linked to Professional)
        receiver_user = professional.user

        # ✅ Create the message with the correct sender and receiver
        Message.objects.create(
            sender=request.user,
            receiver=professional,
            content=message_content
        )

        success = True  # ✅ Set success to True when message is sent

    return render(request, "message_professional.html", {
        "professional": professional,
        "success": success
    })

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from myapp.models import Message

@login_required
def clear_messages(request):
    if request.method == "POST":
        try:
            professional = request.user.professional_profile
            Message.objects.filter(receiver=professional).delete()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"})