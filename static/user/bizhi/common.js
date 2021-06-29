/*! jquery.cookie v1.4.1 | MIT */
!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?a(require("jquery")):a(jQuery)}(function(a){function b(a){return h.raw?a:encodeURIComponent(a)}function c(a){return h.raw?a:decodeURIComponent(a)}function d(a){return b(h.json?JSON.stringify(a):String(a))}function e(a){0===a.indexOf('"')&&(a=a.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return a=decodeURIComponent(a.replace(g," ")),h.json?JSON.parse(a):a}catch(b){}}function f(b,c){var d=h.raw?b:e(b);return a.isFunction(c)?c(d):d}var g=/\+/g,h=a.cookie=function(e,g,i){if(void 0!==g&&!a.isFunction(g)){if(i=a.extend({},h.defaults,i),"number"==typeof i.expires){var j=i.expires,k=i.expires=new Date;k.setTime(+k+864e5*j)}return document.cookie=[b(e),"=",d(g),i.expires?"; expires="+i.expires.toUTCString():"",i.path?"; path="+i.path:"",i.domain?"; domain="+i.domain:"",i.secure?"; secure":""].join("")}for(var l=e?void 0:{},m=document.cookie?document.cookie.split("; "):[],n=0,o=m.length;o>n;n++){var p=m[n].split("="),q=c(p.shift()),r=p.join("=");if(e&&e===q){l=f(r,g);break}e||void 0===(r=f(r))||(l[q]=r)}return l};h.defaults={},a.removeCookie=function(b,c){return void 0===a.cookie(b)?!1:(a.cookie(b,"",a.extend({},c,{expires:-1})),!a.cookie(b))}});

$(function(){
if( !window.env ) window.env = {};

try{ //延迟加载
    $(".list img").lazyload({
        effect: "fadeIn",
        threshold :350
    });
}catch(err){}

$(".loginbar .in,.loginbar .register").click(function() {
		$("#login_opacity_bg,.tbox").fadeIn(300);
        weixinlogin();
});
//关闭弹窗
$(".tbox .close ").click(function() {
		$(".tbox,#login_opacity_bg").fadeOut(300)
});
//下载壁纸
$(".downpic a").click(function() {
		var id=$(this).attr("data-id");
		$.getJSON('/e/extend/downpic.php?id='+id+'&t='+Math.random(), function(data){
		if(data.msg==0){
			$("#login_opacity_bg,.tbox").fadeIn(300);
			weixinlogin();
			
		}else if(data.msg==1){
		$("#footer").before('<div class="tbox viptps"><div class="close">×</div><div class="vipcon">今日下载量已用完，<a href="/e/member/buygroup/" title="赞助1元即可下载">赞助1元即可下载</a></div></div><div id="login_opacity_bg"></div>');
		vipmsg();
	
		}else if(data.msg==2){
			$("#footer").before('<div class="tbox viptps"><div class="close">×</div><div class="vipcon">今天已下载20张，<a href="/e/member/buygroup/" title="赞助会员">升级年会员海量下载</a></div></div><div id="login_opacity_bg"></div>');
			vipmsg()
		}else if(data.msg==3){
			
			if(data.pic){
				var txt='<br />3秒后继续下载';
				setTimeout('goback(\''+data.pic+'\')',3000);
			}else{
				var txt='';
			}
			$("#footer").before('<div class="tbox viptps"><div class="close">×</div><div class="vipcon">'+data.info+txt+'</div></div><div id="login_opacity_bg"></div>');
            $("#login_opacity_bg,.tbox").fadeIn(300);
            weixinlogin();
			$(".tbox .close ").click(function() {
                $(".tbox,#login_opacity_bg").fadeOut(300).remove();	
			});	
		}else if(data.msg==5){
		$("#footer").before('<div class="tbox viptps"><div class="close">×</div><div class="vipcon">一台电脑免费下载一张，<a href="/e/member/buygroup/" title="赞助送会员">立即赞助送会员</a></div></div><div id="login_opacity_bg"></div>');
		vipmsg();
	
		}else{
			//window.location.href=data.pic; 
           // window.open(data.pic);
           $('<iframe style="display:none;"/>').appendTo('html').attr('src',data.pic);
		}
	});
});

//右侧浮动
$(".btn-phone,.btn-qq,.btn-group,.btn-weixin").hover(function() {
         $(this).find("div").fadeIn("fast");
    },function() {
         $(this).find("div").fadeOut("fast");
}); 
$('.gotop .btn-top').click(function(){
        $('body,html').animate({scrollTop: '0px'}, 500);
});
//$.cookie("isclose",'0',{path:'/'});
if($(".view").length>0){
//通栏广告
$(document).on('click', '.banner-top .close', function () {
    $(".banner-top").remove();
   /* $.ajax({type : "get",async:false,url : "/e/extend/ajax.php",data:{"enews":"banner"},dataType : "jsonp",jsonp: "jsonpcallback",success : function(data){
        }
    });*/
    var date = new Date();
    var m = 720; 
    date.setTime(date.getTime()+(m * 60 * 1000)); 
    $.cookie("zkhanisclose",'1',{expires: date,path:'/'});
}); 

if($.cookie("zkhanisclose") != '1' && bannerlink){
    var barmbg='';
    if(bannerm){
        barmbg='style="background:url('+bannerm+') no-repeat center"';
    }
    $(".header").after('<div class="banner-top" style="background:url('+bannerimg+') no-repeat center"><a href="'+bannerlink+'" target="_blank"><p class="w" '+barmbg+'></p></a><span class="close"></span></div>');
}
}
//gotop
$(window).scroll(function(){if ($(window).scrollTop()>200){$(".gotop .btn-top").css("display","block"); }else{$(".gotop .btn-top").hide();}});

});

function weixinlogin(){
    $.ajax({type : "get",async:false,url : "/e/extend/weixin/",data:{"enews":"qrcode"},dataType : "jsonp",jsonp: "jsonpcallback",success : function(data){ 
       // console.log(data);
        if(data.status==1){
            $(".wxdlqrcode").html('<img src="'+data.weixin+'" />');
            if(data.code){
                $(".wxdl span").remove();
                $(".wxdl p").text("微信扫码关注公众号");
                $(".wxdl p").after("<span>并发送数字<em>"+data.code+"</em>至公众号<i>发送后未登录，请重新发送</i></span>");
            }
            time();
            function time(){
              queryorder(data.id);
              setTimeout(time,1500); //time是指本身,延时递归调用自己,100为间隔调用时间,单位毫秒
            }
        }else if(data.status==2){//关闭
           $(".wxdl span").remove();
            $(".wxdlqrcode").html('<img src="'+data.weixin+'" />');
            $(".wxdl p").text("微信扫码关注公众号");
            $(".wxdl p").after("<span>可以留言想要的壁纸</span>");
        }
    } });
}
var timeout = true; //启动及关闭按钮
function queryorder(id){
     $.ajax({type : "get",async:false,url : "/e/extend/weixin/",data:{"enews":"check"},dataType : "jsonp",jsonp: "jsonpcallback",success : function(data){ 
       // console.log(data);
        if (data.status==1) {
			location.reload();
        } else if(data.status==2){
            timeout = false;
            alert("会员未审核，不可用此登录");
            $(".wxdlqrcode").html('');
        }
        }
    });
}
function goback(url)
{
	//window.open(url);
    //window.location.href=url; 
    $('<iframe style="display:none;"/>').appendTo('html').attr('src',url);
}
function vipmsg(){
		$("#login_opacity_bg,.tbox").fadeIn(300);
		weixinlogin();
		//关闭弹窗
		$(".tbox .close ").click(function() {
			$(".tbox,#login_opacity_bg").fadeOut(300);
			window.location.href="/e/member/buygroup/"; 
		});	
}

(function(a,b,c,d){var e=a(b);a.fn.lazyload=function(c){function i(){var b=0;f.each(function(){var c=a(this);if(h.skip_invisible&&!c.is(":visible"))return;if(!a.abovethetop(this,h)&&!a.leftofbegin(this,h))if(!a.belowthefold(this,h)&&!a.rightoffold(this,h))c.trigger("appear"),b=0;else if(++b>h.failure_limit)return!1})}var f=this,g,h={threshold:0,failure_limit:0,event:"scroll",effect:"show",container:b,data_attribute:"src",skip_invisible:!0,appear:null,load:null};return c&&(d!==c.failurelimit&&(c.failure_limit=c.failurelimit,delete c.failurelimit),d!==c.effectspeed&&(c.effect_speed=c.effectspeed,delete c.effectspeed),a.extend(h,c)),g=h.container===d||h.container===b?e:a(h.container),0===h.event.indexOf("scroll")&&g.bind(h.event,function(a){return i()}),this.each(function(){var b=this,c=a(b);b.loaded=!1,c.one("appear",function(){if(!this.loaded){if(h.appear){var d=f.length;h.appear.call(b,d,h)}a("<img />").bind("load",function(){c.hide().attr("src",c.data(h.data_attribute))[h.effect](h.effect_speed),b.loaded=!0;var d=a.grep(f,function(a){return!a.loaded});f=a(d);if(h.load){var e=f.length;h.load.call(b,e,h)}}).attr("src",c.data(h.data_attribute))}}),0!==h.event.indexOf("scroll")&&c.bind(h.event,function(a){b.loaded||c.trigger("appear")})}),e.bind("resize",function(a){i()}),/iphone|ipod|ipad.*os 5/gi.test(navigator.appVersion)&&e.bind("pageshow",function(b){b.originalEvent.persisted&&f.each(function(){a(this).trigger("appear")})}),a(b).load(function(){i()}),this},a.belowthefold=function(c,f){var g;return f.container===d||f.container===b?g=e.height()+e.scrollTop():g=a(f.container).offset().top+a(f.container).height(),g<=a(c).offset().top-f.threshold},a.rightoffold=function(c,f){var g;return f.container===d||f.container===b?g=e.width()+e.scrollLeft():g=a(f.container).offset().left+a(f.container).width(),g<=a(c).offset().left-f.threshold},a.abovethetop=function(c,f){var g;return f.container===d||f.container===b?g=e.scrollTop():g=a(f.container).offset().top,g>=a(c).offset().top+f.threshold+a(c).height()},a.leftofbegin=function(c,f){var g;return f.container===d||f.container===b?g=e.scrollLeft():g=a(f.container).offset().left,g>=a(c).offset().left+f.threshold+a(c).width()},a.inviewport=function(b,c){return!a.rightoffold(b,c)&&!a.leftofbegin(b,c)&&!a.belowthefold(b,c)&&!a.abovethetop(b,c)},a.extend(a.expr[":"],{"below-the-fold":function(b){return a.belowthefold(b,{threshold:0})},"above-the-top":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-screen":function(b){return a.rightoffold(b,{threshold:0})},"left-of-screen":function(b){return!a.rightoffold(b,{threshold:0})},"in-viewport":function(b){return a.inviewport(b,{threshold:0})},"above-the-fold":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-fold":function(b){return a.rightoffold(b,{threshold:0})},"left-of-fold":function(b){return!a.rightoffold(b,{threshold:0})}})})(jQuery,window,document);

$(function(){
    var $page = $(".page");
    if($page.length > 0){
        $next = $page.find(':contains(下一页)');
        var $last = $next.length > 0 ? $next.prev('a') : $page.find('b:last');
        var maxPage = ~~$last.text() * 1;
        var thisPage = ~~$page.find('b:first').text() * 1;
        var urlStr = getPageUrl();
	
        
        // var code = '<span class="text">共'+maxPage+'页&nbsp;&nbsp;到第</span><input type="text" name="page" /><span>页</span><a href="javascript:;" id="jump-url">确定</a>';
		// if(maxPage > 0){
		// 	$page.append(code);
		// }
        
        
        $('#jump-url').click(function(){
            var value = $page.find('input[name="page"]').val();
            value = ~~value;
            var maxPage = $('#count').text().charAt(1);
            if(value === 0){
                alert('请输入数字');
            }else if(value > maxPage){
                alert('超过最大页了');
            }else{
                goUrl = "/user/index/" + value
                window.location.href = goUrl;
            }
        });
		
		$page.find('input[name="page"]').keyup(function(event){
            if(event.keyCode == 13){
                $('#jump-url').click();
            }
        });
        if($next.length > 0){
            var nexturl=$next.attr("href");
            $(".slist ul").append('<li class="nextpage"><a href="'+nexturl+'"><p>下一页<br>更多精彩</p></a></li>');
        }
    }

    function getPageUrl(){
        var url = window.location.href.split('://');
        var arr = url[1].split('/index');
        if(url[1].indexOf('/e/search/result/') > 0){
			arr = url[1].split('?');
			var sid = url[1].split('searchid=')[1].split('&')[0];
			arr[1] = 'page=[#page]&searchid='+sid;
			url[1] = arr.join('?');
		}else if(arr.length > 1){
            arr[1] = '[@page].html';
            url[1] = arr.join('/index');
        }else{
            url[1] += '/index[@page].html';
            url[1] = url[1].replace('//' , '/');
        }
        var purl = url.join('://');
        return purl;
    }
    
    
});