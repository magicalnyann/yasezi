// 좋아요 싫어요 구역
function handleClick(action) {
    var url = '';
    if (action === 'like') {
        url = likeUrl;
    } else if (action === 'dislike') {
        url = dislikeUrl;
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (action === 'like') {
                document.getElementById('like-counter').textContent = response.likes;
            } else if (action === 'dislike') {
                document.getElementById('dislike-counter').textContent = response.dislikes;
            }
            handle(action);
        }
    };

    xhr.send();
}

//이모지 버튼 이벤트
function handle(action) {
    createEmojiEffect(action);
}

function createEmojiEffect(action) {
    const emojiContainer = document.getElementById('emoji-container');
    const buttonContainer = document.querySelector('.button-container');

    const containerRect = buttonContainer.getBoundingClientRect();

    const likeEmojis = ['🎉', '✨', '💘', '😍'];
    const dislikeEmojis = ['🖕', '💩', '💢', '👿'];

    const emojis = action === 'like' ? likeEmojis : dislikeEmojis;


    for (let i = 0; i < 30; i++) {
        const emoji = document.createElement('div');
        emoji.className = 'emoji';
        emoji.textContent = emojis[Math.floor(Math.random() * emojis.length)];

        emoji.style.left = `${Math.random() * (containerRect.width - 30)}px`;
        emoji.style.bottom = `-10%`;
        emoji.style.opacity = Math.random();

        emojiContainer.appendChild(emoji);
        setTimeout(() => {
            emoji.style.transition = 'transform 8s ease-out, opacity 8s ease-out';
            emoji.style.transform = `translateY(-100vh)`;
            emoji.style.opacity = 0;
            setTimeout(() => emoji.remove(), 15000);
        }, Math.random() * 1000);
    }
}