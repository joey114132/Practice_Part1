from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    html = """
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Gloock&display=swap" rel="stylesheet">
        <title>🎬 영화 추천</title>
        <style>
            body { font-family: 'Gloock', serif; padding: 2em; }
            .container {display: flex;flex-direction: column;align-items: center; gap: 1.5em; margin-top: 2em;}
            .movie { border: 1px solid #ccc; padding: 1em; margin-bottom: 1em; border-radius: 10px; text-align: center; width: 100%; max-width: 600px;}
            .title { font-size: 1.5em; font-weight: bold; }
            .genre { color: gray;}
            .description { margin-top: 0.5em; }
            .btn { margin-top: 1em; display: inline-block; padding: 0.5em 1em; background: linear-gradient(90deg, black, white,black); color: black; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">🎬 오늘의 영화 추천</h1>
        <div class = "container">
            <div class="movie">
                <div class="title">인터스텔라</div>
                <div class="genre">장르: SF, 드라마</div>
                <div class="description">우주를 배경으로 한 아버지의 위대한 사랑과 모험 이야기.</div>
                <a href="https://namu.wiki/w/%EC%9D%B8%ED%84%B0%EC%8A%A4%ED%85%94%EB%9D%BC" class="btn" target="_blank">추천하기</a>
            </div>

            <div class="movie">
                <div class="title">기생충</div>
                <div class="genre">장르: 드라마, 스릴러</div>
                <div class="description">상류층과 하류층의 현실을 꼬집는 블랙코미디 영화.</div>
                <a href="https://namu.wiki/w/%EA%B8%B0%EC%83%9D%EC%B6%A9(%EC%98%81%ED%99%94)" class="btn" target="_blank">추천하기</a>
            </div>

            <div class="movie">
                <div class="title">토이 스토리</div>
                <div class="genre">장르: 애니메이션, 가족</div>
                <div class="description">장난감들의 유쾌한 우정과 모험 이야기.</div>
                <a href="https://namu.wiki/w/%ED%86%A0%EC%9D%B4%20%EC%8A%A4%ED%86%A0%EB%A6%AC" class="btn" target="_blank">추천하기</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)