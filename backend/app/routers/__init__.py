"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import craftsman as router_craftsman
from app.routers import apprentice as router_apprentice
from app.routers import timber as router_timber
from app.routers import component as router_component
from app.routers import mortise as router_mortise
from app.routers import building as router_building
from app.routers import tool as router_tool
from app.routers import workshop as router_workshop
from app.routers import drawing as router_drawing
from app.routers import carving as router_carving
from app.routers import lacquer as router_lacquer
from app.routers import exhibition as router_exhibition
from app.routers import heritage as router_heritage
from app.routers import training as router_training
from app.routers import exchange as router_exchange
from app.routers import media as router_media
from app.routers import donation as router_donation

ROUTERS = [router_craftsman, router_apprentice, router_timber, router_component, router_mortise, router_building, router_tool, router_workshop, router_drawing, router_carving, router_lacquer, router_exhibition, router_heritage, router_training, router_exchange, router_media, router_donation]
