# my-apt-repo

一个面向 iOS 越狱设备的 Sileo / APT 软件源，提供 RootHide、Rootless 与系统工具类软件包。

源在 Sileo 中显示为 **⭐ MikeHuang01**，用星标前缀方便在已添加的软件源中快速找到。

## 添加软件源

在 Sileo 中添加：

`https://mikehuang01.github.io/my-apt-repo/v2/`

如果 Sileo 仍显示旧的“AD”源图标，请先删除旧源，再添加上面的 **v2 地址**。旧地址和新地址的仓库身份不同，Sileo 不会继续沿用旧地址缓存的图标。

源图标与 GitHub 账号头像保持一致；NoAds 等插件的图标独立设置，不会替换源图标。添加后下拉刷新即可读取最新索引。

软件包的更新记录放在详情页的“更新日志”标签中，功能说明与安装提示保留在“详情”标签中。

## 软件分类

- **roothide packages**：RootHide 专用软件包
- **rootless 插件**：Rootless 越狱插件
- **Tweak**：系统功能与界面增强
- **System**：系统组件与系统工具
- **工具**：实用工具与文件管理器
- **应用程序**：普通 iOS 应用
- **插件**：扩展组件（如去广告、功能增强）
- **应用插件**：抖音 DYYY、小红薯、Lead 等应用扩展

## 当前收录

| 分类 | 软件包 | 版本 | 适用环境 |
| --- | --- | --- | --- |
| roothide packages / 工具 | Filza All-in-One | 4.0.1-4 | RootHide arm64e |
| 插件 | WatchFix | 2.1.15 | RootHide arm64e |
| roothide packages / Tweak / 插件 | FloatingView | 1.6.0-7 | RootHide arm64e |
| roothide packages / Tweak | Hello 3Q | 2.5+mike.13 | RootHide arm64e |
| roothide packages / Tweak / 插件 | NoAds | 1.3.5-3-7 | RootHide arm64e |
| roothide packages / Tweak / 插件 | ActionBar Reborn | 1.1-2.5 | RootHide arm64e |
| roothide packages / Tweak / 插件 | iCleaner Pro | 7.10.05 | RootHide arm64e |

### NoAds

RootHide 去广告插件，包含应用去广告、功能扩展与独立开关，二改自 NoadsX。按总开关和应用开关加载模块。

- 包名：`com.mikehuang01.noads`
- 适用环境：RootHide，`iphoneos-arm64e`
- 依赖：`mobilesubstrate`、`preferenceloader`、`firmware (>= 15.0)`、`rootless-compat (>= 0.9)`
- 支持抖音 DYYY 精简版、小红薯、Lead 与 KAlert 等插件。
- NoAds 1.3.5-3-7 移除内置 ActionBar Reborn。需要键盘工具栏时可安装独立包 `1.1-2.5`。
- NoAds 1.3.5-3-6
  - 酷安接入酷安净化 1.0，保留 NoAds 的信息流、插屏及其他去广告规则，移除重复的 7 个广告钩子。
  - 更新 Swiftgram 的 Lead，继续配合 KAlert 使用。
- NoAds 1.3.5-3-5：抖音模块完整替换为 DYYY 精简版 2.3-0.roothide，支持抖音标准版与极速版，包含去广告、播放倍速、界面隐藏、长按保存与复制文案等功能，使用 DYYY 内置设置。
- Swiftgram 同时加载 Lead 与 KAlert，覆盖防撤回、编辑记录、隐藏故事等扩展功能。
- 已加入 StressWatch 会员解锁，并优化插件体积与资源占用。
- 微信去广告之外新增更新拦截，减少微信自动更新打断插件。
- 修复微信禁用热更新相关闪退。
- 在“设置 → NoAds”中选择需要处理的应用；支持禁用摇一摇与开屏跳广等独立功能。
- 安装或更新后注销一次，再打开设置确认开关状态。

### WatchFix

解决 Apple Watch 连接问题，适用于 RootHide / `iphoneos-arm64e`。

- 包名：`com.mlgm.watchfix`
- 版本：`2.1.15`
- 2.1.15：优化安装包 XZ 压缩参数，降低安装解压阶段的内存需求。
- MikeHuang01 修复闪退问题。
- 依赖：`rootless-compat (>= 0.9)`、`mobilesubstrate`、`firmware (>= 15.0)`

### iCleaner Pro

iOS 系统清理工具，整合自定义缓存与 Inbox 规则，适用于 RootHide / `iphoneos-arm64e`。

- 包名：`com.sini.icleanerpro`
- 版本：`7.10.05`
- 二改作者：MikeHuang01。此版本更新至提供的 customrules RH8.4 构建。
- 修复伪装后自定义规则失效问题。
- 依赖：`rootless-compat (>= 0.9)`、`firmware (>= 15.0)`、`findutils`、`apt | apt7`
### FloatingView

保留基本的浮窗功能，删除原有的三屏和 ARC 功能。

- 包名：`com.be-huge.floating-view`
- 版本：`1.6.0-7`
- 1.6.0-7：优化安装包 XZ 压缩参数，降低安装解压阶段的内存需求。
- sidebar25：修复侧边栏手势取消后的布局提交，并跳过不再使用的 HID 回调资源创建与清理。
- 适用环境：RootHide，`iphoneos-arm64e`
- 安装后从“设置 → floating-view”启用浮窗并调整浮窗参数。
- 设置界面支持其他杂项功能，以及配置备份、导出、导入和恢复。

### Hello 3Q

拦截后台热加载 App（节约内存、少杀后台），按 Bundle ID 放行指定应用。

- 包名：`cn.zqbb.stopautolaunchapps`
- 适用环境：RootHide，`iphoneos-arm64e`
- 依赖：`mobilesubstrate (>= 0.9.5000)`、`firmware (>= 16.0)`
- 配置文件：`/var/containers/Bundle/Application/jbroot-*/var/mobile/Library/Preferences/Hello3Q-allowlist.conf`
- 每次修改后注销一次，文件会自动生成；把要放行的 App 包名往下加就行，一行一个。不在白名单的应用继续拦截。
- 用法、示例和运行状态都写在配置文件里。

### ActionBar Reborn

在键盘底部显示撤销、选择、粘贴等按钮。

- 包名：`netskao.actionbarreborns`
- 适用环境：RootHide，`iphoneos-arm64e`
- 版本：`1.1-2.5`
- 此版本包含键盘工具栏生命周期与刷新优化。
- 已安装 NoAds `1.3.5-3-6` 时，先升级到 `1.3.5-3-7`，再安装独立键盘插件。
- 安装或更新后注销一次，再打开键盘测试按钮是否正常显示。

## 目录结构

每个软件包会按兼容环境与用途归类；GitHub Actions 自动生成 APT 索引，Sileo 会从索引中读取包名、版本、架构和图标信息。详情页会展示软件介绍、截图与兼容信息。

## 说明

本源仅用于个人测试与研究。安装前请确认设备越狱环境（RootHide / Rootless）与 iOS 版本兼容。Pages 使用 GitHub Actions 发布 APT 索引。
