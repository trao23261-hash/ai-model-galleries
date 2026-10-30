# ai-model-galleries

## AI 模特素材库

<p align="center">
  <img src="assets/ai-model-galleries-cover.png" alt="AI 模特素材库封面：模特脸、姿势与服装" width="1600" height="900">
</p>

> 封面为 AI 生成的介绍插图，非归档素材样张；按 16:9 横版展示。

这是三个自有 AI 模特素材网站的**私有归档仓库**，用于备份网页与素材，以及后续查找、参考和维护。按照模特脸、姿势、服装分目录保存，不是仅收藏网站链接。

**三个目录均已上传并逐文件校验。图片是真实图片文件，不是图片网址清单，也不是只有缩略图。**

### 目录与已验证内容

| 目录 | 网站内容 | 图片文件 | 归档文件数 | 归档字节数 |
| --- | --- | --- | ---: | ---: |
| [`portrait/`](portrait/) | 模特脸库 | 1,499 张 PNG 原图 + 1,499 张 WebP 缩略图 | 3,027 | 4,915,936,705 |
| [`pose/`](pose/) | 模特姿势库 | 1,439 张 PNG 原图 + 1,439 张 JPG 缩略图 | 2,891 | 696,948,754 |
| [`costume/`](costume/) | 模特服装库 | 1,407 张 PNG 原图 + 1,407 张展示 WebP + 1,407 张 WebP 缩略图 | 4,234 | 1,528,760,002 |
| **合计** | **三个网站** | **10,097 个图片文件，其中 4,345 张原图** | **10,152** | **7,141,645,461** |

以上数字是采集归档本身，不含每个目录额外添加的 `expected-files.json` 与 `github-upload-verification.json` 两个校验文件，也不含本 README。全部图片文件未重新压缩或修改像素。采集日期：2026-10-30 UTC。

### 文件在哪里

- **模特脸库**：`portrait/index.html` 为原始页面，`portrait/index-offline.html` 为离线入口；图片、脚本、字体和快照的具体路径见 [portrait/README.md](portrait/README.md)。
- **姿势库**：`pose/original/` 保存原始页面和图片，`pose/offline/index.html` 为离线入口。
- **服装库**：`costume/original/png/` 是 PNG 原图，`original/img/` 是展示图，`original/thumbs/` 是缩略图；离线入口为 `costume/offline/index.html`。

### 如何打开离线网页

GitHub 用于浏览和下载文件，**本仓库没有部署为在线网站**。下载完整仓库后，在仓库根目录运行：

```sh
python3 -m http.server 8000
```

然后打开对应地址：

- 模特脸库：`http://localhost:8000/portrait/index-offline.html`
- 姿势库：`http://localhost:8000/pose/offline/index.html`
- 服装库：`http://localhost:8000/costume/offline/index.html`

不必登录 Google 邮箱。归档下载、上传与校验已在云端完成；上述本地预览仅在你自己想看离线网页时需要。完整仓库较大，下载需预留空间和时间。

### 校验与归档范围

- 每个目录的 `expected-files.json` 记录完整路径、字节数、SHA-256 和 Git blob SHA；`github-upload-verification.json` 记录上传校验结果。已与 GitHub 远端文件树逐一比对，零缺失、零不匹配。
- 保存可访问网页、公开前端 HTML/CSS/JavaScript、完整已发现素材、字体或必要接口快照。筛选、分页、详情等由单页应用在浏览器中生成，不人为编造不存在的服务器页面。
- 原始页面保持原样；离线副本只做本地路径、遥测和必要离线适配。模特脸库排名是采集时快照；服装库离线副本额外修复分页按钮隐藏样式，原始 HTML 未改。详细差异与浏览器检查见各目录 README 和 QA 文件。
- **不包含未取得的后台、数据库、私有开发源码、部署配置或未知未链接文件**，不能把公开前端归档描述为后台源码的 100% 复制。离线页面不提供原站在线写入能力，第三方社区链接仍需联网。

素材仅用于仓库所有者授权的私有备份与参考。原站声明与限制保留；第三方字体等仍遵循原有许可。
