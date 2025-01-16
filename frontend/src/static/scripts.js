const slider1 = document.getElementById('slider1');
const slider2 = document.getElementById('slider2');
const slider3 = document.getElementById('slider3');
const slider4 = document.getElementById('slider4');
const slider5 = document.getElementById('slider5');
const slider6 = document.getElementById('slider6');
const slider7 = document.getElementById('slider7');
const slider8 = document.getElementById('slider8');
const speedo1 = document.getElementById('speedo1');
const speedo2 = document.getElementById('speedo2');
const speedo3 = document.getElementById('speedo3');
const speedo4 = document.getElementById('speedo4');
const speedo5 = document.getElementById('speedo5');
const speedo6 = document.getElementById('speedo6');
const speedo7 = document.getElementById('speedo7');
const speedo8 = document.getElementById('speedo8');
const sliderValue1 = document.getElementById('sliderValue1');
const sliderValue2 = document.getElementById('sliderValue2');
const sliderValue3 = document.getElementById('sliderValue3');
const sliderValue4 = document.getElementById('sliderValue4');
const sliderValue5 = document.getElementById('sliderValue5');
const sliderValue6 = document.getElementById('sliderValue6');
const sliderValue7 = document.getElementById('sliderValue7');
const sliderValue8 = document.getElementById('sliderValue8');
const scaleCanvas = 0.75;

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
  speedo.strokeStyle = 'black';

  const arcColor = colorToAngle(angle);
  speedo.fillStyle = arcColor;

  const centerX = canvas.width / 2;
  const centerY = canvas.height;
  const radius = 100 * scaleCanvas;

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

slider1.addEventListener('input', function(){
  const angle = slider1.value;
  sliderValue1.textContent = angle;
  drawSpeedo(angle, speedo1);
});


slider2.addEventListener('input', function(){
  const angle = slider2.value;
  sliderValue2.textContent = angle;
  drawSpeedo(angle, speedo2);
});


slider3.addEventListener('input', function(){
  const angle = slider3.value;
  sliderValue3.textContent = angle;
  drawSpeedo(angle, speedo3);
});


slider4.addEventListener('input', function(){
  const angle = slider4.value;
  sliderValue4.textContent = angle;
  drawSpeedo(angle, speedo4);
});


slider5.addEventListener('input', function(){
  const angle = slider5.value;
  sliderValue5.textContent = angle;
  drawSpeedo(angle, speedo5);
});


slider6.addEventListener('input', function(){
  const angle = slider6.value;
  sliderValue6.textContent = angle;
  drawSpeedo(angle, speedo6);
});


slider7.addEventListener('input', function(){
  const angle = slider7.value;
  sliderValue7.textContent = angle;
  drawSpeedo(angle, speedo7);
});


slider8.addEventListener('input', function(){
  const angle = slider8.value;
  sliderValue8.textContent = angle;
  drawSpeedo(angle, speedo8);
});