---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: Generics Examples
permalink: generics
tags: [typescript, generics]
parent_post: typescript-learners-guide
hidden: true
---



### **1. Generic Interfaces**

A **generic interface** allows you to define type-safe interfaces that work with various types.

#### Example with Object Structures:
```typescript
interface Pair<K, V> {
  key: K;
  value: V;
}

const numberPair: Pair<string, number> = {
  key: "age",
  value: 30,
};

console.log(numberPair.key); // Output: age
console.log(numberPair.value); // Output: 30
```

#### Example with Function Types:
```typescript
interface GenericFunction<T> {
  (arg: T): T;
}

const stringFunction: GenericFunction<string> = (arg) => arg.toUpperCase();
console.log(stringFunction("hello")); // Output: HELLO
```
<br>
 

### **2. Generic Constraints with `keyof`**

The `keyof` keyword allows you to constrain a generic to the keys of an object.

#### Example:
```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const person = { name: "Alice", age: 30 };

console.log(getProperty(person, "name")); // Output: Alice
console.log(getProperty(person, "age"));  // Output: 30

// Error: Argument of type '"address"' is not assignable to parameter of type 'keyof T'
// console.log(getProperty(person, "address"));
```

Here, `K` is constrained to be a key of the type `T`.

<br>
 
### **3. Generics with Default Types**

You can provide **default types** for generics to make them optional when the type isn't explicitly specified.

#### Example:
```typescript
class BoxWithDefault<T = string> {
  value: T;
  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

const defaultBox = new BoxWithDefault("Default Value");
console.log(defaultBox.getValue()); // Output: Default Value

const numberBox = new BoxWithDefault<number>(42);
console.log(numberBox.getValue()); // Output: 42
```
<br>
 

### **4. Benefits of Generics**

1. **Type Safety:** Generics enforce type constraints, reducing runtime errors caused by incorrect types.
2. **Reusability:** Create reusable components that work across various data types.
3. **Flexibility:** Allow defining types dynamically while maintaining strong typing.
4. **Readability:** Simplify complex types and make the intent of the code clear.

