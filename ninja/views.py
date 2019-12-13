from django.shortcuts import render
from random import randint
from time import gmtime, strftime
# Create your views here.

def index(request):
    request.session['totalGold'] = 0
    request.session['activityLog'] = []

    context = {
        "totalGold" : request.session['totalGold'],
        'activityLog' : request.session['activityLog']
        }

    return render(request,'index.html',context)


def updateGold(request,place):

    value =  {
        'farm' : {
                    "min" : 0,
                    "max" : 20
                 },
        'cave' :{
                    "min" : 5 ,
                    "max" : 10
                },
        'house' : {
                    "min" : 2,
                    "max" : 5
                 },
        'casino' : {
                    "min" : -50,
                    "max" : 20
                 },
    }

    randNum = randint(value[place]['min'],value[place]['max'])
    timeStamp = strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['totalGold'] = int(request.session['totalGold']) + randNum
    if request.session['totalGold'] < 0:
        request.session['totalGold'] = 0

    if randNum <0:
        request.session['activityLog'].append(f"Entered a place and lost {abs(randNum)} golds...Ouch... ({timeStamp})")
    else:
        request.session['activityLog'].append(f"Earned {randNum} from the {place} ({timeStamp})")

    
    context = {
        "totalGold" : request.session['totalGold'],
        "activityLog" : request.session['activityLog']
        }
    return render(request,'index.html')



# def goCave(request):

# def goHouse(request):

# def goCasino(request):