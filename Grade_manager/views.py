from django.shortcuts import render,redirect
from Grade_manager.models import Grade,Student
from django.views.generic.base import View

# Create your views here.
def insert(request):


    g1 = Grade(g_name="大数据1班")
    g1.save()
    g2 = Grade(g_name="大数据2班")
    g2.save()
    g3 = Grade(g_name="大数据3班")
    g3.save()

    Student.objects.create(s_name= "阿达",age=19,address="咸阳",email="123@qq.com",password="123456",g = g1)
    Student.objects.create(s_name= "等等",age=20,address="西安",email="123@qq.com",password="123456",g = g1)
    Student.objects.create(s_name= "开口",age=21,address="咸阳",email="123@qq.com",password="123456",g = g1)

    Student.objects.create(s_name= "哇咔咔",age=22,address="咸阳",email="123@qq.com",password="123456",g = g2)
    Student.objects.create(s_name= "魁拔",age=23,address="咸阳",email="123@qq.com",password="123456",g = g2)
    Student.objects.create(s_name= "挖吧吧",age=25,address="咸阳",email="123@qq.com",password="123456",g = g2)

    Student.objects.create(s_name= "对对对",age=26,address="咸阳",email="123@qq.com",password="123456",g = g3)
    Student.objects.create(s_name= "喊喊",age=27,address="咸阳",email="123@qq.com",password="123456",g = g3)
    Student.objects.create(s_name= "囖咯",age=28,address="咸阳",email="123@qq.com",password="123456",g = g3)

    return render(request,"insert.html")


def show(request):
    if request.method == "GET":
        g_all = Grade.objects.all()
        s_all = Student.objects.all()

        #第一种方式
        # return render(request,"show.html",{
        #     "s_all":s_all,
        #     "g_all":g_all
        # })

        return render(request, "show.html", {
            "s_all": s_all,
            # "g_all": g_all
        })

    else:
        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        age = request.POST.get("age")
        address = request.POST.get("address")
        email = request.POST.get("email")
        password = request.POST.get("password")

        g = Grade.objects.filter(g_name=g_name).first()
        if g:
            Student.objects.create(s_name=s_name, age=age, address=address, email=email, password=password, g=g)
        else:
            new_g = Grade(g_name=g_name)
            new_g.save()
            Student.objects.create(s_name=s_name, age=age, address=address, email=email, password=password, g=new_g)

        return redirect("show")


def delete(request,id):
    print("-------------",id)
    s = Student.objects.filter(id = id).first()
    if s:
        s.delete()
    return redirect("show")


def update(request,id):
    print("*************************",id)

    s = Student.objects.filter(id = id).first()
    if request.method == "GET":
        return render(request,"update.html",{"s":s})
    else:
        g_name = request.POST.get("g_name")
        s_name = request.POST.get("s_name")
        age = request.POST.get("age")
        address = request.POST.get("address")
        email = request.POST.get("email")
        password = request.POST.get("password")



        if s_name:
            s.s_name = s_name
        if age:
            s.age = age
        if address:
            s.address = address
        if email:
            s.email = email
        if password:
            s.password = password

        gg = Grade.objects.filter(g_name=g_name).first()
        if gg:
            s.g = gg
        else:
            news_g = Grade(g_name=g_name)
            news_g.save()
            s.g = news_g

        s.save()
        return redirect("show")


class Class_view(View):
    def get(self,request,id,*args,**kwargs):
        print("**************************",id)
        g = Grade.objects.filter(id=id).first()

        #通过一个班级找到、班级所对应的全部学生
        nums = g.students()
        print("a-------------------------",nums)
        for i in nums:
            print("名字:",i.s_name)
            # 对机构进行排序

        # class_view.html页面的   a标签?号后面是传参的意思   < a href = "?sort=students" > 哇咔咔 < / a >、
        #后端通过下面的方式进行拿值
        sort = request.GET.get("sort", "")
        print("sort----------------",sort)
        return render(request, 'class_view.html')