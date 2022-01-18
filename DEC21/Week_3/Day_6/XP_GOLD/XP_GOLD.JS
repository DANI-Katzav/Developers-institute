// Exercise 2 : Divisible By Three

let numbers = [123, 8409, 100053, 333333333, 7]

// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log “true” or “false”.

for (let element of numbers) {
    if (element % 3 === 0) {
        console.log('True for', element)
    } else {
        console.log('False for', element)
    }
}


// Exercise 3 : Playing With Numbers

let age = [20, 5, 12, 43, 98, 55];

// 1. Console.log the sum of all the numbers in the age array.
let sum = 0;
for (element of age) {
    sum += element;
}
console.log(sum)


// 2. Console.log the largest age in the array.
let largest = 0;
for (element of age) {
    if (element > largest) {
        largest = element;
    } else {
        largest = largest
    }
}
console.log(largest)