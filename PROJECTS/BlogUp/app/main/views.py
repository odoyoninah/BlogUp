from flask import render_template, flash, redirect, url_for, request

from app.main.forms import PostForm
from app.models import Post

from . import main

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/home')
def home():
    posts = Post.query.all()
    
    return render_template('home.html', posts = posts)


@main.route('/post', methods=['GET', 'POST'])
def post():
    title = 'Post Form'
    postform = PostForm()
    if postform.validate_on_submit():
        post = Post(title=postform.title.data, author=postform.author.data, post=postform.post.data)
        post.save_post()


        flash('Post created successfully!')
        return redirect(url_for('main.home'))



    return render_template('post.html',title=title, postform=postform)






