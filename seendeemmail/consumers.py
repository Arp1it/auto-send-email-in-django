from channels.generic.websocket import AsyncWebsocketConsumer
from . models import *
import json
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model

User = get_user_model()

class FrontendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("frontend_updates", self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)

        title = data.get("title")
        message = data.get("message")
        reemail = data.get("recemail")
        sedate = data.get("sedate")

        usr_id = data.get("sende")
        usr = await sync_to_async(User.objects.get)(id=usr_id)
        print(usr)

        # Create and save the MailSender object asynchronously
        mail_sending = await sync_to_async(MailSender.objects.create)(
            cuser=usr, title=title, msg=message, receiveremail=reemail, sendingdate=sedate
        )

        mail_id = mail_sending.id

        payload = {"title": title, "msg": message, "reemail": reemail, "sedat": sedate, "mail_id": mail_id}
        print(payload)

        await self.channel_layer.group_send(
            f"frontend_updates", {
                "type": "send_message",
                'values': json.dumps(payload)
            }
        )

    async def send_message(self, text_data):
        data = json.loads(text_data.get("values"))
        print(data)
        await self.send(text_data=json.dumps({"payloads": data}))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("frontend_updates", self.channel_name)

    async def data_deleted(self, event):
        await self.send(text_data=str(event["data"]))