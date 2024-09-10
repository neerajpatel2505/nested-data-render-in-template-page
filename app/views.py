from django.shortcuts import render

# Create your views here.
# def home(request):
#     data1=str()
#     data2=['neeraj',10,20]
#     return render(request,'home.html',{'key1':data1,'key2':data2})

# def home(request):
#     data1 = {'name':{'1st':{'name':"Arvind",'age':35},'2nd':"rahul",'3rd':"Raj"},'age':37,'qualification':'M.Tech'}
#     data2 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     data3 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     data4 = {'name':'Neeraj','age':37,'qualification':'M.Tech'}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data 3,'key4':data4})

# def home(request):
#     data1 = {}
#     data2 = {}
#     data3 = {}
#     data4 = {}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})

# def home(request):
#     data1 = {'name':'Neeraj'}
#     data2 = {}
#     data3 = {}
#     data4 = {}
#     # return render(request,'index.html',data)
#     return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})

def home(request):
    data1 = {'value':'From key1'}
    data2 = {'value':'From key2'}
    data3 = {}
    data4 = {}
    # return render(request,'index.html',data)
    return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})