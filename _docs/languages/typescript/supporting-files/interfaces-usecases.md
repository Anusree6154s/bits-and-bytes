---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: Typescript Interfaces Usecases
excerpt: Different Usecases for Typescript Interfaces 
permalink: interfaces-usecases
tags: [typescript, interfaces]
parent_post: typescript-learners-guide
hidden: true
---



### **Interfaces**

An interface defines the structure of an object by specifying its properties and methods. However, interfaces are not limited to describing objects. They can also define function types, arrays, hybrid types, and even work with generics.


<br>
 
#### 1. **Defining Object Structures**
The most common use case for interfaces is to describe the shape of an object, including its properties and methods.

```typescript
interface Person {
  name: string;
  age: number;
  greet(): string;
}

const person: Person = {
  name: "Alice",
  age: 30,
  greet() {
    return `Hello, my name is ${this.name}`;
  },
};
```

<br>

#### 2. **Defining Function Types**
Interfaces can specify the structure of a function, including its parameter types and return type.

```typescript
interface GreetFunction {
  (name: string, age: number): string;
}

const greet: GreetFunction = (name, age) => {
  return `Hello, my name is ${name} and I am ${age} years old.`;
};

console.log(greet("Alice", 30)); // Hello, my name is Alice and I am 30 years old.
```

<br>

#### 3. **Defining Array Types**
Interfaces can describe the shape of arrays, specifying the types of elements they contain.

##### Example: Array with specific element types
```typescript
interface StringArray {
  [index: number]: string;
}

const fruits: StringArray = ["apple", "banana", "cherry"];
```

##### Example: Associative array (key-value pairs)
```typescript
interface Dictionary {
  [key: string]: number;
}

const inventory: Dictionary = {
  apples: 10,
  bananas: 20,
};
```

<br>

#### 4. **Using Interfaces with Classes**
Interfaces can act as contracts that classes must adhere to, ensuring the class implements specific properties and methods.

```typescript
interface Animal {
  name: string;
  makeSound(): void;
}

class Dog implements Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  makeSound() {
    console.log("Woof!");
  }
}

const dog = new Dog("Buddy");
dog.makeSound(); // Woof!
```

<br>

#### 5. **Extending Interfaces**
Interfaces can extend other interfaces, allowing you to build on existing definitions.

```typescript
interface Shape {
  color: string;
}

interface Circle extends Shape {
  radius: number;
}

const circle: Circle = {
  color: "red",
  radius: 10,
};
```

<br>

#### 6. **Hybrid Types**
Interfaces can describe entities that act as both objects and functions.

```typescript
interface Counter {
  (start: number): string; // Function signature
  count: number;           // Property
}

const counter: Counter = (start: number) => {
  counter.count = start;
  return `Counter started at ${start}`;
};

counter.count = 0;
console.log(counter(10)); // Counter started at 10
console.log(counter.count); // 10
```

<br>

#### 7. **Using Generics with Interfaces**
Interfaces can be generic, making them reusable for various types.

```typescript
interface Box<T> {
  content: T;
}

const stringBox: Box<string> = { content: "Hello" };
const numberBox: Box<number> = { content: 42 };

console.log(stringBox.content); // Hello
console.log(numberBox.content); // 42
```

<br>

#### 8. **Index Signatures**
Interfaces can define objects with dynamic keys where the key type is known, but the exact keys are not predefined.

```typescript
interface Roles {
  [role: string]: string;
}

const userRoles: Roles = {
  admin: "Administrator",
  editor: "Content Editor",
  viewer: "Read-Only User",
};
```

<br>

####  9. **Intersection Types with Interfaces**
Interfaces can be combined with other types using intersection (&) or union (|) types.

```typescript
interface User {
  name: string;
}

interface Admin {
  admin: boolean;
}

type AdminUser = User & Admin;

const admin: AdminUser = {
  name: "Alice",
  admin: true,
};
```

<br>

#### 10. **Interfaces vs. Type Aliases**
While interfaces and [type aliases](typescript-learners-guide#9-type-aliases) can overlap in functionality, interfaces are better suited for object-like structures, while type aliases excel with unions and complex compositions.

For example:

```typescript
// Interface for object-like structure
interface Person {
  name: string;
  age: number;
}

// Type alias for union types
type Role = "admin" | "user";

// Type alias for complex composition (union + intersection)
type Employee = Person & { role: Role };
```

<br>

#### 11. Optional Properties in Interfaces
You can make certain properties of an interface optional by adding a question mark (`?`) after the property name. This allows objects that implement the interface to omit these properties.

Example:

```typescript
interface Car {
  make: string;
  model: string;
  year?: number;  // Optional property
}

const myCar: Car = {
  make: "Toyota",
  model: "Corolla",
};
```
In this case, `year` is optional, so the `myCar` object can still be valid even without it.

<br>


### Summary
Interfaces in TypeScript are a powerful tool that extends far beyond simply defining object shapes. They can describe:

1. Object structures.
2. Function types.
3. Array types.
4. Classes (via contracts).
5. Hybrid types (both objects and functions).
6. Generic structures.
7. Indexable types.

Their versatility makes interfaces a foundational feature for designing flexible and type-safe TypeScript applications.
