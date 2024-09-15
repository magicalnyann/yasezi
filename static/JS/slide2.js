document.addEventListener('DOMContentLoaded', function() {
    function setupRollingSlider(rollerId) {
        const roller = document.getElementById(rollerId);
        const clone = roller.cloneNode(true);

        clone.id = rollerId + '-clone';
        document.querySelector('.wrap-2').appendChild(clone);

        roller.style.position = 'absolute';
        clone.style.position = 'absolute';

        roller.style.left = '0px';
        clone.style.left = '-' + roller.scrollWidth + 'px';

        function animateSlider() {
            let pos3 = parseFloat(roller.style.left);
            let pos4 = parseFloat(clone.style.left);
            const rollerWidth = roller.scrollWidth;

            pos3 += 1;
            pos4 += 1;

            if (pos3 >= rollerWidth) {
                 pos3 = pos4 - rollerWidth;
            }

            if (pos4 >= rollerWidth) {
                pos4 = pos3 - rollerWidth;
            }


             roller.style.left = pos3 + 'px';
             clone.style.left = pos4 + 'px';

            requestAnimationFrame(animateSlider);
        }

        animateSlider();
    }

    setupRollingSlider('roller2');
});