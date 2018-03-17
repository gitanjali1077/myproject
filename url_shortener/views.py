from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from django.contrib.auth.models import check_password
from django.core.mail import EmailMessage
from django.contrib import auth
from .models import urls
from django.shortcuts import render_to_response, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .serializer import urlsSerializer
import random
import string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import validators
from django.core.urlresolvers import resolve, Resolver404

class url_response(APIView):
    def get(self ,request,st=None):
        #print (string)
      print(st)

      
      if len(st) == 24 :
          
          find = urls.objects.get(short_url=st)
          print(find)
          if find.long_url :
              print(find.long_url)
              serializer = urlsSerializer(find)
        
              return Response(serializer.data)
          else:
              new_url = urls()
              new_url.long_url = ''
              new_url.short_url = ''
              new_url.status='FAILED'
              new_url.status_codes ='SHORT_URLS_NOT_FOUND' 
              
              serializer = urlsSerializer(new_url)
        
              return Response(serializer.data)
              #return redirect(find.long_url)
      if len(st) > 24 :
       new_url = urls()
       new_url.long_url = ''
       new_url.short_url = ''
       new_url.status='FAILED'
       new_url.status_codes ='INVALID_URLS' 
       serializer = urlsSerializer(new_url)
       try:
         resolve(st)
       except Resolver404:
            return Response(serializer.data)
       if not validators.url(st):
          return Response(serializer.data)

       else:     
        short = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+ string.digits) for _ in range(8))
        print (st)
        print (short)
        objects = urls.objects.all()
        serializer = urlsSerializer(objects,many=True)
        new_url = urls()
        new_url.long_url = st
        new_url.short_url = 'https://py.thon/'+short
        new_url.status='OK'
        new_url.save()
        serializer = urlsSerializer(new_url)
        
        #return Response(serializer.data)
        return Response(serializer.data)


    def post(self,request,string=None):
        
        print (string)
        objects = urls.objects.all()
        serializer = urlsSerializer(objects,many=True)
        return Response(serializer.data)

        #return render(request,'abc.html')

    
class url_response_direct(APIView):
    def get(self ,request,st=None):
        #print (string)
      print(st)

      
      if len(st) == 24 :
          
          find = urls.objects.get(short_url=st)
          print(find)
          if find.long_url :
              print(find.long_url)
              serializer = urlsSerializer(find)
        
              return redirect(find.long_url)
          else:
              new_url = urls()
              new_url.long_url = ''
              new_url.short_url = ''
              new_url.status='FAILED'
              new_url.status_codes ='SHORT_URLS_NOT_FOUND' 
              
              serializer = urlsSerializer(new_url)
        
              return Response(serializer.data)
              #return redirect(find.long_url)
    
