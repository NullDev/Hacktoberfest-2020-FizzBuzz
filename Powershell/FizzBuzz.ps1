# Simple fizzbuzz with powershell 
# Auther: @jmmille

for($x = 1; $x -le 100; $x++) {
  if (($x%3 -eq 0) -and ($x%5 -eq 0)) {
    Write-Output "fizzbuzz"
  } elseif ($x%3 -eq 0) {
    Write-Output "fizz"
  } elseif ($x%5 -eq 0) {
    Write-Output "buzz"
  } else {
    Write-Output $x
  }
}
