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
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
       return render (request, 'login.html')
    

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
    return render(request, 'contact.html') 

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

def professional_detail(request, pk):
    professional = get_object_or_404(Professional, pk=pk)
    return render(request, 'professional_detail.html', {'professional': professional})

    

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
from django.contrib.auth.decorators import login_required
from .models import Appointment, Professional
from datetime import datetime
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, Professional
from datetime import datetime

@login_required
def book_appointment(request):
    if request.method == "POST":
        professional_id = request.POST.get("professional")
        date = request.POST.get("date")
        time = request.POST.get("time")
        reason = request.POST.get("reason")

        # Convert time from "HH:MM AM/PM" to "HH:MM:SS"
        try:
            time_24hr = datetime.strptime(time, "%I:%M %p").strftime("%H:%M:%S")
        except ValueError:
            return render(request, "appointment_error.html", {"error": "Invalid time format."})

        professional = Professional.objects.get(id=professional_id)

        # Ensure the selected time is in the available slots
        if time_24hr not in professional.available_slots:
            return render(request, "appointment_error.html", {"error": "This slot is not available."})

        # Create the appointment
        Appointment.objects.create(
            user=request.user,
            professional=professional,
            date=date,
            time=time_24hr,  # Save in correct format
            reason=reason
        )

        # Remove booked slot from available slots (directly modifying the list)
        professional.available_slots.remove(time_24hr)
        professional.save()

        return redirect("appointment_success")

    return redirect("home")


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
        booked_slots = Appointment.objects.filter(professional=professional).values_list('time', flat=True)

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

def anonymous_chat(request):
    if request.method == "POST":
        message_content = request.POST.get("message")

        if message_content:  # ✅ Ensure message is not empty
            ChatMessage.objects.create(username="Anonymous", content=message_content)  # No room required
            return redirect("anonymous_chat")  # ✅ Refresh page after sending

    messages = ChatMessage.objects.order_by('-timestamp')  # ✅ Fetch all messages
    return render(request, "anonymous_chat.html", {"messages": messages})

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
    return render(request, "chat.html", {"messages": messages})
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
