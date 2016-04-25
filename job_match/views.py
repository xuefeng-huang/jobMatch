#coding:utf-8
from django.shortcuts import render


# score = 赞成比例 * min(投票数, 100)

def index(req):
    if req.method == 'POST':
        
    return render(req, 'index.html', {})
