$(document).ready(function(e) {
	//转义jQuery防止冲突
	var vj = jQuery;
	//视频控件
	var my_video = document.getElementById("v_profile");
	//控制音量
	my_video.volume = 0.5;
	
	//暂停按钮事件
	vj("#v-pause").click(function(){
		//暂停
		my_video.pause();
		// 追加隐藏样式
		vj("#v-pause").addClass("display-none"); 
		// 移除隐藏样式
		vj("#v-play").removeClass("display-none"); 
	});
	//继续播放按钮事件
	vj("#v-play").click(function(){
		//继续播放
		my_video.play();
		// 追加隐藏样式
		vj("#v-play").addClass("display-none"); 
		// 移除隐藏样式
		vj("#v-pause").removeClass("display-none"); 
	});
	//开启音乐按钮事件
	vj("#v-open-voice").click(function(){
		//开启音乐
		my_video.muted = false;
		// 追加隐藏样式
		vj("#v-open-voice").addClass("display-none"); 
		// 移除隐藏样式
		vj("#v-mute").removeClass("display-none"); 
	});
	//关闭音乐按钮事件
	vj("#v-mute").click(function(){
		//关闭音乐
		my_video.muted = true;
		// 追加隐藏样式
		vj("#v-mute").addClass("display-none"); 
		// 移除隐藏样式
		vj("#v-open-voice").removeClass("display-none"); 
	});
});