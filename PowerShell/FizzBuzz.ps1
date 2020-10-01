# [CmdletBinding()]
# param (
#   [Parameter(Mandatory = $false, Position = 0)]
#   $Min = 1,

#   [Parameter(Mandatory = $false, Position = 1)]
#   $Max = 100
# )

for ($I = 1; $I -le 100; $I++) {
  $out = ""
  if ($I % 3 -eq 0) { $out += "Fizz" }
  if ($I % 5 -eq 0) { $out += "Buzz" }
  if ($out -eq "") { $out = $I }

  Write-Output $out
}