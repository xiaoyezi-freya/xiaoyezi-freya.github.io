<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>我的书苑我做主</title>
        <style>
        a {
            text-decoration: none;
        }

        body {
            margin: 0;
            width:100%;
            height: 100%;
        }

        #header {
            background-color:#0c1f27;
            color:#20b2aa;
            text-align:center;
            padding:15px;
        }
        
        #nav {
            line-height:60px;
            background-color:#e0f2f0;
            width:80px;
            padding:30px;
            position: absolute;
            left: 0;
            top:0;
            bottom: 0;
        }

        #footer {
            background-color:#0c1f27;
            color:#20b2aa;
            clear:both;
            text-align:center;
            padding:35px;
        }

        #main {
            margin-left: 140px;
            padding-left: 150px;
            padding-right: 220px;
            overflow: scroll;
        }

        #article {
            display: flex;
            position: relative;
        }

        .catlog{
            font-size:20px;
            color:black;
            font-family: sans-serif;
        }

        .title {
            color:#20b2aa;
            font-size:20px;
        }

        .img {
            width: 185px;
            height: 266px;
        }
        </style>
    </head>

    <body>
        <div id="header">
        <h1 style="font-size:50px;">我的书苑我做主</h1>
        </div>

        <div id="article">
            <div id="nav">
                <a href="#type1" class="catlog">科幻小说</a><br>
                <a href="#type2" class="catlog">人文读物</a><br>
                <a href="#type3" class="catlog">技术参考</a><br>
            </div>
            <div id="main">
                <div class="books">
                    <h2><a name="type1">科幻小说</a></h2>
                    <a href="https://book.douban.com/subject/27077140/" class="title">《奇点遗民》</a>
                    <p class="info">本书精选收录了刘宇昆的科幻佳作共22篇。《奇点遗民》融入了科幻艺术吸引人的几大元素：数字化生命、影像化记忆、人工智能、外星访客……刘宇昆的独特之处在于，他写的不是科幻探险或英雄奇幻，而是数据时代里每个人的生活和情感变化。透过这本书，我们看到的不仅是未来还有当下。</p> 
                    <img class="img" src="https://img3.doubanio.com/view/subject/l/public/s29492583.jpg">
                    <br/>
                    <br/>
                    <hr size="1">
                </div>
                <div class="books">
                    <h2><a name="type1">科幻小说</a></h2>
                    <a href="https://book.douban.com/subject/2567698/" class="title">《三体》</a>
                    <p class="info">人类的末日悄然来临。《三体》军方探寻外星文明的绝秘计划“红岸工程”取得了突破性进展。</p> 
                    <img class="img" src="https://img1.doubanio.com/view/subject/l/public/s2768378.jpg">
                    <br/>
                    <br/>
                    <hr size="1">
                </div>
                <div class="books">
                    <h2><a name="type2">人文读物</a></h2>
                    <a href="https://book.douban.com/subject/26943161/" class="title">《未来简史》</a>
                    <p class="info">未来，人类将面临着三大问题：生物本身就是算法，生命是不断处理数据的过程；意识与智能的分离；拥有大数据积累的外部环境将比我们自己更了解自己。如何看待这三大问题，以及如何采取应对措施，将直接影响着人类未来的发展。</p> 
                    <img class="img" src="https://img3.doubanio.com/view/subject/l/public/s29287103.jpg">
                    <br/>
                    <br/>
                    <hr size="1">
                </div>
                
                <div class="books">
                    <h2><a name="type3">技术参考</a></h2>
                    <a href="https://book.douban.com/subject/25779298/" class="title">《利用Python进行数据分析》</a>
                    <p class="info">本书含有大量的实践案例，你将学会如何利用各种Python库（包括NumPy、pandas、matplotlib以及IPython等）高效地解决各式各样的数据分析问题。由于作者Wes McKinney是pandas库的主要作者，所以本书也可以作为利用Python实现数据密集型应用的科学计算实践指南。本书适合刚刚接触Python的分析人员以及刚刚接触科学计算的Python程序员。</p> 
                    <img class="img" src="ttps://img3.doubanio.com/view/subject/l/public/s27275372.jpg">
                    <br/>
                    <br/>
                    <hr size="1">
                </div>
            </div>
        </div>

        <div id="footer">Copyright © ForChange 风变科技 2016-2020
        </div>
    </body>
</html>