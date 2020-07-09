from gameApp.models import Game
import json
from django.http import JsonResponse
def putsource(request):
    if request.method=="GET":
        return JsonResponse({"code":200,"error":0,"message":"please use post method to insert value!"})
    if request.method=="POST":
        #print(request.body)
        g_client=request.POST.get("g_client")
        if g_client is None:
            return JsonResponse({"code":300,"message":"client must be not null"})
        try:
            g_score=int(request.POST.get("g_score"))
        except:
            return JsonResponse({"code":300,"message":"score must be int"})
        if g_score<1 or g_score>10000000:
            return JsonResponse({"code":300,"message":"score must between (1,10000000)"})
        if len(Game.objects.filter(g_client=g_client).values())==0:
            g_data=Game(g_client=g_client,g_score=g_score)
            g_data.save()
            return JsonResponse({"code":201,"data":" %s %sinsert sucess!"%(g_client,g_score)})
        else:
            Game.objects.filter(g_client=g_client).update(g_score=g_score)
            return JsonResponse({"code":201,"data":" %s %supdate sucess!"%(g_client,g_score)})
def getrank(request):
    if request.method=="GET":
        return JsonResponse({"code":200,"error":0,"message":"please use post method to insert value!"})
    if request.method=="POST":
        #print(request.body)
        g_client=request.POST.get("g_client")
        g_start=request.POST.get("g_start")
        g_end=request.POST.get("g_end")
        print(g_client,g_start,g_end)
        if g_end<g_start or g_client is None or g_start.isdigit() is False or g_end.isdigit() is False or Game.objects.filter().count()<int(g_end):
            return JsonResponse({"code":300,"message":"please input correct value"})
        g_datas=list(Game.objects.filter().order_by("-g_score")[int(g_start)-1:int(g_end)].values('g_client','g_score'))
        if len(Game.objects.filter(g_client=g_client).values())!=0:
            g_datas.append(Game.objects.filter(g_client=g_client).values('g_client','g_score')[0])
        else:
            g_datas.append({'g_client': g_client, 'g_score': "you don't have score"})
        return JsonResponse({"code":200,"reponse_data":"%s"%str(g_datas)})

