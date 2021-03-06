from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from quran.models import Reciter, TafTar, Counter


class GetAllRecitersAPIView(APIView):

    def get(self, request, format=None):
        try:
            # all_reciter = Reciter.objects.filter(r_type=1).order_by('r_id')
            all_reciter = Reciter.objects.order_by('r_id')
            data = []
            for reciter in all_reciter:
                data.append({
                    "r_id": reciter.r_id,
                    "r_img": reciter.r_img,
                    "r_folder": reciter.r_folder,
                    "r_nameAR": reciter.r_nameAR,
                    "r_nameEN": reciter.r_nameEN,
                    "r_nameFA": reciter.r_nameFA,
                    "r_time": reciter.r_time,
                    "r_url1": reciter.r_url1,
                    "r_size1": reciter.r_size1,
                    "r_quality1": reciter.r_quality1,
                    "r_url2": reciter.r_url2,
                    "r_size2": reciter.r_size2,
                    "r_quality2": reciter.r_quality2,
                    "r_url3": reciter.r_url3,
                    "r_size3": reciter.r_size3,
                    "r_quality3": reciter.r_quality3,
                    "r_withBesm": reciter.r_withBesm,
                    "r_type": reciter.r_type,
                    "r_ord": reciter.r_ord,
                    "r_mode": reciter.r_mode,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReciterLastUpdateAPIView(APIView):

    def get(self, request, format=None):
        try:
            from django.db.models import Max
            serverLast = Reciter.objects.aggregate(Max('r_update')).get('r_update__max').strftime('%Y-%m-%d %H:%M')
            return Response(serverLast, status=status.HTTP_200_OK)
        except:
            return Response({'status': "my Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllTafTarTextAPIView(APIView):

    def get(self, request, format=None):
        try:
            all_text = TafTar.objects.order_by('order')
            data = []
            for texts in all_text:
                data.append({
                    "type": texts.type,
                    "mode": texts.mode,
                    "titleFA": texts.titleFA,
                    "titleEN": texts.titleEN,
                    "titleAR": texts.titleAR,
                    "db_name": texts.db_name,
                    "reciter_id": texts.reciter_id,
                    "version": texts.version,
                    "order": texts.order,

                })

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TafTarLastUpdateAPIView(APIView):

    def get(self, request, format=None):
        try:
            p = Counter(type=1, count=1)
            p.save()

            from django.db.models import Max
            serverLast = TafTar.objects.aggregate(Max('update')).get('update__max').strftime('%Y-%m-%d %H:%M')
            return Response(serverLast, status=status.HTTP_200_OK)
        except:
            return Response({'status': "my Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
