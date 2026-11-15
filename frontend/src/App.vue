<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">传统木作营造技艺传习管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向中华传统木作营造的匠人档案、木材甄选、构件制作、榫卯工艺、古建修缮与工坊传承的一体化传习管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "匠人档案", path: "/craftsman" }, { label: "学徒培养", path: "/apprentice" }, { label: "木材甄选", path: "/timber" }, { label: "构件制作", path: "/component" }, { label: "榫卯工艺", path: "/mortise" }, { label: "古建修缮", path: "/building" }, { label: "工具管理", path: "/tool" }, { label: "工坊管理", path: "/workshop" }, { label: "图样档案", path: "/drawing" }, { label: "雕花技艺", path: "/carving" }, { label: "髹漆工艺", path: "/lacquer" }, { label: "作品展陈", path: "/exhibition" }, { label: "非遗传承", path: "/heritage" }, { label: "技艺研习", path: "/training" }, { label: "匠人交流", path: "/exchange" }, { label: "影像记录", path: "/media" }, { label: "资助捐赠", path: "/donation" }]
</script>
