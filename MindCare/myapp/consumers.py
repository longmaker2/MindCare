from channels.generic.websocket import AsyncWebSocketConsumer  # Fix Typo (Capital 'S' in WebSocket)
import json
from django.utils.timezone import now
from myapp.models import Appointment, Message, Notification

class DashboardConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        self.group_name = "dashboard_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("type")

        if event_type == "fetch_updates":
            await self.send_updates()

    async def send_updates(self):
        upcoming_appointments = list(Appointment.objects.filter(
            status='Upcoming',
            date__gte=now().date()
        ).order_by('date', 'time').values('client__username', 'date', 'time'))

        messages = list(Message.objects.all().order_by('-timestamp').values('sender__username', 'content', 'timestamp'))
        notifications = list(Notification.objects.all().order_by('-created_at').values('message', 'created_at'))

        await self.send(text_data=json.dumps({
            'appointments': upcoming_appointments,
            'messages': messages,
            'notifications': notifications
        }))
