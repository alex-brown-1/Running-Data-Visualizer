from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
import seaborn as sns
from website.data_finder import get_data
from website.parse_data import parse_data
from website.data_visualizer import visualize_data

views = Blueprint("views", __name__)


@views.route('/')
def homepage():
    return render_template("home.html")


@views.route("/running_data", methods=["POST"])
def form_response():
    code = request.form["codeInput"]
    activities, token = get_data(code)
    df = parse_data(activities, token)
    
    return render_template("data.html", tables=[activities.to_html(classes='data')], titles=activities.columns.values)
