var slider = document.getElementById("myRange");
var output = document.getElementById("ref");
var temp = document.getElementById("temp");
var alert = document.getElementById("alert");
output.innerHTML = slider.value * 30 / 100;

slider.oninput = function() {
  output.innerHTML = this.value * 30 / 100;
  updateTemp(this.value)
}

setInterval(getTemp, 1000)

async function getTemp(){
  const get = await fetch(`/temp`)
  const formatted = await get.json()
  temp.innerHTML = formatted.temperature
  if (formatted.buzzer == 1){
      alert.style.display = 'flex'
  }
  else {
      alert.style.display = 'none'
  }
}

async function updateTemp(ref){
  fetch(`/update/ref/${ref}`)
}