<script setup lang="ts">
type Theme = "light" | "dark"

const isDark = ref(false)

const colorMode = useColorMode()

const toggleTheme = () => {
    colorMode.preference = colorMode.preference === 'light' ? 'dark' : 'light'
    isDark.value = !isDark.value
}
</script>

<template>
    <nav
        class="fixed w-full z-50 backdrop-blur-2xl bg-white dark:bg-gray-950/50 border-b border-gray-200/10 dark:border-gray-800/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex items-center space-x-4">
                    <div
                        class="bg-gradient-to-tr from-sky-400 to-blue-600 p-2.5 rounded-xl shadow-lg shadow-sky-500/20">
                        <IconWind class="w-6 h-6 text-white" />
                    </div>
                    <span
                        class="text-xl font-bold bg-gradient-to-r from-sky-400 to-blue-600 bg-clip-text text-transparent">
                        Vaidya
                    </span>
                </div>
                <div class="flex items-center space-x-8">
                    <nav class="hidden md:flex space-x-8">
                        <a href="#features"
                            class="text-gray-600 dark:text-gray-300 hover:text-sky-500 dark:hover:text-sky-400 transition-colors duration-300 relative group">
                            Features
                            <span
                                class="absolute bottom-0 left-0 w-full h-0.5 bg-sky-500 scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></span>
                        </a>
                        <a href="#about"
                            class="text-gray-600 dark:text-gray-300 hover:text-sky-500 dark:hover:text-sky-400 transition-colors duration-300 relative group">
                            About
                            <span
                                class="absolute bottom-0 left-0 w-full h-0.5 bg-sky-500 scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></span>
                        </a>
                        <a href="#contact"
                            class="text-gray-600 dark:text-gray-300 hover:text-sky-500 dark:hover:text-sky-400 transition-colors duration-300 relative group">
                            Contact
                            <span
                                class="absolute bottom-0 left-0 w-full h-0.5 bg-sky-500 scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></span>
                        </a>
                    </nav>
                    <button @click="toggleTheme"
                        class="relative p-2.5 rounded-xl bg-white/5 dark:bg-gray-800/50 hover:bg-white/10 dark:hover:bg-gray-800 transition-all duration-300 group backdrop-blur-xl border border-white/10 dark:border-gray-800">
                        <Icon name="line-md:moon" v-if="isDark"
                            class="w-5 h-5 text-amber-400 group-hover:rotate-180 transition-transform duration-500" />
                        <Icon name="solar:sun-bold" v-else
                            class="w-5 h-5 text-gray-600 group-hover:rotate-180 transition-transform duration-500" />
                        <div
                            class="absolute inset-0 rounded-xl bg-gradient-to-r from-sky-400/20 to-blue-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                        </div>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</template>