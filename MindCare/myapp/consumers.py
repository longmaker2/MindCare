import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now
from .models import AnonymousPrivateMessage
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """ Accept WebSocket connection """
        await self.channel_layer.group_add("chat_room", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """ Remove user from chat group """
        await self.channel_layer.group_discard("chat_room", self.channel_name)

    async def receive(self, text_data):
        """ Handle incoming messages """
        data = json.loads(text_data)
        sender = data["sender"]
        recipient = data["recipient"]
        message_content = data["message"]
        timestamp = now().strftime("%Y-%m-%d %H:%M:%S")

        # ✅ Save message to database
        await sync_to_async(AnonymousPrivateMessage.objects.create)(
            sender=sender,
            recipient=recipient,
            content=message_content,
            timestamp=now()
        )

        # ✅ Broadcast message to all clients
        await self.channel_layer.group_send(
            "chat_room",
            {
                "type": "chat_message",
                "sender": sender,
                "recipient": recipient,
                "message": message_content,
                "timestamp": timestamp,
            },
        )

    async def chat_message(self, event):
        """ Send the message to WebSocket clients """
        await self.send(text_data=json.dumps(event))
