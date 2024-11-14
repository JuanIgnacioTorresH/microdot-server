function toggleLed (led){
    fetch(`/led/toggle/${led}`)
    console.log(led)
}