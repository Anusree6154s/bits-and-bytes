---
layout: default
title: Basics of Dart
date: Jul 13, 2025
excerpt: Some basic concepts of dart for flutter
permalink: basics-of-dart
tags: [flutter, dart, mobile, android, ios]
parent: Flutter
---

Since I began learning flutter, dart was a new language for me. I came to know that dart is the most similar to java language which also I was just partially informed in.

<div align=center><img src="{{'/assets/imgs/basics-of-dart.png'| relative_url}}"  width=100/><p style="font-size:12px">And there I was stuck</p></div>

So here goes a small basics chart I made gpt give me that seems to be quite helpful in catching the basic flow of the code it generates futher for my dart project:

<br>

<div style="border:1px solid #ccc; padding:10px; border-radius:5px" markdown="1">

## ✅ Essential Dart Concepts for Flutter Beginners

### 1. **Variables & Data Types**

```dart
int age = 25;
double price = 9.99;
String name = 'Anu';
bool isLoggedIn = true;
var anything = 'Can be any type';
```

- `var` = type inferred automatically
- `final` / `const` = cannot be changed after initialization

  ```dart
  final name = 'Anu';  // run-time constant
  const pi = 3.14;     // compile-time constant
  ```

### 2. **Functions**

```dart
String greet(String name) {
  return 'Hello, $name!';
}

void printMessage() {
  print('Hi there!');
}
```

- You can also write short functions like:

  ```dart
  int square(int x) => x * x;
  ```

### 3. **Classes & Objects**

```dart
class Person {
  String name;
  int age;

  Person(this.name, this.age);

  void introduce() {
    print('I am $name and I am $age years old.');
  }
}
```

- Create an object:

  ```dart
  var p = Person('Anu', 21);
  p.introduce();
  ```

### 4. **Constructors**

- Default, named, and optional constructors:

  ```dart
  class Product {
    String name;
    double price;

    Product({required this.name, required this.price});
  }

  var p = Product(name: 'Shoes', price: 99.99);
  ```

### 5. **Collections: Lists, Maps, Sets**

#### Lists (Arrays)

```dart
List<String> fruits = ['apple', 'banana'];
fruits.add('mango');
```

#### Maps (Key-Value pairs)

```dart
Map<String, int> scores = {'math': 90, 'english': 85};
print(scores['math']);
```

#### Sets (Unique items)

```dart
Set<String> cities = {'Paris', 'London', 'Paris'};
print(cities.length);  // 2
```

### 6. **Control Flow**

- If/Else, For, While, Switch

```dart
if (age > 18) {
  print('Adult');
} else {
  print('Minor');
}

for (var i = 0; i < 3; i++) {
  print(i);
}
```

### 7. **Null Safety**

- Dart doesn’t allow null unless you tell it:

```dart
String? name;  // nullable
name = null;   // OK

String name2 = 'Anu';
// name2 = null; // ❌ Error
```

### 8. **Async / Await & Futures**

Used when dealing with APIs, delays, etc.

```dart
Future<String> fetchData() async {
  await Future.delayed(Duration(seconds: 2));
  return 'Data loaded';
}

void main() async {
  print('Start');
  String data = await fetchData();
  print(data);
}
```

### 9. **Getters & Setters**

```dart
class Rectangle {
  double width, height;

  Rectangle(this.width, this.height);

  double get area => width * height;

  set resize(double factor) {
    width *= factor;
    height *= factor;
  }
}
```

### 10. **Basic Error Handling**

```dart
try {
  int result = 10 ~/ 0;
} catch (e) {
  print('Caught error: $e');
}
```

## 🧠 Bonus: Flutter-Specific Must-Knows

| Concept           | Why it matters                        |
| ----------------- | ------------------------------------- |
| `main()`          | Entry point of every Dart/Flutter app |
| `Widget`          | Everything is a widget (UI blocks)    |
| `StatelessWidget` | For static UIs                        |
| `StatefulWidget`  | For interactive UIs                   |
| `setState()`      | Rebuilds part of the UI               |
| `async/await`     | Needed for API, DB, etc. in Flutter   |

## ✅ Summary: Start With These 10

| ✅ Must-Learn Concepts |
| ---------------------- |
| ✅ Variables & Types   |
| ✅ Functions           |
| ✅ Classes & Objects   |
| ✅ Collections         |
| ✅ Null Safety         |
| ✅ Control Flow        |
| ✅ Async/Await         |
| ✅ Constructors        |
| ✅ Getters/Setters     |
| ✅ Error Handling      |

</div>
