//출석체크버튼  anim 이벤트 함수
var offTop = 50;
var offLeft = 50;

var speed_x = Math.random() * 5;
var speed_y = Math.random() * 3;

var w = 0;
var h = 0;

function anim() {
    offTop += speed_y;
    offLeft += speed_x;

    w = $(window).width();
    h = $(window).height();

    if (offTop >= h - 100) {
        offTop = h - 100;
        speed_y = -speed_y;
    }
    if (offTop < 100) {
        offTop = 100;
        speed_y = -speed_y;
    }
    if (offLeft >= w - 100) {
        offLeft = w - 100;
        speed_x = -speed_x;
    }
    if (offLeft < 50) {
        offLeft = 50;
        speed_x = -speed_x;
    }

    $("#imageButtonContainer").animate({top: offTop + 'px', left: offLeft + 'px'}, 10);
}

$(document).ready(function () {
    setInterval(anim, 10);
});
