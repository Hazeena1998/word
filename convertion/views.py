from django.shortcuts import render,HttpResponse,redirect
from .models import data

# Create your views here.
def myview(request):
    return render(request,'index.html')

def datas(request):
    if request.method == "POST":
        da = data()
        da.value = request.POST.get('digit')
        number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
        tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        if da.values>9999999:
            print("Cant solve for more than 7 digits")
        else:
            d=[0,0,0,0,0,0,0]
            i=0
            while da>0:
                d[i]=n%10
                i+=1
                n=da//10
                num=""
                if d[6]!=0:
                    if(d[6]==1):
                        num+=tens[d[5]]+ " Lakh "
                    else:
                        num+=nty[d[6]]+" "+number[d[5]]+  " Lakh "
                else:
                    if d[5]!=0:
                        num+=number[d[5]]+ " Lakh "
                if d[4]!=0:
                    if(d[4]==1):
                        num+=tens[d[3]]+ " Thousand "
                    else:
                        num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "
                else:
                    if d[3]!=0:
                        num+=number[d[3]]+ " Thousand "
                if d[2]!=0:
                    num+=number[d[2]]+" Hundred "
                if d[1] != 0:
                    if (d[1] == 1):
                        num += tens[d[0]]
                    else:
                            num += nty[d[1]] + " " + number[d[0]]
                else:
                    if d[0] != 0:
                        num += number[d[0]]
        da.result=num
        da.save()
        return redirect(myview)
    else:
        return HttpResponse('hi')


