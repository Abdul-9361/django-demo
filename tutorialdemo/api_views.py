from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import product

@csrf_exempt
def product_api(req):
    if req.method == "GET":
        prod=product.objects.all()

        data=[]

        for i in prod:
            data.append({
                'id':i.id,
                'name':i.name
            })
        return JsonResponse(data,safe=False)

    elif req.method=="POST":

        body=json.loads(req.body)

        prod=product.objects.create(
            name=body.get('name')
        )

        return JsonResponse({
            "message":"data created successfully",
            "list":{
                "id":prod.id,
                "name":prod.name
            }
        })

@csrf_exempt
def details(req,id):

    if req.method=="DELETE":
        prod=product.objects.get(id=id)
        prod.delete()
        return JsonResponse({
            "message":"data deleted successfully"
        })
