# 应用结构

## 主进程和渲染进程

在 `package.json` 中配置的 `main.js` 的进程就是主进程，通过创建web页面来展示用户图像界面。一个 `electron` 应用程序只会有一个主进程。

由于 Electron 使用 Chromium 来显示 web 页面，所以 Chromium 的多进程架构也是可用的。 每个 Electron 中的 web 页面运行在它的叫渲染进程的进程中。

在通常的浏览器内，网页通常运行在一个沙盒的环境隔离并且不能够使用原生的资源。 然而 Electron 的用户在 Node.js 的 API 支持下可以在页面中和操作系统进行一些底层交互。

## 主进程和渲染进程之间的区别

主进程使用 `BrowserWindow` 实例创建页面。 每个 `BrowserWindow` 实例都在自己的渲染进程里运行页面。 当一个 `BrowserWindow` 实例被销毁后，相应的渲染进程也会被终止。

主进程管理所有的 `web` 页面和相关的渲染进程。每一个渲染进程都是独立的，只处理自己的渲染页面。

由于在页面里管理原生 GUI 资源是非常危险而且容易造成资源泄露，所以在页面调用 GUI 相关的 APIs 是不被允许的。 如果你想在网页里使用 GUI 操作，其对应的渲染进程必须与主进程进行通讯，请求主进程进行相关的 GUI 操作。

## 使用 electron API

`electron` 提供了一系列 `API` 支持主进程和渲染进程来开发桌面应用。


通过引用 `electron` 模块来使用：
```
const electron = require('electron')
```

其中，大多数接口都是通过主进程来调用，少部分只能通过渲染进程调用，其他的都可以。

`electron` 中的窗口通过创建 `BrowserWindow` 实例来使用，它只在主进程中可用：
```
// This will work in the main process, but be `undefined` in a
  // renderer process:
  const { BrowserWindow } = require('electron')
  
  const win = new BrowserWindow()
```
