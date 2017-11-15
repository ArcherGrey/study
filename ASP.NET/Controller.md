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
