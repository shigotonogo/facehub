<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="/assets/css/page/edit-photo.css">
        <link rel="stylesheet" href="/assets/css/lib/jquery.Jcrop.min.css">
    </head>
    <body>
        <div class='top'>
            <div class='title pull-left'>
                添加新成员
            </div>
            <div class='home pull-right'>
                <a class='home' href="/">返回照片墙 >></a>
            </div>
        </div>
        <div class="container">
            <div class="operations">
                <h1>按你的喜好裁剪这张照片</h1>
                <span class="tips pull-left">首先，移动下方绿色的取景框，选择一张合适的半身照</span>
                <input type="button" value="取消" class="pull-right">
                <input id="submit" type="submit" value="下一步" class="pull-right"></input>
            </div>
            <div class="raw-photo">
               <input type='hidden' value='{{id}}'>
               <input type='hidden' value=''>
               <img src="{{image}}">
            </div>
            <div class="preview blank pull-right">
                <img src="{{image}}">
            </div>
            
        </div>
    </body>
    <script src='/assets/js/lib/jquery.min.1.9.1.js'></script>
    <script src='/assets/js/lib/jquery.Jcrop.min.js'></script>
    <script src='/assets/js/lib/jquery.color.js'></script>
    <script src='/assets/js/page/edit-photo.js'></script>
</html>