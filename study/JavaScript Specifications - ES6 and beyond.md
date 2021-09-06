---
title: JavaScript 语法规格整理 - ES6 及以后版本
tags:
  - JavaScript
categories:
  - study
---

我们通常说的 JavaScript 其实指的是 ECMAScript 的子集。JavaScript 遵从 ECMAScript 定义的语言标准提供接口，但是内部实现则完全取决于运行环境。根据 ECMAScript 规格实现的语言还有 ActionScript、JScript 等等。这些实现了同一个规范的语言可以类比做使用了同一种引擎的不同汽车，每辆车的外观都不尽相同，而每种语言都有其独特的风格。

ECMAScript 是 Netscape 的 Brendan Eich 所开发的一个脚本语言的标准化规格，这个脚本语言最初叫 Mocha，随后改名为 LiveScript，最后改名为我们熟知的 JavaScript。可以说 ECMAScript 就是当时的 “JavaScript”，但是因为种种原因这个名称没能保留下来，我们现在经常使用的 JavaScript 主要是各浏览器实现的版本。

ECMAScript 的作用在于定义 JavaScript 语言的核心标准和 API，经过多个版本的迭代之后，ECMAScript 如今稳定每一年会发布一个新版本，给 JavaScript 添加一些新的语言特性以及改善。这篇文章将主要讨论 ECMAScript 第 6 个版本（即 ES6）及往后版本中推出的新特性和推出这些特性的缘由。

> 内容包括**更新时间截止**的所有已添加的特性。

<!-- more -->

## ECMAScript

ECMAScript 也叫 ECMA-262，是 JavaScript 的语言规范。下面是截止本文更新时间 ECMAScript 的版本列表。整体上来说，ECMAScript 在 ES3 为止都是对初版的修补，但到了第 4 版（ES4）时，由于提案的很多特性的引入会导致与先前版本的不兼容，被 Netscape、Mozilla 和微软等方面指责为“breaking the web”。随后雅虎、微软和谷歌牵头构成了工作小组在 ES3 的基础上做了一些安全方面、库的更新方面的工作，并且着重强调了兼容性。这两个小组并行工作了一段时间后做出了妥协，ES4 的版本被废止，后来的这个版本作为 ES5 发布。ES4 中的部分特性在 ES6 以后得到引入。并且从 ES6 开始，ECMAScript 每一年会发布一个新版本，添加一些新特性和做出一些改善。

| Edition | Date Published       | Name                     | Changes                                                                                                                                                         |
| ------- | -------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1       | 1997 年 6 月         |                          | 初版                                                                                                                                                            |
| 2       | 1998 年 6 月         |                          | 修改以符合 ISO/IEC 16262 国际标准                                                                                                                               |
| 3       | 1999 年 12 月        |                          | 加入正则表达式、更好的字符串处理、新的流程控制语句、Try Catch 异常处理、更细致的 Errors 定义、数值输出以及其他改善。                                            |
| 4       | （废弃）2003 年 6 月 |                          | 由于语言复杂度上的策略分歧而被分歧，其中的部分提案被完全抛弃，另一部分在第 6 版中发布。                                                                         |
| 5       | 2009 年 12 月        | ECMAScript 2015 (ES2015) | 加入严格（`strict`）模式；解决了第 3 版中的很多模糊定义，并且包容与规格有所不同的实际语言实现；添加了 setter 和 getter、JSON 支持以及更加完整的对象属性的反射。 |
| 5.1     | 2011 年 6 月         |                          | 修改以符合 ISO/IEC 16262:2011 国际标准                                                                                                                          |
| 6       | 2015 年 6 月         | ECMAScript 2016 (ES2016) | \*见下文                                                                                                                                                        |
| 7       | 2016 年 6 月         | ECMAScript 2016 (ES2016) | \*见下文                                                                                                                                                        |
| 8       | 2017 年 6 月         | ECMAScript 2017 (ES2017) | \*见下文                                                                                                                                                        |
| 9       | 2018 年 6 月         | ECMAScript 2018 (ES2018) | \*见下文                                                                                                                                                        |
| 10      | 2019 年 6 月         | ECMAScript 2019 (ES2019) | \*见下文                                                                                                                                                        |
| 11      | 2020 年 6 月         | ECMAScript 2020 (ES2020) | \*见下文                                                                                                                                                        |
| 12      | 2021 年 6 月         | ECMAScript 2021 (ES2021) | \*见下文                                                                                                                                                        |

### 脚本引擎的支持情况

ECMA 国际标准化组织为 ECMAScript 语言规格开发了一套测试代码集 Test262，用来检验每一种 JavaScript 实现遵守语言标准的程度。下面是目前为止各个主流的脚本引擎对新语言特性的支持情况。可见对于主流浏览器来说，就算是最新推出的语言标准也能得到快速适配。

> 数据来自[维基百科](https://en.wikipedia.org/wiki/ECMAScript#Conformance)。

| Scripting engine | Reference application(s)                      | ES5  | ES6 (2015) | ES7 (2016) | Newer (2017+) |
| ---------------- | --------------------------------------------- | ---- | ---------- | ---------- | ------------- |
| Chakra           | Microsoft Edge 18                             | 100% | 96%        | 100%       | 33%           |
| SpiderMonkey     | Firefox 79                                    | 100% | 98%        | 100%       | 100%          |
| V8               | Google Chrome 84, Microsoft Edge 84, Opera 70 | 100% | 98%        | 100%       | 100%          |
| JavaScriptCore   | Safari 13.1                                   | 99%  | 99%        | 100%       | 84%           |

## ES12（ES2021）

## ES11（ES2020）

### `BigInt`

## ES10（ES2019）

### 数组实例：`.flat()` 和 `.flatMap()`

### 字符串实例：`.trimStart()` 和 `.trimEnd()`

## ES9（ES2018）

### 扩展运算符 Spread Operator

### Rest 参数

### 异步迭代 Asynchronous Iteration

### 正则表达式的更新

## ES8（ES2017）

### 异步操作：`async` 和 `await`

### `Object.values()` 和 `Object.entries()`

### `Object.getOwnPropertyDescriptors()`

### 字符串实例：`.padStart()` 和 `.padEnd()`

## ES7（ES2016）

### 数组实例：`.includes()`

## ES6（ES2015）

ES6 是 ECMAScript 自 97 年的初版发布以来的最大的一次拓展性更新。ES6 的目标在于为大型应用开发、库的创建和以 ECMAScript 为标准的各种语言提供更好的支持。ES6 主要的更新内容包括模块化特性、类的声明、块级作用域、迭代器和生成器、非同步的 Promise、解构模式和尾调用优化。内置的库被扩展为支持新增的 map、set 和二进制数值数组结构，同时字符串和正则表达式支持新增的 Unicode 补充字符。这些内置库现在可以通过子类进行拓展。

### `let` 和 `const`

### 模版字符串 Template Literals

### 对象解构/数组结构 Objects/Arrays Destructuring

### 对象字面量 Object Literals

### `for of` 循环

### 箭头函数 Arrow Functions

### 默认参数 Default Params

### 类的声明 Class Declaration

### 模块 Module

### 数据结构：`Set`

### Symbol

## References

- [ECMAScript - Wikipedia](https://en.wikipedia.org/wiki/ECMAScript)
- [ECMA-262 - Ecma International](https://262.ecma-international.org/6.0/)
