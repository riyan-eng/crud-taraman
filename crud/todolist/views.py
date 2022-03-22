from django.shortcuts import render

# Create your views here.
def create(req):
    if req.POST:
        respon = req.POST["nama"]
        print(respon)
    return render(req, 'index.html')