from flask import Blueprint, render_template, request

import pyrebase
import json

import random

db = Blueprint('db' , __name__)

config = {
 "apiKey": "AIzaSyAtsPSQN0aF3krFKkEexQjvaTU5H03Jxdg",
  "authDomain": "imaimaindb.firebaseapp.com",
  "databaseURL": "https://imaimaindb-default-rtdb.firebaseio.com",
  "projectId": "imaimaindb",
  "storageBucket": "imaimaindb.appspot.com",
  "messagingSenderId": "633750202756",
  "appId": "1:633750202756:web:21903b32ae9c116af655d1"
}

firebase = pyrebase.initialize_app(config)
data_base = firebase.database()
#db연결
@db.route('/db', methods=['GET'])
def data():
    gender = request.args.get('gender')
    shorder = request.args.get('shorder')
    chet = request.args.get('chet')
    body = request.args.get('body')
    hight = request.args.get('hight')
    shorder = int(shorder)
    chet = int(chet)
    body = int(body)
    hight = int(hight)

    shorder /= 10
    chet /= 10
    body = body / 10 + 30

    S_s = 49
    S_m = 51
    S_l = 54
    S_xl = 56

    C_s = 52
    C_m = 55
    C_l = 58
    C_xl = 60

    B_s = 68
    B_m = 71
    B_l = 73
    B_xl = 75
    
    ##사용자가 해당하는 치수에 count++
    S_count = 0
    M_count = 0
    L_count = 0
    XL_count = 0

    ##user_size는 최종 출력
    total = 0
    user_size = ""

    ##shorder 사이즈
    if shorder <= S_s:
        user_shorder = "S"
    elif shorder > S_s and shorder <= S_m:
        user_shorder = "M"
    elif shorder > S_m and shorder <= S_l:
        user_shorder = "L"
    elif shorder > S_l:
        user_shorder = "XL"


    ##chet 사이즈
    if chet <= C_s:
        user_chet = "S"
    elif chet > C_s and chet <= C_m:
        user_chet = "M"
    elif chet > C_m and chet <= C_l:
        user_chet = "L"
    elif chet > C_l:
        user_chet = "XL"
        
        
    ##body 사이즈
    if body <= B_s:
        user_body = "S"
    elif body > B_s and body <= B_m:
        user_body = "M"
    elif body > B_m and body <= B_l:
        user_body = "L"
    elif body > B_l:
        user_body = "XL"


    ##어깨치수 카운트
    if user_shorder == "S":
        S_count += 1
    elif user_shorder == "M":
        M_count += 1
    elif user_shorder == "L":
        L_count += 1
    else:
        XL_count += 1

    ##가슴치수 카운트
    if user_chet == "S":
        S_count += 1
    elif user_chet == "M":
        M_count += 1
    elif user_chet == "L":
        L_count += 1
    else:
        XL_count += 1
        
            ##총장치수 카운트
    if user_body == "S":
        S_count += 1
    elif user_body == "M":
        M_count += 1
    elif user_body == "L":
        L_count += 1
    else:
        XL_count += 1

    ##사용자 사이즈
    if total < S_count:
        total = S_count
        user_size = "S"
    if total < M_count:
        total = M_count
        user_size = "M"
    if total < L_count:
        total = L_count
        user_size = "L"
    if total < XL_count:
        total = XL_count
        user_size = "XL"
        
            #male
    if gender == "male" and user_size == "S":
        form = "thin"
    elif gender == "male" and user_size == "M" and hight >= 183:
        form = "hfat"
    elif gender == "male" and user_size == "M":
        form = "normal"
    elif gender == "male" and user_size == "L" and hight >= 183:
        form = "hfat"
    elif gender == "male" and user_size == "L" and hight <= 163:
        form = "fat"
    elif gender == "male" and user_size =="L":
        form = "bfat"

    #female
    if gender == "female" and user_size == "S":
        form = "thin"
    elif gender == "female" and user_size == "M" and hight >= 170:
        form = "bfat"
    elif gender == "female" and user_size == "M":
        form = "normal"
    elif gender == "female" and user_size == "L" and hight >= 170:
        form = "normal"
    elif gender == "female" and user_size == "L":
        form = "fat"



    num = random.randrange(1,11)
    user_top = data_base.child(gender).child(form).child(num).child("top").get().val()
    user_pants = data_base.child(gender).child(form).child(num).child("pants").get().val()
    return render_template("costest.html", top = user_top, pants = user_pants)

#routes.py
#요청