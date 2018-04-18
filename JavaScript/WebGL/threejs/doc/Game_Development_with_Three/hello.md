# Hello,Three.js

为了能够显示，我们需要一些最基本的对象：
- camera（摄像机）
- scene（场景）
- renderer（渲染器）
- geometry（几何体）
- material（材质）
- mesh（网格对象）

所有的东西都需要在场景中显示，所以我们需要先创建一个场景：
```
var scene = new THREE.Scene();
```
然后我们需要创建一个 `mesh` 对象在场景中显示，`mesh` 对象是由 `geometry` 和 `material` 决定的（也就是一个物体是由形状和材质决定的）：
```
var geometry = new THREE.IcosahedronGeometry(200,1);
var material = new THREE.MeshBasicMaterial({color:0x00FF7F,wireframe:true,wireframeLinewidth:2});
var mesh = new THREE.Mesh(geometry,material);
```
创建完毕，将 `mesh` 添加到场景中：
```
scene.add(mesh);
```
还是什么都看不到，是因为我们还没有渲染，现在我们来创建渲染器，然后把它添加到浏览器中：
```
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth,window.innerHeight);
document.body.appendChild(renderer.domElement);
```
现在有了一片黑的，还是没有显示出我们想要的，是因为还没有添加摄像机：
```
var camera = new THREE.PerspectiveCamera(75,window.innerWidth/window.innerHeight,1,1000);
camera.position.z=500;
```
还是一样黑，是因为我们没有开始渲染，我们把场景和摄像机添加到渲染器中，开始渲染：
```
renderer.render(scene,camera);
```
现在可以看到一个绿色的多面体了，我们现在让它动起来：
```
animate();
function animate(){
  requestAnimationFrame(animate);
  mesh.rotation.x+=0.1;
  renderer.render(scene,camera);
}
```
现在可以看到一个滚动的多面体了，`requestAnimationFrame` 是动画的关键，它不停的使得渲染器重新渲染。

## 总结

现在已经完成了第一个用`Three.js`实现的3D动画。这一章简单的了解了整个流程和环境，下一章会更详细的说明每个部分（场景、渲染器。。。）还有灯光

