# booking

```python
from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def available_hours(self):
        bookings = self.booking_set.all()  # Assuming a related name of 'booking_set' for the Booking model
        booked_hours = set()

        # Collect booked hours
        for booking in bookings:
            booked_hours.update(range(booking.timeslot.start_time.hour, booking.timeslot.end_time.hour + 1))

        # Calculate available hours
        all_hours = set(range(self.start_time.hour, self.end_time.hour + 1))
        available_hours = all_hours - booked_hours

        return list(available_hours)

    def get_available_timeslots(self):
        available_hours = self.available_hours()
        available_timeslots = []

        # Create a list of available timeslots based on available hours
        for hour in available_hours:
            start_time = timezone.make_aware(datetime.datetime(self.start_time.year, self.start_time.month, self.start_time.day, hour))
            end_time = start_time + timedelta(hours=1)
            available_timeslots.append({'start_time': start_time, 'end_time': end_time})

        return available_timeslots

```

# Video chat

Install required packages

```bash
pip install channels channels-redis
```

Configure Django settings
```python
# settings.py

INSTALLED_APPS = [
    # ...
    'channels',
    'video',
]

# Use channels layer as the default backend for Django.
ASGI_APPLICATION = 'videostream.asgi.application'

# Redis as the channels layer backend.
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

Create a consumers.py file in the video app:

```python
# video/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
```

Create a routing.py file in the video app:
```python
# video/routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<room_name>\w+)/$', consumers.VideoConsumer.as_asgi()),
]
```

Create an asgi.py file in the project root
```python
# videostream/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from video.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videostream.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

Update your routing.py to include the consumer
```python
# videostream/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from video.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

Create a view in your views.py to render the HTML template
```python
# video/views.py

from django.shortcuts import render

def video_stream(request, room_name):
    return render(request, 'video/stream.html', {
        'room_name': room_name
    })
```

Create a template stream.html
```html
<!-- video/templates/video/stream.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Video Stream</title>
</head>
<body>
    <script>
        const roomName = "{{ room_name }}";
        const socket = new WebSocket(`ws://${window.location.host}/ws/video/${roomName}/`);

        socket.onmessage = function(event) {
            const message = event.data;
            // Handle the received message, e.g., update the video element.
        };
    </script>
</body>
</html>
```

Update your urls.py to include the new view
```python
# video/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('video/<str:room_name>/', views.video_stream, name='video_stream'),
]
```

Add the video app URLs to your project's urls.py
```python
# videostream/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video.urls')),
]

```