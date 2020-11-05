from flask import Flask, render_template, request, session, redirect, url_for, g
import os
import string
import random
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

redirect_url = r'http://localhost:5000/get-code'
url_token = r"https://powerful-inlet-11533.herokuapp.com/auth"
access_token = None
name = None

USER_NAME = None
PASSWORD = None

def state_key():
    """
    Generate a random key.

    Args:
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits))


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    """
    Show the current page.

    Args:
    """
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['user'] = USER_NAME
            return redirect(url_for('profile'))

    if 'user' in session:
        return redirect(url_for('profile'))

    return render_template('index.html')


@app.route('/profile')
def profile():
    """
    Renders the user.

    Args:
    """
    if g.user:
        return render_template('profile.html', user_name=session['user']['name'])
    return redirect(url_for('index'))


@app.before_request
def auth_check():
    """
    Check if the user is authenticated

    Args:
    """
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/login')
def login():
    """
    Login to the login page.

    Args:
    """
    return redirect("https://www.facebook.com/v3.2/dialog/oauth?client_id={{" + CLIENT_ID + "}}&redirect_uri=" + redirect_url + "&state={\"{{ st_key }}\"}")


@app.route('/get-code', methods=['GET', 'POST'])
def get_code():
    """
    Get access token

    Args:
    """
    if 'code' in request.args:
        code = request.args.get('code')
        access_token = r'https://graph.facebook.com/v3.2/oauth/access_token?{{client_id=}}&redirect_uri=' + redirect_url + '&client_secret={{secret}}&code=' + code + ''
        contents = requests.get(access_token)
        access_token = contents.json()
        access_token = access_token.get('access_token')
        session['access_token'] = access_token
        return redirect(url_for('auth'))
    return '0'


def get_name(token):
    """
    Get the name of a user

    Args:
        token: (str): write your description
    """
    ver = requests.get(r'https://graph.facebook.com/debug_token?input_token=' + token + '&access_token={{}}')
    userid = ver.json()
    name = requests.get(r'https://graph.facebook.com/v3.2/' + userid['data']['user_id'] + '?access_token=' + token)

    return name.json().get('name')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    """
    Authenticate to the session.

    Args:
    """
    if 'access_token' in session:
        if 'user' not in session:
            session['user'] = {'name': get_name(session['access_token']), 'access_token': session['access_token']}
            return redirect(url_for('profile'))
    return 'No!'


@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    """
    Returns a list of the user - private key

    Args:
    """
    return 'App is only for an educational demonstration purpose.'


@app.route('/logout')
def logout():
    """
    Log out the user.

    Args:
    """
    if 'user' in session:
        session.pop('user')
        return 'Logged out!'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
