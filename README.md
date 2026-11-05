# my-apt-repo

一个面向 iOS 越狱设备的 Sileo / APT 软件源，提供 RootHide、Rootless 与系统工具类软件包。

## 添加软件源

在 Sileo 中添加：

`https://mikehuang01.github.io/my-apt-repo/`

如果无法连接，请确认地址末尾包含 `/`，并在 Sileo 中刷新软件源。源图标与 NoAds 使用同一图标。

## 软件分类

- **roothide packages**：RootHide 专用软件包
- **rootless 插件**：Rootless 越狱插件
- **Tweak**：系统功能与界面增强
- **System**：系统组件与系统工具
- **工具**：实用工具与文件管理器
- **应用程序**：普通 iOS 应用
- **插件**：其他扩展组件

## 当前收录

| 分类 | 软件包 | 版本 | 适用环境 |
| --- | --- | --- | --- |
| roothide packages / 工具 | Filza All-in-One | 4.0.1-4 | RootHide arm64e |
| 应用程序 | Widgy | 1.0.0 | iOS |
| 插件 | WatchFix | 2.0.4 | RootHide arm64e |
| Tweak | StepOfLife | 1.0.0 | iOS |
| roothide packages / Tweak / 插件 | FloatingView | 1.6.0-6+sidebar19 | RootHide arm64e |
| roothide packages / Tweak | Hello 3Q | 2.5+mike.13 | RootHide arm64e |
| roothide packages / Tweak / 插件 | NoAds | 1.3.5-3-1 | RootHide arm64e |
| roothide packages / Tweak / 插件 | ActionBar Reborn | 1.1-2+mikehuang01.1 | RootHide arm64e |

### NoAds

RootHide 去广告插件，包含应用去广告、功能扩展与独立开关，二改自 NoadsX。按总开关和应用开关加载模块。

- 包名：`com.mikehuang01.noads`
- 适用环境：RootHide，`iphoneos-arm64e`
- 依赖：`mobilesubstrate`、`preferenceloader`、`rootless-compat (>= 0.9)`
- 支持抖音 DYYY、小红薯、Lead 等插件。
- 在“设置 → NoAds”中选择需要处理的应用；支持禁用摇一摇与开屏跳广等独立功能。
- 安装或更新后注销一次，再打开设置确认开关状态。

### FloatingView

保留基本的浮窗功能，删除原有的三屏和 ARC 功能。

- 包名：`com.be-huge.floating-view`
- 适用环境：RootHide，`iphoneos-arm64e`
- 安装后从“设置 → floating-view”启用浮窗并调整浮窗参数。
- 设置界面支持其他杂项功能，以及配置备份、导出、导入和恢复。

### Hello 3Q

拦截 App 后台预热（省内存、少杀后台），支持按 Bundle ID 放行指定应用。

- 包名：`cn.zqbb.stopautolaunchapps`
- 适用环境：RootHide，`iphoneos-arm64e`
- 依赖：`mobilesubstrate (>= 0.9.5000)`、`firmware (>= 16.0)`
- 安装后注销一次，配置文件会自动生成：`/var/mobile/Library/Preferences/Hello3Q-allowlist.conf`
- RootHide 实际路径可用 Filza 搜索 `Hello3Q-allowlist.conf`。将要放行的 App Bundle ID 逐行加入白名单；不在白名单的应用继续拦截。

### ActionBar Reborn

在键盘底部显示撤销、选择、粘贴等按钮。

- 包名：`netskao.actionbarreborns`
- 适用环境：RootHide，`iphoneos-arm64e`
- 版本：`1.1-2+mikehuang01.1`
- 修改内容：调整首次聚焦时的按钮初始化条件。
- 安装或更新后注销一次，再打开键盘测试按钮是否正常显示。

## 目录结构

每个软件包会按兼容环境与用途归类；GitHub Actions 自动生成 APT 索引，Sileo 会从索引中读取包名、版本、架构和图标信息。详情页会展示软件介绍、截图与兼容信息。

## 说明

本源仅用于个人测试与研究。安装前请确认设备越狱环境（RootHide / Rootless）与 iOS 版本兼容。Pages 使用 GitHub Actions 发布 APT 索引。