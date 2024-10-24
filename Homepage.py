from flask import Blueprint, render_template
from flask import Flask,render_template
from tensorflow import keras
from keras import layers
import numpy as np
import tensorflow as tf
from Wetter import simpleai


homepage = Blueprint('Homepage', __name__)


@homepage.route('/')
def Start():
    return  "<h1>Home</h1>"
@homepage.route('/Ai')
def start(name=None):
    Ai = simpleai()
    return simpleai()




