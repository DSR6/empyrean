<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Void and Memento</title>
<style>
  body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: lightblue;
  }
  .container {
    position: relative;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  .void {
    color: yellow;
    font-size: 48px;
    font-weight: bold;
  }
  .memento {
    color: black;
    font-size: 24px;
    margin-top: 20px;
  }
</style>
</head>
<body>

<div class="container">
  <div class="void">VOID</div>
  <div class="memento">MEMENTO</div>
</div>

</body>
</html>
