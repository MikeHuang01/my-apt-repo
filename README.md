# my-apt-repo

一个面向 iOS 越狱设备的 Sileo / APT 软件源，提供 RootHide、Rootless 与系统工具类软件包。

## 添加软件源

在 Sileo 中添加：

`https://mikehuang01.github.io/my-apt-repo/`

如果无法连接，请确认地址末尾包含 `/`，并在 Sileo 中刷新软件源。

## 软件分类

- **roothide packages**：RootHide 专用软件包
- **rootless 插件**：Rootless 越狱插件
- **Tweak**：系统功能与界面增强
- **System**：系统组件与系统工具
- **工具**：实用工具与文件管理器
- **应用程序**：普通 iOS 应用
- **插件**：其他扩展组件

## 当前收录

| 分类 | 软件包 |
| --- | --- |
| roothide packages / 工具 | Filza All-in-One |
| 应用程序 | Widgy |
| 插件 | WatchFix |
| Tweak | StepOfLife |
| roothide packages | FloatingView |

## 目录结构

每个软件包会按兼容环境与用途归类；GitHub Actions 自动生成 APT 索引，Sileo 会从索引中读取包名、版本、架构和图标信息。

## 说明

本源仅用于个人测试与研究。安装前请确认设备越狱环境（RootHide / Rootless）与 iOS 版本兼容。

Pages 使用 GitHub Actions 发布 APT 索引。
