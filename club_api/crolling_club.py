
import requests
from bs4 import BeautifulSoup
from club_api.models import Club


html = '''
<!DOCTYPE html>
<!-- saved from url=(0044)https://sejongclubunion.com/centralclub/show -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link rel="icon" href="https://sejongclubunion.com/centralclub/public/favicon.ico"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="세종대학교 총동아리연합회 홈페이지"><link rel="manifest" href="https://sejongclubunion.com/centralclub/public/manifest.json"><title>세종대학교 총동아리연합회</title><link rel="icon" href="https://sejongclubunion.com/favicon.ico"><script defer="defer" src="./show_files/app.88d14a2c4992412493f0.js"></script><style>@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSansNeo.css);</style><style>* {
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
</style><style data-styled="active" data-styled-version="5.3.5"></style></head><body><noscript>You need to enable JavaScript to run this app.</noscript><script async="" src="./show_files/js"></script><script>window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5689BD5H8V');</script><div id="root"><div class="sc-bczRLJ lbyuYo"><div width="100%" height="60px" class="sc-bczRLJ fGdOIA"><div width="100%" height="60px" class="sc-bczRLJ diPTxK"><div class="sc-ftvSup WSaws"><a href="https://sejongclubunion.com/"><div width="60px" height="60px" class="sc-bczRLJ hPTYuP"><img src="./show_files/a660614d029d191959b043e07106455f.png" class="App-logo" alt="logo" height="50px"></div></a><ul width="800px" class="sc-eCYdqJ jVBVqc"><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">총동아리연합회 소개</li><div class="submenu" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="https://sejongclubunion.com/clubunion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">총동아리연합회</button></a></div><div><a href="https://sejongclubunion.com/clubunion/introduce"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">집행부 소개</button></a></div><div><a href="https://sejongclubunion.com/clubunion/way2us"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">찾아오시는 길</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">중앙동아리 소개</li><div class="submenu2" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="https://sejongclubunion.com/centralclub/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">동방 배치도</button></a></div><div><a href="https://sejongclubunion.com/centralclub/show"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공연 분과</button></a></div><div><a href="https://sejongclubunion.com/centralclub/culture"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">문화 분과</button></a></div><div><a href="https://sejongclubunion.com/centralclub/volunteer"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">봉사 분과</button></a></div><div><a href="https://sejongclubunion.com/centralclub/religion"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">종교 분과</button></a></div><div><a href="https://sejongclubunion.com/centralclub/physical"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">체육 분과</button></a></div><div><a href="https://sejongclubunion.com/centralclub/academic"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">학술 분과</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">정보</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="https://sejongclubunion.com/information/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">공약 이행도</button></a></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제휴 사업</button></div><div><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">서동협</button></div><div><a href="https://sejongclubunion.com/information/report"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">예결산 보고</button></a></div><div><a href="https://sejongclubunion.com/information/meetinglog"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회의록</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">소통</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="https://sejongclubunion.com/communication/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">건의 사항</button></a></div><div><a href="https://sejongclubunion.com/communication/petition"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙 개정 요구 청원</button></a></div></div></div><div class="sc-papXJ dwMRqb"><li class="sc-jSMfEi lnZdhU">자료</li><div class="submenu3" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow"></div><div><a href="https://sejongclubunion.com/document/"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">회칙</button></a></div><div><a href="https://sejongclubunion.com/document/election-policy"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">선거 시행 세칙</button></a></div><div><a href="https://sejongclubunion.com/document/form"><button font-size="18px" width="183px" height="40px" class="sc-hKMtZM gRAkDe navigation-submenu-button">제출서류 양식</button></a></div></div></div></ul><div width="32px" class="sc-papXJ dwMRqb"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" color="white" height="32" width="32" xmlns="http://www.w3.org/2000/svg" style="color: white;"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg><div class="submenu4" style="background-color: rgb(173, 30, 45);"><div class="navigation-uparrow2"></div><div><a href="https://sejongclubunion.com/signin/"><button font-size="18px" width="100px" height="40px" class="sc-hKMtZM gorkbp navigation-submenu-button">로그인</button></a></div></div></div></div></div></div><div class="sc-bczRLJ gzshHK"><img src="./show_files/04803832ac76bb44360719b4d0b6a5b9.png" alt="" width="100%"></div><div height="1800px" class="sc-bczRLJ jHPOZq"><div width="200px" class="sc-bczRLJ fRKJDZ"><div width="200px" height="366px" class="sc-bczRLJ kfYqJo"><div height="50px" class="sc-bczRLJ humgJY"><img src="./show_files/22a7b28ae5bd4f5725ec16092465f36f.png" alt="" width="40px"><p font-size="21px" class="sc-gsnTZi jzLTAT">중앙동아리 소개</p></div><div width="200px" class="sc-gKXOVf dvsOip"><ul class="sc-eCYdqJ jyRjrj"><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="https://sejongclubunion.com/centralclub/"><li height="40px" class="sc-jSMfEi SrAva">동방 배치도</li></a></button><button class="sc-hKMtZM uhghM"><a aria-current="page" class="active" href="https://sejongclubunion.com/centralclub/show"><li height="40px" class="sc-jSMfEi SrAva">공연 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="https://sejongclubunion.com/centralclub/culture"><li height="40px" class="sc-jSMfEi SrAva">문화 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="https://sejongclubunion.com/centralclub/volunteer"><li height="40px" class="sc-jSMfEi SrAva">봉사 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="https://sejongclubunion.com/centralclub/religion"><li height="40px" class="sc-jSMfEi SrAva">종교 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="https://sejongclubunion.com/centralclub/physical"><li height="40px" class="sc-jSMfEi SrAva">체육 분과</li></a></button><button class="sc-hKMtZM uhghM"><a href="https://sejongclubunion.com/centralclub/academic"><li height="40px" class="sc-jSMfEi SrAva">학술 분과</li></a></button></ul></div></div></div><div width="1062px" class="sc-bczRLJ iDQkNA"><div width="1000px" height="40px" class="sc-bczRLJ iSXVHH"><p font-size="32px" class="sc-gsnTZi cYtBzp">공연 분과</p></div><div display="block" width="1000px" class="sc-bczRLJ dsaYGm"><div width="1000px" height="50px" class="sc-bczRLJ knUBwB"><p font-size="21px" class="sc-gsnTZi kVyySf">동아리 로고를 클릭하시면 각 동아리 페이지로 이동합니다.</p></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/PMYkIIZhDLE" target="_blank" rel="noreferrer"><img src="./show_files/7037470af7cc6b19bc5f13fe5a5b2c15.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">늘혬코러스</p><p class="sc-gsnTZi bfvMEX">1988년 설립된 중앙 밴드동아리 늘혬코러스입니다. 합주 및 스터디를 통해 정기적으로 공연을 진행하고 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/iIFDstHEnVM" target="_blank" rel="noreferrer"><img src="./show_files/3d1c5400eaa3c1594c68dea6f7d2c622.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">더블랙</p><p class="sc-gsnTZi bfvMEX">세종대학교 흑인음악동아리 더블랙입니다. 저희는 노래를 좋아하는 친구들이 모여 축제, 버스킹 등 여러가지 공연을 하는 동아리입니다. 노래를 좋아하는 분이라면 누구든 환영입니다! </p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><img src="./show_files/5bc0a11bc49b8b1095734761234066d7.png" alt="" width="100%" height="auto"></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">사운드플러스</p><p class="sc-gsnTZi bfvMEX">올해로 30기가 된 밴드 동아리입니다. 동아리명처럼 부원들이 서로 교류하며 좋은 공연을 해오고 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/A-r8QC7DxQU" target="_blank" rel="noreferrer"><img src="./show_files/5d42f4c2871dfca3f51bd1ac2811e3bb.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">세종극회</p><p class="sc-gsnTZi bfvMEX">중앙 연극동아리 ‘세종극회'입니다. 세종극회는 연기, 연출, 소품 등의 분야가 모여 공연 준비를 하여 정기적인 연극 공연을 올립니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/tu1DTkavqOs" target="_blank" rel="noreferrer"><img src="./show_files/9c115a54122e9f4977dc35f6a622ce52.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">소울트레인</p><p class="sc-gsnTZi bfvMEX">2005년 설립된 중앙흑인음악동아리 소울트레인입니다. 주된 활동은 교내 행사에서의 공연과 외부공연장에서의 정기공연이며, 곡 작업 및 스터디, 공연을 위한 연습을 진행합니다. </p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/mVHErWyjVAw" target="_blank" rel="noreferrer"><img src="./show_files/0bbc25724c2e59ca0313e3e5a238ffcc.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">인트로</p><p class="sc-gsnTZi bfvMEX">춤과 랩을 즐기며 열정이 넘치는 중앙힙합동아리로, 교내행사 및 자체 정기공연을 통해 대학생활에 잊지못할 추억을 남겨드립니다!</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/kd98LUhfUgY" target="_blank" rel="noreferrer"><img src="./show_files/5f85497cbb7d922d167ff3ca1c78408b.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">터벌림</p><p class="sc-gsnTZi bfvMEX">1984년 창립된 사물놀이 동아리입니다. 사물놀이 공연을 위해 연습하며, 많은 이에게 국악에 대한 관심을 도모할 수 있도록 노력합니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/t_FiZ7R8RL4" target="_blank" rel="noreferrer"><img src="./show_files/94a0fa9b775c32f993eaeed9f172ba0e.png" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">페이지세븐</p><p class="sc-gsnTZi bfvMEX">락, 어쿠스틱, 발라드, 팝 다해버리는 중앙 밴드동아리 PAGE7입니다. OT, 대동제, 힘미제 등 교내 행사 무대, 타 학교 협동 공연과 초심자들을 위한 악기 레슨을 진행하고 있습니다.</p></div></div></div><div display="inline-block" width="500px" height="210px" class="sc-bczRLJ enYwEW club-container"><div class="sc-bczRLJ gWfVyj club-contents-container"><div width="150px" height="150px" class="sc-bczRLJ kPRhgr club-image-container"><a href="https://youtu.be/uhCJj_hf1Wc" target="_blank" rel="noreferrer"><img src="./show_files/550d5a75df3436c0397cc33528725736.jpg" alt="" width="100%" height="auto"></a></div><div width="310px" class="sc-bczRLJ jUUhDx club-info-container"><p class="sc-gsnTZi cndoxw">한울림</p><p class="sc-gsnTZi bfvMEX">기타를 가르치고 배우고 연주하고 감상하면서 음악을 통해 사람들과 친목을 쌓는 동아리입니다.</p></div></div></div></div></div></div><div class="sc-bczRLJ fnfoDd"><div width="1200px" class="sc-bczRLJ dBMvHw"><div class="sc-bczRLJ eNvhpm"><img src="./show_files/df1675eb8917fddff053e362fdedab4c.png" alt="Sejong Logo" height="50px"><div style="width: 0px; height: 30px; border-left: 1px solid grey; margin-left: 10px; margin-right: 10px;"></div><p font-size="28px" font-family="SeoulLight" class="sc-gsnTZi eoDMQx">총동아리연합회</p></div><div class="sc-bczRLJ kxMSMO"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">05006 서울특별시 광진구 능동로 209 세종대학교 학생회관 408호</p><div style="width: 0px; height: 10px; border-left: 1px solid grey; margin-left: 10px; margin-right: 10px;"></div><div width="80px" class="sc-bczRLJ dYRkdb"><a href="https://sejongclubunion.com/makers"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi Jwivn">만든 사람들</p></a></div></div><div class="sc-bczRLJ hNCVEb"><p font-size="18px" font-family="SeoulLight" class="sc-gsnTZi fkWRaC">Copyright(C) 세종대학교 총동아리연합회 All rights reserved</p></div></div></div></div></div></body></html>
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

    Club.objects.create(
        name = cc.find('p', class_='cndoxw').text,
        introduce = cc.find('p', class_='bfvMEX').text,
        club_logo_url=base_url + '/' + cc.find('img')['src'].split('/')[-1],
    )



