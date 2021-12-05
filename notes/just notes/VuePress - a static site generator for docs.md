---
title: VuePress - 一个为技术文档而设计的静态网页生成器
date: "2021-12-05T14:25:20.334Z"
tags:
  - Vue.js
  - VuePress
---

Vue.js 项目 2.x 文档使用 Hexo 驱动，而其很多子项目在使用 GitBook 维护，这些工具在配置方式、构建速度和灵活性上都有很大限制。VuePress 被设计用来解决这些问题，而且更进一步，让你可以在文档中使用 Vue 的能力。

先来简单介绍一下 VuePress。VuePress 是一个静态站点生成工具，其主要功能是将 Markdown 内容渲染成静态站点，以方便查阅和公开。这个工具具有以下特性及定位：

- 工具将生成一个由 Vue 和 Vue Router 驱动的单页应用
  > 熟悉的配方
- Markdown 文档经过 markdown-it 编译后作为 Vue 组件的 `<template>` 渲染
  > 这意味着你可以在 Markdown 文档内直接使用 Vue 的能力
- 生成静态页面对 SEO 友好
  > 搜索引擎爬虫可以直接抓取网页内容，优化搜索结果
- 提供插件 API 和主题 API，配置和二次开发更加灵活
  > 通过插件和主题配置，你可以用 VuePress 来生成博客或者其他任何网站

<!-- more -->

## 基本用法

### Getting Started

跟随以下步骤来开始使用 VuePress。

1. 项目初始化

```shell
# 准备目录
mkdir vuepress-starter
cd vuepress-starter

# 初始化项目
git init
yarn init

# 安装本地依赖
yarn add -D vuepress@next
```

2. 在 `package.json` 文件添加以下脚本

```json
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}
```

3. 将临时目录和缓存文件添加到 `.gitignore` 文件中

```shell
echo 'node_modules' >> .gitignore
echo '.temp' >> .gitignore
echo '.cache' >> .gitignore
```

4. 添加第一篇文档

```shell
mkdir docs
echo '# Hello VuePress' > docs/README.md
```

5. 启动本地服务

```shell
yarn docs:dev
```

VuePress 会在 [http://localhost:8080](http://localhost:8080) 启动一个热重载的开发服务器。

### 配置 VuePress

目前为止我们已经得到了一个基本的 VuePress 项目，其包含了以下内容：

- 一个默认主题支持浅色模式和深色模式
- 一个 `'/'` 路径下的默认两栏页面：左边显示目录，右边显示正文

这显然不足够驱动我们的技术文档，所以我们需要添加一些配置，让我们的文档能被方便的查阅。

通过配置，我们希望达到以下效果：

- 配置站点的基本信息，如站点名称和描述等
- 一个首页来介绍技术文档的主题并向常用连接跳转
- 合理的导航栏，方便在文档的不同部分之间导航
- 基于路径的侧边栏，让同一个目录下的文档使用相同的侧边栏
- 简单的本地搜索，可以搜索文档大小标题
- 简单的定制化，对默认主题进行少许样式调整

#### 约定的配置文件

VuePress 会根据优先级加载约定的配置文件：

- `vuepress.config.js`
  > VuePress 项目的根目录下
- `<sourceDir>/.vuepress/config.js`
  > VuePress 项目的文档开发目录下，比如你按照上面的步骤来做的话，`<sourceDir>` 为 `docs` 目录

由于 VuePress 官方指南中提到了后者，我们就以后者为准，来配置我们的 VuePress 文档项目。

#### 站点配置

#### 配置首页

默认情况下，页面的路由路径是根据 Markdown 文件的相对路径来决定的。目录下的 `README.md` 文件绑定到目录名称的路径上，而目录内的其他文件则根据文件名绑定到对应名称加 `.html` 后缀的路径上。

### Frontmatter

在每篇 Markdown 文档的头部可以插入 Frontmatter 来针对这篇文档配置一些定制化选项。

```markdown
---
lang: zh-CN
title: 页面标题
description: 页面描述
---
```

### 内容

页面内容使用 Markdown 书写，VuePress 会将其转换为 HTML，并作为 Vue 组件的 `<template>` 的内容进行渲染。这表示你可以在 Markdown 中使用 Vue.js 的模版语法能力。

## 参考

- [VuePress 官方文档](https://v2.vuepress.vuejs.org/zh/)
