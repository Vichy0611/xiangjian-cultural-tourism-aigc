# 乡见文旅影像导演

一个面向城市文旅影像创作的 Codex Skill。它把现实资料、创意策划、逐镜生成、声音设计、成本路由和成片质检组织成一套可执行的工作流。

**Xiangjian Cultural Tourism AIGC** turns evidence about a place into production-ready short-film plans. The Skill is vendor-neutral and keeps the default workflow economical, while reserving higher-cost generation for the few shots that materially benefit from it.

## 它解决什么

- 先核实地点、历史、非遗与景区细节，再进入创作；
- 用一个贯穿意象组织短片，避免地标清单和空泛抒情；
- 将每个镜头写成可生成、可剪辑、可听审的“逐镜合同”；
- 默认走低成本动态方案，只为复杂动作、真实地标和核心收束镜头升级质量；
- 分角色选择声音，支持方言听审、国际传播和环境声设计；
- 检查稳定性、动作衔接、事实准确、文字位置、声音重叠与城市落款；
- 将多次生成中的结构化经验沉淀到本地候选库，经人工审核后再升级为 Skill 规则。

## 安装

克隆仓库后，将 Skill 文件夹复制到 Codex Skills 目录。

### Windows PowerShell

```powershell
Copy-Item -Recurse -Force .\skills\cultural-tourism-aigc "$HOME\.codex\skills\cultural-tourism-aigc"
```

### macOS / Linux

```bash
cp -R skills/cultural-tourism-aigc ~/.codex/skills/
```

重启 Codex 后，可直接描述文旅短片任务，或显式使用：

```text
$cultural-tourism-aigc
```

## 典型交付物

Skill 可以生成事实与素材表、创意脊柱、完整旁白、逐镜表、逐镜生成说明、参考素材编号、模型路由、角色声音表、音乐与环境声设计、片尾版式、质量检查结果和局部返修清单。

## 持续学习

持续学习采用三层结构：本地事件、待审核候选、正式规则。系统只记录片型、镜头数、路由、转场家族和返修问题类别等聚合信号，不记录用户素材、完整文案、完整提示词、路径、账号或密钥。

候选模式达到重复阈值后会生成本地审核摘要。只有人工确认其适用条件和复现性后，才应写入正式 Skill 指南。详情见 [`learning-loop.md`](skills/cultural-tourism-aigc/references/learning-loop.md)。

## 验证

```bash
python skills/cultural-tourism-aigc/scripts/validate_plan.py plan.json
python skills/cultural-tourism-aigc/scripts/consolidate_learnings.py summary.json --output review.md
```

## 设计原则

真实材料优先；一条创意主线；镜头动作可执行；声音逐角色选择；成本按镜头分配；失败镜头局部返修；经验经过审核再晋升。

## License

[MIT](LICENSE)

