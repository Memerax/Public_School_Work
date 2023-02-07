function calculateArea() {
  let lengthOfField = parseInt(document.querySelector("#length").value)
  let widthOfField = parseInt(document.querySelector("#width").value)
  let areaOfField = lengthOfField * widthOfField
  document.querySelector('#result1').innerHTML = `${areaOfField}`
}

function calculateReturn() {
  let numberLessThenLiter = parseFloat(document.querySelector("#lessthenliter").value)
  let numberGreaterThenLiter = parseFloat(document.querySelector("#greaterthenliter").value)
  let total =(numberGreaterThenLiter * 0.25) + (numberLessThenLiter * 0.1)
  document.querySelector("#result2").innerHTML = `${total.toFixed(2)}`
}

function resetArea() {
  document.querySelector('#result1').innerHTML = `0`
}

function resetBottleTotal() {
  document.querySelector("#result2").innerHTML = `0`

}