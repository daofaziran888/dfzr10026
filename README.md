# 传统木作营造技艺传习管理平台

面向中华传统木作营造的匠人档案、木材甄选、构件制作、榫卯工艺、古建修缮与工坊传承的一体化传习管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 匠人档案 | `craftsman` | 木作匠人 | 匠人编号、姓名、师承流派 |
| 学徒培养 | `apprentice` | 学徒 | 学徒编号、姓名、师从匠人 |
| 木材甄选 | `timber` | 木材批次 | 批次编号、木材种类、产地来源 |
| 构件制作 | `component` | 木构件 | 构件编号、构件名称、构件类型 |
| 榫卯工艺 | `mortise` | 榫卯节点 | 节点编号、榫卯名称、榫卯类型 |
| 古建修缮 | `building` | 修缮项目 | 项目编号、项目名称、建筑类型 |
| 工具管理 | `tool` | 木工工具 | 工具编号、工具名称、工具类别 |
| 工坊管理 | `workshop` | 木作工坊 | 工坊编号、工坊名称、工坊类型 |
| 图样档案 | `drawing` | 营造图样 | 图样编号、图样名称、图样类型 |
| 雕花技艺 | `carving` | 雕花作品 | 作品编号、作品名称、雕花题材 |
| 髹漆工艺 | `lacquer` | 漆面工序 | 工序编号、关联构件、漆料配方 |
| 作品展陈 | `exhibition` | 展陈记录 | 展陈编号、展陈主题、展陈地点 |
| 非遗传承 | `heritage` | 传承项目 | 项目编号、项目名称、申报级别 |
| 技艺研习 | `training` | 研习课程 | 课程编号、课程名称、授艺匠人 |
| 匠人交流 | `exchange` | 交流记录 | 记录编号、交流主题、参与匠人 |
| 影像记录 | `media` | 技艺影像 | 影像编号、拍摄主题、拍摄日期 |
| 资助捐赠 | `donation` | 资助记录 | 资助编号、资助方、资助方向 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
