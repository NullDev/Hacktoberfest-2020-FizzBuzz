for ($i=0; $i -le 100; $i++){
$r = Get-Random -Maximum 100
if (($r%3 -eq 0) -and ($r%5 -eq 0)){
write-output "FizzBuzz ($r)"
} elseif($r%3 -eq 0){
Write-Output "Fizz ($r)"
}elseif ($r%5 -eq 0){
Write-Output "Buzz ($r)"
}else{
Write-Output $r
}

}