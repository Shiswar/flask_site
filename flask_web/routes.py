from flask import render_template, url_for, flash, redirect
from flask_web.forms import RegistrationForm, LoginForm
from flask_web.models import User, Post
from flask_web import app
import math, random, requests

#           Post template
#   {
#        'author': '',
#        'title': '',
#        'review': '',
#        'date': '',
#        'category':'',
#        'picture':''
#    }
#           Category template
#   {
#        'name':'',
#        'description':''
#    }



posts = [
    {
        'author': 'Shae Iswar',
        'title': 'Call of Duty: Warzone',
        'review': 'Warzone is a really good game that i really love and that is the end of this review....',
        'date': 'September 23 2020',
        'category':'BR',
        'picture':'static/warzone_thumb.jpg'
    },
    {
        'author': 'Shae Iswar',
        'title': 'Destiny 2',
        'review': 'I really like destiny 2 aswell because i pkay with my friends',
        'date': 'September 27 2020',
        'category':'MMORPG, FPS',
        'picture':'static/warzone_thumb.jpg'
    },
    {
        'author': 'Shae Iswar',
        'title': 'Destiny 2',
        'review': 'I really like destiny 2 aswell because i pkay with my friends',
        'date': 'September 27 2020',
        'category':'MMORPG, FPS',
        'picture':'static/warzone_thumb.jpg'
    },
    {
        'author': 'Shae Iswar',
        'title': 'Destiny 2',
        'review': 'I really like destiny 2 aswell because i pkay with my friends',
        'date': 'September 27 2020',
        'category':'MMORPG, FPS',
        'picture':'static/warzone_thumb.jpg'
    }
]

categories = [
    {
        'name':'Battle Royale',
        'description':'Drop in to a huge map with a hundred players, the aim of the game is to be the last man standing'
    },
    {
        'name':'RPG',
        'description':'Play the role of a hero or character and take part in a journey full of thrilling quests, epic battles and a whole lot of loot'
    },
    {
        'name':'FPS',
        'description':'First person shooter games usually come as fast paced, action shooters. Whether you are playing PvE or PvP, it is in your best interest to aim for the head'
    }

]



#word_response = requests.get("https://random-word-api.herokuapp.com//word?number=1")
#json_response = word_response.json()








@app.route("/")
@app.route("/game")
def game():
    return render_template('game.html', posts=posts, categories=categories)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Success! An account for {form.username.data} has been created', 'success')
        return redirect(url_for('game'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form= form)

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
