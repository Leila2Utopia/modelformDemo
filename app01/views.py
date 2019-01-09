from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import View
from django import forms
from .models import *
from django.forms import ModelForm


# class BookForm(forms.Form):
#     title=forms.CharField()
#     price=forms.DecimalField()
#     publishDate=forms.DateField()
#     state=forms.ChoiceField(choices=[(1,'已出版'),(2,'未出版')])
#     publish=forms.ModelChoiceField(queryset=Publish.objects.all())
#     authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
#
# class AddBookView(View):
#     def get(self,request):
#         form=BookForm()
#         return render(request,'add_book.html',locals())
#
#     def post(self,request):
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data.pop("authors")
#             Book.objects.create(**form.cleaned_data)
#
#             return HttpResponse("OK")
#         else:
#             print(form.cleaned_data)
#             print(form.errors)
#
#         return HttpResponse('OK')

class BookModelForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class AddBookView(View):

    def get(self,request):
        form=BookModelForm
        return render(request,'add_book.html',locals())

    def post(self,request):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
        else:
            print(form.cleaned_data)
            print(form.errors)

        return HttpResponse('OK')

class EditBookView(View):

    def get(self,request,id):
        edit_book=Book.objects.get(pk=id)
        form=BookModelForm(instance=edit_book)
        return render(request,'editbook.html',locals())

    def post(self,request,id):
        edit_book=Book.objects.get(pk=id)
        form=BookModelForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')

        else:
            print(form.cleaned_data)
            print(form.errors)
        return HttpResponse('OK')
