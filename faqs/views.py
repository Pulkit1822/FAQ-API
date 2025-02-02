from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        faqs = cache.get(cache_key)

        if not faqs:
            faqs = FAQ.objects.all()
            serialized_faqs = FAQSerializer(faqs, many=True).data
            cache.set(cache_key, serialized_faqs, timeout=60*15)  # Cache for 15 minutes
        else:
            serialized_faqs = faqs

        translated_faqs = []
        for faq in serialized_faqs:
            question, answer = FAQ.objects.get(id=faq['id']).get_translated_text(lang)
            translated_faqs.append({
                'question': question,
                'answer': answer
            })

        return Response(translated_faqs, status=status.HTTP_200_OK)
