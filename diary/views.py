from flask import Blueprint

# Create Blueprint
views = Blueprint('views', __name__)

#route
@views.route('/')
def home():
    return "<h1>home</h1>"