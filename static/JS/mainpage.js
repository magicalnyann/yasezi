
document.addEventListener('DOMContentLoaded', function() {

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