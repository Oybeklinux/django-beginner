from django.http import HttpResponse
from django.shortcuts import render
from .db import news
# Create your views here.
def yangiliklar(request):
    return render(request, "yangiliklar/news.html")


def ozgartirish(request):
     return render(request, "yangiliklar/news_edit.html")

def yangilik(request, id):
    if id > 0 and id < 4:
        yangilklar_ = [
            """<div class=item style="display:flex;width:900px;margin:40px auto"><div class=left style=margin-right:20px><img height=150; src=https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455_960_720.jpg width=300></div><div class=right><h2>Lorem ipsum dolor sit.</h2><b>23.02.2021</b><p class=text>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse mollitia aliquid quisquam amet non ipsum provident fuga consectetur sunt doloremque.</div></div>""",
            """<div class=item style="display:flex;width:900px;margin:40px auto"><div class=left style=margin-right:20px><img height=150; src=https://myrepublica.nagariknetwork.com/uploads/media/nature_20210209150332.jpeg width=300></div><div class=right><h2>Lorem ipsum dolor sit.</h2><b>23.02.2021</b><p class=text>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse mollitia aliquid quisquam amet non ipsum provident fuga consectetur sunt doloremque.</div></div>""",
            """<div class=item style="display:flex;width:900px;margin:40px auto"><div class=left style=margin-right:20px><img height=150; src=https://myrepublica.nagariknetwork.com/uploads/media/dfdfdfdfd_20210928153823.jpg width=300></div><div class=right><h2>Lorem ipsum dolor sit.</h2><b>23.02.2021</b><p class=text>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse mollitia aliquid quisquam amet non ipsum provident fuga consectetur sunt doloremque.</div></div>"""
        ]

        return HttpResponse( yangilklar_[id-1])
    else:
        return HttpResponse("Bunday yangilik mavjud emas")

class Talaba:


    def __init__(self) -> None:
        self.name = "Anvar"
        self.age = 45

def ozgaruvchi_bilan_ishlash(request, son):
    
    context = {
        "sarlavha": "O'zgaruvchilar bilan ishlash",
        "lst": news,        
       
        }
    return render(request, "yangiliklar/test.html", context )


