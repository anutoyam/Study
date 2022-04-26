const images = ["0.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg"];
const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");
bgImage.src = `img/${chosenImage}`;

//prepend 제일 위에 추가 append 제일 아래에 추가
document.body.appendChild(bgImage);
//document.body.prepend(bgImage);
