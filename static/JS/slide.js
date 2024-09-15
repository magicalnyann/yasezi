document.addEventListener('DOMContentLoaded', function() {
    function setupRollingSlider(rollerId) {
        const roller = document.getElementById(rollerId);
        const clone = roller.cloneNode(true);

        clone.id = rollerId + '-clone';
        document.querySelector('.wrap').appendChild(clone);

        // 초기 위치 설정
        roller.style.position = 'absolute';
        clone.style.position = 'absolute';

        roller.style.left = '0px';
        clone.style.left = roller.scrollWidth + 'px';

        function animateSlider() {
            let pos1 = parseFloat(roller.style.left);
            let pos2 = parseFloat(clone.style.left);
            const rollerWidth = roller.scrollWidth;

            pos1 -= 1;
            pos2 -= 1;


            if (pos1 <= -rollerWidth) {
                 pos1 = pos2 + rollerWidth;
            }
            if (pos2 <= -rollerWidth) {
                 pos2 = pos1 + rollerWidth;
            }

            roller.style.left = pos1 + 'px';
            clone.style.left = pos2 + 'px';

            requestAnimationFrame(animateSlider);
        }

        animateSlider();
    }

    setupRollingSlider('roller1');
});
