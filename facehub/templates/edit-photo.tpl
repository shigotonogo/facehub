<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>裁剪半身照</title>
        <link rel="stylesheet" href="/assets/css/page/edit-photo.css">
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
                    <a class='top-button' href="/">取消</a>
                </div>
            </div>
        </nav>
        <div class="mask"></div>
        <div class="container">
            <div class="operations">
                <div class="pull-left">
                    <h1>按你的喜好裁剪这张照片</h1>
                    <span class="tips">首先，移动下方的取景框，选择一张合适的半身照</span>
                </div>
                <div class="buttons">
                    <input id="submit" type="submit" value="下一步" class="pull-right small-button"></input>
                </div>
            </div>
            <div class="raw-photo">
               <input id="image-type" type='hidden' value='photo'>
               <img src="{{image}}">
            </div>
            <div class="preview">
                <img src="{{image}}">
            </div>
            <div class="sample pull-right">
                <img src="http://7xr6pw.com1.z0.glb.clouddn.com/sample_half%402x.jpg" width="160">
                <div class="tips">半身照示例</div>
            </div>
        </div>
        <footer class="copyright">© Shigotongo.2014</footer>
    </body>
    <script src="//cdn.bootcss.com/jquery/1.9.1/jquery.min.js"></script>
    <script src='/assets/js/lib/jquery.Jcrop.min.js'></script>
    <script src='/assets/js/lib/jquery.color.js'></script>
    <script src='/assets/js/page/edit-photo.js'></script>
</html>