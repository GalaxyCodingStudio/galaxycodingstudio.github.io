document.write("<div id=\"overlay\"></div>")
var overlay = document.getElementById("overlay");

// 创建样式元素并设置蒙版样式
var styleElement = document.createElement("style");
styleElement.innerHTML = `
    /* 定义蒙版样式 */
    #overlay {
        display: none; /* 最初不显示 */
        position: fixed; /* 固定在窗口上方 */
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.93); /* 半透明黑色背景 */
        z-index: 99999999999999999999999999999999999999999999999999999; /* 设置z-index使其覆盖其他元素 */
    }`

document.head.appendChild(styleElement);

// 创建并设置文字元素
var text = document.createElement("div");
text.classList.add("text");
text.innerHTML = "网站更新升级中，暂时无法使用…";

// 设置文字样式
text.style.position = "absolute";
text.style.top = "50%";
text.style.left = "50%";
text.style.transform = "translate(-50%, -50%)";
text.style.color = "#fff";
text.style.textAlign = "center";

// 将文字元素添加到蒙版中
overlay.appendChild(text);

function checkWidth() {
    if (window.innerWidth < 3000) {
        overlay.style.display = "block";
    } else {
        overlay.style.display = "none";
    }
}

// 页面加载时检查页面宽度，并注册窗口调整大小的事件监听器
window.addEventListener("load", checkWidth);
window.addEventListener("resize", checkWidth);
