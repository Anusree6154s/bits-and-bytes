---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Declaration Merging
permalink: declaration-merging
tags: [typescript, declaration merging]
parent_post: typescript-learners-guide
hidden: true
---

### **Declaration Merging in TypeScript**

Declaration merging is a feature in TypeScript where **two or more declarations with the same name** are automatically combined into a **single definition**. This feature is particularly useful for extending existing types, interfaces, namespaces, and modules. It ensures that TypeScript provides flexible and extensible code constructs.

<br>

### **1. How Declaration Merging Works**

When TypeScript encounters multiple declarations of the same name, it merges their members into a single composite type. The way merging happens depends on the type of the declaration:

1. **Interfaces**: Members are combined.
2. **Namespaces**: Members are combined.
3. **Enums**: Members are combined.
4. **Functions and Classes**: Overloads are created.

<br>

### **2. Interface Merging**

Interfaces with the same name are automatically merged, with their members combined into a single definition.

#### **Example: Merging Interfaces**
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
}; // Both `name` and `age` are available due to merging
```

#### **Rules for Interface Merging**
- If two members have the same name and type, they are compatible.
- If two members have the same name but different types, a compilation error occurs.

#### **Example: Conflicting Members**
```typescript
interface Animal {
  name: string;
}

interface Animal {
  name: number; // Error: Subsequent property declarations must have the same type
}
```

<br>

### **3. Namespace Merging**

Namespaces with the same name are merged, and their members are combined into a single namespace.

#### **Example: Merging Namespaces**
```typescript
namespace MyNamespace {
  export const greeting = "Hello";
}

namespace MyNamespace {
  export function sayHello() {
    console.log(greeting);
  }
}

MyNamespace.sayHello(); // Logs: Hello
```

#### **Use Case: Extending External Libraries**
Declaration merging can extend third-party libraries by adding additional functionality.

```typescript
namespace Express {
  export interface Request {
    user?: string;
  }
}
```

<br>

### **4. Enum Merging**

Enums with the same name are merged, combining their members into a single enum.

#### **Example: Merging Enums**
```typescript
enum Colors {
  Red,
}

enum Colors {
  Blue = 2,
}

console.log(Colors.Red);  // 0
console.log(Colors.Blue); // 2
```

<br>

### **5. Function and Class Merging**

For functions or classes, declaration merging results in **overload declarations**.

#### **Example: Function Merging**
```typescript
function add(x: number): number;
function add(x: string): string;

function add(x: any): any {
  return x;
}

console.log(add(10));     // 10
console.log(add("hello")); // hello
```

#### **Example: Class Merging with Namespace**
```typescript
class Car {
  constructor(public make: string) {}
}

namespace Car {
  export const numberOfWheels = 4;
}

const myCar = new Car("Toyota");
console.log(Car.numberOfWheels); // 4
```

<br>

### **6. Practical Applications of Declaration Merging**

1. **Extending Third-Party Libraries**
   - Adding additional members to interfaces from external libraries.

   ```typescript
   interface Window {
     customProperty: string;
   }

   window.customProperty = "Hello, world!";
   ```

2. **Combining Related Code**
   - Grouping related declarations (interfaces, namespaces, etc.) without modifying original declarations.

3. **Creating Overloads**
   - Defining multiple versions of functions or methods using merging.

<br>

### **Key Topics Recap**

| **Topic**                     | **Description**                                                                                     | **Example**                                                                                      |
|-------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Declaration Merging**       | Combining multiple declarations of the same name into one.                                          | Merging interfaces, namespaces, enums, or creating function overloads.                         |
| **Interfaces**                | Members are combined into one.                                                                     | `interface A { x: number; }` and `interface A { y: string; }` => `{ x: number; y: string }`     |
| **Namespaces**                | Members are merged into the same namespace.                                                        | Adding methods to an existing namespace.                                                       |
| **Enums**                     | Enum members are merged into one enum.                                                             | `enum Colors { Red }` and `enum Colors { Blue }` => `Colors.Red` and `Colors.Blue`.             |
| **Functions and Classes**     | Overloads are created during merging.                                                              | Adding a namespace to a class or defining multiple function signatures.                        |

