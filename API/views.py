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
        startIndex = (int(get_data['page']) - 1) * int(get_data['pagesize'])
        endIndex = int(get_data['page']) * int(get_data['pagesize'])
        resp= scrape(
            query=query,
            start_date=get_data['start_date'],
            end_date=get_data['end_date']
            )[startIndex:endIndex]
        return Response(data = resp)