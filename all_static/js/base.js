$('body a').attr('target', '_blank');


$(function(){

	document.addEventListener('keydown', function(e){
          e = window.event || e;
         var keycode = e.keyCode || e.which;

         if(e.ctrlKey && keycode == 87){    
            e.preventDefault();
            window.event.returnValue = false;
         }else if(e.ctrlKey && keycode == 80){    
            e.preventDefault();
            window.event.returnValue = false;
         }else if(e.ctrlKey && keycode == 82){    
            e.preventDefault();
            window.event.returnValue= false;
         }else if(e.ctrlKey && keycode== 83){  
            e.preventDefault();
            window.event.returnValue= false;
         }else if(e.ctrlKey && keycode == 72){    
            e.preventDefault();
            window.event.returnValue= false;
         }else if(e.ctrlKey && keycode == 74){    
            e.preventDefault();
            window.event.returnValue= false;
         }else if(e.ctrlKey && keycode == 75){    
            e.preventDefault();
            window.event.returnValue= false;
         }else if(e.ctrlKey && keycode == 78){    
            e.preventDefault();
            window.event.returnValue= false;
         }
	});
});

$(".menu-title i").click(function () {
   $(this).parent().parent().next().toggleClass('hides');
    if ($(this).hasClass('fa-plus')){
        $(this).removeClass('fa-plus');
        $(this).addClass('fa-minus');
    }else {
        $(this).removeClass('fa-minus');
        $(this).addClass('fa-plus');

    }
});

$(window).scroll(function () {
        if ($(window).scrollTop() < 500 ){
            $('#back-to-top').addClass('hides');
        } else {
            $('#back-to-top').removeClass('hides');
        }
});

$('#back-to-top').click(function () {
    $(window).scrollTop(0);
});


function click(e) {
if (document.all) {
if (event.button==2||event.button==3) { alert("欢迎光临寒舍，有什么需要帮忙的话，请与站长联系！谢谢您的合作！！！");
oncontextmenu='return false';
}
}
if (document.layers) {
if (e.which == 3) {
oncontextmenu='return false';
}
}
}
if (document.layers) {
document.captureEvents(Event.MOUSEDOWN);
}
document.onmousedown=click;
document.oncontextmenu = new Function("return false;")
document.onkeydown =document.onkeyup = document.onkeypress=function(){
if(window.event.keyCode == 123) {
window.event.returnValue=false;
return(false);
}
}
