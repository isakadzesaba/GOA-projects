function makeChoice(choice) {
    if (choice === 'yes') {
    
    } else {
    window.location.href = 'celebrate.html';
    }
}

function moveButton() {
    var button = document.getElementById('yes-button');
    var buttonRect = button.getBoundingClientRect();
    var maxX = window.innerWidth - buttonRect.width;
    var maxY = window.innerHeight - buttonRect.height;
    var newX = Math.floor(Math.random() * 500);
    var newY = Math.floor(Math.random() * 500);

    // Set new position
    button.style.transform = `translate(${newX}px, ${newY}px)`;
}