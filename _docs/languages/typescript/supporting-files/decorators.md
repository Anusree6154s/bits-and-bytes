---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Decorators in Typescript
permalink: decorators
tags: [typescript, decorators]
parent_post: typescript-learners-guide
hidden: true
---

### **Decorators in TypeScript**

Decorators are a powerful feature in TypeScript that allows you to **annotate and modify classes, methods, properties, and parameters** at runtime. They provide a clean way to apply reusable behaviors or metadata to your code. Decorators are particularly useful in frameworks like Angular, where they are extensively used for dependency injection and metadata annotation.

<br>

### **1. What Are Decorators?**

A **decorator** is a special kind of declaration attached to a class, method, accessor, property, or parameter. Decorators are defined using the **`@`** symbol followed by a function.

#### Decorator Syntax

```typescript
@decorator
class MyClass {}
```

<br>

### **2. Enabling Decorators**

Decorators are an experimental feature in TypeScript and must be explicitly enabled in the `tsconfig.json`:

```json
{
  "experimentalDecorators": true
}
```

<br>

### **3. Types of Decorators**

TypeScript provides several types of decorators:

| Decorator Type          | Targeted Element                   |
| ----------------------- | ---------------------------------- |
| **Class Decorator**     | Classes                            |
| **Method Decorator**    | Methods                            |
| **Accessor Decorator**  | Getters and setters                |
| **Property Decorator**  | Properties                         |
| **Parameter Decorator** | Function or constructor parameters |

<br>

### **4. Class Decorators**

A class decorator applies to a class declaration. It can modify or replace the class definition.

#### Example 1: Logging Class Creation

```typescript
function logClass(target: Function) {
  console.log(`${target.name} class is being created!`);
}

@logClass
class MyClass {}

const instance = new MyClass(); // Logs: MyClass class is being created!
```

#### Example 2: Adding Static Properties

```typescript
function addTimestamp(target: Function) {
  target.prototype.timestamp = Date.now();
}

@addTimestamp
class MyClass {}

const instance = new MyClass();
console.log((instance as any).timestamp); // Logs the timestamp
```

<br>

### **5. Method Decorators**

A method decorator is applied to a method of a class. It can modify the method or add functionality.

#### Example: Logging Method Calls

```typescript
function logMethod(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with arguments:`, args);
    return originalMethod.apply(this, args);
  };
}

class MyClass {
  @logMethod
  sayHello(name: string) {
    console.log(`Hello, ${name}!`);
  }
}

const instance = new MyClass();
instance.sayHello("Alice");
// Logs:
// Calling sayHello with arguments: [ 'Alice' ]
// Hello, Alice!
```

<br>

### **6. Property Decorators**

A property decorator applies to class properties. It allows you to attach metadata or modify how the property is used.

#### Example: Marking Required Properties

```typescript
function required(target: any, propertyKey: string) {
  console.log(`Property "${propertyKey}" is required.`);
}

class MyClass {
  @required
  name!: string;
}
// Logs: Property "name" is required.
```

<br>

### **7. Accessor Decorators**

Accessor decorators are used on getters and setters of properties.

#### Example: Validating Property Access

```typescript
function logAccess(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  const originalGet = descriptor.get;
  descriptor.get = function () {
    console.log(`Accessing property "${propertyKey}"`);
    return originalGet?.apply(this);
  };
}

class MyClass {
  private _value = 42;

  @logAccess
  get value() {
    return this._value;
  }
}

const instance = new MyClass();
console.log(instance.value);
// Logs:
// Accessing property "value"
// 42
```

<br>

### **8. Parameter Decorators**

A parameter decorator applies to the parameters of a method or constructor. It’s often used for dependency injection or metadata collection.

#### Example: Logging Parameter Metadata

```typescript
function logParameter(
  target: any,
  propertyKey: string,
  parameterIndex: number
) {
  console.log(
    `Parameter at index ${parameterIndex} in method "${propertyKey}" is being logged.`
  );
}

class MyClass {
  greet(@logParameter name: string) {
    console.log(`Hello, ${name}`);
  }
}

const instance = new MyClass();
instance.greet("Alice");
// Logs:
// Parameter at index 0 in method "greet" is being logged.
// Hello, Alice
```

<br>

### **9. Composing Multiple Decorators**

You can stack multiple decorators on a single element. Decorators are applied in **reverse order** (bottom to top).

```typescript
function first(target: any, propertyKey: string) {
  console.log("First decorator");
}

function second(target: any, propertyKey: string) {
  console.log("Second decorator");
}

class MyClass {
  @first
  @second
  method() {}
}
// Logs:
// Second decorator
// First decorator
```

<br>

### **10. Practical Use Cases for Decorators**

- **Dependency Injection**: Used in frameworks like Angular for injecting dependencies into classes.
- **Logging**: Automatically log class instantiation, method calls, or property accesses.
- **Validation**: Mark required properties or validate method arguments.
- **Metadata**: Attach additional metadata to classes or members, useful for libraries like `reflect-metadata`.

<br>
---

### **Summary of All Topics**

| Feature                    | Description                                                                                           | Example                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Class Decorator**         | Modifies or replaces class definitions.                                                              | `@logClass`                                                            |
| **Method Decorator**        | Enhances or overrides method behavior.                                                               | `@logMethod`                                                           |
| **Property Decorator**      | Adds metadata or modifies properties.                                                                | `@required`                                                            |
| **Accessor Decorator**      | Applies to getters or setters to log or modify access behavior.                                      | `@logAccess`                                                           |
| **Parameter Decorator**     | Logs or injects data into parameters.                                                                | `@logParameter`                                                        |
| **Indexed Access Types**    | Retrieves the type of a property dynamically.                                                        | `type Name = Person["name"];`                                          |
| **Template Literal Types**  | Constructs string types dynamically.                                                                 | `type API = \${"GET" | "POST"} /${"users"}\`                         |
| **Utility Types**           | Built-in types for manipulating types (`Partial`, `Readonly`, `Pick`, `Omit`).                       | `type PartialPerson = Partial<Person>;`                                |
| **Conditional Types**       | Constructs types conditionally based on logic (`extends ? :`).                                       | `type IsString<T> = T extends string ? true : false;`                  |
| **Mapped Types**            | Creates new types by transforming existing ones (`readonly`, `optional`).                           | `type Readonly<T> = { readonly [K in keyof T]: T[K] };`                |
| **Keyof and Lookup Types**  | Dynamically access object keys and properties.                                                       | `type Key = keyof Person;`                                             |
| **Generics**                | Enables reusable, flexible code for any type.                                                       | `function identity<T>(arg: T): T;`                                     |
| **Modules**                 | Allows splitting code into separate files for better organization (`import/export`).                 | `import { greet } from "./file";`                                      |

---



























