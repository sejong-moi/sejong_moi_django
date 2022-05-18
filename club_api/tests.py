# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


html = '''
<html lang="en"><head><meta charset="utf-8"><link rel="icon" href="public/favicon.ico"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="세종대학교 총동아리연합회 홈페이지"><link rel="manifest" href="public/manifest.json"><title>세종대학교 총동아리연합회</title><link rel="icon" href="/favicon.ico"><script defer="defer" src="/app.88d14a2c4992412493f0.js"></script><style>@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSansNeo.css);</style><style>* {
  font-family: 'Spoqa Han Sans Neo', -apple-system, BlinkMacSystemFont, “Segoe UI”, “Roboto”, “Oxygen”, “Ubuntu”, “Cantarell”, “Fira Sans”, “Droid Sans”, “Helvetica Neue”, sans-serif;
}

html {
  height: 100%;
}
input:focus {
  outline: 0;
}
body {
  margin: 0;
  height: 100%;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 0;
  margin: 0;
}
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background-color: transparent;
}
::-webkit-scrollbar-thumb {
  border-radius: 3px;
  background-color: grey;
}
::-webkit-scrollbar-button {
  width: 0;
  height: 0;
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes logo_fadein {
  0% {
    transform: translateX(200px);
    opacity: 0;
  }
  50% {
    transform: translateX(200px);
    opacity: 1;
  }
  100% {
    transform: translateX(-100px);
    opacity: 1;
  }
}
@keyframes intro_animation {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    z-index: -100;
  }
}
@keyframes club-container-animation {
  from {
    transform: translateY(100px);
    opacity: 0;
  }
  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

.navigation-uparrow {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 9px;
  left: 82px;
  position: absolute;
}
.navigation-uparrow2 {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 8px;
  left: 40px;
  position: absolute;
}

.submenu {
  display: none;
  position: absolute;
  transform: translateX(-12px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu2 {
  display: none;
  position: absolute;
  transform: translateX(-30px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu3 {
  display: none;
  position: absolute;
  transform: translateX(-75px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu4 {
  display: none;
  position: absolute;
  background-color: #ad1e2d;
  transform: translateX(-33px) translateY(-5px);
  padding-top: 18px;
  animation: fadein 0.2s;
}
.progressBar-container:hover .progressBar-content {
  border: 2px solid #ad1e2d;
}
.progressBar-container:hover > .subProgress {
  display: block;
}
.progressBar-container:hover > .subProgress-big {
  display: block;
}
.progressBar-container:hover > .totalProgress {
  display: block;
}
.subProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(81px);
}
.subProgress-big {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(51px);
}
.subProgress-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  z-index: 10;
}
.subProgress-big-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 195px;
  z-index: 10;
}
.subProgress-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-2px);
  z-index: 10;
}
.subProgress-big-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 195px;
  transform: translateY(-2px);
  z-index: 10;
}
.totalProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  top: 25px;
  z-index: 10;
  transform: translateX(81px);
}
.totalProgress-uparrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  transform: translateY(-15px);
  z-index: 10;
}
.totalProgress-uparrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-13px);
  z-index: 10;
}
.suggestions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.petitions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.report-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.report-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.suggestions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.petitions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.invisible {
  display: none !important;
}
.input-container {
  position: relative;
  background-color: #f6f6f6;
}
.input-container .input-label {
  position: absolute;
  color: grey;
  top: 12px;
  left: 12px;
  transition: all 0.1s ease-out;
  cursor: text;
}
.login-focused .input-label {
  top: 3px;
  font-size: 12px;
}
.manage-input {
  border-bottom: 1px solid #ad1e2d;
  padding-bottom: 30px;
}
.manage-label1 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 20px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-label2 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 40px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-input input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
input[type="submit"] {
  width: 120px;
  height: 60px;
  background-color: #ad1e2d;
  color: white;
  border-radius: 5px;
  margin-left: 30px;
  font-size: 22px;
  cursor: pointer;
  border: none;
}
</style><style>.carousel .control-arrow,.carousel.carousel-slider .control-arrow{-webkit-transition:all .25s ease-in;-moz-transition:all .25s ease-in;-ms-transition:all .25s ease-in;-o-transition:all .25s ease-in;transition:all .25s ease-in;opacity:.4;filter:alpha(opacity=40);position:absolute;z-index:2;top:20px;background:none;border:0;font-size:32px;cursor:pointer}.carousel .control-arrow:focus,.carousel .control-arrow:hover{opacity:1;filter:alpha(opacity=100)}.carousel .control-arrow:before,.carousel.carousel-slider .control-arrow:before{margin:0 5px;display:inline-block;border-top:8px solid transparent;border-bottom:8px solid transparent;content:''}.carousel .control-disabled.control-arrow{opacity:0;filter:alpha(opacity=0);cursor:inherit;display:none}.carousel .control-prev.control-arrow{left:0}.carousel .control-prev.control-arrow:before{border-right:8px solid #fff}.carousel .control-next.control-arrow{right:0}.carousel .control-next.control-arrow:before{border-left:8px solid #fff}.carousel-root{outline:none}.carousel{position:relative;width:100%}.carousel *{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.carousel img{width:100%;display:inline-block;pointer-events:none}.carousel .carousel{position:relative}.carousel .control-arrow{outline:0;border:0;background:none;top:50%;margin-top:-13px;font-size:18px}.carousel .thumbs-wrapper{margin:20px;overflow:hidden}.carousel .thumbs{-webkit-transition:all .15s ease-in;-moz-transition:all .15s ease-in;-ms-transition:all .15s ease-in;-o-transition:all .15s ease-in;transition:all .15s ease-in;-webkit-transform:translate3d(0, 0, 0);-moz-transform:translate3d(0, 0, 0);-ms-transform:translate3d(0, 0, 0);-o-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0);position:relative;list-style:none;white-space:nowrap}.carousel .thumb{-webkit-transition:border .15s ease-in;-moz-transition:border .15s ease-in;-ms-transition:border .15s ease-in;-o-transition:border .15s ease-in;transition:border .15s ease-in;display:inline-block;margin-right:6px;white-space:nowrap;overflow:hidden;border:3px solid #fff;padding:2px}.carousel .thumb:focus{border:3px solid #ccc;outline:none}.carousel .thumb.selected,.carousel .thumb:hover{border:3px solid #333}.carousel .thumb img{vertical-align:top}.carousel.carousel-slider{position:relative;margin:0;overflow:hidden}.carousel.carousel-slider .control-arrow{top:0;color:#fff;font-size:26px;bottom:0;margin-top:0;padding:5px}.carousel.carousel-slider .control-arrow:hover{background:rgba(0,0,0,0.2)}.carousel .slider-wrapper{overflow:hidden;margin:auto;width:100%;-webkit-transition:height .15s ease-in;-moz-transition:height .15s ease-in;-ms-transition:height .15s ease-in;-o-transition:height .15s ease-in;transition:height .15s ease-in}.carousel .slider-wrapper.axis-horizontal .slider{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-horizontal .slider .slide{flex-direction:column;flex-flow:column}.carousel .slider-wrapper.axis-vertical{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-vertical .slider{-webkit-flex-direction:column;flex-direction:column}.carousel .slider{margin:0;padding:0;position:relative;list-style:none;width:100%}.carousel .slider.animated{-webkit-transition:all .35s ease-in-out;-moz-transition:all .35s ease-in-out;-ms-transition:all .35s ease-in-out;-o-transition:all .35s ease-in-out;transition:all .35s ease-in-out}.carousel .slide{min-width:100%;margin:0;position:relative;text-align:center}.carousel .slide img{width:100%;vertical-align:top;border:0}.carousel .slide iframe{display:inline-block;width:calc(100% - 80px);margin:0 40px 40px;border:0}.carousel .slide .legend{-webkit-transition:all .5s ease-in-out;-moz-transition:all .5s ease-in-out;-ms-transition:all .5s ease-in-out;-o-transition:all .5s ease-in-out;transition:all .5s ease-in-out;position:absolute;bottom:40px;left:50%;margin-left:-45%;width:90%;border-radius:10px;background:#000;color:#fff;padding:10px;font-size:12px;text-align:center;opacity:0.25;-webkit-transition:opacity .35s ease-in-out;-moz-transition:opacity .35s ease-in-out;-ms-transition:opacity .35s ease-in-out;-o-transition:opacity .35s ease-in-out;transition:opacity .35s ease-in-out}.carousel .control-dots{position:absolute;bottom:0;margin:10px 0;padding:0;text-align:center;width:100%;z-index:1}@media (min-width: 960px){.carousel .control-dots{bottom:0}}.carousel .control-dots .dot{-webkit-transition:opacity .25s ease-in;-moz-transition:opacity .25s ease-in;-ms-transition:opacity .25s ease-in;-o-transition:opacity .25s ease-in;transition:opacity .25s ease-in;opacity:.3;filter:alpha(opacity=30);box-shadow:1px 1px 2px rgba(0,0,0,0.9);background:#fff;border-radius:50%;width:8px;height:8px;cursor:pointer;display:inline-block;margin:0 8px}.carousel .control-dots .dot.selected,.carousel .control-dots .dot:hover{opacity:1;filter:alpha(opacity=100)}.carousel .carousel-status{position:absolute;top:0;right:0;padding:5px;font-size:10px;text-shadow:1px 1px 1px rgba(0,0,0,0.9);color:#fff}.carousel:hover .slide .legend{opacity:1}
</style><style data-styled="active" data-styled-version="5.3.5"></style><style data-emotion="css" data-s=""></style></head><body><noscript>You need to enable JavaScript to run this app.</noscript><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-5689BD5H8V"></script><script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script><div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div></body></html>
<head><meta charset="utf-8"><link rel="icon" href="public/favicon.ico"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="세종대학교 총동아리연합회 홈페이지"><link rel="manifest" href="public/manifest.json"><title>세종대학교 총동아리연합회</title><link rel="icon" href="/favicon.ico"><script defer="defer" src="/app.88d14a2c4992412493f0.js"></script><style>@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSansNeo.css);</style><style>* {
  font-family: 'Spoqa Han Sans Neo', -apple-system, BlinkMacSystemFont, “Segoe UI”, “Roboto”, “Oxygen”, “Ubuntu”, “Cantarell”, “Fira Sans”, “Droid Sans”, “Helvetica Neue”, sans-serif;
}

html {
  height: 100%;
}
input:focus {
  outline: 0;
}
body {
  margin: 0;
  height: 100%;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 0;
  margin: 0;
}
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background-color: transparent;
}
::-webkit-scrollbar-thumb {
  border-radius: 3px;
  background-color: grey;
}
::-webkit-scrollbar-button {
  width: 0;
  height: 0;
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes logo_fadein {
  0% {
    transform: translateX(200px);
    opacity: 0;
  }
  50% {
    transform: translateX(200px);
    opacity: 1;
  }
  100% {
    transform: translateX(-100px);
    opacity: 1;
  }
}
@keyframes intro_animation {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    z-index: -100;
  }
}
@keyframes club-container-animation {
  from {
    transform: translateY(100px);
    opacity: 0;
  }
  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

.navigation-uparrow {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 9px;
  left: 82px;
  position: absolute;
}
.navigation-uparrow2 {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 8px;
  left: 40px;
  position: absolute;
}

.submenu {
  display: none;
  position: absolute;
  transform: translateX(-12px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu2 {
  display: none;
  position: absolute;
  transform: translateX(-30px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu3 {
  display: none;
  position: absolute;
  transform: translateX(-75px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu4 {
  display: none;
  position: absolute;
  background-color: #ad1e2d;
  transform: translateX(-33px) translateY(-5px);
  padding-top: 18px;
  animation: fadein 0.2s;
}
.progressBar-container:hover .progressBar-content {
  border: 2px solid #ad1e2d;
}
.progressBar-container:hover > .subProgress {
  display: block;
}
.progressBar-container:hover > .subProgress-big {
  display: block;
}
.progressBar-container:hover > .totalProgress {
  display: block;
}
.subProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(81px);
}
.subProgress-big {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(51px);
}
.subProgress-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  z-index: 10;
}
.subProgress-big-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 195px;
  z-index: 10;
}
.subProgress-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-2px);
  z-index: 10;
}
.subProgress-big-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 195px;
  transform: translateY(-2px);
  z-index: 10;
}
.totalProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  top: 25px;
  z-index: 10;
  transform: translateX(81px);
}
.totalProgress-uparrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  transform: translateY(-15px);
  z-index: 10;
}
.totalProgress-uparrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-13px);
  z-index: 10;
}
.suggestions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.petitions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.report-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.report-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.suggestions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.petitions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.invisible {
  display: none !important;
}
.input-container {
  position: relative;
  background-color: #f6f6f6;
}
.input-container .input-label {
  position: absolute;
  color: grey;
  top: 12px;
  left: 12px;
  transition: all 0.1s ease-out;
  cursor: text;
}
.login-focused .input-label {
  top: 3px;
  font-size: 12px;
}
.manage-input {
  border-bottom: 1px solid #ad1e2d;
  padding-bottom: 30px;
}
.manage-label1 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 20px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-label2 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 40px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-input input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
input[type="submit"] {
  width: 120px;
  height: 60px;
  background-color: #ad1e2d;
  color: white;
  border-radius: 5px;
  margin-left: 30px;
  font-size: 22px;
  cursor: pointer;
  border: none;
}
</style><style>.carousel .control-arrow,.carousel.carousel-slider .control-arrow{-webkit-transition:all .25s ease-in;-moz-transition:all .25s ease-in;-ms-transition:all .25s ease-in;-o-transition:all .25s ease-in;transition:all .25s ease-in;opacity:.4;filter:alpha(opacity=40);position:absolute;z-index:2;top:20px;background:none;border:0;font-size:32px;cursor:pointer}.carousel .control-arrow:focus,.carousel .control-arrow:hover{opacity:1;filter:alpha(opacity=100)}.carousel .control-arrow:before,.carousel.carousel-slider .control-arrow:before{margin:0 5px;display:inline-block;border-top:8px solid transparent;border-bottom:8px solid transparent;content:''}.carousel .control-disabled.control-arrow{opacity:0;filter:alpha(opacity=0);cursor:inherit;display:none}.carousel .control-prev.control-arrow{left:0}.carousel .control-prev.control-arrow:before{border-right:8px solid #fff}.carousel .control-next.control-arrow{right:0}.carousel .control-next.control-arrow:before{border-left:8px solid #fff}.carousel-root{outline:none}.carousel{position:relative;width:100%}.carousel *{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.carousel img{width:100%;display:inline-block;pointer-events:none}.carousel .carousel{position:relative}.carousel .control-arrow{outline:0;border:0;background:none;top:50%;margin-top:-13px;font-size:18px}.carousel .thumbs-wrapper{margin:20px;overflow:hidden}.carousel .thumbs{-webkit-transition:all .15s ease-in;-moz-transition:all .15s ease-in;-ms-transition:all .15s ease-in;-o-transition:all .15s ease-in;transition:all .15s ease-in;-webkit-transform:translate3d(0, 0, 0);-moz-transform:translate3d(0, 0, 0);-ms-transform:translate3d(0, 0, 0);-o-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0);position:relative;list-style:none;white-space:nowrap}.carousel .thumb{-webkit-transition:border .15s ease-in;-moz-transition:border .15s ease-in;-ms-transition:border .15s ease-in;-o-transition:border .15s ease-in;transition:border .15s ease-in;display:inline-block;margin-right:6px;white-space:nowrap;overflow:hidden;border:3px solid #fff;padding:2px}.carousel .thumb:focus{border:3px solid #ccc;outline:none}.carousel .thumb.selected,.carousel .thumb:hover{border:3px solid #333}.carousel .thumb img{vertical-align:top}.carousel.carousel-slider{position:relative;margin:0;overflow:hidden}.carousel.carousel-slider .control-arrow{top:0;color:#fff;font-size:26px;bottom:0;margin-top:0;padding:5px}.carousel.carousel-slider .control-arrow:hover{background:rgba(0,0,0,0.2)}.carousel .slider-wrapper{overflow:hidden;margin:auto;width:100%;-webkit-transition:height .15s ease-in;-moz-transition:height .15s ease-in;-ms-transition:height .15s ease-in;-o-transition:height .15s ease-in;transition:height .15s ease-in}.carousel .slider-wrapper.axis-horizontal .slider{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-horizontal .slider .slide{flex-direction:column;flex-flow:column}.carousel .slider-wrapper.axis-vertical{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-vertical .slider{-webkit-flex-direction:column;flex-direction:column}.carousel .slider{margin:0;padding:0;position:relative;list-style:none;width:100%}.carousel .slider.animated{-webkit-transition:all .35s ease-in-out;-moz-transition:all .35s ease-in-out;-ms-transition:all .35s ease-in-out;-o-transition:all .35s ease-in-out;transition:all .35s ease-in-out}.carousel .slide{min-width:100%;margin:0;position:relative;text-align:center}.carousel .slide img{width:100%;vertical-align:top;border:0}.carousel .slide iframe{display:inline-block;width:calc(100% - 80px);margin:0 40px 40px;border:0}.carousel .slide .legend{-webkit-transition:all .5s ease-in-out;-moz-transition:all .5s ease-in-out;-ms-transition:all .5s ease-in-out;-o-transition:all .5s ease-in-out;transition:all .5s ease-in-out;position:absolute;bottom:40px;left:50%;margin-left:-45%;width:90%;border-radius:10px;background:#000;color:#fff;padding:10px;font-size:12px;text-align:center;opacity:0.25;-webkit-transition:opacity .35s ease-in-out;-moz-transition:opacity .35s ease-in-out;-ms-transition:opacity .35s ease-in-out;-o-transition:opacity .35s ease-in-out;transition:opacity .35s ease-in-out}.carousel .control-dots{position:absolute;bottom:0;margin:10px 0;padding:0;text-align:center;width:100%;z-index:1}@media (min-width: 960px){.carousel .control-dots{bottom:0}}.carousel .control-dots .dot{-webkit-transition:opacity .25s ease-in;-moz-transition:opacity .25s ease-in;-ms-transition:opacity .25s ease-in;-o-transition:opacity .25s ease-in;transition:opacity .25s ease-in;opacity:.3;filter:alpha(opacity=30);box-shadow:1px 1px 2px rgba(0,0,0,0.9);background:#fff;border-radius:50%;width:8px;height:8px;cursor:pointer;display:inline-block;margin:0 8px}.carousel .control-dots .dot.selected,.carousel .control-dots .dot:hover{opacity:1;filter:alpha(opacity=100)}.carousel .carousel-status{position:absolute;top:0;right:0;padding:5px;font-size:10px;text-shadow:1px 1px 1px rgba(0,0,0,0.9);color:#fff}.carousel:hover .slide .legend{opacity:1}
</style><style data-styled="active" data-styled-version="5.3.5"></style><style data-emotion="css" data-s=""></style></head>
<body><noscript>You need to enable JavaScript to run this app.</noscript><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-5689BD5H8V"></script><script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script><div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div></body>
<noscript>You need to enable JavaScript to run this app.</noscript>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-5689BD5H8V"></script>
<script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script>
<div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div>
<div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div>
<div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div>
<div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div>
<div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div>
<div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div>
<div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div>
<div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div>
<div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div>
<div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div>
<div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div>
<div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div>
<a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a>
<img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto">
<a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a>
<div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div>
<div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div>
<div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div>
<div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div>
<div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div>
<div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div>
<div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div>
<div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div>
<div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div>
<div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div>
<body><noscript>You need to enable JavaScript to run this app.</noscript><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-5689BD5H8V"></script><script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script><div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div></body>
<html lang="en"><head><meta charset="utf-8"><link rel="icon" href="public/favicon.ico"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="세종대학교 총동아리연합회 홈페이지"><link rel="manifest" href="public/manifest.json"><title>세종대학교 총동아리연합회</title><link rel="icon" href="/favicon.ico"><script defer="defer" src="/app.88d14a2c4992412493f0.js"></script><style>@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSansNeo.css);</style><style>* {
  font-family: 'Spoqa Han Sans Neo', -apple-system, BlinkMacSystemFont, “Segoe UI”, “Roboto”, “Oxygen”, “Ubuntu”, “Cantarell”, “Fira Sans”, “Droid Sans”, “Helvetica Neue”, sans-serif;
}

html {
  height: 100%;
}
input:focus {
  outline: 0;
}
body {
  margin: 0;
  height: 100%;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 0;
  margin: 0;
}
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background-color: transparent;
}
::-webkit-scrollbar-thumb {
  border-radius: 3px;
  background-color: grey;
}
::-webkit-scrollbar-button {
  width: 0;
  height: 0;
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes logo_fadein {
  0% {
    transform: translateX(200px);
    opacity: 0;
  }
  50% {
    transform: translateX(200px);
    opacity: 1;
  }
  100% {
    transform: translateX(-100px);
    opacity: 1;
  }
}
@keyframes intro_animation {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    z-index: -100;
  }
}
@keyframes club-container-animation {
  from {
    transform: translateY(100px);
    opacity: 0;
  }
  to {
    transform: translateY(0px);
    opacity: 1;
  }
}

.navigation-uparrow {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 9px;
  left: 82px;
  position: absolute;
}
.navigation-uparrow2 {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  top: 8px;
  left: 40px;
  position: absolute;
}

.submenu {
  display: none;
  position: absolute;
  transform: translateX(-12px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu2 {
  display: none;
  position: absolute;
  transform: translateX(-30px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu3 {
  display: none;
  position: absolute;
  transform: translateX(-75px);
  background-color: #ad1e2d;
  padding-top: 19px;
  animation: fadein 0.2s;
}
.submenu4 {
  display: none;
  position: absolute;
  background-color: #ad1e2d;
  transform: translateX(-33px) translateY(-5px);
  padding-top: 18px;
  animation: fadein 0.2s;
}
.progressBar-container:hover .progressBar-content {
  border: 2px solid #ad1e2d;
}
.progressBar-container:hover > .subProgress {
  display: block;
}
.progressBar-container:hover > .subProgress-big {
  display: block;
}
.progressBar-container:hover > .totalProgress {
  display: block;
}
.subProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(81px);
}
.subProgress-big {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  bottom: 35px;
  z-index: 10;
  transform: translateX(51px);
}
.subProgress-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  z-index: 10;
}
.subProgress-big-downarrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid #ad1e2d;
  position: absolute;
  left: 195px;
  z-index: 10;
}
.subProgress-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-2px);
  z-index: 10;
}
.subProgress-big-downarrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-top: 15px solid white;
  position: absolute;
  left: 195px;
  transform: translateY(-2px);
  z-index: 10;
}
.totalProgress {
  background-color: white;
  border: 2px solid #ad1e2d;
  border-radius: 10px;
  display: none;
  position: absolute;
  left: 240px;
  top: 25px;
  z-index: 10;
  transform: translateX(81px);
}
.totalProgress-uparrow {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid #ad1e2d;
  position: absolute;
  left: 165px;
  transform: translateY(-15px);
  z-index: 10;
}
.totalProgress-uparrow-cover {
  width: 0;
  height: 0;
  border-left: 15px solid transparent;
  border-right: 15px solid transparent;
  border-bottom: 15px solid white;
  position: absolute;
  left: 165px;
  transform: translateY(-13px);
  z-index: 10;
}
.suggestions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.petitions-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(80px);
  border: 1px solid #ad1e2d;
}
.report-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-sort-options {
  position: absolute;
  transform: translateX(-368px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.report-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.meetinglogs-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.suggestions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.petitions-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(65px);
  border: 1px solid #ad1e2d;
}
.forms-search-options {
  position: absolute;
  transform: translateX(-233px) translateY(50px);
  border: 1px solid #ad1e2d;
}
.invisible {
  display: none !important;
}
.input-container {
  position: relative;
  background-color: #f6f6f6;
}
.input-container .input-label {
  position: absolute;
  color: grey;
  top: 12px;
  left: 12px;
  transition: all 0.1s ease-out;
  cursor: text;
}
.login-focused .input-label {
  top: 3px;
  font-size: 12px;
}
.manage-input {
  border-bottom: 1px solid #ad1e2d;
  padding-bottom: 30px;
}
.manage-label1 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 20px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-label2 {
  color: white;
  background-color: #ad1e2d;
  width: 120px;
  height: 40px;
  padding-left: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-right: 20px;
  border-radius: 5px;
  cursor: pointer;
}
.manage-input input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
input[type="submit"] {
  width: 120px;
  height: 60px;
  background-color: #ad1e2d;
  color: white;
  border-radius: 5px;
  margin-left: 30px;
  font-size: 22px;
  cursor: pointer;
  border: none;
}
</style><style>.carousel .control-arrow,.carousel.carousel-slider .control-arrow{-webkit-transition:all .25s ease-in;-moz-transition:all .25s ease-in;-ms-transition:all .25s ease-in;-o-transition:all .25s ease-in;transition:all .25s ease-in;opacity:.4;filter:alpha(opacity=40);position:absolute;z-index:2;top:20px;background:none;border:0;font-size:32px;cursor:pointer}.carousel .control-arrow:focus,.carousel .control-arrow:hover{opacity:1;filter:alpha(opacity=100)}.carousel .control-arrow:before,.carousel.carousel-slider .control-arrow:before{margin:0 5px;display:inline-block;border-top:8px solid transparent;border-bottom:8px solid transparent;content:''}.carousel .control-disabled.control-arrow{opacity:0;filter:alpha(opacity=0);cursor:inherit;display:none}.carousel .control-prev.control-arrow{left:0}.carousel .control-prev.control-arrow:before{border-right:8px solid #fff}.carousel .control-next.control-arrow{right:0}.carousel .control-next.control-arrow:before{border-left:8px solid #fff}.carousel-root{outline:none}.carousel{position:relative;width:100%}.carousel *{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}.carousel img{width:100%;display:inline-block;pointer-events:none}.carousel .carousel{position:relative}.carousel .control-arrow{outline:0;border:0;background:none;top:50%;margin-top:-13px;font-size:18px}.carousel .thumbs-wrapper{margin:20px;overflow:hidden}.carousel .thumbs{-webkit-transition:all .15s ease-in;-moz-transition:all .15s ease-in;-ms-transition:all .15s ease-in;-o-transition:all .15s ease-in;transition:all .15s ease-in;-webkit-transform:translate3d(0, 0, 0);-moz-transform:translate3d(0, 0, 0);-ms-transform:translate3d(0, 0, 0);-o-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0);position:relative;list-style:none;white-space:nowrap}.carousel .thumb{-webkit-transition:border .15s ease-in;-moz-transition:border .15s ease-in;-ms-transition:border .15s ease-in;-o-transition:border .15s ease-in;transition:border .15s ease-in;display:inline-block;margin-right:6px;white-space:nowrap;overflow:hidden;border:3px solid #fff;padding:2px}.carousel .thumb:focus{border:3px solid #ccc;outline:none}.carousel .thumb.selected,.carousel .thumb:hover{border:3px solid #333}.carousel .thumb img{vertical-align:top}.carousel.carousel-slider{position:relative;margin:0;overflow:hidden}.carousel.carousel-slider .control-arrow{top:0;color:#fff;font-size:26px;bottom:0;margin-top:0;padding:5px}.carousel.carousel-slider .control-arrow:hover{background:rgba(0,0,0,0.2)}.carousel .slider-wrapper{overflow:hidden;margin:auto;width:100%;-webkit-transition:height .15s ease-in;-moz-transition:height .15s ease-in;-ms-transition:height .15s ease-in;-o-transition:height .15s ease-in;transition:height .15s ease-in}.carousel .slider-wrapper.axis-horizontal .slider{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-horizontal .slider .slide{flex-direction:column;flex-flow:column}.carousel .slider-wrapper.axis-vertical{-ms-box-orient:horizontal;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:-moz-flex;display:-webkit-flex;display:flex}.carousel .slider-wrapper.axis-vertical .slider{-webkit-flex-direction:column;flex-direction:column}.carousel .slider{margin:0;padding:0;position:relative;list-style:none;width:100%}.carousel .slider.animated{-webkit-transition:all .35s ease-in-out;-moz-transition:all .35s ease-in-out;-ms-transition:all .35s ease-in-out;-o-transition:all .35s ease-in-out;transition:all .35s ease-in-out}.carousel .slide{min-width:100%;margin:0;position:relative;text-align:center}.carousel .slide img{width:100%;vertical-align:top;border:0}.carousel .slide iframe{display:inline-block;width:calc(100% - 80px);margin:0 40px 40px;border:0}.carousel .slide .legend{-webkit-transition:all .5s ease-in-out;-moz-transition:all .5s ease-in-out;-ms-transition:all .5s ease-in-out;-o-transition:all .5s ease-in-out;transition:all .5s ease-in-out;position:absolute;bottom:40px;left:50%;margin-left:-45%;width:90%;border-radius:10px;background:#000;color:#fff;padding:10px;font-size:12px;text-align:center;opacity:0.25;-webkit-transition:opacity .35s ease-in-out;-moz-transition:opacity .35s ease-in-out;-ms-transition:opacity .35s ease-in-out;-o-transition:opacity .35s ease-in-out;transition:opacity .35s ease-in-out}.carousel .control-dots{position:absolute;bottom:0;margin:10px 0;padding:0;text-align:center;width:100%;z-index:1}@media (min-width: 960px){.carousel .control-dots{bottom:0}}.carousel .control-dots .dot{-webkit-transition:opacity .25s ease-in;-moz-transition:opacity .25s ease-in;-ms-transition:opacity .25s ease-in;-o-transition:opacity .25s ease-in;transition:opacity .25s ease-in;opacity:.3;filter:alpha(opacity=30);box-shadow:1px 1px 2px rgba(0,0,0,0.9);background:#fff;border-radius:50%;width:8px;height:8px;cursor:pointer;display:inline-block;margin:0 8px}.carousel .control-dots .dot.selected,.carousel .control-dots .dot:hover{opacity:1;filter:alpha(opacity=100)}.carousel .carousel-status{position:absolute;top:0;right:0;padding:5px;font-size:10px;text-shadow:1px 1px 1px rgba(0,0,0,0.9);color:#fff}.carousel:hover .slide .legend{opacity:1}
</style><style data-styled="active" data-styled-version="5.3.5"></style><style data-emotion="css" data-s=""></style></head><body><noscript>You need to enable JavaScript to run this app.</noscript><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-5689BD5H8V"></script><script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script><div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/culture" aria-current="page" class="active"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">문화 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/2AFi4qtnZ_Y" target="_blank" rel="noreferrer"><img src="/fe9f097adb1e4aa4f19395099eaabff7.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">BAMBOO</p><p class="sc-gsnTZi bfvMEX">2014년에 설립된 밤부는 캐주얼 사진동아리입니다. 촬영 장비에 구애를 받지 않고 사진찍고자 하는 마음만 있다면 누구나 함께 할 수 있는 사진 동아리입니다. 매달 정기출사와 1년에 2번 사진전을 개최합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/j8g_kJwf_Kw" target="_blank" rel="noreferrer"><img src="/3a57d17fa6dfffde888a75e5f2928ac0.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">두바퀴</p><p class="sc-gsnTZi bfvMEX">"두바퀴"는 바이크 소지 여부와 상관없이, 바이크를 좋아하거나 관심있는 사람이라면 누구나 함께 즐길 수 있는 동아리입니다. 매주 목요일 바이크를 타고 수도권 맛집, 카페 탐방을 하고 한달에 한번 서울을 벗어나 전국팔도 어디든 누비는 MT, 투어를 갑니다. 무려 이륜차로 제주도도 가능!!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/X2accuys6WE" target="_blank" rel="noreferrer"><img src="/b5df4845f3940ee49335c70f457be268.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">마스터</p><p class="sc-gsnTZi bfvMEX">동아리내 100여종 이상의 게임을 보유하고 있어 다양한 종류의 보드게임을 즐길 수 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/jxfPX7vtYoA" target="_blank" rel="noreferrer"><img src="/6311b5a79845d598dae6d9a0e1dddb72.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">MIS</p><p class="sc-gsnTZi bfvMEX">지방에서 고등학교를 마치고 서울로 처음 올라오는 학생들을 위한 서울탐방과, 고등학생 때 해보지 못한 활동들을 동아리를 통해서 여러 사람들과 어울려 할 수 있는 문화생활동아리!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/TW4oJZls09g" target="_blank" rel="noreferrer"><img src="/05c752d9cf8c5586cbf3d9a3ec421617.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">유스호스텔</p><p class="sc-gsnTZi bfvMEX">1967년 설립된 중앙 여행동아리 유스호스텔입니다. 국내 여러 곳 여행 및 타 대학과의 연합 또한 정기적으로 진행 중입니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/pssHAOwATM4" target="_blank" rel="noreferrer"><img src="/67bf3b171f05ae497c535fa4d1eb350a.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">율</p><p class="sc-gsnTZi bfvMEX">몸짓패, 민중 가요를 몸으로 표현</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/IMLooQdIT_8" target="_blank" rel="noreferrer"><img src="/b5560777734023198eff2259f1bcc226.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한손</p><p class="sc-gsnTZi bfvMEX">오랜 역사를 가진 만화 동아리 한손입니다. 매년마다 창립제와 회지 발간, 그 외 다양한 활동을 통해 친목과 경험을 쌓고 있습니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left-width: 1px; border-left-style: solid; border-left-color: grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div></body></html>
'''
base_url = 'https://sejongclubunion.com'

soup = BeautifulSoup(html, 'html.parser')
print(soup)
# print(soup.find('div', id= 'root'))
root = soup.find('div', id= 'root')

club_container = root.find_all('div', class_='club-container')

for cc in club_container:
    # print(cc)
    print()
    print(cc.find('p', class_='cndoxw').text)   # 동아리 이름
    print(cc.find('p', class_='bfvMEX').text)   # 동아리 소개
    print(base_url + '/' + cc.find('img')['src'].split('/')[-1]) # 이미지 경로




