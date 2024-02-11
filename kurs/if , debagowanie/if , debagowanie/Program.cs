int number = 5;
int number2 = 10;

//==  równa się
//!=  różni się
//>  większa 
//<  mniejsza
//>=  większa lub równa
//<=  mniejsza lub równa   OPERATORY RELACYJNE

if (number > number2) //operator relacyjny
{
    // Console.WriteLine("JESTEM TUTAJ W LINI 6");
}
else
{
    //Console.WriteLine("JESTEM TUTAJ W LINI 10");
}


var name = "Michalina";
var age = 14;

if (name == "Michalina" && age < 20) // && - i    || - lub  ! - negowanie  OPERATORY LOGICZNE
{
    // Console.WriteLine("JESTEM MICHALINA PRZED 20");
}
else
{
    // Console.WriteLine("JESTEM KIMS INNYM");
}

if (age > 30)
{
    //Console.WriteLine("JESTEM PO 30");
}
else if (age > 20)
{
    // Console.WriteLine("JESTEM PO 20 ");
}
else if (age > 10)
{
    // Console.WriteLine("JESTEM PO 10 ");
}


if (age > 30)
{
    //Console.WriteLine("JESTEM PO 30");
}
else if (age > 20)
{
    // Console.WriteLine("JESTEM PO 20 ");
}
else if (age > 10) //zagnieżdżanie
{
    if (name == "Adam")
    {
        Console.WriteLine("JESTEM PO 10 I MAM NA IMIE MICHALINA ");
    }
    else
    {
        Console.WriteLine("JESTEM PO 10 I NIE MAM NA IMIE MICHALINA ");
    }
}

// formatowanie kodu ( ctrl + k + d )
