document.write("<div id=\"overlay\"><span class=\"text\">网站升级中，暂时无法使用…</span><br><br><a href=\"/chanping\" style=\"color:#fff\" class=\"footer-a\">< 我们的产品 ></a><br><br><a href=\"/doc/2\" style=\"color:#fff\" class=\"footer-a\">< 赞助我们 ></a><br><br></div>");
document.head.appendChild(styleElement);
var overlay = document.getElementById("overlay");
    document.addEventListener("DOMContentLoaded", function() {
        var overlay = document.getElementById("overlay");

        function showOverlay() {
            overlay.style.display = "block";
        }

        function hideOverlay() {
            overlay.style.display = "none";
        }

        var styleElement = document.createElement("style");
        styleElement.innerHTML = `
   #overlay {
        display: none; /* 最初不显示 */
        position: fixed; /* 固定在窗口上方 */
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.93); /* 半透明黑色背景 */
        z-index: 99999999999999999999999999999999999999999999999999999; /* 设置z-index使其覆盖其他元素 */
    }
    .text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #fff;
        text-align: center;
    };
        `;

        document.head.appendChild(styleElement);

        var text = document.querySelector("#overlay .text");
        overlay.appendChild(text);
    });
