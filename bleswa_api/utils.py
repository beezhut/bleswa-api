from rest_framework.response import Response
from rest_framework import pagination
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        has_next = False
        if(self.get_next_link()):
            has_next = True
        return Response({
            'data': data,
            'info':{
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'has_next': has_next,
                'page_count': len(data),
                'total_count': self.page.paginator.count
            }
        })
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)