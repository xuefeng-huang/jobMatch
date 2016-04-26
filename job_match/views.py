#coding:utf-8
from django.shortcuts import render
from services import get_writer_score
from models import Writer


# score = 赞成比例 * min(投票数, 100)

def index(req):
    if req.method == 'POST':
        writer_list = Writer.objects.all()
        for writer in writer_list:
            writer.score = get_writer_score(writer)
            print writer.score
            
        # sort the list
        writer_list = list(writer_list)
        writer_list.sort(key=lambda writer : writer.score, reverse=True)
        for writer in writer_list:
            print writer.name, writer.score
        return render(req, 'match_writer.html', {'writer_list' : writer_list})
    return render(req, 'index.html', {})
