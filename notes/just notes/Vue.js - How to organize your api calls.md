---
title: 前端数据流的处理 - Vue.js 应该把 API 调用逻辑放在哪里？
tags:
  - JavaScript
  - Vue.js
---

经历了业务快速迭代、上线期限紧急等一系列挑战，代码悄然进入野蛮生长时代，等松下一口气时才猛然发现，此时想重构任何东西都属于地狱难度，而面对接下来依然紧急的业务迭代，要不就选择放任不管，先实现眼前的功能，任由重构代码库的难度从地狱难度继续升级；要不就咬咬牙着手重构，以事倍功半的效率痛苦的消化接下来的业务迭代，拉上整个部门一起加班加点。

前端架构没有很好的分离视图渲染逻辑和数据流处理逻辑时就很容易进入上面的困境中，而最极端的结果就是重构变得举步维艰，任何一点修改都可能造成雪崩式的灾难后果。

先不论事件的前因后果，今天我们来好好聊聊如何处理前端的逻辑分层，这次我们的主题是如何处理数据流的处理。在前后端分离的时代，前端渲染视图的数据流有两个来源。

1. 用户的输入
2. 后端 API 的返回

<!-- more -->
