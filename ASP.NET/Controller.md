# Controller 

> `Controller[控制器]` 在 `MVC` 框架中负责控制所有客户端与服务器之间的交互，并且协调 `Model` 和 `View` 之间的数据传递，可以说是 `MVC` 中的核心角色。

## 类别和方法

```
using System.Web.Mvc;
namespace MvcApplication3.Controllers{ 
  public class HomeController:Controller{
    public ActionResult Index(){
      ViewBag.Message = "修改此模板以快速启动你的 ASP.NET MVC 应用程序";
      return View();
    }
  }
}
```
整个 `Controller` 就是一个命名空间，前面的 `MvcApplication3` 就是 `MVC3` ，每一个具体的 `Controller` 都是一个类，其中会有很多方法，只要是 `Public` 方法就是一个 `Action` ，通过 `Action` 就可以接收客户端传来的要求，响应对应的 `View` 。

`Controller` 的基本要求：
- `Controller` 必须为 `Public` 类型
- `Controller` 的名称必须以 `Controller` 结尾
- 所有 `Controller` 都必须继承自 `MVC` 内建的 `Controller` 
- 所有的 `Action` 都应该为 `Public` 


## 运行过程

`MvcHandler` 选中某一个 `Controller` 之后，再通过 `ActionInvoker` 来选定适合的 `Action` 来运行。

每个 `Action` 可以定义 0 到多个参数，`ActionInvoker` 会根据 `RouteValue` 和客户端传来的数据来调用 `Action` 方法。

参数传入的属性都是通过**模型绑定**机制，从 `RequestContext` 取得数据，然后将数据传入方法的参数中。

`Action` 运行完成后的回传值通常是 `ActionResult` 类别。`ActionResult`是一个抽象类。

`MvcHandler` 得到 `ActionResult` 后运行 `ExecuteResult` 方法，将结果响应到客户端，到这里 `Controller` 任务完成。
