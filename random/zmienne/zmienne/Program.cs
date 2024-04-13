//liczby całkowite
int myAge = 30;
int newAge = myAge + 5;
//Console.WriteLine(newAge);
int myVar = int.MinValue;
uint myVar2 = int.MaxValue;
ulong myVar3 = ulong.MaxValue;

// liczby zmienne przecinkowe 
float myNumer = float.MaxValue;
double myNumer2 = double.MaxValue;

//zmienne tekstowe 
string namy = "Michalina";
string surname = "Janowska";
string result = namy + surname + myAge;
//Console.WriteLine(result);
char myVar4 = 'c';
var result2 = namy.ToArray();

//zmienne logiczne
bool isActive = true;
isActive = false;
var isValid = 5 > 6;
//Console.WriteLine(isValid);




string name = "Ewa";
var age = 33;
string gender = "kobieta";
string surnam = "Kowalska";



if (name == "Ewa" && age == 33)
{
    Console.WriteLine("Ewa, lat 33");
}
else if (gender == "kobieta" && age < 30)
{
    Console.WriteLine("Kobieta poniżej 30 lat");
}
else if (gender != "kobieta" && age < 18)
{
    Console.WriteLine("Niepełnoletni Mężczyzna");
}
else if (surname != "Kowalska" && age == 33)
{
    Console.WriteLine("Ktoś kto nie ma na nazwisko Kowalska, ma 33 lata");
}