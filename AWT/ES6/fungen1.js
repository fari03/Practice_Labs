function* evenNumbers() {
    let number = 0;
    while (true) {
      yield number;
      number += 2;
    }
  }
  
  const generator = evenNumbers();
  console.log(generator.next().value); // Output: 0
  console.log(generator.next().value); // Output: 2
  console.log(generator.next().value); // Output: 4
  
