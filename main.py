import win32com.client as wincl
import json
import requests
import urllib3
import random
from urllib3.exceptions import InsecureRequestWarning
import re
import sys
import time
import os
from google.cloud import speech_v1 as speech
import pyaudio
from six.moves import queue

urllib3.disable_warnings(InsecureRequestWarning)