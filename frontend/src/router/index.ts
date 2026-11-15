import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Craftsman = () => import('@/views/craftsman/index.vue')
const Apprentice = () => import('@/views/apprentice/index.vue')
const Timber = () => import('@/views/timber/index.vue')
const Component = () => import('@/views/component/index.vue')
const Mortise = () => import('@/views/mortise/index.vue')
const Building = () => import('@/views/building/index.vue')
const Tool = () => import('@/views/tool/index.vue')
const Workshop = () => import('@/views/workshop/index.vue')
const Drawing = () => import('@/views/drawing/index.vue')
const Carving = () => import('@/views/carving/index.vue')
const Lacquer = () => import('@/views/lacquer/index.vue')
const Exhibition = () => import('@/views/exhibition/index.vue')
const Heritage = () => import('@/views/heritage/index.vue')
const Training = () => import('@/views/training/index.vue')
const Exchange = () => import('@/views/exchange/index.vue')
const Media = () => import('@/views/media/index.vue')
const Donation = () => import('@/views/donation/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/craftsman', name: 'craftsman', component: Craftsman },
    { path: '/apprentice', name: 'apprentice', component: Apprentice },
    { path: '/timber', name: 'timber', component: Timber },
    { path: '/component', name: 'component', component: Component },
    { path: '/mortise', name: 'mortise', component: Mortise },
    { path: '/building', name: 'building', component: Building },
    { path: '/tool', name: 'tool', component: Tool },
    { path: '/workshop', name: 'workshop', component: Workshop },
    { path: '/drawing', name: 'drawing', component: Drawing },
    { path: '/carving', name: 'carving', component: Carving },
    { path: '/lacquer', name: 'lacquer', component: Lacquer },
    { path: '/exhibition', name: 'exhibition', component: Exhibition },
    { path: '/heritage', name: 'heritage', component: Heritage },
    { path: '/training', name: 'training', component: Training },
    { path: '/exchange', name: 'exchange', component: Exchange },
    { path: '/media', name: 'media', component: Media },
    { path: '/donation', name: 'donation', component: Donation },
  ],
})

export default router
