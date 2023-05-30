function* fibonacci() {
    let prev = 0;
    let current = 1;
  
    while (true) {
      yield current;
      [prev, current] = [current, prev + current];
    }
  }
  
  const fib = fibonacci();
  console.log(fib.next().value); // Output: 1
  console.log(fib.next().value); // Output: 1
  console.log(fib.next().value); // Output: 2
  console.log(fib.next().value); // Output: 3
  
