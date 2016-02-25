<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>裁剪头像</title>
        <link rel="stylesheet" href="/assets/css/page/edit-avatar.css">
        <link rel="stylesheet" href="/assets/css/lib/jquery.Jcrop.min.css">
        <link rel="stylesheet" href="/assets/css/lib/base.css">
        <link rel="stylesheet" href="/assets/css/page/crop-photo.css">
    </head>
    <body>
        <nav>
            <div class='top'>
                <div class='title pull-left'>
                    添加新成员
                </div>
                <div class='home pull-right'>
                    <a class='top-button' href="/">返回照片墙 >></a>
                </div>
            </div>
        </nav>
        <div class="mask"></div>
        <div class="container">
            <div class="operations">
                <h1>看起来很棒</h1>
                <span class="tips pull-left">现在，裁剪出一张合适的头像，它会出现在照片墙上</span>
                <input id="back" type="button" value="上一步" class="small-button pull-right secondary">
                <input id="submit" type="submit" value="完成" class="small-button pull-right"></input>
            </div>
            <div class="raw-photo">
               <input id="image-type" type='hidden' value='avatar'>
               <img src="{{image}}">
            </div>
            <div class="preview">
                <img src="{{image}}">
            </div>
            <div class="sample pull-right">
                <img src="http://7xr6pw.com1.z0.glb.clouddn.com/sample_head%402x.jpg" width="160" height="160">
                <div class="name">谢耳朵</div>
                <div class="tips">头像示例</div>
            </div>
            
        </div>
        <footer class="copyright">© Shigotongo.2014</footer>
    </body>
    <script src='/assets/js/lib/jquery.min.1.9.1.js'></script>
    <script src='/assets/js/lib/jquery.Jcrop.min.js'></script>
    <script src='/assets/js/lib/jquery.color.js'></script>
    <script src='/assets/js/page/edit-avatar.js'></script>
</html>