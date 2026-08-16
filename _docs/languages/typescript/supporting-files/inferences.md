---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Inferences in Typescript
permalink: inferences
tags: [typescript, inferences]
parent_post: typescript-learners-guide
hidden: true
---


### **1. Contextual Typing**

TypeScript uses the surrounding context to infer types, especially in scenarios like function callbacks.

#### Example:
```typescript
const names = ["Alice", "Bob", "Charlie"];

// The type of `name` is inferred as string
names.forEach((name) => {
  console.log(name.toUpperCase());
});
```

Here, the type of `name` is inferred from the array `names`, which is of type `string[]`.

<br>
 
### **2. Best Common Type**

When inferring the type of a more complex expression, TypeScript tries to find the **best common type**.

#### Example:
```typescript
const mixedArray = [1, "string", true]; // Type: (string | number | boolean)[]
```

TypeScript combines all the types in the array and assigns the union type `(string | number | boolean)` to the `mixedArray` variable.

<br>
 

### **3. Type Assertions with Inference**

Sometimes, you may know more about a type than TypeScript does. In such cases, you can use **type assertions** to explicitly tell TypeScript what type to consider.

#### Example:
```typescript
let someValue: unknown = "Hello, world!";
let stringLength = (someValue as string).length; // Type: number
```

<br>
 

### **4. Limitations of Type Inference**

Type inference works well for simple cases but may require explicit types in more complex scenarios.

#### Example:
```typescript
function parseInput(input: string | number) {
  if (typeof input === "string") {
    return input.toUpperCase(); // Return type inferred as string
  } else {
    return input.toFixed(2); // Return type inferred as string
  }
}
```

Here, TypeScript infers the return type as `string`, but using explicit typing can clarify intent.

<br>
 

### **5. Inference in Generics**

Generics also benefit from type inference, allowing you to omit the generic type when TypeScript can infer it.

#### Example:
```typescript
function identity<T>(value: T): T {
  return value;
}

let inferredString = identity("Hello"); // T inferred as string
let inferredNumber = identity(42);      // T inferred as number
```

<br>
 

### **6. Return Type Inference in Arrow Functions**

TypeScript can infer the return type of arrow functions based on their bodies.

#### Example:
```typescript
const multiply = (a: number, b: number) => a * b; // Return type inferred as number
```

Explicit return types are still helpful for clarity:
```typescript
const multiply = (a: number, b: number): number => a * b;
```

<br>
 

### **7. Type Inference with Destructuring**

TypeScript infers types even in destructuring assignments.

#### Example:
```typescript
const point = { x: 10, y: 20 };

// x and y inferred as number
const { x, y } = point;

const colors = ["red", "blue", "green"];
const [firstColor, secondColor] = colors; // Inferred as string
```
