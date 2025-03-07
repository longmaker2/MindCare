from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .forms import QuestionForm, Video_form
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
from googletrans import Translator
import logging
from django.utils.translation import activate, get_language
from django.utils import translation
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Professional, Appointment
import random
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now  # ✅ Import for date validation
from .models import Professional, Appointment
from myapp.utils import send_email_async  # ✅ Absolute import
import smtplib
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from myapp.models import Professional, Appointment
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import json
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
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ChatMessage
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Professional
from django.http import JsonResponse
from .models import AnonymousPrivateMessage
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Video
from .forms import VideoUploadForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AnonymousPrivateMessage
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import AnonymousPrivateMessage
from django.shortcuts import render, get_object_or_404
from myapp.models import Professional, Appointment, Message
from django.shortcuts import render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from myapp.models import Professional, Appointment, Message, Notification
from django.utils.timezone import now
from datetime import datetime
from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment, Message, Notification
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .models import Professional
#from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .models import Message, Notification, Appointment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Video
from .forms import VideoUploadForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.models import Appointment, Notification, Professional
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Article, Course
from .forms import BookForm, ArticleForm, CourseForm
from .models import CompletedCourse  # Move import inside function
from django.shortcuts import render
from django.shortcuts import render
from .models import Quiz
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Professional, Appointment
from .forms import AppointmentForm
from django.shortcuts import render
from .models import Appointment, CompletedCourse, Achievement, QuizResult
from django.shortcuts import render
from django.shortcuts import render
from .models import Quiz
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Professional
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Quiz, Question
from .forms import QuizForm

logger = logging.getLogger(__name__)


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

    return render(request, 'dashboard.html')

#def training_materials(request):
    #return render(request, 'training_materials.html' )


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # Debugging log to ensure data is received
        print(f"📩 New Message from {name} ({email}): {message}")
        
        if not name or not email or not subject or not message:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"error": "All fields are required."}, status=400)
            else:
                messages.error(request, "All fields are required.")
                return redirect('index')  # Or whatever page you want to redirect to
        
        messages.success(request, "Message sent successfully!")
        
        # For AJAX requests, return JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"message": "Message sent successfully!"}, status=200)
        # For normal form submission, redirect back
        else:
            return redirect('index')  # Or whatever page you want to redirect to
    
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


def send_email(subject, message, recipient_email):
    """Send email synchronously to ensure it's sent properly."""
    try:
        print(f"📧 Sending email to {recipient_email}...")
        send_mail(
            subject, 
            message, 
            settings.EMAIL_HOST_USER, 
            [recipient_email], 
            fail_silently=False
        )
        print(f"✅ Email successfully sent to {recipient_email}")
    except smtplib.SMTPException as smtp_error:
        print(f"❌ SMTP error: {smtp_error}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")

@csrf_exempt  
def book_appointment(request):

    if request.method == "GET":
        # ✅ Get professional details for the booking form
        professional_id = request.GET.get("professional")
        professional = get_object_or_404(Professional, id=professional_id)
        form = AppointmentForm()

        return render(request, "book_appointment.html", {"form": form, "professional": professional})

    elif request.method == "POST":
        try:
            if request.content_type == "application/json":
                data = json.loads(request.body)  
            else:
                data = request.POST.dict()  
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        professional_id = data.get("professional")
        date = data.get("date")
        time = data.get("time")
        reason = data.get("reason")

        if not all([professional_id, date, time, reason]):
            return JsonResponse({"error": "All fields are required!"}, status=400)

        today_date = now().date()
        if date < today_date.isoformat():
            return JsonResponse({"error": "You cannot book an appointment for a past date."}, status=400)

        professional = get_object_or_404(Professional, id=professional_id)
        professional.refresh_from_db()

        if time in professional.booked_slots:
            return JsonResponse({"error": "This time slot is already booked. Please choose another."}, status=400)

        updated_available_slots = professional.available_slots.copy()
        updated_booked_slots = professional.booked_slots.copy()

        if time in updated_available_slots:
            updated_available_slots.remove(time)
            updated_booked_slots.append(time)

        professional.available_slots = updated_available_slots
        professional.booked_slots = updated_booked_slots
        professional.save()

        # ✅ Save appointment using `professional_name`
        appointment = Appointment.objects.create(
            client=request.user,  
            professional_name=professional.name,  
            date=date,
            time=time,
            reason=reason
        )

        # ✅ Generate Google Meet link
        google_meet_link = f"https://meet.google.com/{random.choice(['abc', 'xyz', 'lmn'])}-{random.randint(100,999)}-{random.randint(100,999)}"

        # ✅ Prepare email content for the client
        subject_client = "Your Appointment Confirmation"
        user_message = f"""
        Hello {request.user.username},

        Your appointment with {professional.name} has been confirmed.

        📅 Date: {date}
        ⏰ Time: {time}

        Join the meeting via Google Meet:
        🔗 {google_meet_link}

        If you have any questions, feel free to contact {professional.name} at {professional.contact_email}.

        Best regards,  
        MindCare Team
        """

        # ✅ Prepare email content for the professional
        subject_professional = f"New Appointment: {request.user.username}"
        professional_message = f"""
        Hello {professional.name},

        A new appointment has been booked.

        📅 Date: {date}
        ⏰ Time: {time}
        👤 Client: {request.user.username} ({request.user.email})

        Google Meet Link:
        🔗 {google_meet_link}

        Please be prepared for the session.

        Best regards,  
        MindCare Team
        """

        # ✅ Send emails synchronously (not in a thread)
        print("📨 Sending email to client:", request.user.email)
        send_email(subject_client, user_message, request.user.email)

        print("📨 Sending email to professional:", professional.contact_email)
        send_email(subject_professional, professional_message, professional.contact_email)

        return JsonResponse({
            "message": "Appointment successfully booked! A confirmation email with a Google Meet link has been sent.",
            "google_meet_link": google_meet_link,
            "booked_slots": updated_booked_slots
        }, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_available_slots(request, professional_id, date):
    """Returns available slots for a professional on a given date."""
    professional = get_object_or_404(Professional, id=professional_id)

    return JsonResponse({'available_slots': professional.available_slots})

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

# Generate random anonymous username
def generate_anonymous_username():
    adjectives = ["Brave", "Smart", "Quick", "Happy", "Clever"]
    nouns = ["Panda", "Tiger", "Dolphin", "Eagle", "Fox"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

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

@login_required
def anonymous_chat(request):
    # ✅ Fetch messages for "Everyone" AND private messages sent to the logged-in user
    messages = AnonymousPrivateMessage.objects.filter(
        recipient__in=["Everyone", request.user.username]
    ).order_by('-timestamp')  # Show newest messages first

    # ✅ Get all users **except the current logged-in user**
    users = User.objects.exclude(username=request.user.username)
    
    # Check if the user is a professional by looking for a professional_profile
    is_professional = hasattr(request.user, 'professional_profile')

    return render(request, 'anonymous_chat.html', {
        'messages': messages,
        'users': users,
        'is_professional': is_professional
    })

from django.shortcuts import render, redirect

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

#def training_materials(request):
   # """Allow all users to view and filter uploaded videos"""
    #videos = Video.objects.all()
    #return render(request, "training_materials.html", {"videos": videos})

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

@login_required
def professional_dashboard(request):
    professional = request.user.professional_profile
    current_datetime = now()  # Get current date and time

    # ✅ Retrieve only future appointments (including today, but checking time as well)
    upcoming_appointments = Appointment.objects.filter(
        professional_name=professional.name,
        status='Upcoming'
    ).filter(
        date__gt=current_datetime.date()  # Appointments in future dates
    ).union(
        Appointment.objects.filter(
            professional_name=professional.name,
            status='Upcoming',
            date=current_datetime.date(),  # Include today's appointments
            time__gt=current_datetime.time()  # Only future times
        )
    ).order_by('date', 'time')

    # ✅ Retrieve messages where the professional is the receiver
    messages = Message.objects.filter(receiver=professional).order_by('-timestamp')

    # ✅ Retrieve unread notifications
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by("-created_at")

    return render(request, 'professional_dashboard.html', {
        'professional': professional,
        'upcoming_appointments': upcoming_appointments,
        'messages': messages,
        'notifications': notifications,
        'current_datetime': current_datetime  # ✅ Pass the current timestamp
    })

@login_required
def fetch_updates(request):
    professional = request.user.professional_profile
    current_datetime = now()

    # ✅ Get upcoming appointments
    upcoming_appointments = list(Appointment.objects.filter(
        professional_name=professional.name,
        status='Upcoming'
    ).filter(
        date__gt=current_datetime.date()
    ).union(
        Appointment.objects.filter(
            professional_name=professional.name,
            status='Upcoming',
            date=current_datetime.date(),
            time__gt=current_datetime.time()
        )
    ).order_by('date', 'time').values('client__username', 'date', 'time'))

    # ✅ Fix sender username key manually
    messages = Message.objects.filter(receiver=professional).order_by('-timestamp').values(
        'sender__username', 'content', 'timestamp'
    )
    
    messages_list = [
        {
            "sender_username": msg["sender__username"],  # ✅ Fix the key name
            "content": msg["content"],
            "timestamp": msg["timestamp"].strftime("%Y-%m-%d %H:%M")
        }
        for msg in messages
    ]

    # ✅ Fetch notifications
    notifications = list(Notification.objects.filter(recipient=request.user)
                        .order_by('-created_at')
                        .values('message', 'created_at'))

    return JsonResponse({
        'appointments': upcoming_appointments,
        'messages': messages_list,  # ✅ Now correctly formatted
        'notifications': notifications
    })

def login_view(request):
    if request.method == 'POST':
        # Check if this is an AJAX request to validate the role
        if 'role_check' in request.POST and request.POST['role_check'] == 'true':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                # Determine the user's role
                user_role = 'professional' if hasattr(user, 'professional_profile') else 'user'
                return JsonResponse({
                    'status': 'success',
                    'user_role': user_role
                })
            else:
                return JsonResponse({
                    'status': 'invalid_credentials',
                    'message': 'Invalid username or password'
                })
        
        # Normal login flow
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(request, username=username, password=password)

        if user:
            # Determine the user's actual role
            is_professional = hasattr(user, 'professional_profile')
            
            # Validate that the user is trying to log in with their correct role
            if (role == 'professional' and not is_professional) or (role == 'user' and is_professional):
                messages.error(request, f"You cannot log in as {role}. Your registered role is {'professional' if is_professional else 'user'}.")
                return redirect('login')
            
            # Proceed with normal login
            login(request, user)

            if role == 'professional':
                if is_professional:  # Check if the user has a Professional profile
                    return redirect(reverse('professional_dashboard'))
                else:
                    messages.error(request, 'No professional profile found. Contact support.')
                    return redirect('login')

            return redirect(reverse('dashboard'))  # Redirect regular users
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BookForm, ArticleForm, CourseForm
#from .models import UserProfile

def is_admin_or_professional(user):
    """ Check if user is a superuser or a professional """
    return user.is_superuser or getattr(user, "is_professional", False)
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import BookForm, ArticleForm, CourseForm

@login_required
def upload_book(request):
    # ✅ Check if the user is a professional or a superuser
    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
        return redirect('training_materials')  # Restrict access

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
    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
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
    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
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

def training_materials(request):
    books = Book.objects.all()
    articles = Article.objects.all()
    courses = Course.objects.all()
    videos = Video.objects.all()
    
    # Check if the user is a professional
    is_professional = hasattr(request.user, 'professional_profile')
        
    return render(request, 'training_materials.html', {
        'books': books,
        'articles': articles,
        'courses': courses,
        'videos': videos,
        'is_professional': is_professional
    })
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
def my_view(request):
    from .models import CompletedCourse  # Move import inside function

from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Professional
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quiz


def user_appointments(request):
    user_appointments = Appointment.objects.filter(client=request.user).order_by('-date')
    return render(request, 'user_appointments.html', {'appointments': user_appointments})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, client=request.user)

    if appointment.status != "Upcoming":
        return redirect("user_appointments")  # ✅ Redirect to user's appointment list if already canceled

    # ✅ Mark the appointment as canceled
    appointment.status = "Canceled"
    appointment.save()

    # ✅ Find the professional related to this appointment
    professional = get_object_or_404(Professional, name=appointment.professional_name)

    # ✅ Send a notification to the professional
    Notification.objects.create(
        recipient=professional.user,
        message=f"🚨 Your appointment with {request.user.username} on {appointment.date} at {appointment.time} was canceled."
    )

    # ✅ Redirect Based on User Type
    if hasattr(request.user, "professional_profile"):
        return redirect("professional_dashboard")  # Redirect professionals to their dashboard
    else:
        return redirect("user_appointments")  # Redirect regular users to their appointments list
def completed_courses(request):
    courses = CompletedCourse.objects.filter(user=request.user)  # Now valid
    return render(request, 'completed_courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(CompletedCourse, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def achievements(request):
    return render(request, 'achievements.html', {})

from django.shortcuts import render

def quiz_category(request, category):
    return render(request, 'quiz_category.html', {'category': category})

@login_required
def regular_user_dashboard(request):
    # Debugging: Print logged-in user
    print("DEBUG: Logged-in user →", request.user)

    # Retrieve upcoming appointments
    appointments = Appointment.objects.filter(
        client=request.user,  # ✅ Correct field name
        date__gte=timezone.localdate(),  # ✅ Fetch only future appointments
        status="Upcoming"  # ✅ Ensure it's filtering by "Upcoming"
    ).order_by("date", "time")

    # Debugging: Check if any appointments are retrieved
    print("DEBUG: Retrieved Appointments Count →", appointments.count())

    for appointment in appointments:
        print(f"DEBUG: Appointment - {appointment.professional_name} on {appointment.date} at {appointment.time}")

    return render(request, 'dashboard.html', {"appointments": appointments})


def professional_home(request):
    professionals = Professional.objects.all()  # Fetch professionals
    return render(request, 'professional_home.html', {'professionals': professionals})


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


@receiver(post_save, sender=User)
def create_professional_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff:  # Assuming professionals are staff users
        Professional.objects.get_or_create(user=instance, name=instance.username, contact_email=instance.email)


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

@login_required
def remove_appointment(request, appointment_id):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=appointment_id)
        client = appointment.client  # Get the client of the appointment

        # ✅ Create a notification for the client
        Notification.objects.create(
            recipient=client,
            message=f"Your appointment with {appointment.professional_name} on {appointment.date} at {appointment.time} was canceled."
        )

        appointment.delete()  # ✅ Remove the appointment
        
        # ✅ Redirect to the professional dashboard instead of returning JSON
        return redirect('professional_dashboard')

    return redirect('professional_dashboard')

@login_required
def update_availability(request):
    professional = request.user.professional_profile

    if request.method == "POST":
        if "remove_slot" in request.POST:
            slot_to_remove = request.POST.get("remove_slot")
            if slot_to_remove in professional.available_slots:
                professional.available_slots.remove(slot_to_remove)
                professional.save()
                return JsonResponse({"message": "Slot removed successfully"}, status=200)

        if "new_slots" in request.POST:
            new_slot = request.POST.get("new_slots").strip()
            if new_slot and new_slot not in professional.available_slots:
                professional.available_slots.append(new_slot)
                professional.save()
                return JsonResponse({"message": "Slot added successfully"}, status=200)

    return render(request, "update_availability.html", {"professional": professional})

@login_required
def clear_notifications(request):
    request.user.notifications.all().delete()
    return redirect("professional_dashboard")

@csrf_exempt
def translate_view(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        target_language = request.POST.get("language", "en")  # Default to English

        if not text:
            return JsonResponse({"error": "No text provided"}, status=400)

        try:
            translator = Translator()
            translated = translator.translate(text, dest=target_language)

            logger.info(f"Translated text: {translated.text}")  # ✅ Debug log

            return JsonResponse({"translated_text": translated.text})
        except Exception as e:
            logger.error(f"Translation Error: {str(e)}")  # ✅ Log errors
            return JsonResponse({"error": str(e)}, status=500)

def translate_page(request):
    return render(request, 'translate.html')

# ✅ Use absolute import
from myapp.utils.email_utils import send_email_async

def some_function():
    from myapp.utils.email_utils import send_email_async  # ✅ Import inside function
    send_email_async("user@example.com", "Test Subject", "Hello World!")

from django.http import JsonResponse
from googletrans import Translator

def translate_text(text, target_language):
    """
    Function to translate text using Google Translate API or another translation method.
    """
    from googletrans import Translator  # Ensure googletrans is installed (`pip install googletrans==4.0.0-rc1`)
    
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    
    return translated.text


def settings_view(request):
    return render(request, 'settings.html') 
from django.shortcuts import render

def settings_professional(request):
    return render(request, 'settings_professional.html')


logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)

@login_required
def cancel_appointment_by_professional(request, appointment_id):
    """
    Allows a professional to cancel an appointment and notifies the user.
    """
    print(f"🔍 Attempting to cancel appointment {appointment_id} by {request.user.username}")  # ✅ Force print to server

    appointment = get_object_or_404(Appointment, id=appointment_id)

    # ✅ Ensure only the assigned professional can cancel the appointment
    if request.user != appointment.professional:
        messages.error(request, "You are not authorized to cancel this appointment.")
        print(f"❌ Unauthorized attempt by {request.user.username} to cancel appointment {appointment.id}")  # ✅ Force print
        return redirect("professional_dashboard")

    # ✅ Prevent re-canceling an already canceled/completed appointment
    if appointment.status != "Upcoming":
        messages.warning(request, "This appointment has already been canceled or completed.")
        print(f"⚠️ Attempt to cancel an already canceled appointment {appointment.id}")  # ✅ Force print
        return redirect("professional_dashboard")

    # ✅ Mark appointment as canceled
    with transaction.atomic():  # Ensure database consistency
        appointment.status = "Canceled"
        appointment.save()
        print(f"✅ Appointment {appointment.id} was successfully marked as canceled.")  # ✅ Force print

        # ✅ Ensure the client exists before creating a notification
        if appointment.client:
            print(f"🔔 Creating notification for {appointment.client.username}")  # ✅ Force print

            notification = Notification(
                recipient=appointment.client,
                message=f"🚨 Your appointment with {appointment.professional.username} on {appointment.date} at {appointment.time} was canceled."
            )
            notification.save(force_insert=True)  # Explicitly save the notification

            print(f"📌 [SUCCESS] Notification Created: {notification.message}")  # ✅ Force print
            messages.success(request, "Appointment canceled successfully. The user has been notified.")
        else:
            print(f"❌ [ERROR] No client assigned to appointment {appointment.id}")  # ✅ Force print
            messages.error(request, "Error: No client is assigned to this appointment.")

    return redirect("professional_dashboard")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Notification, Appointment  # Ensure Appointment model is imported

@login_required
def user_dashboard(request):
    """
    Displays the user dashboard with notifications and upcoming appointments.
    """
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')

    # Get upcoming appointments (Assuming there's a 'date' field in the Appointment model)
    upcoming_appointments = Appointment.objects.filter(
        user=request.user, date__gte=datetime.now()
    ).order_by('date')[:5]  # Get only the next 5 upcoming appointments

    return render(request, 'dashboard.html', {
        'notifications': notifications,
        'upcoming_appointments': upcoming_appointments
    })


@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by("-created_at").values("message", "created_at")

    return JsonResponse({"notifications": list(notifications)})


logger = logging.getLogger(__name__)  # Enable logging

@login_required
def clear_notificationsss(request):
    """
    Deletes all notifications for the logged-in user.
    """
    notifications = Notification.objects.filter(recipient=request.user)
    
    # Log before deletion
    logger.info(f"Attempting to delete {notifications.count()} notifications for user {request.user.username}")

    deleted_count, _ = notifications.delete()
    
    # Log after deletion
    logger.info(f"Deleted {deleted_count} notifications for user {request.user.username}")

    return JsonResponse({'success': True, 'message': 'Notifications cleared.'})


@login_required
def upload_quiz(request):
    if not request.user.is_superuser and not hasattr(request.user, "is_professional"):
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            quiz = Quiz.objects.create(title=data["title"], description=data["description"])

            for question in data["questions"]:
                Question.objects.create(
                    quiz=quiz,
                    text=question["text"],
                    options=question["options"],
                    correct_answer=question["correct_answer"]
                )

            return JsonResponse({"message": "Quiz uploaded successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)


def language_settings(request):
    """Render the language settings page."""
    return render(request, 'language_settings.html')

def change_language(request):
    """Change the language based on user selection."""
    if request.method == "POST":
        lang_code = request.POST.get('language', 'en')  # Default to English
        request.session['django_language'] = lang_code  # Store language in session
        activate(lang_code)  # Apply the selected language

        print(f"Language changed to: {lang_code}")  # Debugging statement
        print(f"Session language: {request.session.get('django_language')}")  # Verify session storage

    return redirect('dashboard')


def set_language(request, lang_code):
    """Set user language preference via URL."""
    if lang_code in ['en', 'fr', 'es']:  # Ensure valid language codes
        activate(lang_code)  # Apply the selected language
        request.session['django_language'] = lang_code  # Store in session
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Return to previous page

def about(request):
    return render(request, 'about.html')

@login_required
def available_slots(request):
    professionals = Professional.objects.all()  # Remove any invalid filtering

    for professional in professionals:
        professional.available_slots = [slot for slot in professional.available_slots if slot not in professional.booked_slots]

    return render(request, "available_slots.html", {"professionals": professionals})

@login_required
def quizzes(request):
    """Display quizzes and allow actions based on user role."""
    quizzes = Quiz.objects.all()
    
    # ✅ Check if user is a superuser or has a professional profile
    is_admin_or_professional = request.user.is_superuser or hasattr(request.user, 'professional_profile')

    return render(request, "quizzes.html", {
        "quizzes": quizzes, 
        "is_admin_or_professional": is_admin_or_professional
    })


@login_required
def upload_quiz(request):
    """Allow **both** superusers and professionals to upload a quiz."""
    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
        messages.error(request, "You are not authorized to upload quizzes.")
        return redirect('quizzes')

    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        question_forms = [QuestionForm(request.POST, prefix=str(i)) for i in range(3)]  # 3 question forms by default

        if quiz_form.is_valid() and all(q_form.is_valid() for q_form in question_forms):
            quiz = quiz_form.save()

            for q_form in question_forms:
                question = q_form.save(commit=False)
                question.quiz = quiz
                question.save()

            messages.success(request, "Quiz and questions uploaded successfully!")
            return redirect('quizzes')

    else:
        quiz_form = QuizForm()
        question_forms = [QuestionForm(prefix=str(i)) for i in range(3)]

    return render(request, 'upload_quiz.html', {
        'quiz_form': quiz_form,
        'question_forms': question_forms
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Quiz, Question
from .forms import QuizForm, QuestionForm  # Ensure QuestionForm is imported

def edit_quiz(request, quiz_id):
    """View to allow superusers and professionals to edit quizzes and their questions."""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)  # Fetch related questions

    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
        messages.error(request, "You are not authorized to edit quizzes.")
        return redirect('quizzes')

    if request.method == 'POST':
        quiz_form = QuizForm(request.POST, instance=quiz)
        question_forms = [QuestionForm(request.POST, instance=q, prefix=str(q.id)) for q in questions]

        if quiz_form.is_valid() and all(q_form.is_valid() for q_form in question_forms):
            quiz_form.save()

            for q_form in question_forms:
                q_form.save()

            messages.success(request, "Quiz and questions updated successfully!")
            return redirect('quizzes')

    else:
        quiz_form = QuizForm(instance=quiz)
        question_forms = [QuestionForm(instance=q, prefix=str(q.id)) for q in questions]

    return render(request, 'edit_quiz.html', {
        'quiz_form': quiz_form,
        'question_forms': question_forms,
        'quiz': quiz
    })


@login_required
def delete_quiz(request, quiz_id):
    """Allow **both** superusers and professionals to delete quizzes."""
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if not (request.user.is_superuser or hasattr(request.user, 'professional_profile')):
        messages.error(request, "You are not authorized to delete quizzes.")
        return redirect('quizzes')

    if request.method == "POST":
        quiz.delete()
        messages.success(request, "Quiz deleted successfully!")
        return redirect('quizzes')

    return render(request, 'confirm_delete.html', {'quiz': quiz})

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import QuizResult, Quiz

@login_required
def submit_quiz(request, quiz_id):
    if request.method == "POST":
        user = request.user
        quiz = Quiz.objects.get(id=quiz_id)
        data = request.POST

        # Calculate score
        total_questions = len(data.getlist("questions"))
        correct_answers = sum(1 for q in data.getlist("questions") if q in data.getlist("correct_answers"))
        percentage = (correct_answers / total_questions) * 100
        feedback = "🎉 Well done!" if percentage >= 70 else "❌ Try again!"

        # Save result to database
        result, created = QuizResult.objects.update_or_create(
            user=user, quiz=quiz,
            defaults={"score": correct_answers, "total_questions": total_questions, "feedback": feedback}
        )

        return JsonResponse({
            "message": "Quiz submitted successfully!",
            "percentage": percentage,
            "feedback": feedback,
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

def get_user_results(request):
    user = request.user
    results = QuizResult.objects.filter(user=user).select_related("quiz")

    user_results = {result.quiz.id: {
        "percentage": result.percentage,
        "feedback": f"Your Score: {result.percentage}%"
    } for result in results}

    return JsonResponse({"user_results": user_results})


@csrf_exempt
def save_user_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        quiz_id = data.get("quiz_id")
        score = data.get("score")
        percentage = data.get("percentage")

        quiz = Quiz.objects.get(id=quiz_id)

        result, created = QuizResult.objects.update_or_create(
            user=user, quiz=quiz,
            defaults={"score": score, "percentage": percentage}
        )

        return JsonResponse({"message": "Result saved", "percentage": percentage})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json

@csrf_exempt
def check_user_role(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Check user type from your user model
            # This depends on how you've implemented user roles in your system
            # For example, if you have a UserProfile model with a user_type field:
            user_type = user.userprofile.user_type if hasattr(user, 'userprofile') else 'user'
            
            return JsonResponse({
                'exists': True,
                'user_type': user_type
            })
        
        return JsonResponse({'exists': False})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)