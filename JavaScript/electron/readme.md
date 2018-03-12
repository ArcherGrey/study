# 关于 Electron

`Electron` 是由 `Github` 开发，用 `HTML`，`CSS`和`JavaScript`来构建跨平台桌面应用程序的一个开源库。 `Electron`通过将`Chromium`和`Node.js`合并到同一个运行时环境中，并将其打包为`Mac`，`Windows`和`Linux`系统下的应用来实现这一目的。

`Electron` 于2013年作为构建 `Github` 上可编程的文本编辑器`Atom`的框架而被开发出来。这两个项目在2014春季开源。

目前它已成为开源开发者、初创企业和老牌公司常用的开发工具。 

# 核心理念

为了保持 `Electron` 的小 (文件体积) 和可持续性 (依赖和API的扩展) ，`Electron` 限制了使用的核心项目的范围。

比如 `Electron` 只用了 `Chromium` 的渲染库而不是全部。 这使得容易升级 `Chromium`，但也意味着 `Electron` 缺少 `Google Chrome` 里的一些浏览器特性。

`Electron` 所添加的的新特性应主要用于原生 `API`。 如果一个特性能够成为一个 `Node.js`模块，那它就应该成为。
