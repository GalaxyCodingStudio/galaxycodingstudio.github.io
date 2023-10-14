        // 发起GET请求
        function fetchRandomQuote() {
            fetch('https://api-omega-opal.vercel.app/api/quote')
                .then(response => response.json())
                .then(data => {
                    if (data && data.quote) {
                        document.getElementById("quote").innerHTML = data.quote;
                    }
                })
                .catch(error => console.log('Error:', error));
        }

        window.onload = fetchRandomQuote;  // 页面加载时自动获取随机文案