<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="/assets/css/page/edit-photo.css">
        <link rel="stylesheet" href="/assets/css/lib/jquery.Jcrop.min.css">
    </head>
    <body>
        <div class="raw-photo">
           <input type='hidden' value='{{id}}'>
            <img src="{{image}}">
        </div>
        <div class="preview blank">
            <img src="{{image}}">
        </div>
        <input id="submit" type="submit" value="裁剪"></input>
    </body>
    <script src='/assets/js/lib/jquery.min.1.9.1.js'></script>
    <script src='/assets/js/lib/jquery.Jcrop.min.js'></script>
    <script src='/assets/js/lib/jquery.color.js'></script>
    <script src='/assets/js/page/edit-photo.js'></script>
</html>