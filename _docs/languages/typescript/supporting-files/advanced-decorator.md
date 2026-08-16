---
parent: Typescript learners guide
layout: default
date: 19 jan 2025
title: More about Advanced Decorator
permalink: advanced-decorator
tags: [typescript, advanced decorator]
parent_post: typescript-learners-guide
hidden: true
---

### **Advanced Decorator Usage**

Decorators in TypeScript are a powerful feature, primarily used for metadata reflection in frameworks like Angular. They allow you to modify or annotate classes, methods, properties, and parameters. In Angular, decorators are extensively used for features like dependency injection, routing, and more.

<br>
 
#### Key Concepts:

1. **What is a Decorator?**

   - A decorator is a special kind of function that can be attached to a class, method, property, or parameter to modify or add metadata to it.
   - Decorators are commonly used in frameworks like Angular and NestJS to add extra functionality to components, services, and other entities.

2. **Types of Decorators**:

   - **Class Decorators**: Used to modify or annotate classes.
   - **Method Decorators**: Used to modify methods.
   - **Property Decorators**: Used to modify properties.
   - **Parameter Decorators**: Used to modify method parameters.

3. **Class Decorators**:

   - Class decorators are functions that take the class constructor as an argument and can modify its behavior or add metadata.

   **Example: A simple class decorator**:

   ```typescript
   function Injectable(target: Function) {
     console.log(`Injectable: ${target.name}`);
   }

   @Injectable
   class MyService {}
   ```

   - **How it works**:
     - The `Injectable` decorator takes the class constructor (`target`) and logs a message with the class name.
     - The `@Injectable` decorator is applied to the `MyService` class, making it injectable (this concept is widely used in Angular for dependency injection).

4. **Decorator Syntax**:

   - **Decorator Declaration**: A decorator is defined as a function that typically takes arguments like the target class, method, or property.
   - **Decorator Application**: You apply a decorator by prefixing it with the `@` symbol before a class, method, property, or parameter.

5. **Advanced Use Cases for Decorators**:

   - **Metadata Reflection**:

     - Decorators are often used in frameworks like Angular for dependency injection, routing, and more by attaching metadata to classes and methods.
     - For instance, Angular uses the `@Injectable` decorator to mark services that can be injected into other components or services.

   - **Method Decorators**:

     - You can create decorators to modify or enhance the behavior of methods, such as logging, authentication, etc.

     **Example**:

     ```typescript
     function Log(
       target: any,
       propertyKey: string,
       descriptor: PropertyDescriptor
     ) {
       const originalMethod = descriptor.value;
       descriptor.value = function (...args: any[]) {
         console.log(
           `Calling ${propertyKey} with arguments: ${JSON.stringify(args)}`
         );
         return originalMethod.apply(this, args);
       };
     }

     class Calculator {
       @Log
       add(a: number, b: number) {
         return a + b;
       }
     }

     const calc = new Calculator();
     calc.add(2, 3); // Logs: Calling add with arguments: [2,3]
     ```

     - **How it works**: The `@Log` decorator wraps the `add` method to log the arguments every time it's called.

6. **Dependency Injection in Angular (Example)**:

   - Decorators like `@Injectable`, `@Component`, and `@Directive` in Angular are used to add metadata for dependency injection and component configuration.

   **Example: Angular-style `@Injectable` decorator**:

   ```typescript
   function Injectable(target: Function) {
     console.log(`${target.name} is injectable!`);
   }

   @Injectable
   class MyService {
     // Service logic
   }
   ```

   - **How it works**: The `@Injectable` decorator marks `MyService` as a service that can be injected into other parts of the application, helping Angular’s dependency injection system manage instances of `MyService`.

7. **Parameter Decorators**:

   - These decorators are used to modify the behavior or add metadata to method parameters.

   **Example**:

   ```typescript
   function Param(target: any, propertyKey: string, parameterIndex: number) {
     console.log(
       `Parameter at index ${parameterIndex} in method ${propertyKey} was decorated`
     );
   }

   class MyClass {
     greet(@Param name: string) {
       console.log(`Hello, ${name}!`);
     }
   }
   ```

8. **Use Cases for Decorators in Frameworks**:
   - **Angular**: Dependency injection, lifecycle hooks, component metadata, routing.
   - **NestJS**: Controllers, services, and route handlers.
   - **Logging**: Method decorators for logging inputs and outputs.
   - **Access Control**: Decorators for controlling access to methods based on user roles (e.g., `@Role('admin')`).

<br>
 
#### Summary:
- **Decorators** in TypeScript are used to modify or annotate classes, methods, properties, and parameters with additional functionality or metadata.
- They are widely used in frameworks like **Angular** for dependency injection and **NestJS** for routing and middleware handling.
- **Advanced usage** includes using decorators for **metadata reflection**, **logging**, **dependency injection**, and more.
- **Examples** of common decorators include `@Injectable`, `@Component`, `@Log`, and custom decorators to modify method behavior.
