open System
let s = Console.ReadLine() |> int
let x = 
    [
        let mutable n = Console.ReadLine()
        while not (n = "bk") do
            yield n |> int
            n <- Console.ReadLine()
    ]
for elm in x do
    for i in 1..s do
        printfn "%i" elm