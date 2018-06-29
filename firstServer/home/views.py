from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests
def keyboard(request):
        return JsonResponse(
            {
                "type" : "buttons",
                "buttons" : ["선택 1", "선택 2", "선택 3"]
            }
        )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] 

    if return_str == '선택 1':
        return JsonResponse(
            { 
            "message": {
                "text": "안녕하십니까~~~"
            }
        }
        )
    if return_str == '선택 2':
        return JsonResponse(
            { 
            "message": {
                "text": "너가 원하는건 뭘까요~~~ "
            }
        }
        )
    if return_str == '선택 3':
        return JsonResponse(
            { 
            "message": {
                "text":"그걸 내가 알면 무당을 했죠~~~"
            }
        }
        )

