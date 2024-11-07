const slider1 = document.getElementById('slider1');
const slider2 = document.getElementById('slider2');
const slider3 = document.getElementById('slider3');
const slider4 = document.getElementById('slider4');
const slider5 = document.getElementById('slider5');
const slider6 = document.getElementById('slider6');
const speedometer1 = document.getElementById('speedometer-tip1');
const speedometer2 = document.getElementById('speedometer-tip2');
const speedometer3 = document.getElementById('speedometer-tip3');
const speedometer4 = document.getElementById('speedometer-tip4');
const speedometer5 = document.getElementById('speedometer-tip5');
const speedometer6 = document.getElementById('speedometer-tip6');
const thrust_value1 = document.getElementById('thrust-value1');
const thrust_value2 = document.getElementById('thrust-value2');
const thrust_value3 = document.getElementById('thrust-value3');
const thrust_value4 = document.getElementById('thrust-value4');
const thrust_value5 = document.getElementById('thrust-value5');
const thrust_value6 = document.getElementById('thrust-value6');
const max_thrust = 127;

slider1.addEventListener('input', function(){
    const rotation = slider1.value;
    speedometer1.style.transform = `rotate(${rotation}deg)`;
    const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
    thrust_value1.textContent = `Thrust: ${actual_thrust}`;
});

slider2.addEventListener('input', function(){
  const rotation = slider2.value;
  speedometer2.style.transform = `rotate(${rotation}deg)`;
  const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
  thrust_value2.textContent = `Thrust: ${actual_thrust}`;
});

slider3.addEventListener('input', function(){
  const rotation = slider3.value;
  speedometer3.style.transform = `rotate(${rotation}deg)`;
  const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
  thrust_value3.textContent = `Thrust: ${actual_thrust}`;
});

slider4.addEventListener('input', function(){
  const rotation = slider4.value;
  speedometer4.style.transform = `rotate(${rotation}deg)`;
  const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
  thrust_value4.textContent = `Thrust: ${actual_thrust}`;
});

slider5.addEventListener('input', function(){
const rotation = slider5.value;
speedometer5.style.transform = `rotate(${rotation}deg)`;
const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
thrust_value5.textContent = `Thrust: ${actual_thrust}`;
});

slider6.addEventListener('input', function(){
const rotation = slider6.value;
speedometer6.style.transform = `rotate(${rotation}deg)`;
const actual_thrust = (rotation * (max_thrust / 90)).toFixed(2);
thrust_value6.textContent = `Thrust: ${actual_thrust}`;
});


