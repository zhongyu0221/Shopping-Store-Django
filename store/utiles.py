import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['Cart'])
    return {}