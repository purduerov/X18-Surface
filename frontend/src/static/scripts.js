
const speedo1 = document.getElementById('speedo1');
const speedo2 = document.getElementById('speedo2');
const speedo3 = document.getElementById('speedo3');
const speedo4 = document.getElementById('speedo4');
const speedo5 = document.getElementById('speedo5');
const speedo6 = document.getElementById('speedo6');
const speedo7 = document.getElementById('speedo7');
const speedo8 = document.getElementById('speedo8');


function colorToAngle(angle){
  if(angle < 0){
    return `rgb(200, 0, 0)`
  }else if(angle > 0){
    return `rgb(0, 200, 0)`
  }else{
    return `rgb(0, 0, 0)`
  }
}

function drawSpeedo(angle, canvas){
  const speedo = canvas.getContext('2d');
  
  speedo.clearRect(0, 0, canvas.width, canvas.height);

  speedo.lineWidth = 2;
  speedo.strokeStyle = 'white';

  const arcColor = colorToAngle(angle);
  speedo.fillStyle = arcColor;

  const centerX = canvas.width / 2;
  const centerY = canvas.height;
  const radius = 100;

  let startAngle = 0;
  let endAngle = 0;

  if(angle >= 0){
    startAngle = 3 * Math.PI / 2; 
    endAngle = startAngle + (angle * Math.PI / 180);
  }else if(angle < 0){
    endAngle = 3 * Math.PI / 2; 
    startAngle = endAngle + (angle * Math.PI / 180);
  }

  speedo.beginPath();
  speedo.arc(centerX, centerY, radius, startAngle, endAngle);
  speedo.lineTo(centerX, centerY);
  speedo.fill();

  speedo.beginPath();
  speedo.arc(centerX, centerY, radius, Math.PI, 2 * Math.PI);
  speedo.stroke();


}

drawSpeedo(75, speedo1);
drawSpeedo(-60, speedo2);
drawSpeedo(35, speedo3);
drawSpeedo(20, speedo4);
drawSpeedo(-16, speedo5);
drawSpeedo(-85, speedo6);
drawSpeedo(-30, speedo7);
drawSpeedo(67, speedo8);