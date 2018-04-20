# 创建一个世界

## Geometries (几何体)

一个物体的形状有很多种，`Three.js` 提供了一系列不同的类来创建一些常用的形状，下面简单介绍下：

> 3D

- cube(立方体)：长方体
- sphere(球形)：球由经线纬线组成
- polyhedra(多面体)
- cylinder(圆桶)
- torus(环形)

> 2D

- plane(长方形)
- circle(圆形)
- ring(环形)

上面都是常用的形状，我们还可以创建自定义的形状：
```
var geo = new THREE.Geometry();
geo.vertices = {
  new THREE.Vector3(0,0,0),
  new THREE.Vector3(0,100,0),
  new THREE.Vector3(0,0,100)
};
geo.faces.push(new THREE.Face3(0,1,2));
geo.computeBoundingSphere();
```
给出顶点和边就可以创建自定义的形状。（创建的是一个直角三角形）

## text(文字)

渲染3D文字还需要导入相关的字体文件。

创建文字：
```
var text = new THREE.TextGeometry("hello",{
  size:30,
  height:30,
  font:'helvetiker',
  weight:'normal',
  style:'normal',
});
```

## Materials(材质)

（Three.js 入门指南有详解）

## 创建一个地球

```
// 先创建场景
var scene = new THREE.Scene();

// 然后创建摄像机
var camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,0.1,1000);
camera.position.set(0,0,100);

// 再创建渲染器
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth,window.innerHeight);
document.body.appendChild(renderer.domElement);

// 创建地球：1.创建球体 2.创建地球贴图
var geo = new THREE.SphereGeometry(40,20,20);
var texture = new THREE.TextureLoader().load('https://threejs.org/examples/textures/land_ocean_ice_cloud_2048.jpg');
var material = new THREE.MeshBasicMaterial({map:texture});
var earth = new THREE.Mesh(geo,material);
earth.position.set(0,0,0);
scene.add(earth);

// 创建动画，循环渲染
var render = function(){
  requestAnimationFrame(render);
  earth.rotation.y += 0.01;
  renderer.render(scene,camera);
}
render();
```

上面的代码可以得到一个不停在转动的地球。

## 创建一个城市
```

// 先创建场景
var scene = new THREE.Scene();

// 然后创建摄像机
var camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,1,10000);
camera.position.set(0,400,400);
camera.rotation.x = -45 *Math.PI/180;

// 再创建渲染器
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setClearColor(0xd7f0f7);
document.body.appendChild(renderer.domElement);

// 创建一栋楼
var geo = new THREE.CubeGeometry(1,1,1);
geo.applyMatrix(new THREE.Matrix4().makeTranslation(0,0.5,0));
var material = new THREE.MeshLambertMaterial({color:0xDEDEDE});

// 创建楼群
for(var i=0; i<300 ;++i){
  var building = new THREE.Mesh(geo.clone(),material.clone());
  building.position.x = Math.floor(Math.random()*200-100)*4;  
  building.position.z = Math.floor(Math.random()*200-100)*4;
  building.scale.x = Math.random() * 50 + 10;
  building.scale.y = Math.random() * building.scale.x * 8 + 8;
  building.scale.z = building.scale.x;
  scene.add(building);
}

// 创建光源
var light = new THREE.PointLight( 0xF2F2F2);
light.position.set( 0, 100, 500 );
scene.add( light );

// 创建地板
var floor = new THREE.PlaneGeometry(2000,2000,20,20);

var mat = new THREE.MeshBasicMaterial({color:0x9db3b5});
var mesh = new THREE.Mesh(floor,mat);
mesh.rotation.x = -90 * Math.PI/180;
scene.add(mesh);

// 创建动画，循环渲染
document.body.style.backgroundColor = '#d7f0f7';
var render = function(){
  requestAnimationFrame(render);
  renderer.render(scene,camera);
}
render();
```
---

## 灯光

常用的几种类型光源：
- AmbientLight（环境光）：照亮场景中的所有物体，不能用于投射阴影，因为它没有方向
- DirectionalLight（定向光/太阳光）：以特定方向发射的光，这种光线表现得好像无限远，而且它产生的光线都是平行的。 常见的用例是模拟日光; 太阳距离足够远以至于它的位置可以被认为是无限的，并且来自它的所有光线是平行的（可以投射阴影）
- HemisphereLight（半球光）：位于场景正上方的光源，颜色从天空颜色渐变为地面颜色，这光不能用于投射阴影
- PointLight（点光源）：从各个方向单点发出的光。 一个常见的用例是复制裸灯泡发出的光线（可以投射阴影）
- SpotLight（聚光灯）：这个光线从一个方向上的单个点发射出去，沿着一个圆锥体发射，该圆锥体的大小随着光线的进一步增大而增大（可以投射阴影）

还有雾效果：
- Fog:随着距离线性变化
- FogExp2:随着距离指数变化

---

## 阴影

只有特殊的光源可以产生阴影，显示阴影需要打开设置：
```
renderer.shadowMapEnabled = true;
```

## 总结

下面是有雾和阴影效果的城市完成版代码：
```
// 先创建场景
var scene = new THREE.Scene();

// 然后创建摄像机
var camera = new THREE.PerspectiveCamera(65,window.innerWidth/window.innerHeight,1,10000);
camera.position.y=400
camera.position.z=400
camera.rotation.x = -45 *Math.PI/180;

// 再创建渲染器
var renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setClearColor(0xd7f0f7);
document.body.appendChild(renderer.domElement);

// 创建一栋楼
var geo = new THREE.BoxGeometry(1,1,1);
geo.applyMatrix(new THREE.Matrix4().makeTranslation(0,0.5,0));
var material = new THREE.MeshPhongMaterial({color:0xcccccc});

// 创建楼群
for(var i=0; i<90 ;++i){
  var building = new THREE.Mesh(geo.clone(),material.clone());
  building.position.x = Math.floor(Math.random()*200-100)*4;  
  building.position.z = Math.floor(Math.random()*200-100)*4;
  building.scale.x = Math.random() * 50 + 10;
  building.scale.y = Math.random() * building.scale.x * 5 + 8;
  building.scale.z = building.scale.x;
  building.receiveShadow=true;
  building.castShadow=true;
  scene.add(building);
}

// 创建光源
var light = new THREE.DirectionalLight( 0xf6e86d,1);
light.position.set( 500, 1500, 1000 );
// 设置阴影
light.castShadow=true;
light.shadowDarkness=0.5;
light.shadow.mapSize.width = 2048;  // default
light.shadow.mapSize.height = 2048; // default

light.shadow.camera.far = 2500;  
light.shadowCameraVisible=true;
light.shadowCameraLeft=-1000
light.shadowCameraRight=1000
light.shadowCameraTop=1000
light.shadowCameraBottom=-1000
scene.add( light );
// 添加雾
scene.fog=new THREE.Fog(0x9db3b5,0,800)
// 创建地板
var floor = new THREE.PlaneGeometry(2000,2000,20,20);
floor.receiveShadow=true;
var mat = new THREE.MeshBasicMaterial({color:0x9db3b5});
var mesh = new THREE.Mesh(floor,mat);
mesh.rotation.x = -90 * Math.PI/180;
scene.add(mesh);

// 创建动画，循环渲染
document.body.style.backgroundColor = '#d7f0f7';
var render = function(){
  requestAnimationFrame(render);
  renderer.shadowMapEnabled = true;
  renderer.render(scene,camera);
}
render();
```
