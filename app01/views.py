from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 整个执行的过程是，ajax传递参数给了函数ajax_demo，函数获取到用户键入的值，然后通过HttpResponse返回给回调函数success，回调函数再执行相应的操作
# def ajax_demo(request):
#     if request.method == 'POST':
#         user = request.POST.get('user')
#         pwd = request.POST.get('pwd')
#         print(user,pwd)
#         if user == '111' and pwd == '222':
#             return HttpResponse('1')
#         else:
#             return HttpResponse('2')
#     return render(request,'ajax_demo.html')

import json
def ajax_demo(request):
    if request.method == 'POST':
        ret = {'status':False,'message':''}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user == '111' and pwd == '222':
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(ret))
    return render(request,'ajax_demo.html')

def html(request):
    return render(request, 'ajax_demo.html')