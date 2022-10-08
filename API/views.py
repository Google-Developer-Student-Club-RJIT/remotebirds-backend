from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from scrape import scrape


class GetTweets(generics.ListAPIView):
    def get(self, *args, **kwargs):
        get_data = self.request.query_params
        query = get_data['search']
        if get_data.get('wfh') and get_data.get('wfh') == 'true':
            query = query+' remote'
            
        resp= scrape(
            query=query,
            start_date=get_data['start_date'],
            end_date=get_data['end_date']
            )
        return Response(data = resp)