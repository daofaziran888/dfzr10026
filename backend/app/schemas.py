"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class CraftsmanEntry(BaseModel):
    """木作匠人明细结构。"""

    field_0: str | None = None  # 匠人编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 师承流派
    field_3: str | None = None  # 从艺年限
    field_4: str | None = None  # 擅长技艺
    field_5: str | None = None  # 代表作数
    field_6: str | None = None  # 资质等级
    field_7: str | None = None  # 在册状态

class ApprenticeEntry(BaseModel):
    """学徒明细结构。"""

    field_0: str | None = None  # 学徒编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 师从匠人
    field_3: str | None = None  # 入门日期
    field_4: str | None = None  # 学习阶段
    field_5: str | None = None  # 考核成绩
    field_6: str | None = None  # 出师日期
    field_7: str | None = None  # 学徒状态

class TimberEntry(BaseModel):
    """木材批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 木材种类
    field_2: str | None = None  # 产地来源
    field_3: str | None = None  # 树龄等级
    field_4: str | None = None  # 干燥方式
    field_5: str | None = None  # 入册日期
    field_6: str | None = None  # 存放区域
    field_7: str | None = None  # 木材状态

class ComponentEntry(BaseModel):
    """木构件明细结构。"""

    field_0: str | None = None  # 构件编号
    field_1: str | None = None  # 构件名称
    field_2: str | None = None  # 构件类型
    field_3: str | None = None  # 所用木材
    field_4: str | None = None  # 制作匠人
    field_5: str | None = None  # 开始日期
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 构件状态

class MortiseEntry(BaseModel):
    """榫卯节点明细结构。"""

    field_0: str | None = None  # 节点编号
    field_1: str | None = None  # 榫卯名称
    field_2: str | None = None  # 榫卯类型
    field_3: str | None = None  # 关联构件
    field_4: str | None = None  # 契合精度
    field_5: str | None = None  # 检验匠人
    field_6: str | None = None  # 检验日期
    field_7: str | None = None  # 节点状态

class BuildingEntry(BaseModel):
    """修缮项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 建筑类型
    field_3: str | None = None  # 建筑年代
    field_4: str | None = None  # 修缮部位
    field_5: str | None = None  # 开工日期
    field_6: str | None = None  # 完工日期
    field_7: str | None = None  # 项目状态

class ToolEntry(BaseModel):
    """木工工具明细结构。"""

    field_0: str | None = None  # 工具编号
    field_1: str | None = None  # 工具名称
    field_2: str | None = None  # 工具类别
    field_3: str | None = None  # 制作匠人
    field_4: str | None = None  # 使用人员
    field_5: str | None = None  # 保养周期
    field_6: str | None = None  # 最后一次保养
    field_7: str | None = None  # 工具状态

class WorkshopEntry(BaseModel):
    """木作工坊明细结构。"""

    field_0: str | None = None  # 工坊编号
    field_1: str | None = None  # 工坊名称
    field_2: str | None = None  # 工坊类型
    field_3: str | None = None  # 所属匠人
    field_4: str | None = None  # 工位数量
    field_5: str | None = None  # 启用日期
    field_6: str | None = None  # 设施状况
    field_7: str | None = None  # 工坊状态

class DrawingEntry(BaseModel):
    """营造图样明细结构。"""

    field_0: str | None = None  # 图样编号
    field_1: str | None = None  # 图样名称
    field_2: str | None = None  # 图样类型
    field_3: str | None = None  # 绘制匠人
    field_4: str | None = None  # 绘制日期
    field_5: str | None = None  # 比例尺
    field_6: str | None = None  # 保存方式
    field_7: str | None = None  # 图样状态

class CarvingEntry(BaseModel):
    """雕花作品明细结构。"""

    field_0: str | None = None  # 作品编号
    field_1: str | None = None  # 作品名称
    field_2: str | None = None  # 雕花题材
    field_3: str | None = None  # 雕刻匠人
    field_4: str | None = None  # 所用木材
    field_5: str | None = None  # 开始日期
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 作品状态

class LacquerEntry(BaseModel):
    """漆面工序明细结构。"""

    field_0: str | None = None  # 工序编号
    field_1: str | None = None  # 关联构件
    field_2: str | None = None  # 漆料配方
    field_3: str | None = None  # 涂刷层数
    field_4: str | None = None  # 干燥方式
    field_5: str | None = None  # 操作匠人
    field_6: str | None = None  # 操作日期
    field_7: str | None = None  # 工序状态

class ExhibitionEntry(BaseModel):
    """展陈记录明细结构。"""

    field_0: str | None = None  # 展陈编号
    field_1: str | None = None  # 展陈主题
    field_2: str | None = None  # 展陈地点
    field_3: str | None = None  # 参展作品
    field_4: str | None = None  # 布展人员
    field_5: str | None = None  # 开始日期
    field_6: str | None = None  # 结束日期
    field_7: str | None = None  # 展陈状态

class HeritageEntry(BaseModel):
    """传承项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 申报级别
    field_3: str | None = None  # 代表性传承人
    field_4: str | None = None  # 申报日期
    field_5: str | None = None  # 认定结果
    field_6: str | None = None  # 传习记录
    field_7: str | None = None  # 项目状态

class TrainingEntry(BaseModel):
    """研习课程明细结构。"""

    field_0: str | None = None  # 课程编号
    field_1: str | None = None  # 课程名称
    field_2: str | None = None  # 授艺匠人
    field_3: str | None = None  # 课程内容
    field_4: str | None = None  # 课时安排
    field_5: str | None = None  # 学员人数
    field_6: str | None = None  # 开课日期
    field_7: str | None = None  # 课程状态

class ExchangeEntry(BaseModel):
    """交流记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 交流主题
    field_2: str | None = None  # 参与匠人
    field_3: str | None = None  # 交流地点
    field_4: str | None = None  # 交流日期
    field_5: str | None = None  # 交流成果
    field_6: str | None = None  # 后续计划
    field_7: str | None = None  # 记录状态

class MediaEntry(BaseModel):
    """技艺影像明细结构。"""

    field_0: str | None = None  # 影像编号
    field_1: str | None = None  # 拍摄主题
    field_2: str | None = None  # 拍摄日期
    field_3: str | None = None  # 拍摄地点
    field_4: str | None = None  # 影像类型
    field_5: str | None = None  # 拍摄人员
    field_6: str | None = None  # 存储位置
    field_7: str | None = None  # 影像状态

class DonationEntry(BaseModel):
    """资助记录明细结构。"""

    field_0: str | None = None  # 资助编号
    field_1: str | None = None  # 资助方
    field_2: str | None = None  # 资助方向
    field_3: str | None = None  # 资助金额
    field_4: str | None = None  # 资助日期
    field_5: str | None = None  # 接收方
    field_6: str | None = None  # 用途说明
    field_7: str | None = None  # 资助状态
