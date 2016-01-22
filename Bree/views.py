'''
Created on Jan 22, 2016

@author: dspring
'''
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
#
#
#
def mainIndex(request):
    #
    Iamtext = "HELLO"
    #
    return HttpResponse(Iamtext)