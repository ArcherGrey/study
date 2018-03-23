# VUE 2
## 安装
- 兼容性：不支持IE8及以下版本，因为VUE使用了IE8无法模拟的ECMAScript5特性，但支持所有兼容ECMAScript5的浏览器
- 推荐安装 `Vue Devtools` 可以在一个友好的界面中审查和调试 vue 应用

使用方法：
1. 通过 <script> 标签导入：
- 使用本地下载，开发的时候最好不要使用压缩版本，这样会失去所有常见错误相关的警告
- 使用cdn 
  
2. 大型应用开发使用NPM安装 `npm install vue`

vue提供了一个官方命令行工具来快速开发
```
# 全局安装 vue-cli
$ npm install --global vue-cli
# 创建一个基于 webpack 模板的新项目
$ vue init webpack my-project
# 安装依赖，走你
$ cd my-project
$ npm run dev

```
