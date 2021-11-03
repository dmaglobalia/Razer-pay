from django.shortcuts import render

# Create your views here.
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import pay


def home(request):
    if request.method == 'POST' :
        data = request.POST.get("pay")

        print("++++++++++++++++++++++++++++++",data)
    return render(request,'one/home.html')


def paya(request):

    database = pay.objects.get(pk = 7) 
                                                                    ####
    print("############################ id = ",database)            ####

    if request.method == "POST":
        name = request.POST.get('name')
           
        amount = 500                                                ####

        client = razorpay.Client(
            auth=("rzp_test_QBZ8PD02nTPnoy","8yUZOwFm7GQe0i3IwMSnlCe9"))
                            
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request,'one/payment.html',{'amount':database})


@csrf_exempt
def success(request):

    return render(request, "one/success.html")
 