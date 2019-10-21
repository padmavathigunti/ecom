from django.shortcuts import render,HttpResponse,redirect
from .models import Product_field, User_field, Buyed_product, buyed
# Create your views here.




def product_field(request):
    if request.method == 'POST':
        Product_name = request.POST['Product_name']
        Product_description = request.POST['Product_description']
        Product_cost = request.POST['Product_cost']
        no_of_products = request.POST['no_of_products']
        Product_field.objects.create(Product_name=Product_name,Product_description=Product_description,Product_cost=Product_cost,no_of_products=no_of_products)
        return redirect("data")
    return render(request,'Product_field.html')

def data(request):
    data = Product_field.objects.all()
    return render(request,'data.html',{'details':data})

def data1(request):
    data = User_field.objects.all()
    return render(request,'data1.html',{'details':data})

def single_data(request,pk):
    data = Product_field.objects.get(pk=pk)
    if request.method == 'POST':
        email = request.POST['email']
        data1 = User_field.objects.get(email=email)
        if data1.Account_balance > data.Product_cost:
            data1.Account_balance = data1.Account_balance-data.Product_cost
            print(data1.Account_balance)
            data1.save()
            buyed.objects.create(user=data1,product=data)
            return render(request,'data2.html',{'details':data1})
        else:
            return HttpResponse("Don’t Have sufficient amount to buy the product")
        
    return render(request,'single_data.html',{'details':data})

def data2(request,pk):
    data=User_field.objects.get(pk=pk)
    return render(request,'data2.html',{'details':data})

def destroy(request,pk):
    data = Product_field.objects.get(pk=pk)
    data.delete()
    return redirect('data')

def destroy1(request,pk):
    data = User_field.objects.get(pk=pk)
    data.delete()
    return redirect('data1')

def user_field(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        Account_balance = request.POST['Account_balance']
        User_field.objects.create(Username=Username,email=email,phone_number=phone_number,Account_balance=Account_balance)
        return redirect('data1')
    return render(request,'User_field.html')



def buyed_product(request):
    if request.method == 'POST':
        Product_name = request.POST['Product_name']
        user_email = request.POST['user_email']
        cost_product = request.POST['cost_product']
        Buyed_product.objects.create(Product_name=Product_name,user_email=user_email,cost_product=cost_product)
        return redirect('data')
    return render(request,'Buyed_product.html')

