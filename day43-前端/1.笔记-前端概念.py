'''
前端概念

https://www.cnblogs.com/clschao/articles/10439958.html
https://www.cnblogs.com/clschao/articles/10077261.html
    html - 骨架 最新版本 H5
        <html> </html> 包体标签
        <head> </head> 包着一起页面配置信息
            <title>
            <style>-css
            <script>-动画
            <link/>
            <meta>
                http-equiv
                name='keywords'  -配置网页关键字-搜索
                name='description'  -配置网页说明-搜索
        <body> </body> 主体**
    标签 - 属性 -值
        标签：必须是封闭
            <meta>  自封闭-语法
                <标签名 属性1=“属性值1” 属性2=“属性值2”…… />
             <h1> id="1" </h1>
                <标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>
        属性 ：标签内 如id='ddddd'
        标签分两类
            --内敛标标 不独占一行-
                b | i | u|s|button|span特殊效果
                    br --手动换行
            --块级标签 |行外标签--独占一行
                h1|...|h6 | br换行|hr整行横线|p段落|div分行-无特殊效果|
        标签的嵌套
            --块级标签 可以嵌套行内标签和 某些块级标签
            --<p>较特殊标签不能嵌套|也不能嵌套块级标签-但也不会报错自动被优化




    css -颜色 尺寸
    js -页面动态效果
    jQuery - js的封装版
    bootstrap --所有内容的封装版

域名解释
    域名---对应IP地址
    192.168.1.10：9001 - www.jd.com - DNS解释 {'www.jd.com':'192.168.1.10'}
请求-响应

http协议完整请求信息
    GET / HTTP/1.1
    Host: 127.0.0.1:9001
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
    Sec-Fetch-Dest: document
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: cross-site
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9

http协议完整-响应信息
    b'HTTP/1.1 200 ok \r\n\r\n'   #200状态码表示正常
#-----example for 假网页 客户端发前求服务器响应发一网页
    不用自已写socket 在pycharm 创建html时右上角可直接选用浏览器预览

url--统一资源定位器
    https://www.jd.com/

浏览器的兼容性问题
    IE与其它浏览器的渲染引擎有些标签不一致，大多数一样，开发时要注意
'''
'''
标签
    1.<head> </head> 中常用的四个标签
        <title>
            只有title用户能看到，在上面的任务条上的标签
        <style>-css

        <link/>

        <meta>--文件配置信息，有两个属性
            http-equiv--
            name --
                "keyword"别人搜索你的关键字
                "description"搜索出来时下面的说明文字

    2.<body></body> 用户可见的内容
        h1-h6| button 按钮| b 加粗| i 倾斜| u 加下划线|s 加删除线 （看body演示.html)|a 超链接标签 属性herf;target|br换行|hr整行横线|img 图片|table|p段落|input|div分行-无特殊效果|span用来定义内联(行内)元素-无特殊效果
        内敛标签
            h 标题字大小| button 按钮| b 加粗| i 倾斜|u 加下划线|s 加删除线 （看body演示.html)|a 超链接标签 属性herf;target|
        块级标签
            h1|...|h6 | br换行|hr整行横线|p段落|div分行-无特殊效果|img 图片|table
特殊字符
    空格--不和加多少个空格都只识别为1个空格，所以要表示空格等要用特殊字符表示
    &nbsp 空格|.....|
        input标签-属性
            text | password | date | radio 圆点选择器|checkbox 勾选项|file 文件选择器|submit|reset|button|hidden
            name 属性 == key 提交给后台的key
            value属性 == 提交给后台的values
            checked 属性 -默认选中
            readonly 属性
            disabled 属性

        table 标签-属性
        img 标签-属性
        a 标签-属性

'''


'''二、css 选择器--标签样式 标签{}
<https://www.cnblogs.com/clschao/articles/10082587.html
    语法
    引用方式1 ： head - style -css
    引用方式2： 内敛方式 例<div css> </div>
    引用方式3：外部链接stylesheet
    style样式：

        边框 border

        显示 display
            display:none 隐藏 不占位| visibility:hidden 隐藏 占位
            inline --内联-不能设高宽|不独占一行
            block --块级-能设高宽|独占一行
            inline-block --内联+块级---能设高宽|不独占一行
        盒子模型
            contens-内容 | padding-内边距 | border -边框 | margin 外边距

        浮动 float
            文字环线效果-用于页面布局
                产生父标签塌陷问题-解决-父设高度| clear 清除浮动
        溢出 overflow
            overflow:auto 出现滚动条....
        定位 position
            相对定位 position:relative --保留自已位置|相对自已位移
               绝对定位 position:absolute -以父级标签最近一个有定位的标签为参照
                固定定位 position:fixed -以窗口为参照
                    静态定位  position:static -默认效果，不用设
        层级控制z-index

        透明度  opacity
            color:rgba() | opacity
        锚点
            在a标签url=‘回到位置的id|name

 '''


'''三、js - javascrip 用来做页面动态效果|js是一种全栈开发语言
https://www.cnblogs.com/clschao/articles/10092896.html
    现在公司主要使用emcascrip5.1 -后期版本坑多
    在浏览器console 调试 相当于python 在 cmd 操作
    1.变量
        声明变量 var
            var a=10
                a
                    --显示 10
            命名方式推荐驼峰式：YourName=10;
        数据类型：数值 |
            1.数值-number 类型-整数|小数|科学计算都是 number 类型

                var a=10
                var b=10.1
                var c=123e5
                    typeof a;
            2.字符串-string
                var a='123abc123';
                    字符串转数字--由首个数字到第一个不是数字的数
                       b= parseInt(a)
                       c= parseFloat(a)
                     字符串相加
                        a='hello'
                        b='world'
                        c=a+b
                字符串常用方法 .length计算长度|.trim 删除空格|.chartAt(index)索引|.concat()字符串拼接|.indexof()通过元素找索引,找不到返回-1|
                    .substring(from，to)-不支持负数，一般不用|.slice((from，to)支持负数|.toUpperCase()|.toLowerCase()|.split(de)分割
                        示例
                        a='hello'
                            a.length -->5
                            a.split('e',2) -->(2) ["h", "llo"]---返回数组，后面数值表示返回元素数量
            3.布尔值 true|false-""-0-NaN-undefined都是

        对象类型object
            在JavaScrip 所有都可以定义对象
            例 a =new string ('hello') --> typeof a -> object
            1.数组 类型是object
                a =[1,2,3];  --> typeof a -> object
                a= new Array([1,2,3]);--> typeof a -> object

                数组的方法- .length|.push追加|.pop去尾|unshift头部追加|shift去头
                    例1 数组取数
                        console.log(a[1]); --> 2 数组取数 （用new Array 方法定义的取不出数？）
                    例2 排序.sort()
                        a=[11,4,73,95];  --直接.sort()按首字符排序,按大小排需定义函数(4) [11, 4, 73, 85]
                        升序
                         function SortNumber(a,b) { return a-b };
                            a.sort(SortNumber);  --》 [4, 11, 73, 85]
                        降序
                         function SortNumber(a,b) { return b-q };
                            a.sort(SortNumber); --》 [85, 73 ,11, 4]

                    例3 删除元素 .splice 1.删除哪里 2.删除几个 3.是不是要替换
                        a=[85, 73 ,11, 4];
                            a.splice(1,2,'aa','bb','cc','dd') -从index=1开始|删除2个元素|加入。。。--》(2) [73, 11]
                                a  -->(6) [85, "aa", "bb", "cc", "dd", 4]

        自定义对象 {  }
            例：
                a=[85, "aa", "bb", "cc", "dd", 4]
                    for (var i in a) {console.log(i)}; -->console相当于py的print->0,1,2,3,4,5
                    for (var i in a){console.log(a[i])} -->85, "aa", "bb", "cc", "dd", 4
        类型查询
            typeof 100 ->number|typeof true ->boolean|typeof function -function|typeof undefined -undefined|
                typeof new object() -object| typeof a=[1,2] - object| typeof NaN - number|typeof null -object
        运算符
            + - * / | ++ -- (相当于py + =)
                例
                    a=10;
                    a++  -->显示10
                        a  -->结果 11
                     a=10;
                    ++a  -->显示11 ,过程不一样，结果一样
                    a  -->结果
        比较运算符 == 两个等号 弱等于-不比较数据类型| === 强等于 - 基本用强等于 |> |<| >!|>=|<=
            a=10;
              b='10'
                a==b --> true
                a===b --> false
        逻辑运算符 && 与 | || or | ！ 非 | null true
        赋值运算符 += | -= | *= | /=

    流程控制
        1. if （） -- else  if（）  -- else 多条件
        a=10;
         if (a===10) {console.log('yes')} else if(a===11) {console.log('no')} else{console.log('xx')} ;
            --> yes

        2. switch (数值或算式）--》 case  条件 --》break --》default 上面条件都不成立时的返回
            例
                var day = 10;
                switch(a){
                    case 9:console.log('999');
                    break;
                    case 10:console.log('1999');
                    break;
                    case 11:console.log('11119');
                    break;
                    default:console.log('xxxx')}
                        --》 1999

        3. for 循环
            两种写法
            for (var i=0 ; i<8;i++){console.log(i)}

            a=[85, "aa", "bb", "cc", "dd", 4]
                for (var i in a) {console.log(i)}; -->console相当于py的print->0,1,2,3,4,5
                for (var i in a){console.log(a[i])} -->85, "aa", "bb", "cc", "dd", 4

        4.while 循环
            var i= 10;
            while (i <13){console.log(i);i++)
        5.三元运算
            var a=1;
            var b=2;
            c=a>b?a:b
                -->2
    函数 -function | return -只能返回一个结果，如有多个结果需放在1个对象内
        function f1(){console.log('hello world');return [1,2]}
            f1()
                --> hello world'
        匿名函数
            var sum=function(a,b){return a+b;}
                var a=1;
                    var b=2;
                        sum(a,b)--》 3
        自执行函数
            (function(a,b){console.log(a,b);})(2,5);-->2 5

        函数的全局变量和局部变量--函数外|函数内定义

        作用域--从内往外找
            var city = 'beijing';
            function outer(){
                var city='shanghai';
                function inner(){var city='shenzhen';console.log(city);}
                inner()
                };
            outer() -->shenzhen
        闭包 --在这里不是很重要
    面向对象 -- es5 没有类的概念，实现类的封闭方式是用构造函数的方式--es6有class方法
          this.相当于py中类的self
          1.定义类--可在封装参数
            function Person(name){
                    this.name=name;
                    }
           2.实例化
              var p= Person('taibai');
              p.name    --调用类的参数 -->taibai
            3.封闭方法
              person.propotype.sum(function(a,b){return a+b;} --用propotype属性+匿名函数封闭方法
    date对象 --时间对象
        var d1 =new Date() ---获取当前时间-->"Sat Jun 27 2020 08:28:26 GMT+0800 (中国标准时间)"
            d1.toLocaleString() -->"2020/6/27 上午8:32:39"
        var d2 =new Date('1999/1/1/ 11:30'); ---自定义时间
            d1.get day() ---> 获取星期几 0-6 ，0-表示星期天
            d1.get.month()-->获取月份 0-11 ，1-表示1月
    序列化 - JSON.Parser(object) 等于 py json.load() 反序列化| JSON.Stringify(object)等于 py json.dump() 序列化

    正则 - RegExp 写法 不能有不必要的空格-两种方式（^表达式$）| /^表大式$/ --
        例 正测规则
            var reg1=new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$") --定义一条正则表达式- 小or大写字母+小or大写字母or数字or下划线，长度5至11位
                var r_object1='abc123';
                var r_object2='123abc';
                    reg1.test(r_object1);--》true  |-->.test方法测试object是否符合正则表达式
                    reg1.test(r_object2);--》false
                    一个坑
                        reg1.test() -->内里不写内容==('undefined')

        正则组合使用 match 可+g找多个-加g找一个光标移动位置| search  找一个g不会返回组合，光标会移动| split 分割| replace 替换
            var s1='helloworld';
                s1.match(/o/); -->["o", index: 4, input: "helloworld", groups: undefined]
                 s1.match(/o/g); -->["o", "o"] 返回一个groups，所有匹配项的集
            一个坑  --g参数的位置移动
                reg2=/a/g;
                s1='abbdacc';
                    reg2.lastInde;    -->0
                       reg2.test(s1); ->true
                         reg2.lastInde;    -->1
                            reg2.test(s1); ->true
                               reg2.lastIndex;    -->5
                                reg2.test(s1); ->false
                                    reg2.lastIndex;    -->0

            内置函数 Math --.abs|.log|.pow|.random|.round|.sin|.. 数字处理函数，不用new定义直接可用
'''

'''
四 、BOM 和 DOM --前端基础
https://www.cnblogs.com/clschao/articles/10092896.html
https://www.cnblogs.com/clschao/articles/10092991.html
    引入- avaScript分为 ECMAScript，DOM-文档，BOM。
        BOM（Browser Object Model）是指浏览器对象模型，它使 JavaScript 有能力与浏览器进行“对话”。
　　      DOM （Document Object Model）是指文档对象模型，通过它，可以访问HTML文档的所有元素。
    
    1.BOM模型 -了解 其中较常用的两个应用
        1.1 window对象--是一个全局对象
            window对象
                写var a =10;
                全写是 window.a
                window.innerheight-当前浏览器窗口大小|window.inerwidth 宽度| window.open()新开窗口|window.close()关闭
            window对象的子对象
                navigator对象（了解即可）
                    navigator.appName　　// Web浏览器全称
                    navigator.appVersion　　// Web浏览器厂商和版本的详细字符串
                    navigator.userAgent　　// 客户端绝大部分信息
                    navigator.platform　　　// 浏览器运行所在的操作系统
                    
                screen对象（了解即可）
                history对象（了解即可）
                    history.forward()  // 前进一页，其实也是window的属性，window.history.forward()
                    history.back()  // 后退一页
                location对象 -掌握*
                    location.href  获取URL
                    location.href="URL" // 跳转到指定页面  
                        location.href="http://www.baidu.com"   
                    location.reload() 重新加载页面,就是刷新一下页面
                弹出框  alert 警告| confirm 确认 | prompt 提示   -自带的不常用，一般自已写
                    
            1.2 计时器相关（比较重要）--一定时间做一件事情*
            　setInterval() 每隔一段时间做一些事情
                setTimeout() 延时 --写法一( '语句',秒*1000）一般不用易出错| 常用函数的方式
                    setTimeout( function(){confirm('你好')},3000) 
             clearInterval()
    　　　　　　clearInterval() 方法可取消由 setInterval() 设置的 timeout。  
    　　　　　　clearInterval() 方法的参数必须是由 setInterval() 返回的 ID 值。
                
     2.DOM 模型--DOM（Document Object Model）是一套对文档的内容进行抽象和概念化的方法。 
　      当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。
        HTML DOM 模型被构造为对象的树。    
            节点：DOM标准规定HTML文档中的每个成分都是一个节点(node)：
                文档节点(document对象)：代表整个文档
                元素节点(element 对象)：代表一个元素（标签）
                文本节点(text对象)：代表元素（标签）中的文本
                属性节点(attribute对象)：代表一个属性，元素（标签）才有属性
                注释是注释节点(comment对象)　
            作用：
                JavaScript 可以通过DOM创建动态的 HTML：
                JavaScript 能够改变页面中的所有 HTML 元素
                JavaScript 能够改变页面中的所有 HTML 属性
                JavaScript 能够改变页面中的所有 CSS 样式
                JavaScript 能够对页面中的所有事件做出反应（鼠标点击事件，鼠标移动事件等）
            1.查找标签
                直接查找
                    document.getElementById           根据ID获取一个标签
                    document.getElementsByClassName   根据class属性获取（可以获取多个元素，所以返回的是一个数组）
                    document.getElementsByTagName     根据标签名获取标签合集
                 间接查找
                    parentElement            父节点标签元素
                    children                 所有子标签
                    firstElementChild        第一个子标签元素
                    lastElementChild         最后一个子标签元素
                    nextElementSibling       下一个兄弟标签元素
                    previousElementSibling   上一个兄弟标签元素　
            2.创建节点 （用js创建标签）
                示例
                 。。。
                    var dd=document.getElementById('dd');
                    a=document.createElement('a');
                    a.innerText='我是a-创建节点';
                    dd.appendChild(a); 加在最后
                    dd.insertBefore(a,d2); 加在前面
            3.删除节点 dd.removeChild(T)
            4.替换节点 dd.replaceChild(T)
            5.文本操作 
                dd.d1.innerText=("<a href=''> 百度 </a>") --不能识别内容是标签
                dd.d1.innerHtml=("<a href=''> 百度 </a>") --能识别内容是标签
            6.设置标签属性 查看属性 删除属性
                    a.setAttribute('href','http://www.baidu.com')  | 方法二  a.href='XXX'
                       a.getAttribute('href')
                        a.removeAttribute('href')
            7.获取值操作 --输入框|选择框
                。。。
                   var inp=document.getElementById('inp');
                    // 获取值
                    inp_v=inp.value
                    // 设置值
                    inp.value='helloworld'
                    
            8.class 操作 css设置
                d.classList
                    d.classList.add('xx2')
                        dclassList.contents('xx") --返回 true|false
                            d.classList.toggle('xx2')
                css-设置属性的方法二： 写法--有横杠的去掉横杠，最后单词首字母大写
                d.style.backgroundColor='red'
            9.事件- 操作 用户操作触发的反应
                onclick        当用户点击某个对象时调用的事件句柄。
                ondblclick     当用户双击某个对象时调用的事件句柄。
                
                onfocus        元素获得焦点。               // 练习：输入框
                onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
                onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）
                
                onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
                onkeypress     某个键盘按键被按下并松开。
                onkeyup        某个键盘按键被松开。
                onload         一张页面或一幅图像完成加载。
                onmousedown    鼠标按钮被按下。
                onmousemove    鼠标被移动。
                onmouseout     鼠标从某元素移开。
                onmouseover    鼠标移到某元素之上。
                
                onselect      在文本框中的文本被选中时发生。
                onsubmit      确认按钮被点击，使用的对象是form。
                                


                                　       

'''



















        '''



