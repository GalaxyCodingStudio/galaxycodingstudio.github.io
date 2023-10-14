import os
import random
import time
import threading
import os.path
import flask
import requests as rq
import datetime
from datetime import datetime

from flask import Flask, request, jsonify, send_file, session, make_response
from flask_mail import Mail

import json
from tkinter import Tk, Entry, Button
from flask_cors import CORS

app = flask.Flask(__name__)
app.secret_key = b'_114514\n\xec]/'


app.config['MAIL_SERVER'] = 'smtp.163.com'  # 163邮箱的SMTP服务器地址
app.config['MAIL_PORT'] = 465  # SMTP端口，一般为465或25
app.config['MAIL_USE_TLS'] = False  # 不使用TLS
app.config['MAIL_USE_SSL'] = True  # 使用SSL加密



def _reload():
    global forbidden, common, ppage
    forbidden = eval(open("forbidden.json", encoding="UTF-8").read())
    common = eval(open("common/data/common.json", encoding="UTF-8").read())

    print("重载完成。")


_reload()

def page4():
    return send_file("404/index.html")

def create_window():
    global w
    w = Tk()
    w.title("Flask GUI")
    e = Entry(w, font=["Consolas", 10, ""])
    e.pack()
    b1 = Button(
        w,
        text="Enter CMD",
        command=lambda: os.system(e.get()),
        font=["Consolas", 10, ""],
    )
    b2 = Button(
        w, text="Enter CPY", command=lambda: exec(e.get()), font=["Consolas", 10, ""]
    )
    b1.pack()
    b2.pack()
    w.mainloop()


@app.route("/")
def nonepage():
    return flask.redirect("/index.html")


@app.route("/<path:page>")
def mainpage(page):
    for i in forbidden:
        if i in page:
            return common["forbidden_tip"]
    if os.path.isdir(page):
        page = page
        page += "/index.html"
    try:
        return flask.send_file(page)
    except FileNotFoundError:
        return page4()
    



@app.route("/api/quote")
def generate_random_quote():
    quotes = [
        "欢迎来到银河编程 Welcome to GalaxyCode",
        "山重水复疑无路，make后面不加to",
        "想致富，先撸树。",
        "要是追你那么容易，那我爱你干嘛",
        "花开花落终有时，相逢相聚无本意",
        "1+1+4+(5+1+4+1+9-1+9-8-1)x0=6",
        "你干嘛哈哈哎哟",
        "千里之行，始于足下",
        "没有BUG的代码是不完美的！",
        "失败是成功之母，想失败，就多成功。",
        "菠萝biu~菠萝biu~",
        "恐龙抗狼抗狼抗",
        "最迷人的最危险",
        "星星之火，可以燎原",
        "大漠沙如雪，燕山月似钩。",
        "氢氢敲醒沉睡的心灵",
        "瘦巴巴的老爷们，一起走哇",
        "9（6翻了）",
        "发掘无限创意，开启编程之旅。",
        "不识庐山真面目，只缘身在此山中",
        "我命由我不由天",
        "记忆是痛苦的根源。",
        "野旷天低树，江清月近人",
        "世上无难事，只要肯放弃。",
        "我就是小气，想让你成为我一个人的专利",
        "人生中最大的遗憾，就是没和初恋在一起吧...",
        "欲买桂花同载酒，终不似、少年游。",
        "世界那么大，我想去看看",
        "原神，启动！",
        "海内存知己，天涯若比邻",
        "离离原上谱，越来越离谱",
        "学好数理化，走遍天下都不怕",
        "木叶飞舞之处，火亦生生不息",
        "欲买桂花同载酒，荒泷天下第一斗。",
        "三长一短选最短，三短一长选最长",
        "人是要整活的。因为不整活，不就死了吗？",
        "Nya~",
        "看着风景美景美如画，本想吟诗赠天下。奈何本君没文化，一句卧槽风好大。",
        "shift",
        "有志者事竟成",
        "啊巴啊巴啊巴",
        "风吹柳叶遮黄雀，薄翅不觉已落蝉。",
        "忽如一夜春风来，千树万树梨花开。",
        "任何邪恶，终将绳之以法",
        "妮可妮可妮~",
        "盼望着，盼望着，东风来了，春天的脚步近了。",
        "其实世界上没有路，走的人多了，变形成了路。",
        "与时间赛跑",
        "一年之计在于春",
        "一日之计在于晨",
        "你总是这样轻言放弃的话，无论多久都只会原地踏步",
        "天空是青红色，窗外有核辐射。",
        "趁着年轻，好好犯病。",
        "海上生明月，天涯共此时。",
        "没有人类的文明，毫无意义。",
        "让人类保持理智，确实是一种奢求。",
        "花有重开日，人无再少年。",
        "6",
        "即使听一万遍反方向的钟，你也不回来.",
        "尽管我拥有了全世界，也还是没法拥有你.",
        "只有失去了才懂得珍惜.",
        "珍惜眼前人，心存感恩。",
        "积极向上，无所畏惧。",
        "勇往直前，才能到达目标。",
        "善待他人，善待自己。",
        "热爱生活，享受每一天。",
        "山重水复疑无路，柳暗花明又一村。",
        "春江潮水连海平，海上明月共潮生。",
        "人间四月芳菲尽，山寺桃花始盛开。",
        "枯藤老树昏鸦，小桥流水人家。",
        "千山鸟飞绝，万径人踪灭。",
        "为什么太阳不结婚？因为太阳到处晒。",
        "为什么刘备顶着个大光头？因为他是个“无发”之人。",
        "有一只猫叫三条腿，它一跳就变成了二条腿。",
        "什么动物最喜欢读书？书虫。",
        "心事随风，无处安放。",
        "无助的孤单，一遍又一遍。",
        "失去了你，失去了整个世界。",
        "痛彻心扉，难以自拔。",
        "风吹散了我的梦，泪湿了我的夜。",
        "寂寞如影，无人能懂。",
        "心如刀割，痛不欲生。",
        "默默流淌的泪水，谁能懂得？",
        "时光老去，回忆阑珊。",
        "回首往事，泪水满满。",
        "心碎成千上万的碎片。",
        "孤独是最深的伤痛。",
        "失去爱的人，是多么的脆弱和孤单。",
        "回首过往，心如刀绞。",
        "伤感的心情，无法言喻。",
        "演绎着自己的悲伤，无人识别。",
        "那些过去的泪水，再也洗不净心灵。",
        "心如寒冬，冰冷无比。",
        "冷漠的世界，没有温暖可依靠。",
        "失去了你，心已被撕裂。",
        "无声的哭泣，淹没在黑暗中。",
        "冷漠的背影，让人心伤。",
        "无言的离别，痛彻心扉。",
        "心如断线的风筝，飘荡在空旷的天空。",
        "梦醒时分，泪已成河。",
        "刻骨铭心的伤害，犹如刀割。",
        "遗憾的悲伤，无法填补。",
        "孤独是心底最深的伤痛。",
        "无尽的寂寞，漫过心间。",
        "思念像一缕清风，轻轻拂过心间。",
        "心之所动，泪随所溢。",
        "遥望远方，离别如此滋味。",
        "浮生若梦，情深难舍。",
        "失去不是最痛苦的事，最痛苦的是爱过。",
        "冰冷的夜色里，心在微微颤抖。",
        "回忆是最美的刺痛，带来岁月的沉重。",
        "难过的日子里，寂寞如影相伴。",
        "心碎成一地的瓣瓣花，无人采撷。",
        "断了线的风筝，追不回失去的曾经。",
        "冷漠的眼神，让我心如刀割。",
        "纵然泪眼朦胧，也要坚强面对。",
        "世间万物，唯有孤独永恒。",
        "为什么鸟儿不会玩扑克牌？因为它会打鸟语。",
        "青山一道同云雨，明月何曾是两乡。",
        "采得百花成蜜后，为谁辛苦为谁甜。",
        "花开堪折直须折，莫待无花空折枝。",
        "山外青山楼外楼，西湖歌舞几时休。",
        "问余何意栖碧山，笑而不语心自闲。",
        "千年之前，悠然诗琴麻衫岭。",
        "春风又绿江南岸，明月何时照我还。",
        "采菊东篱下，悠然见南山。",
        "夕阳无限好，只是近黄昏。",
        "满地黄花堆积。憔悴损，如今有谁堪摘？",
        "两个黄鹂鸣翠柳，一行白鹭上青天。",
        "不畏浮云遮望眼，只缘身在最高层。",
        "东篱乌啼，一夜湘君百忧愁。",
        "白日依山尽，黄河入海流。",
        "黄河远上白云间，一片孤城万仞山。",
        "梅子黄时日日晴，小溪泛尽却山行。",
        "遥知不是雪，为有暗香来。",
        "碧云天，黄叶地，秋色连波，波上寒烟翠。",
        "小楼昨夜又东风，故国不堪回首月明中。",
        "天若有情天亦老，人间正道是沧桑。",
        "小明对小红说：“你们班上有个男生长得像章鱼。”, 小红问：“长得像章鱼？为什么？”, 小明回答：“因为他有八个妈妈！”",
    ]

    random_quote = random.choice(quotes)
    
    data = {"quote": random_quote}
    return json.dumps(data)



def update_last_login_time(username):
    user_dir = os.path.join("users", username)
    user_file = os.path.join(user_dir, "user.json")

    if os.path.exists(user_file):
        with open(user_file, "r+", encoding="UTF-8") as f:
            user_data = json.load(f)
            user_data["last_login_time"] = str(datetime.now())
            f.seek(0)
            json.dump(user_data, f, indent=4)
            f.truncate()
def verify_password(username, password):
    session['username'] = username
    user_dir = os.path.join("users", username)
    user_file = os.path.join(user_dir, "user.json")

    if not os.path.exists(user_file):
        return False

    with open(user_file, "r", encoding="UTF-8") as f:
        user_data = json.load(f)

    if user_data["username"] == username and user_data["password"] == password:
        update_last_login_time(username)
        return True
    else:
        return False
from flask import make_response
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if not username or not password:
        return jsonify({"type": "error", "code": 400, "error": "用户名和密码不能为空!"}), 400

    if verify_password(username, password):
        response = make_response(jsonify({"type": "success", "message": "登录成功"}))
        response.set_cookie('username', username)
        return response, 200
    else:
        return jsonify({"type": "error", "code": 401, "error": "密码不正确"}), 401
    

    
@app.route("/logout", methods=['POST'])
def logout():
    request = flask.request  # 获取request对象
    # 删除存储在cookie中的用户名
    response = flask.redirect('/login')  # 重定向到登录页面
    response.delete_cookie('username')
    return response


import time
from collections import defaultdict
ip_register_time = defaultdict(float)

prohibited_words = ["官方", "52Lzx", "涛", "琦怪的人呀", "dqt", "daiqitao", "DAIQITAO", "琦", "乞讨", "中国", "CN", "China", "习近平", "廖", "瑄", "组织", "傻", "病", "死", "妈", "脑瘫", "脑残", "逼", "sb"]

@app.route("/api/register", methods=['POST'])
def registerP():
    if not os.path.exists("users"):
        os.makedirs("users")
    ip = request.remote_addr

    current_time = time.time()
    if current_time - ip_register_time[ip] < 30:
        return jsonify({"type": "error", "code": "", "error": "1010", "message": "请求频繁！请30秒后再进行注册请求！"})
    
    ip_register_time[ip] = current_time
    ip_register_count = defaultdict(int)
    if ip in ip_register_count and ip_register_count[ip] > 0:
      return jsonify({"type": "error", "code": "", "error": "1011", "message": "同一IP地址只能注册一个账号！"})
    
    ip_register_count[ip] += 1

    data = request.json
    if not data:
        return jsonify({"type": "error", "code": "", "error": "1000", "message": "请求数据为空！"})

    username = data.get("username")
    password = data.get("password")

    if not username:
        return jsonify({"type": "error", "code": "", "error": "1001", "message": "用户名不能为空！"})
    if any(word in username for word in prohibited_words):
        return jsonify({"type": "error", "code": "", "error": "1008", "message": "用户名含有违禁词！"})

    if not password:
        return jsonify({"type": "error", "code": "", "error": "1002", "message": "密码不能为空！"})

    if os.path.exists("users/" + username):
        return jsonify({"type": "error", "code": "", "error": "1007", "message": "用户名已存在！"})

    user_count = len(os.listdir('users'))
    new_id = str(user_count + 1)

    user_dir = os.path.join("users", username)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    user_file = os.path.join(user_dir, "user.json")
    user = {
        "id": new_id,
        "username": username,
        "password": password,
    }

    with open(user_file, "w", encoding="UTF-8") as f:
        json.dump(user, f)

    message = "注册成功！ 用户名：{}，ID：{}".format(username, new_id)
    return make_response(jsonify({"type": "OK", "error": "", "code": new_id, "message": message}))




@app.route('/api/email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        sender = request.form['sender']  # 发件人邮箱地址
        password = request.form['password']  # 发件人邮箱密码
        recipient = request.form['recipient']  # 收件人邮箱地址
        subject = request.form['subject']  # 邮件主题
        body = request.form['body']  # 邮件内容

        try:
            # 创建邮件对象
            msg = Message(subject, sender=sender, recipients=[recipient])
            msg.body = body

            # 更新邮件服务器配置
            app.config['MAIL_USERNAME'] = sender
            app.config['MAIL_PASSWORD'] = password

            # 发送邮件
            mail.send(msg)
            return 'Email sent!'
        except Exception as e:
            return str(e)
        




def onserver():
    global w
    time.sleep(0.5)
    os.system("cls&start server.py")
    print("欢迎使用 ©DAIQITAO-v1.0 服务端。")
    print("服务端已准备就绪！\n开始记录日志：\n")

    threading.Thread(target=create_window).start()

    app.run(host="0.0.0.0", port=80)
    print("服务端已停止运行。\n")
    if 'w' in globals():
        w.destroy()

if __name__ == "__main__":
    threading.Thread(target=onserver).start()