const quotes = [
    {
        quote: "꿈을 이루고자 하는 용기만 있다면 모든 꿈을 이룰 수 있다.",
        author: "월트 디즈니"
    }, {
        quote: "웃음이 없는 하루는 버린 하루다.",
        author: "찰리 채플린"
    }, {
        quote: "무슨 일을 하기 전에는 그 일에 대해 기대를 가져야 한다.",
        author: "마이클 조던"
    }, {
        quote: "행동은 모든 성공의 가장 기초적인 핵심이다.",
        author: "파블로 피카소"
    }, {
        quote: "너는 머뭇거릴 수 있지만, 시간은 그렇지 않다.",
        author: "벤자민 프랭클린"
    }, {
        quote: "인생이란 공평하지 않다는 사실에 익숙해져라.",
        author: "빌 게이츠"
    }, {
        quote: "밤 사이 어려웠던 문제가 한 잠 푹 자고 나면 아침에 해결되어 있는 일은 흔한 경험이다.",
        author: "존 스타인벡"
    }, {
        quote: "간단함이 훌륭함의 열쇠다.",
        author: "이소룡"
    }, {
        quote: "자기 신뢰는 성공의 첫번째 비결이다.",
        author: "랄프 왈도 에머슨"
    }, {
        quote: "모든 성취의 시작점은 갈망이다.",
        author: "나폴레온 힐"
    }
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
