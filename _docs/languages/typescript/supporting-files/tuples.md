---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: Tuples and how it differs from Arrays
excerpt: More about tuples, and difference between tuples and arrays
permalink: tuples
tags: [typescript, tuples]
parent_post: typescript-learners-guide
hidden: true
---

### **Table of Contents**
1. [What is Tuple](#1-what-is-tuple)
2. [Key Characteristics of Tuples](#2-key-characteristics-of-tuples)
3. [Optional and Rest Elements in Tuples](#3-optional-and-rest-elements-in-tuples)
4. [Tuples with Named Types or Objects](#4-tuples-with-named-types-or-objects)
5. [Destructuring Tuples](#5-destructuring-tuples)
6. [Readonly Tuples](#6-readonly-tuples)
7. [Using Tuples with Functions](#7-using-tuples-with-functions)
8. [Differences Between Arrays and Tuples](#8-differences-between-arrays-and-tuples)
<br>
 
### 1. **What is Tuple**

A **tuple** is a special type of array in TypeScript where the number of elements and their types are fixed. Unlike regular arrays, where all elements must be of the same type, a tuple can contain elements of different types, and the number of elements is fixed when the tuple is created.

#### **Syntax for Tuples**

A tuple is defined using square brackets `[]`, with types specified for each element. The order of the types in the tuple corresponds to the order of the elements in the tuple.

Example:

```typescript
let tuple: [string, number] = ["Alice", 30];
```

- The first element is a `string`, and the second element is a `number`.
- The tuple can only contain exactly two elements, and the types must match exactly: the first element must always be a `string`, and the second must always be a `number`.

<br>
 
### 2. **Key Characteristics of Tuples**

- **Fixed Size**: The size of a tuple is fixed. You cannot add or remove elements without causing a type error.

```typescript
let tuple: [string, number] = ["Alice", 30];
tuple.push(100); // Error: Tuple type '[string, number]' of length '2' has no element at index '2'.
```

- **Mixed Types**: Each element in a tuple can be of a different type.

```typescript
let user: [string, number, boolean] = ["Alice", 30, true];
```

Here, the tuple has three elements:

- The first is a `string`.
- The second is a `number`.
- The third is a `boolean`.

- **Accessing Elements**: You can access the elements of a tuple using their index, just like arrays.

```typescript
let user: [string, number] = ["Alice", 30];
console.log(user[0]); // Output: "Alice"
console.log(user[1]); // Output: 30
```

TypeScript will enforce the correct types when you access the elements, ensuring that the type of the value at the specified index matches the type in the tuple's definition.

<br>
 
### 3. **Optional and Rest Elements in Tuples**

Tuples in TypeScript can also support **optional elements** (using `?`) and **rest elements** (using `...`), allowing for more flexibility when defining the tuple's structure.

#### **Optional Elements**

Optional elements in tuples can be used when an element is not always required. This is done by adding a `?` after the element's type.

Example:

```typescript
let user: [string, number?, boolean?] = ["Alice"];
console.log(user); // Output: ["Alice"]
user = ["Bob", 25];
console.log(user); // Output: ["Bob", 25]
user = ["Charlie", 35, true];
console.log(user); // Output: ["Charlie", 35, true]
```

In this case:

- The second element (`number`) and the third element (`boolean`) are optional.
- The tuple can have 1, 2, or 3 elements.

#### **Rest Elements**

Rest elements allow you to define a tuple that can accept additional elements beyond the ones specified in the tuple’s definition. Rest elements are placed after the fixed elements and are prefixed with `...`.

Example:

```typescript
let coordinates: [number, number, ...number[]] = [0, 0, 1, 2, 3];
console.log(coordinates); // Output: [0, 0, 1, 2, 3]
```

In this example:

- The tuple starts with two `number` elements (`[0, 0]`).
- Then it can accept any `number` of additional number values after the first two elements.

<br>
 

### 4. **Tuples with Named Types or Objects**

You can also use **named types** or **objects** in a tuple. This allows you to combine the benefits of tuples and objects, making it possible to work with structured data in a more readable way.

Example:

```typescript
let employee: [string, number, { role: string }] = [
  "Alice",
  30,
  { role: "Engineer" },
];
```

In this example, the third element in the tuple is an object with a property `role` that is a `string`. This allows you to store more complex data in tuples while preserving type safety.
<br>
 
### 5. **Destructuring Tuples**

TypeScript allows destructuring of tuples just like arrays, making it easy to extract values from a tuple and assign them to variables.

Example:

```typescript
let person: [string, number] = ["John", 25];

let [name, age] = person;

console.log(name); // Output: "John"
console.log(age); // Output: 25
```

Here, we use array destructuring syntax to extract the `name` and `age` from the `person` tuple.
<br>
 
### 6. **Readonly Tuples**

If you want to prevent modification of a tuple's elements after its creation, you can use the `readonly` modifier to create a **readonly tuple**. This ensures that once the tuple is created, its values cannot be changed.

Example:

```typescript
let person: readonly [string, number] = ["John", 25];

person[0] = "Jane"; // Error: Index signature in type 'readonly [string, number]' only permits reading.
```

In this example, `person` is a readonly tuple, so trying to modify its elements will result in an error.
<br>
 
### 7. **Using Tuples with Functions**

You can also use tuples as function return types or arguments. This is useful when a function returns multiple values of different types.

Example:

```typescript
function getUserInfo(): [string, number] {
  return ["John", 25];
}

let [name, age] = getUserInfo();
console.log(name); // Output: "John"
console.log(age); // Output: 25
```
<br>
 
### 8. **Differences Between Arrays and Tuples**

While both arrays and tuples can store multiple values, they differ in the following key ways:

- **Arrays** are homogeneous collections, meaning all elements are of the same type (e.g., an array of numbers, an array of strings).
- **Tuples** are heterogeneous collections, meaning the elements can be of different types, and the types are fixed and predefined.

#### Example of an Array:

```typescript
let numbers: number[] = [1, 2, 3, 4]; // All elements are of type 'number'
```

#### Example of a Tuple:

```typescript
let user: [string, number, boolean] = ["Alice", 30, true]; // Different types
```
<br>
 
### **Conclusion**


- **Tuples** are a special type of array that allows you to store values of different types in a fixed-length collection. Tuples are useful when you want to represent heterogeneous data in a fixed order.
- Both **arrays** and **tuples** are essential for organizing collections of values, with arrays offering flexibility for homogeneous collections and tuples offering structure and type safety for heterogeneous collections.

By using arrays and tuples effectively, you can write more robust, maintainable, and type-safe code in TypeScript.
