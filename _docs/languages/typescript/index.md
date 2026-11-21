---
layout: default
date: 18 jan 2025
title: Typescript learners guide
excerpt: To study basic and advanced typescript
permalink: typescript-learners-guide
tags: [typescript]
parent: Languages
has_children: true
---

To study basic and advanced typescript:

<br>
<br>

## <ins>Table of Contents</ins>

- [Basic](#basic-typescript-concepts)
  1. [Basic Types](#1-basic-types)
  2. [Type Annotations](#2-type-annotations)
  3. [Interfaces](#3-interfaces)
  4. [Classes](#4-classes)
  5. [Enums](#5-enums)
  6. [Functions](#6-functions)
  7. [Arrays and Tuples](#7-arrays-and-tuples)
  8. [Union and Intersection Types](#8-union-and-intersection-types)
  9. [Type Aliases](#9-type-aliases)
  10. [Generics](#10-generics)
  11. [Modules](#11-modules)
  12. [Type Inference](#12-type-inference)
- [Advanced](#advanced-typescript-concepts)
  1. [Advanced Types](#1-advanced-types)
  2. [Type Guards](#2-type-guards)
  3. [Discriminated Unions](#3-discriminated-unions)
  4. [Keyof and Lookup Types](#4-keyof-and-lookup-types)
  5. [Template Literal Types](#5-template-literal-types)
  6. [Decorators](#6-decorators)
  7. [Declaration Merging](#7-declaration-merging)
  8. [Namespace](#8-namespace)
  9. [Type Manipulation](#9-type-manipulation)
  10. [Module Augmentation](#10-module-augmentation)
  11. [Strict Type Checking](#11-strict-type-checking)
  12. [Advanced Generics](#12-advanced-generics)
  13. [Dynamic Import Types](#13-dynamic-import-types)
  14. [Compiler Configuration](#14-compiler-configuration)
  15. [Advanced Decorator Usage](#15-advanced-decorator-usage)
- [Interview Questions](#3-interview-questions)

<br>
<br>

## <ins>Basic Typescript Concepts</ins>

### 1. **Basic Types**

TypeScript provides a set of basic types for handling data:

#### **`string`, `number`, `boolean`**

```typescript
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;
```

<br>

#### **`null`, `undefined`, `void`**

- `null` and `undefined` represent absence of value.
- `void` is used for functions that don’t return a value.

```typescript
let emptyValue: null = null;
let notAssigned: undefined = undefined;

function logMessage(): void {
  console.log("Hello!");
}
```

#### **`any`, `unknown`**

- `any` allows any type and essentially disables type checking.
- `unknown` is similar to `any`, but more restrictive, requiring type checking before usage.

```typescript
let anything: any = 42;
anything = "Now a string"; // No error

let uncertain: unknown = 42;
if (typeof uncertain === "string") {
  console.log(uncertain.toUpperCase()); // OK after checking the type
}
```

#### **`never`**

`never` is used for functions that never return a value, like functions that throw exceptions or enter infinite loops.

```typescript
function throwError(message: string): never {
  throw new Error(message);
}
```

<br>
 
### 2. **Type Annotations**

Type annotations specify the type of variables, function parameters, and return values explicitly.

```typescript
let x: number = 10; // Type annotation for a number

function greet(name: string): string {
  return `Hello, ${name}`;
}
```

<br>
 
### 3. **Interfaces**

An interface defines the structure of an object by specifying its properties and methods. However, interfaces are not limited to describing objects. They can also define function types, arrays, hybrid types, and even work with generics.

#### Defining Object Structures

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

#### **For other use cases visit [here](interfaces-usecases)**

<br>
 
### 4. **Classes**

Classes allow you to define blueprints for objects, including properties and methods.

```typescript
class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }

  speak(): void {
    console.log(`${this.name} makes a sound`);
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name);
  }

  speak(): void {
    console.log(`${this.name} barks`);
  }
}

let dog = new Dog("Buddy");
dog.speak(); // Buddy barks
```

#### Access Modifiers

- `public`: Can be accessed from anywhere (default).
- `private`: Can only be accessed within the class.
- `protected`: Can be accessed within the class and subclasses.

```typescript
class User {
  public name: string;
  private password: string;

  constructor(name: string, password: string) {
    this.name = name;
    this.password = password;
  }

  showName() {
    console.log(this.name);
  }
}
```

<br>
 
### 5. **Enums**

Enums define named constant values. TypeScript supports numeric and string enums.

#### Numeric Enum:

```typescript
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

console.log(Direction.Up); // 1
```

#### String Enum:

```typescript
enum Status {
  Pending = "PENDING",
  InProgress = "IN_PROGRESS",
  Completed = "COMPLETED",
}

console.log(Status.Pending); // "PENDING"
```

<br>
 
### 6. **Functions**

TypeScript allows specifying types for function parameters and return values. It also supports optional, default, and rest parameters.

#### Parameter Types and Return Types

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

#### Optional Parameters (`?`)

```typescript
function greet(name: string, age?: number): string {
  return age ? `${name} is ${age} years old` : `${name}`;
}

console.log(greet("Alice")); // Alice
console.log(greet("Bob", 30)); // Bob is 30 years old
```

#### Default Parameters

```typescript
function greet(name: string, age: number = 25): string {
  return `${name} is ${age} years old`;
}
```

#### Rest Parameters (`...args`)

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
```

<br>
 
### 7. **Arrays and Tuples**

#### Typed Arrays

Arrays can be strongly typed.

```typescript
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];
```

#### Tuples

Tuples are arrays with fixed sizes and types for each element.

```typescript
let tuple: [string, number] = ["Alice", 30];
```

**More about tuples, and difference between tuples and arrays [here](tuples)**

<br>
 
### 8. **Union and Intersection Types**

#### Union Types (`|`)

A variable can hold multiple types.

```typescript
function print(value: string | number): void {
  console.log(value);
}

print("Hello");
print(42);
```

#### Intersection Types (`&`)

Combining multiple types into one.

```typescript
interface Person {
  name: string;
  age: number;
}

interface Employee {
  employeeId: string;
  role: string;
}

type EmployeePerson = Person & Employee;

const emp: EmployeePerson = {
  name: "Alice",
  age: 30,
  employeeId: "E123",
  role: "Engineer",
};
```

<br>
 
### 9. **Type Aliases**

Type aliases allow creating custom types that can be reused across the codebase.

```typescript
type ID = string | number;

function getUser(id: ID): void {
  console.log(`Fetching user with ID: ${id}`);
}

getUser(1);
getUser("abc123");
```

**More about type aliases [here](type-aliases)**

<br>
 
### 10. **Generics**

Generics allow writing functions, classes, and interfaces that work with any data type, providing more flexibility and reusability.

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output = identity<string>("Hello");
console.log(output); // Hello

let numberOutput = identity<number>(100);
console.log(numberOutput); // 100
```

#### Generic Classes

```typescript
class Box<T> {
  value: T;
  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

const stringBox = new Box<string>("Hello");
console.log(stringBox.getValue()); // Hello
```

**More of generic types and examples [here](generics)**

<br>
 
### 11. **Modules**

Modules allow code to be split into separate files, which can be imported/exported.

```typescript
// file1.ts
export function greet(name: string): string {
  return `Hello, ${name}`;
}

// file2.ts
import { greet } from "./file1";

console.log(greet("Alice")); // Hello, Alice
```

**More about modules [here](modules)**

<br>
 
### 12. **Type Inference**

TypeScript automatically infers the type of a variable when the type is not explicitly declared.

```typescript
let inferredString = "Hello"; // inferred as string
let inferredNumber = 42; // inferred as number

// TypeScript can infer types from function return values as well
function multiply(x: number, y: number) {
  return x * y; // inferred return type is number
}

let result = multiply(3, 4);
```

**More about inferences [here](inferences)**

<br>
<br>

## <ins>Advanced Typescript Concepts</ins>

### 1. **Advanced Types**

#### **Mapped Types**

Mapped types allow you to create a new type based on an existing one by transforming its properties. You can modify the properties or their types.

Example: Create a `Readonly` type that marks all properties of an object as `readonly`:

```typescript
type Readonly<T> = { readonly [K in keyof T]: T[K] };

interface Person {
  name: string;
  age: number;
}

type ReadonlyPerson = Readonly<Person>;

const person: ReadonlyPerson = { name: "Alice", age: 30 };
// person.name = 'Bob'; // Error: cannot assign to 'name' because it is a read-only property.
```

Here, in `type Readonly<T> = { readonly [K in keyof T]: T[K] };`

- **`Readonly<T>`**: This is a **type alias** that accepts a generic type parameter `T`. This means that `T` can be any type (such as an object, interface, etc.).
- **`{ readonly [K in keyof T]: T[K] }`**: This is a **mapped type** that iterates over all the keys of type `T` and makes each of them `readonly`. Let’s break it down further:
  - **`keyof T`**: This expression gets all the keys (property names) of type `T` as a **union** of string literals. For example, if `T` is `{ name: string; age: number; }`, then `keyof T` would be `"name" | "age"`.
  - **`[K in keyof T]`**: This is the syntax for a **mapped type** that iterates over each key `K` in `keyof T`. Essentially, `K` will take each key of `T` one by one.
  - **`T[K]`**: This accesses the type of the property `K` in type `T`. For example, if `T` is `{ name: string; age: number; }`, then `T["name"]` would be `string` and `T["age"]` would be `number`.
- **`readonly [K in keyof T]: T[K]`**: The `readonly` modifier makes each property of type `T` **immutable**. This means that once a property is assigned a value, it cannot be changed. So, the final result is that for every property `K` in type `T`, the property is transformed into a `readonly` version.

**More about mapped types [here](mapped-types)**

#### **Conditional Types**

Conditional types use the `extends` keyword to define conditional logic based on the type of a variable.

Example: Check if a type `T` is `string`:

```typescript
type IsString<T> = T extends string ? true : false;

type Test1 = IsString<string>; // true
type Test2 = IsString<number>; // false
```

**More about conditional types [here](conditional-types)**

#### **Utility Types**

TypeScript provides several built-in utility types that help manipulate types.

- **`Partial<T>`**: Makes all properties of `T` optional.
- **`Required<T>`**: Makes all properties of `T` required.
- **`Readonly<T>`**: Makes all properties of `T` read-only.
- **`Pick<T, K>`**: Picks a subset of properties `K` from type `T`.
- **`Omit<T, K>`**: Omits properties `K` from type `T`.

```typescript
interface Person {
  name: string;
  age: number;
  address?: string;
}

type PartialPerson = Partial<Person>; // All properties are optional
type RequiredPerson = Required<Person>; // All properties are required
type NameOnly = Pick<Person, "name">; // Only `name` is picked
type WithoutAddress = Omit<Person, "address">; // `address` is omitted
```

<br>
 
### 2. **Type Guards**

Type guards help narrow the type within a conditional block using `x is Type` syntax or built-in checks.

#### Custom Type Guard

You can create your own type guards to narrow types based on logic.

```typescript
function isString(value: any): value is string {
  return typeof value === "string";
}

const input: any = "Hello, world!";
if (isString(input)) {
  // TypeScript now knows that `input` is a string here.
  console.log(input.toUpperCase()); // OK
}
```

#### `instanceof` and `typeof`

`instanceof` and `typeof` are used for runtime type checks.

```typescript
class Dog {
  bark() {
    console.log("Woof!");
  }
}

const pet = new Dog();

if (pet instanceof Dog) {
  pet.bark(); // OK, `pet` is now recognized as a `Dog`
}

const value = 42;
if (typeof value === "number") {
  console.log(value.toFixed(2)); // OK
}
```

<br>

### 3. **Discriminated Unions**

Discriminated unions allow for union types that include a tag (discriminant) to help narrow down types.

Example: Different actions for different shapes using a `type` property:

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; sideLength: number };

function area(shape: Shape): number {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;
  } else {
    return shape.sideLength ** 2;
  }
}
```

**More about Discriminated Unions [here](discriminated-unions)**

<br>

### 4. **Keyof and Lookup Types**

`keyof` and **lookup types** allow you to dynamically access the keys and values of a type.

#### `keyof` Operator

The `keyof` operator creates a union of string literal types representing the keys of an object type.
Get the keys of an object type as a union of string literals.

- Definition:

  ```typescript
  keyof T
  ```

  - `T`: An object type.
  - **Result**: A union of string literal types representing all keys of `T`

- Example:

  ```typescript
  interface Person {
    name: string;
    age: number;
  }

  type Key = keyof Person; // "name" | "age"
  ```

#### Lookup Types

**Lookup types** also called as **Indexed Access Types** let you access the type of a specific property dynamically using bracket notation (`T[K]`).Access the value of a specific property dynamically.

- Definition:
  ```typescript
  T[K];
  ```
  - `T`: An object type.
  - `K`: A key in `T` (must be assignable to `keyof T`).
  - **Result**: The type of the property `K` in `T`.
- Example:
  ```typescript
  interface Person {
    name: string;
    age: number;
  }
  type Value = Person["name"]; // string
  ```

<br>

### 5. **Template Literal Types**

Template literal types allow you to construct types by combining string literals, creating dynamic string types.

```typescript
type Greeting = `Hello, ${string}!`;

const greeting: Greeting = "Hello, Alice!"; // Valid
// const invalidGreeting: Greeting = "Hi, Alice!";  // Error: doesn't match `Hello, ${string}!`
```

<br>
 
### 6. **Decorators**

Decorators are an experimental feature that allows you to modify the behavior of classes, methods, or properties. Decorators are defined using the `@` symbol followed by a function.

- Decorator Syntax:
  ```typescript
  @decorator
  class MyClass {}
  ```
- Example: A simple class decorator that logs class creation.

      ```typescript
      function logClass(target: Function) {
      console.log(`${target.name} class is being created!`);
      }

      @logClass
      class MyClass {}

      const instance = new MyClass(); // Logs: MyClass class is being created!
      ```

  **More about decorators [here](decorators)**
  <br>

### 7. **Declaration Merging**

Declaration merging occurs when multiple declarations of the same type or interface are combined into one.

- Example:

  ```typescript
  interface Person {
    name: string;
  }

  interface Person {
    age: number;
  }

  const person: Person = {
    name: "Alice",
    age: 30,
  }; // Declaration of `Person` is merged
  ```

**More about Declaration Merging [here](declaration-merging)**

<br>

### 8. **Namespace**

Namespaces are used to organize code into logical groups (legacy feature but still used in some scenarios).

```typescript
namespace Shapes {
  export interface Circle {
    radius: number;
  }

  export interface Square {
    sideLength: number;
  }
}

const circle: Shapes.Circle = { radius: 5 };
const square: Shapes.Square = { sideLength: 10 };
```

**More about Namespace [here](namespace)**

<br>

### 9. **Type Manipulation**

Advanced type manipulation allows you to infer types using `infer` and perform conditional type transformations. The `infer` keyword allows you to **extract** a type from a more complex type within conditional types

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type MyFunction = (x: number, y: number) => string;

type Result = ReturnType<MyFunction>; // string
```

Here, `ReturnType<T>` is a conditional type that:

- Checks if `T` is a function (denoted by (`...args: any[]) =>`).
- If `T` is a function, it **infers** the return type of that function and assigns it to `R`.
- If `T` is not a function, it returns `never` (meaning an invalid type).

**More about Type Manipulation [here](type-manipulation)**

<br>

### 10. **Module Augmentation**

Module augmentation allows you to extend or modify existing modules, adding new functionality.

Example: Augmenting a module to add new properties to an existing interface.

```typescript
// Augmenting a global module or third-party library
// express.d.ts (this can be a separate declaration file or inside your main code)
declare module "express" {
  interface Request {
    user?: string;
  }
}
```

Now you can edit/access `user` property on `Request`:

```typescript
import express from "express";

const app = express();

// Middleware to add a user to the request
app.use((req, res, next) => {
  req.user = "Alice"; // Adding a `user` property to the Request object
  next();
});

// Route handler that accesses the augmented `user` property
app.get("/", (req, res) => {
  if (req.user) {
    res.send(`Hello, ${req.user}!`); // TypeScript recognizes `req.user` due to augmentation
  } else {
    res.send("Hello, guest!");
  }
});
```
**More about module augmentation [here](module-augmentation)**

### 11. **Strict Type Checking**

Enable strict type checking options to enforce safer coding practices.

In `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "strictNullChecks": true,
    "noImplicitAny": true
  }
}
```

`strictNullChecks` ensures that `null` and `undefined` are not assignable to other types by default. `noImplicitAny` disallows variables from being implicitly typed as `any`.

<br>

### 12. **Advanced Generics**

#### Generic Constraints (`T extends U`)

Restrict the types that can be used with generics.

```typescript
function echo<T extends string>(value: T): T {
  return value;
}

echo("Hello"); // OK
// echo(123);  // Error: Argument of type 'number' is not assignable to parameter of type 'string'.
```

#### Default Generic Parameters

You can set default types for generics.

```typescript
function identity<T = string>(value: T): T {
  return value;
}

identity("Hello"); // string
identity(42); // number
```

#### Recursive Generics

Generics can be recursive, allowing more complex types.

The type `List<T>` is defined in such a way that it can refer to itself. That is, it can be an array of `List<T>`, or a single value of type `T`. This allows the type to represent a list that can contain other lists, and so on, creating a **recursive structure**.

```typescript
type List<T> = T | List<T>[];

// Example with numbers
let listOfNumbers: List<number> = 42; // Single number (T)
let nestedListOfNumbers: List<number> = [42, [42, 100], 57]; // Array of numbers and nested arrays
```

<br>

### 13. **Dynamic Import Types**

Using `import()` syntax to dynamically load modules at runtime.

```typescript
// This defines the type of the module (its exports).
type Module = typeof import("./module");

// The async function dynamically loads the module at runtime.
async function loadModule() {
  const module = await import("./module");

  // The 'module' is dynamically loaded and now you can access its exports.
  module.someFunction();

  // You can also use the `Module` type to type-check the `module` variable.
  let myModule: Module = module; // Ensure the module matches the defined type
  myModule.someFunction(); // Now TypeScript will type-check it
}
```

### 14. **Compiler Configuration**

`tsconfig.json` is the configuration file for TypeScript. It lets you set compiler options, such as module resolution, strict settings, and more.

Example `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist"
  }
}
```

<br>

### 15. **Advanced Decorator Usage**

For frameworks like Angular, decorators play an essential role in metadata reflection. This enables functionality such as dependency injection.

Example: An Angular-style decorator for a class:

```typescript
function Injectable(target: Function) {
  console.log(`Injectable: ${target.name}`);
}

@Injectable
class MyService {} // Injectable: MyService
```

**More about Advanced Decorator [here](advanced-decorator)**
<br>

### **Key Use Cases for Advanced Topics**

Advanced TypeScript concepts often come into play when building:

- Frameworks or libraries.
- Complex type-safe APIs.
- Enterprise-level projects requiring strict type safety.
- Integration with JavaScript libraries using type declarations.

<br>
<br>

## <ins>Interview Questions</ins>

Here are some commonly asked questions in TypeScript interviews:

1. What is TypeScript, and how does it differ from JavaScript?
2. What are the key benefits of using TypeScript over JavaScript?
3. Explain the concept of types in TypeScript.
4. What are the primitive types in TypeScript?
5. What is type inference in TypeScript?
6. Can you explain the `any` type in TypeScript? When should it be used?
7. What is the difference between `interface` and `type` in TypeScript?
8. What are generics in TypeScript? Can you provide an example?
9. What is the `unknown` type in TypeScript, and how does it differ from `any`?
10. How do you define optional properties in TypeScript interfaces or types?
11. What are tuples in TypeScript? Provide an example.
12. How does TypeScript handle null and undefined values?
13. What is a union type in TypeScript? Provide an example.
14. What is an intersection type in TypeScript? Provide an example.
15. Explain the concept of "type guards" in TypeScript.
16. What are enums in TypeScript? How are they different from strings or numbers?
17. How can you declare and use classes in TypeScript?
18. What is the `never` type in TypeScript? Provide a use case for it.
19. How do you extend interfaces or types in TypeScript?
20. What are decorators in TypeScript? How are they used?
21. What is the difference between `public`, `private`, and `protected` access modifiers in TypeScript?
22. How do you handle modules in TypeScript?
23. How can you use TypeScript with third-party JavaScript libraries that don't have type definitions?
24. What are ambient declarations in TypeScript?
25. Explain the difference between `const`, `let`, and `var` in TypeScript.
26. What is the purpose of the `as` keyword in TypeScript?
27. What is the difference between type assertions and type casting in TypeScript?
28. What are some of the TypeScript configuration options (tsconfig.json)?
29. How do you configure TypeScript for a React project?
30. How do you work with promises and async/await in TypeScript?
31. What is the `Readonly` utility type in TypeScript?
32. How do you handle errors in TypeScript?
33. What are some common pitfalls to avoid when using TypeScript?
34. How does TypeScript support asynchronous programming?
35. What is the purpose of `strict` mode in TypeScript, and what are the advantages of enabling it?

<br>

Here’s a mix of easy, medium, and advanced TypeScript interview questions:

### Easy Level:
1. What is TypeScript and why is it used?
2. How do you install TypeScript?
3. What is the difference between `let` and `const` in TypeScript?
4. What are type aliases in TypeScript, and how do you use them?
5. Can you explain the purpose of the `void` type in TypeScript?
6. What are the basic types in TypeScript (number, string, boolean, etc.)?
7. What is the syntax for defining a function in TypeScript?
8. How do you declare an array in TypeScript?
9. How do you define a parameter type in a function in TypeScript?
10. What are default values for function parameters in TypeScript?

### Medium Level:
11. What are the advantages of using `interface` over `type` in TypeScript?
12. What is the purpose of `strictNullChecks` in TypeScript?
13. Can you explain how TypeScript helps in avoiding null pointer exceptions?
14. What is the difference between `undefined` and `null` in TypeScript?
15. What is the `keyof` type operator in TypeScript? Provide an example.
16. Explain the difference between an object type and a class type in TypeScript.
17. How do you use `readonly` properties in TypeScript?
18. What is type widening in TypeScript? Can you give an example?
19. How does TypeScript handle function overloading? Provide an example.
20. Can you explain type inference and how it works in TypeScript?

### Advanced Level:
21. What is the purpose of generics in TypeScript? How do you implement them in functions or classes?
22. What is the `this` keyword in TypeScript, and how is its behavior different from JavaScript?
23. How do you use mapped types in TypeScript?
24. What are conditional types in TypeScript? Provide an example.
25. What is type narrowing, and how does TypeScript perform it?
26. How do you create and use custom decorators in TypeScript?
27. What is the `never` type in TypeScript? When should you use it?
28. Can you explain how TypeScript works with modules and namespaces?
29. How does TypeScript handle asynchronous programming (async/await) in terms of type safety?
30. What is the `unknown` type, and how is it different from `any` in TypeScript?
31. How can you create a union of types that only accepts a subset of values in TypeScript?
32. What are "advanced" types in TypeScript and how do they differ from primitive types?
33. How do you use `declaration merging` in TypeScript? Provide an example.
34. What is the purpose of `tsconfig.json`? What are some of the most commonly used options?
35. How can TypeScript help when working with large codebases?
36. What is the `in` operator in TypeScript, and how does it work in conjunction with type guards?
37. How do you declare and use abstract classes in TypeScript?
38. What is a `construct signature` in TypeScript, and when would you use it?
39. What are `template literal types` in TypeScript, and how do they work?
40. How do you deal with third-party libraries in TypeScript when they don’t have type definitions?
