from django.shortcuts import render

def form(request):
    
    if request.method == 'POST':
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        email = request.POST.get("mail")
        gender = request.POST.get("gender")
        contact= request.POST.get("phone")
        address= request.POST.get("adrs")
        country= request.POST.get("country")
        city= request.POST.get("city")

        context={
            'fn':fn,
            'ln':ln,
            'email':email,
            'gender':gender,
            'contact':contact,
            'address' :address,
            'country' :country,
            'city' :city,
        }
        return render(request,'data.html',context)

    return render(request,"form.html")