var myURL='/-fs0/4/4/d/home_ad/ad.html';
var myWidth='550';
var myHeight='120';
var popV='width='+myWidth+',height='+myHeight+',titlebar=0,toolbar=0,location=0,menubar=0,scrollbars=no,resizable=yes';
popV+='scrollbars=0,resizable=0,channelmode=0,directories=0,status=0';
if(parseFloat(navigator.appVersion)>=4){var myTI=screen.height/2-myHeight/2;
var myLI=screen.width/2-myWidth/2;popV+=',top='+myTI+',left='+myLI;}
fastClickpopWindow();
function fastClickpopWindow(){window.open(myURL,'etangWHSAD',popV)}

