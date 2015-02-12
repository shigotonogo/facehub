<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="/assets/css/page/edit-photo.css">
        <link rel="stylesheet" href="/assets/css/lib/jquery.Jcrop.min.css">
        <link rel="stylesheet" href="/assets/css/lib/base.css">
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
        <div class="container">
            <div class="operations">
                <div class="pull-left">
                    <h1>按你的喜好裁剪这张照片</h1>
                    <span class="tips">首先，移动下方的取景框，选择一张合适的半身照</span>
                </div>
                <div class="buttons">
                    <input type="button" value="取消" class="pull-right small-button secondary">
                    <input id="submit" type="submit" value="下一步" class="pull-right small-button"></input>
                </div>
            </div>
            <div class="raw-photo">
               <input id="user-id" type='hidden' value='{{id}}'>
               <input id="image-type" type='hidden' value='photo'>
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