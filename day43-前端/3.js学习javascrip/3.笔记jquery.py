'''
https://www.cnblogs.com/clschao/articles/10093264.html
    https://jquery.cuishifeng.cn/  ---官方文档
1.jquery 介绍

    下载-安装
        https://jquery.com/download/点击 download
            Download the compressed, production jQuery 3.5.1 ---压缩版，速度快，原码可读性差，正式生产上用
           Download the uncompressed, development jQuery 3.5.1--不压缩版，学习使用
           点击其中一个全选复制--在pycharm新建一个.js  如jquery.js把内容贴进去--OK
    文件引用到html
        <script src="jquery.js"></script>

    jQuery 对象 和 DOM 对象
        用jQuery语句找到的是jQuery对象|用原生js语句找到的是DOM对象
            两种对象各有各的方法，但可以转换
                jQuery对象 -> DOM对象转换-> $(#d1)[0]
                    DOM对象转换-> jQuery对象 ---$(DOM)
     基本语法
        $(#d1);--返回id='d1'的对象
        $(#d1).text='aa';

'''
'''
1. 查找标签
    选择器--和css一样
    $('#d1') id选择器| $('.c1') 类选择器|$('div') 标签选择器|$('div.c1')  组合选择器|$('#d1','c1','div') 组合选择器|$(dom对象)。。。
    
    $('.c1') --有多个值时返回jQuery对象是一个数组，但还是jQuery对象能免使用其方法，可统一设置，也可用索引值取值单独设置，但注意索引值取值出来的是DOM对象只能用DOM的方法，可以再转一次为jQuery再用方法 aa=$('.c1')[0]  -> $(aa)  -- 单个jquery对象，也可以用选择器eq(index)方法
        -->console显示：
            jQuery.fn.init(2) [div#d1.c1, div#d3.c1, prevObject: jQuery.fn.init(1)]
            0: div#d1.c1
            1: div#d3.c1
            length: 2
            prevObject: jQuery.fn.init [document]
            __proto__: Object(0)
2.筛选器 
    1.基本筛选器 --返回jquery对象| 选择最小是标签级别
        方法
        :first // 第一个
        :last // 最后一个
        :eq(index)// 索引等于index的那个元素
        :even // 匹配所有索引值为偶数的元素，从 0 开始计数
        :odd // 匹配所有索引值为奇数的元素，从 0 开始计数
        :gt(index)// 匹配所有大于给定索引值的元素
        :lt(index)// 匹配所有小于给定索引值的元素
        :not(元素选择器)// 移除所有满足not条件的标签
        :has(元素选择器)// 选取所有包含一个或多个标签在其内的标签(指的是从后代元素找)-注：的后代中查找返回的是自身-看例子
        语法 
            1.所有语句在引号内    
            $('li:eq(1)'); -->返回索引为1的jquery对象
                $('li:eq(1)').text();返回索引为1的jquery对象的文本内容
            2. lable.has()语句是查后代返回本身
            $('li:has(.c1)'
                结果后代中有.c1,返回本身-本身是.c3：
                S.fn.init [li#l3.c3, prevObject: S.fn.init(1)]
                0: li#l3.c3
                length: 1
                prevObject: S.fn.init [document]
                __proto__: Object(0)
    2.属性筛选器 -
        [attribute]
        [attribute=value]// 属性等于
        [attribute!=value]// 属性不等于
           例  $('div[title=xx]') 
    3.表单筛选器-针对input标签的type属性（多用于找form表单里面出现的input标签，当然通过属性选择器找肯定也是没问题的，这样就是写着简单一些）：
        :text
        :password
        :file
        :radio
        :checkbox
        
        :submit
        :reset
        :button
        　　例子：$(":checkbox")  // 找到所有的checkbox
    4.筛选器方法（将来用的很多）
        1.下一个元素：
            $("#id").next()
            $("#id").nextAll()
            $("#id").nextUntil("#i2") #直到找到id为i2的标签就结束查找，不包含它
                例：$("#l1").next() 
        2.上一个元素
            $("#id").prev()
            $("#id").prevAll()
            $("#id").prevUntil("#i2")
        3.找父辈标签
            $("#id").parent()
            $("#id").parents()  // 查找当前元素的所有的父辈元素（爷爷辈、祖先辈都找到）
            $("#id").parentsUntil('body') // 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止，这里直到body标签，不包含body标签，基本选择器都可以放到这里面使用。
         4.　儿子和兄弟元素：
            $("#id").children();// 儿子们
            $("#id").siblings();// 兄弟们，不包含自己，.siblings('#id')，可以在添加选择器进行进一步筛选
        5. find--找的是后代
            $('ul').find('#l3') 等效于 $('ul #l3')
        6.筛选 $("div").filter(".c1") --找的是本身
        7.其它方法 与$('li:first()') 等同
            .first() // 获取匹配的第一个元素
            .last() // 获取匹配的最后一个元素
            .not() // 从匹配元素的集合中删除与指定表达式匹配的元素
            .has() // 保留包含特定后代的元素，去掉那些不含有指定后代的元素。
            .eq() // 索引值等于指定值的元素
            
3.操作标签
    1.操作class --和BOM、DOM一样只是写法简化
        addClass();// 添加指定的CSS类名。
        removeClass();// 移除指定的CSS类名。
        hasClass();// 判断样式存不存在
        toggleClass();// 切换CSS类名，如果有就移除，如果没有就添加。
        例
            加标签 - 注选择类的选择器加点 后面不用加点
            $('.c4').addClass('c5')
4.css操作
    
    
    例：
        改一个 --- 数组形式输入
        $('.c4').css('background-color','blue');
        改多个 ---- 字典形式输入
        $('.c4').css({'background-color'：'blue'，'height'='400px');
        
5. 位置操作  --设置相对位置和绝对位置用css方法， jquery位置只能设相对window的位移
    offset()// 获取匹配元素在当前窗口的相对偏移或设置元素位置
    position()// 获取匹配元素相对父元素的偏移，不能设置位置
        $(window).scrollTop()  //滚轮向下移动的距离
        $(window).scrollLeft() //滚轮向左移动的距离       
            例：$('.c1').offset() -->{top: 8, left: 8}     # 位置参数不用写px单位
6. 绑定点击事件
    jquery方法
    $('.c1').click(function(){
        $(this).css('background-color','blue');
        }
    );
        // 原生JS方法
       $('.c2')[0].onclick=function(){
        this.style.backgroundColor='pink';
        };
7 绑定位置事件 操作 看例3.1
8.尺寸操作--对应盒子模型
    height() //盒子模型content的大小，就是我们设置的标签的高度和宽度
    width()
    innerHeight() //内容content高度 + 两个padding的高度
    innerWidth()
    outerHeight() //内容高度 + 两个padding的高度 + 两个border的高度，不包括margin的高度，因为margin不是标签的，是标签和标签之间的距离
    outerWidth()
9.文本操作 看例3.2
　HTML代码方法：
    html()// 取得第一个匹配元素的html内容，包含标签内容
    html(val)// 设置所有匹配元素的html内容，识别标签，能够表现出标签的效
  text方法 ：
    text()// 取得所有匹配元素的内容，只有文本内容，没有标签
    text(val)// 设置所有匹配元素的内容，不识别标签，将标签作为文本插入进去 
   两者区别：
   读文本：
        .text 方法不读标签
            $('.c1').text()
                " 我是div
                    我是span  "
        .html 方法 读标签
             $('.c1').html()       
            " 我是div
                <span class="s1" id="s1">我是span</span>"
    写文本 
       .text 方法写是不解释标签
        $('.c1').text(' <span class="s2" id="s2">我是span</span>)');
          显示 --><span class="s2" id="s2">我是span</span>)
       .html 方法 写-解释标签
        $('.c1').html(' <span class="s2" id="s2">我是span</span>');
               显示 --> 我是span
10.值操作 .value 例3.2jquery文本操作.html
        值操作
          // 1.文本取值
                //     读
                $('#username1').val();
                        // 写-除文本框外其它多项的用数组输入值，例：(1)-全部元素值设置成1，[1]设置元素值为1的选中
                $('#username1').val('xxx');
                // 2.单选取值 + 表单选择器 --写操作括号内数组格式
                $(':radio:checked').val();
                $(':radio').val([2]);
                // 3.多选取值 - jquery多值返回的数组除了元素还有其它参数，但可.length;获取元素长度;后面有学到封闭好的方法
                var d=$(':checkbox:checked');
                    // 刷新屏幕值
                screen;
                    // d -- -返回含有选中元素的数组还有其它值 --S.fn.init(2) [input, input, prevObject: S.fn.init(1)]
                    // 循环取值
                for ( var i=0;i<d.length;i++){
                    console.log(d.eq(i).val())
                }
                $(':checkbox').val([1,2]);
                // 4.下拉框取值-单选
                $('#city').val();
                $('#city').val(['2']);
                // 5.下拉框取值-多选 -返回只含有选中元素的数组
                $('#village').val();
                    // --> ["1", "2"]
                // 数组内文本格式和数字格式不影响效果
                $('#village').val(['1',3]);
11.属性操作
    // 1.属性操作  .attr 方法
        // 单个设置属性
        $('.c1').attr('xx','oo')
        // 多个设置属性-字典格式
         $('.c1').attr({'x1':'o1','x2':'o2'})
        // 查看属性
         $('.c1').attr('x1');
        // 删除属性
        $('.c1').removeAttr('x1');
    // 2.属性操作  .prop 方法--有些版本jquery设input |select| 中的 disabled| checked|属性 .attr无效要用.prop
        //     读
            $('#r2').prop('checked')
                 // -->true
            // 写--格式true|false 不加引号
            $(':radio').eq(0).prop('checked',true)
             $(':radio').eq(1).prop('checked',false)

　　　总结一下：
　　　　　　　　1.对于标签上有的能看到的属性和自定义属性都用attr
　　　　　　　　2.对于返回布尔值的比如checkbox、radio和option的是否被选中或者设置其被选中与取消选中都用prop。
 　　　　　　　　具有 true 和 false 两个属性的属性，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()
 12.文本操作--添加标签   
         // 1.创造标签方法-里面追加
            a=document.createElement('a');
            a.href='http://www.baidu.com';
            a.innerText='baidu';
          // 1.添加标签写法  $(父).append(a)
          //   $('div').append(a)
             // 2.添加标签写法  $(a).appendTo(父)
            $(a).appendTo('div');
         // 创造标签方法2-jquery --直接用文本 添加
            var b= '<a href="http://www.jd.com">jd</a>';
            // $(b).appendTo('div');
            $('div').append(b);
        // 2.加到里面前面 .prepend和.prependTo
        // 3.同级前面 $(原有标签）.before（追加标签）| $(追加标签）.insertBefore（原有标签）
        // 4.同级后面 $(原有标签）.after（追加标签）| $(追加标签）.insertAfter（原有标签）
        //     5.移除和清空 .remove()-连本身也同时删除 |.empty() -清空保留自身
        //     6. 替换 $（旧）.replaceWith(新)|$（新）.replaceAll(旧)
        //     7.克隆 .clone()-克隆内容| .clone(true)--连带事件一起克降
13.事件
    内容
        click(function(){...})  -->左键占击事件
        hover(function(){...}) --->鼠标悬浮事件 原生JS没有这个由原生的.mouseenter()|.mouseout()封装而来
        blur(function(){...})
        focus(function(){...})
        change(function(){...}) //内容发生变化，input，select等
        keyup(function(){...})  mouseover 和 mouseenter的区别是：mouseover事件是如果该标签有子标签，那么移动到该标签或者移动到子标签时会连续触发，                mmouseenter事件不管有没有子标签都只触发一次，表示鼠标进入这个对象
    // 事件操作
    // 写法1--$（对象）.click(函数)
    $('#d1').click(function(){
        $(this).css({'background-color':'green'})
    });
    // 写法2--$（对象）.on('click',函数)
     $('#d2').on('click',function(){
        $(this).css({'background-color':'blue'})
        }) ;  
        注：特殊 input事件只能用写法2绑定|另外IE9以下不支持input事件对应propertychange代替   $('#d2').on('input',function(){});  例3.6
         $("#i1").on("input propertychange", function () {  //可以支持IE9以下的版本
                            console.log($(this).val());
                        })     
                        
14.事件冒泡  --例3.7
    // 1.冒泡事件演示---点d1显示'父级标签'，点d2先显显示'子标签'再'父级标签'--说明响应从里至外顺序执行
    // 2.阻止冒泡-- 两种方法-使用事件对象.stopPropagation()方法- 英文字面意思停止传递| return false
15.移除事件---.off 方法 --不常用
    $('#d2').off('input',function(){});
16.事件委托
        / 用事件委托实现克隆效果
    //     1.点击第一个克隆有效
            $('.c1').on('click',function(){
                alert('事件委托基于事件冒泡原理|必须用.on绑定|委托给父级标签');
                var btn=document.createElement('button');
                $(btn).addClass('c1');
                $(btn).text('button class="c1"');
                console.log(btn);
                $('#d1').append(btn);
                   });
    //     1.事件委托后-点击任一个克隆有效
            $('#d2').on('click','.c2',function(){
                alert('事件委托基于事件冒泡原理|必须用.on绑定|委托给父级标签');
                var btn=document.createElement('button');
                $(btn).addClass('c2');
                $(btn).text('button class="c2"');
                console.log(btn);
                $('#d2').append(btn);
    
            });
        
17.页面载入---从上至下载入-推荐| 也可声明最后载入
    1.原生声明最后载入方法--> window.onload=function(){}; --有覆盖现象不好用。
    2.jquery声明最后载入方法
        $(document).ready(function(){ // 在这里写你的JS代码...   }) 
       简写    
       $ $(function () {})
18.动画 --（了解内容）
            / 基本
        show([s,[e],[fn]])  $('.c1').show()  //show(5000),就是5秒之后显示出来这个标签，并且有一个动画效果，（搞个img图片看看效果），后面两个参数先不用管
        hide([s,[e],[fn]])  $('.c1').hide()
        toggle([s],[e],[fn])//这几个toggle的意思就是你原来是什么效果，我就反着来
        // 滑动（拉窗帘一样）
        slideDown([s],[e],[fn])  
        //使用的时候别忘了给标签设置一个高度和宽度，其实就是控制你的标签高度，如果你写$('#di').slideUp(5000)；意思就是5秒内把你的高度变为0
        //还有如果你直接操作的是img标签和操作img标签的父级标签，两个的效果是不同的
        slideUp([s,[e],[fn]]) 
        slideToggle([s],[e],[fn])
        // 淡入淡出（控制透明度）
        fadeIn([s],[e],[fn])
        fadeOut([s],[e],[fn])
        fadeTo([[s],o,[e],[fn]])  o参数是透明度，0-1的区间，意思是淡入或者淡出到一个多大的透明读
        fadeToggle([s,[e],[fn]])
        // 自定义（了解即可）
        animate(p,[s],[e],[fn])   
        
 19.事件 each 方法-- 代替for方法循环数组方法 | 还可循环普通数组
        // 1.直接for循环数组，出来包含一些元素外的数据项
                for (var i in $('li')){ console.log($('li').eq(i).text())};
         // 2.jquery方法.each 在函数内设两个参数k-索引 v-标签，可取出标签元素-
                $('li').each(function(k,v){console.log(k,v)});
         // 3.参数v是一个dom对象，可使用dom方法
                $('li').each(function(k,v){console.log(k,v.innerText)});
        // 4.调用$.each()方法循环一般数组
                $.each(a,function(k,v){ console.log(k,v)});
            5.终止循环-- return false
                  
 20 jQuery--data方法 ---给标签定义一个key -value-->类似于声明一个全局变量
        $('.c1').data('name','x1')
    
21.  jQuery - 插件 .extend 方法（了解）-->添加自定义方法
        1.jQuery.extend(object)
　　　　jQuery的命名空间下添加新的功能。多用于插件开发者向 jQuery 中添加新函数时使用。 
        使用：
            $.xxx();
         2.jQuery.fn.extend(object)
               使用：
                     $('div').xxx();
                
          
 '''
'''
作业讲解    
    1.a标签 href=''，默认点击刷新页面



'''
