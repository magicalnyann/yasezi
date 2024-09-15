from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json
import logging
import random
from evento.models import Evento, UserEvent


# 로거 객체
logger = logging.getLogger(__name__)


def event(request):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            # 로그인 여부를 확인 / 비로그인은 로그인 페이지로 go
            return JsonResponse({'status': 'error', 'message': '로그인이 필요합니다.'})


        try:
            data = json.loads(request.body)
            evento_id = data.get('evento_id')
            user = request.user

            logger.info(f"User {user.username} is attempting to get points for event {evento_id}.")

            # 이벤트 객체를 가져옴
            evento = get_object_or_404(Evento, id=evento_id)

            
            #포인트 지급 로직

            # 이미 포인트를 받은 경우
            today = timezone.now().date()
            if UserEvent.objects.filter(user=user, evento=evento, date=today).exists():
                logger.warning(f"User {user.username} 이미 포인트를 받은 고객 입니다 {evento_id} today.")

                return JsonResponse({'status': 'error', 'message': '이미 포인트를 받았습니다.'})


            # 포인트 받기 성공
            points_awarded = random.randint(10, 1000)
            UserEvent.objects.create(user=user, evento=evento, date=timezone.now(), points_awarded=points_awarded)

            logger.info(f"User {user.username} awarded {points_awarded} points for event {evento_id}.")

            return JsonResponse({'status': 'success', 'points': points_awarded, 'message': f'{points_awarded} 포인트가 적립되었습니다.'})

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return JsonResponse({'status': 'error', 'message': '서버에서 오류가 발생했습니다.'})

        else:
            return JsonResponse({'status': 'error', 'message': '올바르지 않은 요청입니다.'})


    # GET 요청에 대한 처리
    eventos = Evento.objects.all()
    return render(request, 'evento/evento.html', {'eventos': eventos})
