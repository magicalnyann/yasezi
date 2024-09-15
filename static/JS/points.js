$(document).ready(function() {
    var csrfToken = $('meta[name="csrf-token"]').attr('content');

    $('#nyanImage').click(function() {
        var eventoId = $(this).data('evento-id');
        var pokPalUrl = $(this).data('pok-pal-url');

        console.log(`Evento ID: ${eventoId}`);
        console.log(`PokPal URL: ${pokPalUrl}`);

        $.ajax({
            type: 'POST',
            url: '/',
            contentType: 'application/json',
            headers: { "X-CSRFToken": csrfToken },
            data: JSON.stringify({
                'evento_id': eventoId
            }),
            success: function(data) {
                console.log('AJAX 요청 성공:', data);

                if (data.status === 'success') {
                    $('#nyanImage').attr('src', pokPalUrl);
                    setTimeout(() => {
                        $('#nyanImage').hide();
                    }, 3000);
                    alert(`${data.points} 포인트가 적립되었어요. 마이페이지에서 확인해 보세요.`);
                } else {
                    alert(data.message);
                }
            },
            error: function(xhr) {
                console.log('AJAX 요청 실패:', xhr);

                var message = '뭔지 모르겠지만 오류발생! 잠시 후 다시 해 달라냥!';

                if (xhr.responseJSON) {
                    console.log('서버 응답:', xhr.responseJSON);

                    switch (xhr.responseJSON.message) {
                        case '로그인이 필요합니다.':
                            message = '로그인이 필요합니다. 로그인 페이지로 이동합니다.';
                            window.location.href = '/accounts/login/';
                            break;
                        case '이미 포인트를 받았습니다.':
                            message = '이미 포인트를 받았습니다. 나중에 다시 시도해 주세요.';
                            break;
                        case '서버에서 오류가 발생했습니다.':
                            message = '서버에서 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.';
                            break;
                    }
                }

                alert(message);
            }
        });
    });
});
