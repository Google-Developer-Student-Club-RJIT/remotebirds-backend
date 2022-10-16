from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from scrape import scrape
from django.core.paginator import Paginator


class GetTweets(generics.ListAPIView):
    def get(self, *args, **kwargs):
        get_data = self.request.query_params
        query = get_data['search']
        word_list = ['job','developer required','hiring','internship','opportunity','required','full-time','part-time','technical','training','engineering','marketing','recruitment','researching']

        if get_data.get('wfh') and get_data.get('wfh') == 'true':
            query = query+' remote'
        final_query = ''
        for i in word_list:
            final_query+= '"'+query+' '+i+'" OR '
        final_query = '(' + final_query[:-4] + ')'

        resp= scrape(
            query=final_query,
            start_date=get_data['start_date'],
            end_date=get_data['end_date']
            )
        
        p = []
        try:
            p = Paginator(resp, int(get_data['pagesize'])).page(int(get_data['page'])).object_list
        except Exception as e:
            print(e)

        return Response(status=200, data=p, headers={
            'X-Total-Count': len(resp),
            'Access-Control-Expose-Headers': 'X-Total-Count'
        })