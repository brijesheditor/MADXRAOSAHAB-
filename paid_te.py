<!DOCTYPE html>
<html>
<head>
  <script>
    window.onload = function() {
      var url = "https://studymate-sunny.vercel.app";

      // Try opening in Chrome (Android)
      window.location.href = "intent://" + url.replace("https://", "") + "#Intent;scheme=https;package=com.android.chrome;end";

      // Fallback (agar na chale)
      setTimeout(function(){
        window.location.href = url;
      }, 1500);
    };
  </script>
</head>
<body style="background:black;color:white;text-align:center;padding-top:50px;">
  <h2>Opening in Chrome...</h2>
  <p>If not opened, please tap below</p>
  <a href="https://kgs-web.vercel.app" style="color:cyan;">Open Manually</a>
</body>
</html>
