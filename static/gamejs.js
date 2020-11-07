function game_start(){
  gameArea.start();
  gamePiece = new component(30, 30, "red", 10, 200);
}

var gameArea = {
  canvas : document.createElement("canvas"),
  start : function(){
    this.canvas.width = 800;
    this.canvas.height = 500;
    this.context = this.canvas.getContext("2d");
    this.context.fillStyle = "blue";
    this.context.fill();
    document.getElementById("game-div").appendChild(this.canvas);
    this.frameNo=0;
    this.interval = setInterval(updateGameArea, 20);
    window.addEventListener('keydown', function (e) {
      gameArea.keys = (gameArea.keys || []);
      gameArea.keys[e.keyCode] = true;
    })
    window.addEventListener('keyup', function (e) {
      gameArea.keys[e.keyCode]=false;
    })
    window.addEventListener('mousemove', function(e){
      gameArea.mousePosX = e.pageX;
      gameArea.mousePosY = e.pageY;
    })

  },
   clear : function(){
     this.context.clearRect(0,0, this.canvas.width, this.canvas.height);
   }
}

function component(width, height, color, x, y){
  this.width = width;
  this.height = height;
  this.x = x;
  this.y = y;
  this.speedX=0;
  this.speedY = 0;
  this.update = function(){
    ctx = gameArea.context;
    ctx.fillStyle = color;
    if (this.x > 800){
      this.x =10;
    }
    
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }
  this.newPos = function(){
    this.x += this.speedX;
    this.y += this.speedY;
  }
}
function updateGameArea(){
  gameArea.clear();
  gamePiece.speedX=0;
  gamePiece.speedY=0;
  if (gameArea.key && (gameArea.keys[37] || gameArea.keys[65])){gamePiece.speedX = -2; }
  if (gameArea.key && (gameArea.keys[39] || gameArea.keys[68])){gamePiece.speedX = 2; }
  if (gameArea.key && (gameArea.keys[38] || gameArea.keys[87])){gamePiece.speedY = -2; }
  if (gameArea.key && (gameArea.keys[40] || gameArea.keys[83])){gamePiece.speedY = 2; }
  gamePiece.newPos();
  gamePiece.update();
}


