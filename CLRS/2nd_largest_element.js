'use strict';

// use selection sort to find the 2nd largest element
function processData(myArray) {
    if (myArray.lenght === 0) {
        return 0;
    }

    maxVal = myArray[0];
    for (let i = 0; i < myArray.length; i++) {
        for(let j = 0; j < myArray.length - 1 - i; j++) {
            if(myArray[j] > myArray[j+1]) {
                let tmp = myArray[j];
                myArray[j] = myArray[j+1];
                myArray[j+1] = tmp;
            }
        }

        if(i > 0 && myArray[myArray.length - 1 - i] !== myArray[myArray.length - i]) {
            console.log(myArray[myArray.length - 1 - i]);
            return;
        }
    }
    console.log(myArray[0]);
}