# 创建一个场景
本节的目标是对three.js进行简要介绍。 我们将首先创建一个场景，一个旋转的立方体。 

## 准备工作
在你使用three.js之前，你需要将three.js文件下载到本地目录下，然后使用下面的html模板：
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset=utf-8>
		<title>My first three.js app</title>
		<style>
			body { margin: 0; }
			canvas { width: 100%; height: 100% }
		</style>
	</head>
	<body>
		<script src="js/three.js"></script>
		<script>
			// Our Javascript will go here.
		</script>
	</body>
</html>
```
下面所有的代码都可以放到空的<script>标签中
  
## 创建场景

为了能够通过three.js展示，我们需要三个东西：场景、摄像机、渲染器：
```
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
```

其中摄像机的参数按顺序：
1. 第一个参数是视场角（FOV），FOV是在任何给定时刻在显示器上看到的场景的范围，该值以度为单位
2. 第二个是宽高比。 几乎总是使用元素的宽度除以高度，否则将获得与在宽屏幕电视上播放旧电影时相同的结果 - 图像看起来很凹陷
3. 接下来的两个属性是近和远裁剪平面。 这意味着，远离相机的物体远远超过或接近近处的物体不会被渲染。 现在不必担心这一点，但可能想要在应用中使用其他值以获得更好的性能。

除了创建渲染器实例外，我们还需要设置我们希望呈现应用程序的大小。 使用我们想要用我们的应用填充的区域的宽度和高度是一个好主意 - 在这种情况下，使用浏览器窗口的宽度和高度。 对于性能密集型应用程序，您还可以给setSize较小的值，如window.innerWidth / 2和window.innerHeight / 2，这将使应用程序呈现一半尺寸。

如果你想保持你的应用程序的大小，但以较低的分辨率渲染它，你可以通过以false作为updateStyle（第三个参数）调用setSize来实现。 例如，setSize（window.innerWidth / 2，window.innerHeight / 2，false）将以半分辨率呈现您的应用，因为您的<canvas>具有100％的宽度和高度

最后，我们将renderer元素添加到我们的HTML文档中。 这是渲染器用来显示场景的<canvas>元素。

接下来来添加立方体：
```
var geometry = new THREE.BoxGeometry( 1, 1, 1 ); // 立方体的点和面
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } ); // 上色
var cube = new THREE.Mesh( geometry, material ); // 存放立方体
scene.add( cube );

camera.position.z = 5;
```

## 开始渲染

上面虽然添加了立方体，但是还没有在场景上进行渲染，所以还是什么都看不到，现在我们通过调用动画循环来渲染:
```
function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();
```

## 让立方体动起来

在 `renderer.render ` 调用之前加入：
```
cube.rotation.x += 0.1;
cube.rotation.y += 0.1;
```
每一帧都会执行一次（一般一秒60帧）
