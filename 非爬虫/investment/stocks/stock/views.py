from  . import models
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
def stocks_all(request):

    if request.method == 'GET':
        content = {'msg': 'SUCCESS'}
        stock_list=list(models.stocks.objects.values())
        content['stocks']=stock_list
        print(stock_list)
        print(type(stock_list))

        return JsonResponse(data=content, status=status.HTTP_200_OK)

    return HttpResponseNotAllowed(permitted_methods=['GET'])


@csrf_exempt
def investment_all(request):

    if request.method == 'GET':
        content = {'msg': 'SUCCESS'}
        investment=[]

        inves_list=models.portfolio.objects.all()

        for inves in inves_list:
            temp = {}
            temp['tradeId']=inves.trade_id
            temp['investor']=inves.investor_id.name
            temp['stockName']=inves.ticker.ticker
            temp['price']=inves.price
            temp['num']=inves.num
            investment.append(temp)

        content['investment']=investment
        print(investment)
        response=JsonResponse(data=content, status=status.HTTP_200_OK)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    return HttpResponseNotAllowed(permitted_methods=['GET'])


@csrf_exempt
def stocks_add(request):
    print(request.POST)
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            print(data)
            if not 'ticker' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            if not 'company' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            if not 'stock_class' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)

            try:
                models.stocks.objects.update_or_create(ticker=data['ticker'],company=data['company'],stock_class=data['stock_class'])
            except:
                content['msg']='Add Failed'
                return JsonResponse(data=content, status=status.HTTP_200_OK)

            return JsonResponse(data=content, status=status.HTTP_200_OK)

    return HttpResponseNotAllowed(permitted_methods=['POST'])


@csrf_exempt
def investment_add(request):
    print(request.POST)
    if request.content_type != 'application/x-www-form-urlencoded':
        return HttpResponse('only support x-www-form-urlencoded data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    if request.method == 'POST':
        try:
            data = dict(request.POST)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            if not 'investor' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            if not 'num' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            if not 'price' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            if not 'stockName' in data:
                content['msg']='missing parameter!'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            print(data)
            try:
                investor=models.Investors.objects.get(investor_id=int(data['investor'][0]))
                ticker=models.stocks.objects.get(ticker=data['stockName'][0])
                models.portfolio.objects.update_or_create(ticker=ticker,price=int(data['price'][0]),num=int(data['num'][0]),investor_id=investor)
            except:
                raise
                content['msg']='Add Failed'
                respose=JsonResponse(data=content, status=status.HTTP_200_OK)
                response["Access-Control-Allow-Origin"] = "*"
                return respose

            response=JsonResponse(data=content, status=status.HTTP_200_OK)
            response["Access-Control-Allow-Origin"] = "*"
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response

    response = HttpResponseNotAllowed(permitted_methods=['POST'])
    response["Access-Control-Allow-Origin"] = "*"
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@csrf_exempt
def investment_del(request):
    print(request.POST)
    if request.content_type != 'application/x-www-form-urlencoded':

        print(request.content_type)
        response=HttpResponse('only support x-www-form-urlencoded data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        response["Access-Control-Allow-Origin"] = "*"
        response['Access-Control-Allow-Headers'] = "*"
        return response

    if request.method == 'POST':
        try:
        #     data = JSONParser().parse(request)

            data=request.POST
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            print(data)
            if not 'tradeId' in data:
                content['msg']='missing parameter!'
                print(2)
                response=JsonResponse(data=content, status=status.HTTP_200_OK)
                response["Access-Control-Allow-Origin"] = "*"
                response['Access-Control-Allow-Headers'] = 'Content-Type'
                return response

            try:
                tradeId=int(data['tradeId'])
                models.portfolio.objects.get(trade_id=tradeId).delete()
            except:
                raise
                content['msg']='delete Failed'
                return JsonResponse(data=content, status=status.HTTP_200_OK)
            response=JsonResponse(data=content, status=status.HTTP_200_OK)
            response["Access-Control-Allow-Origin"] = "*"
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response
    print(3)
    response=HttpResponseNotAllowed(permitted_methods=['POST'])
    response['Access-Control-Allow-Headers']='Content-Type'
    response["Access-Control-Allow-Origin"] = "*"
    return response