const bg = document.getElementById("bg-img");

const IMG = [
    "https://images.unsplash.com/photo-1517925557224-d4b8badf1056?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1562243061-204550d8a2c9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1591110849062-d54a6fe60847?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80",
    "https://images.unsplash.com/photo-1577368211130-4bbd0181ddf0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1042&q=80"
];

function init(){
    const randomNumber = Math.floor(Math.random() * IMG.length);
    bg.style.backgroundImage = `url(${IMG[randomNumber]})`;
}

init();