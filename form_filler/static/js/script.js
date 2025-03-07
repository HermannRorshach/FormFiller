let inputs = [...document.querySelectorAll('p > *:last-child')];


for (let input of inputs) {
    console.log(input)
}


let charLimits = {
    passport_number: 9,
    birthday: 8,
    date_of_issue: 8,
    date_of_expiry: 8,
    lond_number: 27
}

inputLimits = [...inputs.filter((input) => Object.keys(charLimits).includes(input.name))];

function moveFocusOnFill() {
    console.log("Вызов функции")
    let index = inputs.indexOf(this);
    if (this.value.length >= charLimits[this.name]) {
        inputs[index + 1].focus()
    }
}

function insertHyphen() {
    if (this.value.length === 13) {
        this.value += "-"
    }
}


inputLimits.forEach(input => input.addEventListener("input", moveFocusOnFill))

let textarea = document.querySelector("textarea");
textarea.addEventListener("input", insertHyphen)