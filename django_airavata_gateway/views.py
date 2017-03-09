

from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

def home(request):
    access_token = request.session['ACCESS_TOKEN']
    if access_token:
        return HttpResponse("access token {}, username {}".format(access_token, request.user.username))
    else:
        return HttpResponse("Not logged in!")