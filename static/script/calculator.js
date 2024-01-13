function calculate() {
  var x = document.getElementById("value1").value;
  var y = document.getElementById("value2").value;
  var op = document.getElementById("operator").value;
  var result;

  if (op == "add") {
    result = parseInt(x) + parseInt(y);
  } else if (op == "subtract") {
    result = parseInt(x) - parseInt(y);
  } else if (op == "multiply") {
    result = parseInt(x) * parseInt(y);
  }

  document.getElementById("result").innerHTML = "Result: " + result;
}
