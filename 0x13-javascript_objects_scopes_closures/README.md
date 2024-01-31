# 0x13. JavaScript - Objects, Scopes and Closures
-----

### Why JavaScript programming is amazing

-   JavaScript is versatile, used both on the client and server-side.
-   It has a vast ecosystem of libraries and frameworks.
-   It supports both procedural and object-oriented programming paradigms.

### How to create an object in JavaScript

-   Objects can be created using object literal notation: `{ key: value }`.
-   Constructor functions or ES6 classes can be used to create objects.

### What `this` means

-   `this` refers to the current execution context.
-   In the context of an object method, `this` refers to the object itself.

### What `undefined` means

-   `undefined` is a primitive value automatically assigned to variables that have been declared but not initialized with a value.

### Why variable type and scope are important

-   Variable type defines the kind of data a variable can hold.
-   Scope determines where variables and functions are accessible within the code.
-   Understanding types and scopes helps in writing maintainable and bug-free code.

### What is a `closure`

-   A closure is a function bundled together with its lexical environment, allowing it to access variables from its outer scope even after the outer scope has closed.

### What is a `prototype`

-   Prototypes are mechanisms by which JavaScript objects inherit features from one another.
-   Every JavaScript object has a prototype, which is another object that it inherits properties and methods from.

### How to inherit an object from another

-   Inheritance can be achieved through prototype chaining or using ES6 classes and the `extends` keyword.

----------

**Note:** For a standardized README, use `semistandard` by installing it globally with `npm install semistandard --global`.

## More Info

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://intranet.alxswe.com/rltoken/oc1-9XTUtCiIyZkdAFvoUQ "Documentation")

```
$ sudo npm install semistandard --global
```