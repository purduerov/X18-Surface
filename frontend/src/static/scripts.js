var socket = io();

//list of speedometer elements from the html
const speedoList = [
  document.getElementById('speedo1'), document.getElementById('speedo2'), document.getElementById('speedo3'),
  document.getElementById('speedo4'), document.getElementById('speedo5'), document.getElementById('speedo6'),
  document.getElementById('speedo7'), document.getElementById('speedo8')
];
//list of camera stream elements from the html
const streamList = [
  document.getElementById('stream1'), document.getElementById('stream2'), document.getElementById('stream3')
];

//function to decide if the shaded area in the speedometer should be red or green based on the angle
function colorToAngle(angle){
  if(angle < 0){
    return `rgb(200, 0, 0)`
  }else if(angle > 0){
    return `rgb(0, 200, 0)`
  }else{
    return `rgb(0, 0, 0)`
  }
}

//uses canvas to draw a speedometer based on a given thruster velocity
function drawSpeedo(velo, canvas){
  //convert thruster velocity to angle
  const angle = velo * (90/127)

  //set canavs to 2d and then clear it
  const speedo = canvas.getContext('2d');
  speedo.clearRect(0, 0, canvas.width, canvas.height);

  //define canvas line characteristics
  speedo.lineWidth = 2;
  speedo.strokeStyle = 'white';

  //define canvas arc characteristics
  const arcColor = colorToAngle(angle);
  speedo.fillStyle = arcColor;

  //set centers and radius
  const centerX = canvas.width / 2;
  const centerY = canvas.height;
  const radius = 100;

  let startAngle = 0;
  let endAngle = 0;

  //determine start and end angle by the sign of the angle
  if(angle >= 0){
    startAngle = 3 * Math.PI / 2; 
    endAngle = startAngle + (angle * Math.PI / 180);
  }else if(angle < 0){
    endAngle = 3 * Math.PI / 2; 
    startAngle = endAngle + (angle * Math.PI / 180);
  }

  //draw the shaded
  speedo.beginPath();
  speedo.arc(centerX, centerY, radius, startAngle, endAngle);
  speedo.lineTo(centerX, centerY);
  speedo.fill();

  //draw the lines
  speedo.beginPath();
  speedo.arc(centerX, centerY, radius, Math.PI, 2 * Math.PI);
  speedo.stroke();


}

//generated a random number between -127 and 127
function genRand(){
  return Math.random() * 258 - 127;
}

//generated speedometers with random velocities
for(var i = 0; i < 8; i++){
  drawSpeedo(genRand(), speedoList[i]);
}

socket.on('depth', function(msg) {
  msg = JSON.parse(msg);
  document.getElementById("depth-data").innerHTML = "Depth : " + msg.Float64.toFixed(2);
});

socket.on('pi_temp', function(msg) {
  msg = JSON.parse(msg);
  document.getElementById("temp-data").innerHTML = "Temperature: <br>" + msg.Float32.toFixed(2);
});

