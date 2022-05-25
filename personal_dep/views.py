from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic


class DocumentsView(View):

    def get(self, request):
        context = {
        }
        return render(request, 'documents/index.html', context)


class DocumetnsAdd(View):

    def post(self, request):
        return redirect('documents')

    def get(self, request):
        return render(request, 'documents/add.html', {})


class DocumentsChange(View):

    def post(self, request, **kwargs):
        return render(request, 'documents/add.html', {})

    def get(self, request, **kwargs):

        return render(request, 'documents/add.html', {})


class DocumentsDelete(View):

    def get(self, request, **kwargs):

        return redirect('documents')


class DocumentsFilter(View):

    def get(self, request, **kwargs):

        return render(request, 'documents/index.html', {})
