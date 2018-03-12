# 调试

## 渲染进程

最好用的调试工具就是 Chromium 调试工具，对所有的渲染进程都可用，包括 `BrowserWindow`, `BrowserView`, `WebView`。

通过在 `webContents` 中调用 `openDevTools()` 来使用：
```
const { BrowserWindow } = require('electron')
  
  let win = new BrowserWindow()
  win.webContents.openDevTools()
```

## 调试主进程

调试主进程有点棘手，因为你不能简单地为他们打开开发工具。 由于Google / Chrome和Node.js之间更紧密的协作，Chromium开发工具可用于调试Electron的主流程，但您可能会遇到诸如需求不在控制台中的奇怪现象。
