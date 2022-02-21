from django.shortcuts import render
import math

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    return response


def inputForm(request):
    print(request.POST)
    # return render(request,'formula.html')
    if 'form1' in request.POST['form']:
        if "easy" in request.POST['title']:
            return render(request,'easyship.html')
        elif "self" in request.POST['title']:
            return render(request,'selfship.html')
        elif "FBA" in request.POST['title']:
            return render(request,'fba.html')
        else:
            return render(request,'nodata.html')

def result(request):
    print(request.POST)
    section = request.POST['section']
    Price = float(request.POST['Price'])



    if section == "easy":
        Weight = int(request.POST['Weight'])
        Shipping = request.POST['Shipping']

        # Referrel Fee:
        # 10%
        if Price > 0:
            referrelFee = Price * 0.05
        else:
            referrelFee = 0

        # Closing Fee:
        if Price > 0  and Price <=250:
            closingFee = 5
        elif Price >=251  and Price <=500:
            closingFee = 9
        elif Price >= 501  and Price <=1000:
            closingFee = 30
        elif Price >1000:
            closingFee = 56
        else:
            closingFee = 0
        
        # Shipping Fee:
        if Shipping == 'Local':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 40
            elif Weight >500 and Weight <=1000:
                shippingCost = 40 + 13
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 40 + 13 + (15*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 40 + 13 + (15*6) + (8*dummyVaue)

        if Shipping == 'Regional':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 51
            elif Weight >500 and Weight <=1000:
                shippingCost = 51 + 17
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 51 + 17 + (21*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 51 + 17 + (21*6) + (9*dummyVaue)

        if Shipping == 'National':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 72
            elif Weight >500 and Weight <=1000:
                shippingCost = 72 + 25
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 72 + 25 + (27*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 72 + 25 + (27*6) + (12*dummyVaue)
        
        TotalAmazonCharges = referrelFee + closingFee + shippingCost
        Profit = Price - TotalAmazonCharges
        return render(request,'result.html',{'referrelFee':referrelFee,'closingFee':closingFee,'shippingCost':shippingCost,'TotalAmazonCharges':TotalAmazonCharges,'Profit':Profit,'section':section})

    elif section == "self":
        Packing = int(request.POST['Packing'])
        Shipping = int(request.POST['Shipping'])

        # Referrel Fee:
        # 10%
        if Price > 0:
            referrelFee = Price * 0.05
        else:
            referrelFee = 0

        # Closing Fee:
        if Price > 0  and Price <=250:
            closingFee = 7
        elif Price >=251  and Price <=500:
            closingFee = 20
        elif Price >= 501  and Price <=1000:
            closingFee = 36
        elif Price >1000:
            closingFee = 65
        else:
            closingFee = 0

        TotalAmazonCharges = referrelFee + closingFee + Shipping + Packing
        Profit = Price - TotalAmazonCharges
        return render(request,'result.html',{'referrelFee':referrelFee,'closingFee':closingFee,'shippingCost':Shipping,'TotalAmazonCharges':TotalAmazonCharges,'Profit':Profit,'section':section})
        # Karthi
        # Devi
 
    elif section == "FBA":
        Weight = int(request.POST['Weight'])
        Shipping = request.POST['Shipping']

        
        # Referrel Fee:
        # 5%
        if Price > 0:
            referrelFee = Price * 0.05
        else:
            referrelFee = 0

        # Closing Fee:
        if Price > 0  and Price <=250:
            closingFee = 12
        elif Price >=251  and Price <=500:
            closingFee = 12
        elif Price >= 501  and Price <=1000:
            closingFee = 18
        elif Price >1000:
            closingFee = 35
        else:
            closingFee = 0
            
        # Shipping Fee:
        if Shipping == 'Local':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 29
            elif Weight >500 and Weight <=1000:
                shippingCost = 29 + 13
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 29 + 13 + (15*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 29 + 13 + (15*6) + (8*dummyVaue)

        if Shipping == 'Regional':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 40
            elif Weight >500 and Weight <=1000:
                shippingCost = 40 + 17
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 40 + 17 + (21*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 40 + 17 + (21*6) + (9*dummyVaue)

        if Shipping == 'National':
            # upto 500gms:
            if Weight <=500:
                shippingCost = 61
            elif Weight >500 and Weight <=1000:
                shippingCost = 61 + 25
            elif Weight >1000 and Weight <=5000:
                dummyVaue = math.ceil((Weight - 1000)/500)
                shippingCost = 61 + 25 + (27*dummyVaue)
            elif Weight >5000:
                dummyVaue = math.ceil((Weight - 5000)/500)
                shippingCost = 61 + 25 + (27*6) + (12*dummyVaue)

        # Pick & Pack Fee:
        pickpackFee = 11

        TotalAmazonCharges = referrelFee + closingFee + shippingCost + pickpackFee
        Profit = Price - TotalAmazonCharges
        return render(request,'result.html',{'referrelFee':referrelFee,'closingFee':closingFee,'shippingCost':shippingCost,'TotalAmazonCharges':TotalAmazonCharges,'packFee':pickpackFee,'Profit':Profit,'section':section})

    return render(request,'result.html')
