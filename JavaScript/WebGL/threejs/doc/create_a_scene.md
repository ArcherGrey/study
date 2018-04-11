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
3. 

