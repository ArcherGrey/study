# 探索和互动

这个章节我们来看看互动相关的问题（利用上个章节的城市场景）

## 键盘和鼠标控制移动

我们来添加一个类用来通过键盘控制摄像机移动：
```
function KeyboardControls(object, options) {
  this.object = object;
  options = options || {};
  this.domElement = options.domElement || document;
  this.moveSpeed = options.moveSpeed || 1;
  this.domElement.addEventListener('keydown', this.onKeyDown.bind(this), false);
  this.domElement.addEventListener('keyup', this.onKeyUp.bind(this), false);
}

KeyboardControls.prototype = {
  update: function() {
    if (this.moveForward) this.object.translateZ(-this.moveSpeed);
    if (this.moveBackward) this.object.translateZ(this.moveSpeed);
    if (this.moveLeft) this.object.translateX(-this.moveSpeed);
    if (this.moveRight) this.object.translateX(this.moveSpeed);
  },
  onKeyDown: function(event) {
    switch (event.keyCode) {
      case 38: // up
      case 87: // w
        this.moveForward = true;
        break;
      case 37: // left
      case 65: // a
        this.moveLeft = true;
        break;
      case 40: // down
      case 83: // s
        this.moveBackward = true;
        break;
      case 39: // right
      case 68: // d
        this.moveRight = true;
        break;
    }
  },
  onKeyDown: function(event) {
    switch (event.keyCode) {
      case 38: // up
      case 87: // w
        this.moveForward = false;
        break;
      case 37: // left
      case 65: // a
        this.moveLeft = false;
        break;
      case 40: // down
      case 83: // s
        this.moveBackward = false;
        break;
      case 39: // right
      case 68: // d
        this.moveRight = false;
        break;
    }
  }
};
```

我们添加了对键盘事件的监听器，把 `camera` 作为参数传入就可以实现通过键盘对摄像机的操作。这样很麻烦所以`three.js` 还提供了一系列默认的控制方式给你，可以在 `example/js/controls`找到，把其中的 `FirstPersonControls.js` 导入上一章的城市代码中再添加几个全局变量：
```
var controls,clock;
```
接着，主进程里面添加：
```
clock = new THREE.Clock();
controls = new THREE.FirstPersonControls(camera);
controls.movementSpeed = 100;
controls.lookSpeed = 0.1;
```
最后在渲染进程里添加:
```
controls.update(clock.getDelta());
```
现在你就可以通过鼠标和键盘在城市中探索了。

## 点击

点击屏幕选择或者去触发一些其他请求，相当于在2D屏幕上点击然后反馈到3D世界里。为了处理这样的情况，我们需要一条虚拟的线，称为 `ray` ，从摄像机到鼠标点击的地方。

首先需要一个 `project` ：
```
project = new THREE.Projector();
```
然后，需要注册一个点击事件监听器：
```
renderer.domElement.addEventListener('mousedown',function(event){
  var vector = new THREE.Vector3(renderer.devicePixelRatio * (event.pageX - this.offsetLeft) / this.width * 2 - 1, renderer.devicePixelRatio * (event.pageY - this.offsetTop) / this.height * 2 - 1, 0);
  projector.unprojectVector(vector,camera);
  var raycaster = new THREE.Raycaster(camera.position, vector.sub(camera.position).normalize());
  var intersects = raycaster.intersectObjects(OBJECTS);
  if(intersects.length){
  }
  
},false);
```

## 计时

利用时间来控制画面能够在不同配置的电脑上，保持动画的效果。

---

## 第一人称射击游戏

现在来写一个第一人称射击游戏，游戏具有下面几个特征：
- 基于像素地图的世界
- 玩家可以在世界里看、跑、跳
- 可以窗口或者全屏
- 玩家可以射击敌人，敌人也可以反击
- 被击中会掉血，生命值消耗完会重生
- 被击中时，玩家屏幕会有红光闪现
- 应该有十字线瞄准和生命条
- 光影和纹理效果不是很重要，但是需要能够感知距离

### html
首先是html代码，由于功能变得复杂，需要一个开始界面：
```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>射击</title>
    <link rel="stylesheet" href="main.css">
  </head>
  <body>
    <div id="start">
      <div id="instruction">
        Click to start
      </div>
    </div>
    <div id="hub" class="hidden">
      <div class="hidden" id='hurt'>

      </div>
    </div>
    <script type="text/javascript"src="three.js">
    </script>
    <script type="text/javascript"src="main.js">
    </script>
  </body>
</html>
```

### 地图

