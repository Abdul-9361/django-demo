from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Contactform,productform,DocumentForm,StudentForm
from .models import product,student,Document,Expense
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def home(request):
    # return HttpResponse("Hello Django")
    return render(request, 'home.html')

def footer(request):
   # return HttpResponse("This is footer")
   return render(request, 'footer.html')

def user(request):
    uname="Abdul"
    title=f"User: {uname}"
    role="admin"
    names=["html","css","js","python","Django"]
    return render(request,"user.html",context={'name':uname, 'title':title,'role':role,'language':names})

def contact(req):
    if req.method=='POST':
        form=Contactform(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=Contactform()

    return render(req,'contact.html',{'form':form})

def product_create(req):
    if req.method == "POST":
        form = productform(req.POST)

        if form.is_valid():
            form.save()
            messages.success(req,"data created succesfully!!")
            return redirect('/list/')
    else:
        form = productform()

    return render(req, 'product.html', {'form': form})

def student_form(request):

    studentform = StudentForm()

    if request.method == "POST":
        studentform = StudentForm(request.POST)

        if studentform.is_valid():
            studentform.save()
            return redirect("student_form")

    return render(request, "stu.html", {"form": studentform})

def product_list(req):
    products = product.objects.all()

    paginator=Paginator(products,2)

    page_number=req.GET.get("page")
    product_page=paginator.get_page(page_number)
    return render(req, "product.html", {"products": product_page})


def product_delete(req, id):
    products= product.objects.get(id=id)
    products.delete()
    return redirect('/product/')

def update_data(req,id):
    selected_data=product.objects.get(id=id)

    context={
        "product_form":productform(instance=selected_data)
    }

    if req.method=='POST':
        data=productform(req.POST,instance=selected_data)
        if data.is_valid():
            data.save()
            return redirect("/list/")
    return render(req,"form.html",context)

def file_upload(req):
    if req.method=="POST":
        form=DocumentForm(req.POST,req.FILES)

        if form.is_valid():
            form.save()
            return redirect("/upload/")
    else:
        form=DocumentForm()

    return render(req,"upload.html",{"form":form}) 

def set_session(req):
    req.session["username"]="Abdul"
    req.session["role"]="student"
    return HttpResponse("session data saved")

def get_session(req):
    username=req.session.get("username")
    role=req.session.get("role")
    return HttpResponse(f"Username: {username} <br> Role: {role}")

def delete_session(req):
    req.session.flush()
    return HttpResponse("session removed")

def set_cookie(req):
    response=HttpResponse("Cookie saved")

    response.set_cookie(
        "username","siva",max_age=2500
    )

    return response

def get_cookie(req):
    username=req.COOKIES.get("username")
    return HttpResponse(f"Username {username}")

def delete_cookie(req):
    response=HttpResponse("Cookie deleted")

    response.delete_cookie("username")
    return response

def tracker(req):

    if req.method == "POST":

        if "income" in req.POST:
            income = req.POST.get("income")

            req.session["income"] = float(income)

            return redirect("tracker")

        if "expense" in req.POST:
            item = req.POST.get("item")
            amount = req.POST.get("amount")

            if item and amount:
                Expense.objects.create(
                    item=item,
                    amount=amount
                )

            return redirect("tracker")

    income = req.session.get("income", 0)

    expenses = Expense.objects.all()

    total_expense = sum(float(i.amount) for i in expenses)

    balance = income - total_expense

    context = {
        "income": income,
        "expenses": expenses,
        "total_expense": total_expense,
        "balance": balance,
    }

    return render(req, "expenses.html", context)
