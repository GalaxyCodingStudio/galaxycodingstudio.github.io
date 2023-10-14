document.write("	<div class=\"screen\">");
document.write("		<nav class=\"navbar navbar-expand-lg nav\">");
document.write("			<div class=\"container-fluid\">");
document.write("				<button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">");
document.write("					<span class=\"navbar-toggler-icon\"></span>");
document.write("				</button>");
document.write("				<div class=\"collapse navbar-collapse\" id=\"navbarSupportedContent\">");
document.write("					<ul class=\"navbar-nav me-auto mb-2 mb-lg-0\">");
document.write("						<li class=\"nav-item\"><a class=\"navbar-brand logo-image index-logo-img\" href=\"/main\"><img id=\"logo-image\" src=\"/img/图片2.png\" alt=\"logo\" alt=\"银河编程网\" width=\"130\" title=\"首页\"></a></li>");
document.write("			<div class=\"navbar-nav-right-box\">");
document.write("			   <ul class=\"navbar-nav navbar-nav-right\">   ");
document.write("            <button class=\"btn btn-outline-secondary\" onclick=\"location.href='/chanping'\">我们的产品</button>");
document.write("            <button class=\"btn btn-outline-secondary\" onclick=\"location.href='/admin'\">管理员后台</button>");
document.write("            <button class=\"btn btn-outline-secondary\" onclick=\"location.href='/doc'\">文档站</button>");
document.write("            <button class=\"btn btn-outline-secondary\" onclick=\"location.href='/about'\">关于我们</button>");
document.write("            <button class=\"btn btn-outline-secondary\" onclick=\"location.href='/doc/2'\">赞助我们</button>");
document.write("            <span style=\"margin-left:50px\"></span>");
document.write("            <button onclick=\"toggleDarkMode()\" class=\"btn btn-outline-secondary\">深色模式</a>");
document.write("            <button onclick=\"toggleLightMode()\" class=\"btn btn-outline-secondary2\">浅色模式</a>");
document.write("				</ul>");
document.write("							   </div>");
document.write("	    </div>");
document.write("       </nav>");
document.write("	</div>");
document.write("	<div class=\"i\"></div>");
function toggleDarkMode() {
  document.body.classList.add('dark-mode');
  var targetElement1 = document.querySelector('.screen');
  var logoImage = document.getElementById('logo-image');
  logoImage.src = '/img/图片1.png';
  targetElement1.classList.add('screen2');
}

function toggleLightMode() {
  document.body.classList.remove('dark-mode');
  var targetElement1 = document.querySelector('.screen');
  var logoImage = document.getElementById('logo-image');
  logoImage.src = '/img/图片2.png';
  targetElement1.classList.remove('screen2');
}

function initializeTheme() {
  const preferredTheme = localStorage.getItem('preferred-theme');

  // 根据用户的首选主题设置页面样式
  if (preferredTheme === 'dark' || (preferredTheme === null && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    toggleDarkMode();
  } else {
    toggleLightMode();
  }

  // 监听系统模式的变化
  window.matchMedia('(prefers-color-scheme: dark)').addListener(event => {
    if (event.matches) {
      toggleDarkMode();
    } else {
      toggleLightMode();
    }
  });
}

initializeTheme();