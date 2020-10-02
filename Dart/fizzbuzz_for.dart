import 'dart:io'; 

void main() {
print("Enter a number: ");
int num = int.parse(stdin.readLineSync()); 

for(int cont = 1; cont <= num; cont++){
    if (cont % 3 == 0 && cont % 5 == 0){
        print("fizzbuzz");
    } else if (cont % 3 == 0){
        print("fizz");
    } else if (cont % 5 == 0){
        print("buzz");
    } else {
        print("$cont"); }
}

}