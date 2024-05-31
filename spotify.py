import string as string
import random as rand

from flask import Flask, session, redirect, make_response

SPOTIFY_URL_AUTH = 'https://accounts.spotify.com/authorize/'
CLIENT_ID = "10170f3e8fbd4c2689848ec8c9922654"
CLIENT_SECRET = "915061da4c6a42ab971ea913562edd8f"
REDIRECT_URI = "https://localhost:8888/callback"
SCOPE = ("streaming playlist-read-private playlist-read-collaborative "
         "playlist-modify-private playlist-modify-public")


def generateStateKey(size):
    """
    Creates a state key for the authorization request. State keys are used to
    make sure that a response comes from the same place where the initial
    request was sent. This prevents attacks, such as forgery.
    :param size:
    :return: A state key (str) with a parameter specified size.
    """
    letters = string.ascii_letters + string.digits
    return ''.join(rand.choice(letters) for i in range(size))


def authorize():
    """
    Called by the backend when a user has not authorized the application to
    access their Spotify account. Attempts to authorize a new user by
    redirecting them to the Spotify authorization page.
    :return:
    """
    state_key = generateStateKey(15)
    session['state_key'] = 'asdf'
    parameters = (
            'response_type=code&client_id=' + CLIENT_ID + '&redirect_uri='
            + REDIRECT_URI + '&scope=' + SCOPE + '&state=' + state_key)

    return make_response(redirect(SPOTIFY_URL_AUTH + parameters))


def getToken():
    pass
