

from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)

def home(request):
    if 'ACCESS_TOKEN' in request.session:
        access_token = request.session['ACCESS_TOKEN']
        userinfo = request.session['USERINFO']
        return HttpResponse("""
        <p>access token={}</p>
        <p>Django username={}</p>
        <p>userinfo: <pre>{}</pre></p>
        """.format(access_token, request.user.username, userinfo))
    else:
        return HttpResponse("""
        <p>Not logged in!</p>
        <p>
            <a href="/auth/login">Login</a>
        </p>
        """)