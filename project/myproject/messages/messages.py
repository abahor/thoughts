from flask import Blueprint, render_template, url_for, redirect, abort
from myproject.models import Users

messages = Blueprint('messages',__name__,template_folder='temp')

@messages.route('/')
