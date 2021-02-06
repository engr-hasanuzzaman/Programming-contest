// https://fsharp.org/use/linux/
open System

let hello() = 
  printf "Enter your name : "

  let name = Console.ReadLine()
  printfn "Hello %s" name


hello()
printfn("this is sumon")
Console.ReadKey() |> ignore