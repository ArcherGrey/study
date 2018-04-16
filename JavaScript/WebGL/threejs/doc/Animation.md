# Animation （动画）

## 动画系统概述
在动画系统中，可以为模型设置各种属性的动画：蒙皮、骨骼、变形目标、材质属性、可见性等等。动画属性可以是淡出淡入、交叉渐变和变形。

为了在一个同类系统中实现所有这些，three.js动画系统在2015年彻底改变了（注意过时的信息！），现在它有一个类似于Unity / Unreal Engine 4的体系结构。本页简要概述了系统的主要组成部分以及它们如何一起工作：
- Animation Clips（动画片段）：每个动画片段保存对象的特定活动的数据
- Keyframe Tracks（关键帧轨道）：在动画片段里，每个动画属性的数据都存储在一个独立的 `Keyframe Tracks` 中，也就是说动画片段是由一个或多个关键帧组成的
- Animation Mixer（动画剪辑器）：上面存储的数据只是动画构成的基础，实际播放时通过动画剪辑器再次加工处理
- Animation Actions（动画播放器）：通过对动画播放器的配置可以控制动画片段的播放时机以及是否需要进行剪辑
- Animation Object Groups（动画对象组）：如果希望一组对象接收共享动画状态，则可以使用
- Supported Formats and Loaders（支持的格式和加载器）

## AnimationAction
用来调度 `Animation Clips`

### 构造函数
`AnimationAction( mixer : AnimationMixer, clip : AnimationClip, localRoot : Object3D )`
- mixer - 控制动画的剪辑器.
- clip - 动画片段.
- localRoot - 执行操作的对象.

注意：不要直接调用此构造函数，而应该使用AnimationMixer.clipAction实例化AnimationAction，因为此方法提供缓存以获得更好的性能。

### 属性
> clampWhenFinished : Boolean

如果clampWhenFinished设置为true，则动画将在其最后一帧自动暂停。如果clampWhenFinished设置为false，则当动作的最后一个循环结束时，启用将自动切换为false，以便此操作不会产生进一步的影响。默认为false。
注意：如果动作被中断，则clampWhenFinished没有影响（只有在最后一个循环已经完成时才有效果

---
