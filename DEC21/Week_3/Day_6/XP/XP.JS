// EX1 List Of People

let people = ["Greg", "Mary", "Devon", "James"]

// Write code to remove “Greg” from the people array.
people.shift()
console.log(people)

// Write code to replace “James” to “Jason”.
people.splice(2, 1, 'Jason')
console.log(people)

// Write code to add your name to the end of the people array.
people.splice(3, 0, 'Yona')
console.log(people)

// Using a loop, iterate through the people array and console.log each person.
for (let element of people) {
    console.log(element)
}

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
for (let element of people) {
    if (element === 'Jason') {
        break;
    }
    console.log(element)
}

// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
let people2 = people.slice(-3);
console.log(people2);

let people3 = people.slice(0, 3);
console.log(people3);

// Write code that console.logs Mary’s index.
console.log(people.indexOf('Mary'));


// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
console.log(people.indexOf('Foo'));
// It returns -1 because it does not exist

// Create a variable called last which value is the last element of the array.
let last = people[people.length - 1];
console.log(last)

// ex2
/// Create an array called colors where the value is a list of your favorite colors.
let colors = ['blue', 'red', 'orange', 'purple'];

for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i+1} choice is ${colors[i]}`)
}

let suffixes = ['st', 'nd', 'rd', 'th'];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i+1}${suffixes[i]} choice is ${colors[i]}`)
}


// Exercise 3 : Repeat The Question

// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
let i = parseInt(prompt('Enter a number'));
while (i < 10) {
    console.log("The number is " + i)
    i = parseInt(prompt('Enter a number'));
}


// EX5
// / Exercise 1 : Building Management

let building = {
    numberLevels: 4,
    numberOfAptByLevel: {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        "Sarah": [3, 990],
        "Dan": [4, 1000],
        "David": [1, 500],
    },
}


// Console.log the number of levels in the building.
console.log(building['numberLevels']);
//console.log(Object.keys(building['numberOfAptByLevel']).length)


// Console.log how many apartments are on levels 1 and 3.
console.log(building['numberOfAptByLevel']['1']);
console.log(building['numberOfAptByLevel']['3']);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(`The name of the second tenant is ${building['nameOfTenants'][1]} and he has ${building['numberOfRoomsAndRent']['Dan'][0]} rooms`)

// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
rent1 = building['numberOfRoomsAndRent']['Sarah'][1] + building['numberOfRoomsAndRent']['David'][1];
console.log(rent1)

// If it is than increase Dan’s rent.

if (rent1 > building['numberOfRoomsAndRent']['Dan'][1]) {
    building['numberOfRoomsAndRent']['Dan'][1] = rent1;
    console.log(`The new rent of Dan is ${building['numberOfRoomsAndRent']['Dan'][1]}`);

} else {
    console.log('The rent is inchanged')
}

// Exercise 5 : Family

// Create an object called family with a few key value pairs.
let family = {
    firstname: "Lea",
    Lastname: "Smith",
    children: 4,
    city: "London"
}

// Console.log the keys. (using a for loop).
for (let element in family) {
    console.log(element)
}

// Console.log the values. (using a for loop).
for (let element in family) {
    console.log(family[element])
}


// Exercise 6

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let sentence = []
    // Given the object above, console.log “my name is Rudolf the raindeer”
for (let element in details) {
    sentence += element + ' ' + details[element] + ' '
}
console.log(sentence)



// Exercise 7 : Secret Group

let surname = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
    // A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.

let x = surname.toString();
let society = x.match(/\b(\w)/g).join('');
console.log('The name of their secret society is', society)