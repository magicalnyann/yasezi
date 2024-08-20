document.addEventListener('DOMContentLoaded', function() {
    // 배너 슬라이더
    const bannerSlider = document.getElementById('banner-slider');
    let index = 0;

    function showBannerSlide() {
        const slides = bannerSlider.getElementsByClassName('banner-slide');
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = i === index ? 'block' : 'none';
        }
        index = (index + 1) % slides.length;
        setTimeout(showBannerSlide, 2500);
    }

    showBannerSlide();

    // 롤링 슬라이더와 클론을 설정
    const roller = document.querySelector('.rolling-list');
    if (!roller) {
        console.error('Rolling list element not found!');
        return;
    }

    roller.id = 'roller1';

    // 클론을 생성하고 추가
    const clone = roller.cloneNode(true);
    clone.id = 'roller2';
    roller.parentElement.appendChild(clone);

    // 초기 위치 설정
    const roller1 = document.querySelector('#roller1');
    const roller2 = document.querySelector('#roller2');

    roller1.style.position = 'absolute';
    roller2.style.position = 'absolute';

    roller1.style.left = '0px';
    roller2.style.left = roller1.scrollWidth + 'px'; // 첫 번째 롤러의 너비만큼 위치 이동

    // 애니메이션 루프 설정
    function animateRoll() {
        let left1 = parseFloat(roller1.style.left);
        let left2 = parseFloat(roller2.style.left);

        // 슬라이드가 끝에 도달하면 위치를 초기화
        if (left1 <= -roller1.scrollWidth) {
            roller1.style.left = roller2.scrollWidth + 'px';
        }
        if (left2 <= -roller2.scrollWidth) {
            roller2.style.left = roller1.scrollWidth + 'px';
        }

        // 슬라이드를 왼쪽으로 이동
        roller1.style.left = (left1 - 1) + 'px';
        roller2.style.left = (left2 - 1) + 'px';

        requestAnimationFrame(animateRoll); // 애니메이션 루프를 계속 실행
    }
    animateRoll();

    // 타임아웃
    function updateCountdown() {
        const now = new Date();
        const deadline = new Date();
        deadline.setHours(11, 0, 0, 0);
        if (now > deadline) {
            deadline.setDate(deadline.getDate() + 1);
        }

        const timeDiff = deadline - now;
        const hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);

        document.getElementById('countdown').innerHTML =
            `종료까지 ${hours}시간 ${minutes}분 ${seconds}초`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
});