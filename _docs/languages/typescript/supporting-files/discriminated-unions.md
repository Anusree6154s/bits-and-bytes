---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Discriminated Unions
permalink: discriminated-unions
tags: [typescript, discriminated unions]
parent_post: typescript-learners-guide
hidden: true
---

### **Discriminated Unions in TypeScript**

Discriminated unions, also known as tagged unions or algebraic data types, are a powerful feature in TypeScript. They enable you to work with union types that include a shared property (discriminant) to help narrow down specific types in a type-safe way. This makes it easier to work with complex types and ensures type safety during development.

<br>

### **1. What Are Discriminated Unions?**

A discriminated union is a **union type** where each variant (type in the union) has a unique literal property, often called a **discriminant** or **tag**. The discriminant property is used to determine which variant of the union is currently being used.

#### Key Components:

1. **Union Types**: A type composed of multiple possible types.You define it by using the `|` (pipe) symbol to combine multiple types.

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; sideLength: number };
```

2. **Discriminant Property**: A shared property that uniquely identifies each member of the union. It often uses a literal value like "`circle"` or `"square"`.

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; sideLength: number };
```

3. **Narrowing**: TypeScript uses the discriminant to refine the type within specific branches of code.

```typescript
function area(shape: Shape): number {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2; // shape is narrowed to { kind: "circle"; radius: number }
  } else {
    return shape.sideLength ** 2; // shape is narrowed to { kind: "square"; sideLength: number }
  }
}
```

- **Explanation**: Inside the `if` and `else` branches, TypeScript narrows the type based on the value of `shape.kind`. If `shape.kind` is `"circle"`, TypeScript knows it’s a circle and can access the `radius` property. Similarly, if `shape.kind` is `"square"`, TypeScript knows it’s a square and can access the `sideLength` property.

<br>

### **2. Example: Discriminated Unions**

Here’s an example where `kind` is the discriminant property:

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; sideLength: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    case "rectangle":
      return shape.width * shape.height;
    default:
      throw new Error("Unknown shape");
  }
}

const circle: Shape = { kind: "circle", radius: 10 };
console.log(area(circle)); // 314.1592653589793
```

<br>

### **3. How Discriminated Unions Work**

TypeScript uses **control flow analysis** to refine types within a block of code. When it detects a comparison or check against the discriminant property, it narrows the type automatically.

#### Example:

```typescript
type Animal =
  | { type: "dog"; bark: () => void }
  | { type: "cat"; meow: () => void };

function makeSound(animal: Animal): void {
  if (animal.type === "dog") {
    animal.bark(); // TypeScript knows this is a dog
  } else {
    animal.meow(); // TypeScript knows this is a cat
  }
}
```

<br>

### **4. Benefits of Discriminated Unions**

1. **Type Safety**: Ensures only valid properties and methods are accessed.
2. **Readability**: The discriminant property makes it easy to distinguish between types.
3. **Error Prevention**: TypeScript catches missing cases in functions and ensures exhaustive checks when using `switch` statements.
4. **Code Clarity**: Clear separation of logic for each type in the union.

<br>

### **5. Exhaustiveness Checking**

TypeScript helps ensure that all possible variants of a discriminated union are handled. If you miss a case, TypeScript can throw an error.

#### Example: Adding a `never` Case

```typescript
function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    case "rectangle":
      return shape.width * shape.height;
    default:
      const _exhaustiveCheck: never = shape; // TypeScript error if a new variant is added
      throw new Error(`Unhandled shape: ${_exhaustiveCheck}`);
  }
}
```

<br>

### **6. Practical Use Cases**

Discriminated unions are widely used for scenarios where you need to handle multiple related types with unique behaviors.

#### **6.1 State Management**

```typescript
type State =
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; error: string };

function handleState(state: State): void {
  switch (state.status) {
    case "loading":
      console.log("Loading...");
      break;
    case "success":
      console.log(`Data: ${state.data}`);
      break;
    case "error":
      console.error(`Error: ${state.error}`);
      break;
  }
}
```

#### **6.2 API Responses**

```typescript
type ApiResponse =
  | { status: "ok"; data: any }
  | { status: "error"; error: string };

function handleResponse(response: ApiResponse): void {
  if (response.status === "ok") {
    console.log("Data:", response.data);
  } else {
    console.error("Error:", response.error);
  }
}
```
