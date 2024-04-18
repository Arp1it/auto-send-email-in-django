from channels.generic.websocket import AsyncWebsocketConsumer

class FrontendConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("frontend_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("frontend_updates", self.channel_name)

    async def data_deleted(self, event):
        await self.send(text_data=str(event["data"]))