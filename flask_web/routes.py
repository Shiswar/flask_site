from flask import render_template, url_for, redirect, request, flash
from flask_web.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flask_web.models import User, Post
from flask_web import app,db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import math, random, requests, secrets, os
from PIL import Image

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
    posts = Post.query.all()
    return render_template('game.html', posts=posts, categories=categories)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('game'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Success! An account for {form.username.data} has been created! You can now log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('game'))
    form = LoginForm()
    if form.is_submitted():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
             
            return redirect(next_page) if next_page else redirect(url_for('game'))    
        elif not user:
            flash('Login unsuccessful. Account not found, please register.', 'danger')
            print("elif")
        else:
            flash('Login unsuccessful. Please check your password', 'danger')  
    return render_template('login.html', title='Login', form= form)

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('game'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (150, 150)

    im = Image.open(form_picture)
    im.thumbnail(output_size)

    im.save(picture_path)
    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('account.html', title='Account', image_file = image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()

        flash('Post has been created!', 'success')
        return redirect(url_for('game'))
    return render_template('create_post.html', title='New Post', legend='New Post', form = form)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update",methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', legend='Update Post',form = form)

@app.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('game'))