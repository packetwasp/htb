<?php if ( $_SERVER['SERVER_PORT'] != 60080 ) { die(); } ?>
<?php session_start(); if (isset ($_SESSION['username'])) { header("Location: /menu.php"); } ?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>OneTwoSeven</title>

    <!-- Bootstrap core CSS -->
    <link href="/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">

    <style>
      .bd-placeholder-img { font-size: 1.125rem; text-anchor: middle; -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }
      @media (min-width: 768px) { .bd-placeholder-img-lg { font-size: 3.5rem; } }
    </style>
    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
  </head>
  <body>
    <header>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="/login.php">OneTwoSeven - Administration Backend</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
    </div>
  </nav>
</header>

<main role="main">

  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="dist/img/ai-codes-coding-97077.jpg">
        <div class="container">
          <div class="carousel-caption text-left">
            <h1>OneTwoSeven Administration</h1>
            <p>Administration backend. For administrators only.</p>
          </div>
        </div>
      </div>
    </div>
    <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>


  <!-- Marketing messaging and featurettes
  ================================================== -->
  <!-- Wrap the rest of the page in another container to center all the content. -->

  <div class="container marketing">

    <!-- START THE FEATURETTES -->

    <div class="row featurette">
      <div class="col-md-12">
        <h2 class="featurette-heading">Login to the kingdom.<span class="text-muted"> Up up and away!</span></h2>
          <?php
            $msg = '';
            
            if (isset($_POST['login']) && !empty($_POST['username']) && !empty($_POST['password'])) {
	      if ($_POST['username'] == 'ots-admin' && hash('sha256',$_POST['password']) == '11c5a42c9d74d5442ef3cc835bda1b3e7cc7f494e704a10d0de426b2fbe5cbd8') {
                  $_SESSION['username'] = 'ots-admin';
		  header("Location: /menu.php");
              } else {
                  $msg = 'Wrong username or password.';
              }
            }
         ?>
      </div> <!-- /container -->
      
      <div class = "container">
      
         <form action="/login.php" method="post">
            <h4 class = "form-signin-heading"><font size="-1" color="red"><?php echo $msg; ?></font></h4>
	    <table>
              <tr><td><b>Username:</b></td><td><input type="text" name="username" size="40" required autofocus></td></tr>
              <tr><td><b>Password:</b></td><td><input type="password" name="password" size="40" required></td></tr>
              <tr><td colspan="2"><center><button type="submit" name="login">Login</button></center></td></tr>
            </table>
         </form>
	     </div>
    </div>

    <hr class="featurette-divider">

    <!-- /END THE FEATURETTES -->

  </div><!-- /.container -->


  <!-- FOOTER -->
  <footer class="container">
    <p class="float-right"><a href="#">Back to top</a></p>
    <p>&copy; 2019 OneTwoSeven, Dec. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
  </footer>
</main>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="/docs/4.3/assets/js/vendor/jquery-slim.min.js"><\/script>')</script><script src="dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script></body>
</html>
