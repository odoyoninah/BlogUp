from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Post

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    post = StringField('Post', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_title(self, title):
        post = Post.query.filter_by(title=title.data).first()
        if post:
            raise ValidationError('Title already exists. Please choose a different title.')

    def validate_author(self, author):
        post = Post.query.filter_by(author=author.data).first()
        if post:
            raise ValidationError('Author already exists. Please choose a different author.')

    def validate_post(self, post):
        post = Post.query.filter_by(post=post.data).first()
        if post:
            raise ValidationError('Post already exists. Please choose a different post.')

    

