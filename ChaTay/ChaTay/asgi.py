"""
ASGI config for ChaTay project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

#import os
#from channels.routing import ProtocolTypeRouter
#from django.core.asgi import get_asgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChaTay.settings')

#application =ProtocolTypeRouter(
#    {
 #       "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
  #  }
#) 

# mysite/asgi.py
# real_time_chat/asgi.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
