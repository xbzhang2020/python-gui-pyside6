import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Pyside6 GUI 教程",
  base: "/python-gui-pyside6/",
  description: "Pyside6",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "指南", link: "/guide/getting-started" },
      // { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: "指南",
        collapsed: false,
        items: [
          { text: "快速上手", link: "/guide/getting-started" },
          { text: "信号与插槽", link: "/guide/signals-and-slots" },
          { text: "布局", link: "/guide/layout" },
          { text: "组件化", link: "/guide/widgets" },
          { text: "样式", link: "/guide/styling" },
          { text: "模型与视图", link: "/guide/model-and-view" },
        ],
      },
      {
        text: "常用控件",
        collapsed: true,
        items: [
          { text: "Label", link: "/widgets/label" },
          { text: "Button", link: "/widgets/button" },
          { text: "TextEdit", link: "/widgets/textedit" },
          { text: "ComboBox", link: "/widgets/combobox" },
          { text: "SpinBox", link: "/widgets/spinbox" },
          { text: "Slider", link: "/widgets/slider" },
          { text: "List", link: "/widgets/list" },
          { text: "Table", link: "/widgets/table" },
          { text: "Tree", link: "/widgets/tree" },
          { text: "Tab", link: "/widgets/tab" },
          { text: "Menu", link: "/widgets/menu" },
          { text: "ProgressBar", link: "/widgets/progressbar" },
          { text: "Frame", link: "/widgets/frame" },
          { text: "ScrollArea", link: "/widgets/scrollarea" },
          { text: "Dialog", link: "/widgets/dialog" },
          { text: "Splitter", link: "/widgets/splitter" },
          { text: "MessageBox", link: "/widgets/messagebox" },
          { text: "MainWindow", link: "/widgets/main-window" },
        ],
      },
    ],

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/xbzhang2020/python-gui-pyside6",
      },
    ],

    editLink: {
      pattern: "https://github.com/web-extend/web-extend/blob/main/docs/:path",
      text: "在 GitHub 上编辑此页面",
    },

    docFooter: {
      prev: "上一页",
      next: "下一页",
    },

    outline: {
      label: "页面导航",
    },

    footer: {
      // message: "基于 MIT 许可发布",
      copyright: `版权所有 © 2026-${new Date().getFullYear()} 冰梦`,
    },

    lastUpdated: {
      text: "最后更新于",
      formatOptions: {
        dateStyle: "short",
        timeStyle: "medium",
      },
    },
  },
});
