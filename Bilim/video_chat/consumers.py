from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import ChatMessage, Group_chat
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Validate room_name
        try:
            self.group_chat = await sync_to_async(Group_chat.objects.get)(group_name=self.room_name)
        except Group_chat.DoesNotExist:
            await self.close()  # Close connection if the group does not exist
            return

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send past messages
        past_messages = await self.get_past_messages(self.room_name)
        for msg in past_messages:
            await self.send(text_data=json.dumps({
                'message': msg['message'],
                'username': msg['username'],
                'send_time': msg['send_time']
            }))

    @sync_to_async
    def get_past_messages(self, room_name):
        try:
            group_chat = Group_chat.objects.get(group_name=room_name)
        except Group_chat.DoesNotExist:
            return []

        messages = ChatMessage.objects.filter(room_name=group_chat).order_by('send_time')
        return [
            {
                'message': msg.message,
                'username': msg.sender.username,
                'send_time': msg.send_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            for msg in messages
        ]

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username  # Assuming user is authenticated

        await self.save_message(self.room_name, self.scope['user'], message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, room_name, username, message):
        try:
            group_chat = Group_chat.objects.get(group_name=room_name)
        except Group_chat.DoesNotExist:
            return

        chat = ChatMessage(
            room_name=group_chat,
            sender=username,
            message=message
        )
        chat.save()
