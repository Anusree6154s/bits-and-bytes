---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Type Manipulation
permalink: type-manipulation
tags: [typescript, type manipulation]
parent_post: typescript-learners-guide
hidden: true
---

### **Type Manipulation in TypeScript**

**Type manipulation** in TypeScript refers to the ability to **transform** or **infer** types based on certain conditions, allowing you to create more flexible and reusable code. TypeScript provides powerful tools for manipulating types, such as `infer`, **conditional types**, and utility types, among others. Here's an overview of these key concepts:

<br>

### **1. Conditional Types**

Conditional types allow you to select one type over another based on a condition. This is similar to a ternary operator (`condition ? true : false`) but for types.

**Basic Syntax:**

```typescript
type ConditionalType<T> = T extends SomeCondition ? TrueType : FalseType;
```

In this example, `T` is checked against `SomeCondition`. If it matches, the result is `TrueType`; otherwise, it will be `FalseType`.

<br>

### **2. `infer` Keyword for Type Inference**

The `infer` keyword allows you to **extract** a type from a more complex type within conditional types. It's especially useful for situations where you want to **infer** the type of a function's return value, arguments, or other components without having to explicitly define it.

**Example of `infer` with `ReturnType`:**

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
```

Here, `ReturnType<T>` is a conditional type that:

- Checks if `T` is a function (denoted by `(...args: any[]) =>`).
- If `T` is a function, it **infers** the return type of that function and assigns it to `R`.
- If `T` is not a function, it returns `never` (meaning an invalid type).

**Usage Example:**

```typescript
type MyFunction = (x: number, y: number) => string;

type Result = ReturnType<MyFunction>;  // Result will be `string`
```

Here, the type `Result` will be `string` because the function `MyFunction` returns a `string`. The `ReturnType` utility extracts that return type.

<br>

### **3. Common Use Cases for Type Manipulation**

#### **Extracting Function Arguments**
You can use the `infer` keyword to extract the types of function parameters as well.

```typescript
type ParameterType<T> = T extends (arg: infer U) => any ? U : never;

type MyFunction = (x: number) => string;

type Param = ParameterType<MyFunction>;  // Param will be `number`
```

In this example, `ParameterType` extracts the type of the parameter passed to the function. If `MyFunction` takes a `number`, then `Param` will be `number`.

#### **Discriminated Unions with `infer`**
You can use `infer` to narrow types in conditional types when dealing with **discriminated unions**.

```typescript
type Shape = 
  | { kind: 'circle', radius: number }
  | { kind: 'square', sideLength: number };

type GetShapeType<T> = T extends { kind: 'circle' } ? 'Circle' :
                      T extends { kind: 'square' } ? 'Square' :
                      never;

type CircleType = GetShapeType<{ kind: 'circle', radius: 10 }>;  // 'Circle'
type SquareType = GetShapeType<{ kind: 'square', sideLength: 20 }>;  // 'Square'
```

Here, we use a conditional type to map over a **discriminated union** to extract the types based on the `kind` property.

<br>

### **4. Using Utility Types for Type Transformation**

TypeScript also offers a range of **utility types** that make it easier to manipulate types in common scenarios. These types include `Partial`, `Required`, `Readonly`, `Record`, etc.

#### **Example: `Pick`, `Omit`, and `Exclude`**

```typescript
interface Person {
  name: string;
  age: number;
  address: string;
}

// Pick specific keys from the interface
type NameAndAge = Pick<Person, 'name' | 'age'>;  // { name: string; age: number }

// Omit specific keys from the interface
type WithoutAddress = Omit<Person, 'address'>;  // { name: string; age: number }

// Exclude specific types from a union
type WithoutString = Exclude<string | number | boolean, string>;  // number | boolean
```

- **`Pick<T, K>`**: Picks a subset of properties from a type `T`.
- **`Omit<T, K>`**: Omit specific properties from a type `T`.
- **`Exclude<T, U>`**: Excludes types from a union type.

These utility types are often used for type manipulation, allowing you to create new types based on existing ones.

<br>

### **5. Key Takeaways of Type Manipulation**

| **Concept**            | **Explanation**                                                                                                                                                       | **Example**                                                                                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Conditional Types**   | Types that select one type over another based on a condition.                                                                                                         | `type IsString<T> = T extends string ? true : false;`                                                                                                                           |
| **`infer` Keyword**     | Extracts a type within a conditional type, useful for inferring function return types or extracting types from more complex types.                                      | `type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;`                                                                                                    |
| **Function Arguments**  | Extracts the types of function arguments.                                                                                                                              | `type Param<T> = T extends (arg: infer U) => any ? U : never;`                                                                                                                |
| **Discriminated Unions**| Conditional types combined with discriminated unions to narrow down types.                                                                                             | `type ShapeType<T> = T extends { kind: 'circle' } ? 'Circle' : T extends { kind: 'square' } ? 'Square' : never;`                                                            |
| **Utility Types**       | Built-in utility types like `Pick`, `Omit`, `Partial`, `Required`, and `Exclude` allow transformation of types in useful ways.                                          | `type NameAndAge = Pick<Person, 'name' | 'age'>;`                                                                                                                               |

<br>

### **6. Conclusion**

Type manipulation in TypeScript allows you to create flexible, reusable, and strongly typed code by leveraging the power of conditional types, `infer`, and utility types. These tools enable complex type transformations that are both expressive and maintainable, making TypeScript a robust language for building large and scalable applications.

