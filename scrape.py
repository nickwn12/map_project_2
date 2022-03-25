from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import datetime
import enum
import imp
import math
import pickle
import time
from os import stat
import numpy as np
import pandas as pd
import selenium
from selenium import webdriver


def getStatesData(headless=False):
    chrome_options = Options()
    if(headless):
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.dol.gov/agencies/whd/state/minimum-wage/history")
    

getStatesData()